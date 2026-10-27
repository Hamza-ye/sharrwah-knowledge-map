# S-02, phase A: woocommerce (WC)

Agent: S-02 phase A, woocommerce. Brief: `studies/subjects/S-02/briefs/A-one-platform.md` (re-read after it changed on disk on 2026-10-27: the change adds `quote_check.py --text`).
Read "from what is recorded", with the release's files on countries the brief names.

## Documents read, as finished

1. `studies/subjects/S-02/briefs/A-one-platform.md` (the brief), read 2026-10-27.
2. `studies/subjects/S-02/bullets.tsv`, read 2026-10-27.
3. `studies/subjects/S-02/woocommerce/recorded.tsv`, read in full (87 rows, R001 to R087), 2026-10-27.
4. `studies/subjects/S-02/woocommerce/recorded-citations.tsv`, read in full (105 citations), 2026-10-27.
5. `studies/concern-map/platforms/woocommerce/concerns.tsv`, read in full (columns concern_id, concern, platform_terms), 2026-10-27.
6. `studies/concern-map/platforms/woocommerce/statements.tsv` (1,499 statements), searched with a script by concern and by words on countries, locations, addresses, regions, zones, currency, tax, residence, sanctions and markets, 2026-10-27. Not loaded whole.
7. `studies/concern-map/platforms/woocommerce/citations.tsv`, looked up by cite_id and by source path with scripts, 2026-10-27.
8. `studies/concern-map/platforms/woocommerce/gaps.tsv`, searched with a script for gaps on countries, locations, currency, tax, onboarding and markets, 2026-10-27. Pages its gaps name that bear on a bullet: the WooPayments onboarding (country and account type steps), WC-C-010; Payments > Settings, WC-C-051.
9. `woocommerce-11.2.1:includes/class-wc-countries.php`, read 2026-10-27: lines 1-30 (class docblock), 396-760 (base address, country, state, city and postcode; allowed and shipping countries and states; EU and VAT countries; shipping and estimate prefixes; tax or VAT labels), 740-920 (`get_address_formats()`, `get_formatted_address()`), 917-1075 (`get_default_address_fields()`, `get_country_locale_field_selectors()`, start of `get_country_locale()`); of the locale array (lines 1078-1898), its start (1075-1150) and end (1880-1960) read, and its 100 country keys listed with a script.
10. `woocommerce-11.2.1:includes/admin/settings/class-wc-settings-general.php` lines 118-192 (the Store Address section), read 2026-10-27 under rule 5: the index excerpt WC-S-0599 doesn't show which option holds the store's country.
11. `woocommerce-11.2.1:readme.txt` lines 28-40, read 2026-10-27 under rule 5: the excerpts WC-S-0590 / R008 "(Available in …)" and WC-S-0592 "(U.S.-only)" don't name what they describe.
12. `method/check_subject.py` (lines 1-340) and `method/quote_check.py`, read 2026-10-27 to learn what the checker tests.

## Problems with the method

- WC-C-004's index holds `PaymentsExtensionSuggestions::$country_extensions` as 273 statements, one or two per store country (247 countries, identifiers `$country_extensions['XX']`, index cite_ids WC-S-5016 to WC-S-5288). The concern map holds only three of WC-C-004's statements (recorded R001 to R003), which state that the list is per country. Copying the 273 would on their own pass rule 14's stop at 300 statements before the release's files on countries were read, so they are not copied one by one: R001 to R003 and WC-S-0619 are. The coordinator can ask for them.

## recorded.tsv: what became of each row

- Copied (S02-WC-001 to S02-WC-060): R001-R004, R006-R008, R011-R014, R016-R020, R022, R023, R025-R029, R031, R034, R035, R039-R046, R052, R055-R057, R059-R064, R066, R068, R073-R084, R086, R087. Where two rows hold the same words, the copy keeps both citations (identical citations are one).
- Held in a copied statement with the same words: R005 and R010 (in R066's copy), R009 and R085 (R014), R015 (R086), R024 (R026), R032 and R033 (R034), R054 (R017), R065 (R004), R067 (R006), R069 (R013), R070 (R012), R071 (R011), R072 (R008).
- Left out, not bearing on a bullet: R021 (the collective name of the four entities), R030 (the Integration tab's label), R036-R038 (the geolocation database's and IP lookup services' addresses), R047-R051 (the data API resources), R053 (a Marketplace category's name), R058 (minimum payout amounts, by payout currency; its words don't tie them to a country).

## Q1 index statements copied (not in recorded.tsv)

- S02-WC-061 to S02-WC-107, from the index by `from` (index:<concern>:<cite>): WC-C-004 (WC-S-0619), WC-C-007 (WC-S-0531, WC-S-0530), WC-C-012 (WC-S-5298 with WC-S-0537), WC-C-014 (WC-S-0869, WC-S-0870), WC-C-015 (WC-S-5338), WC-C-021 (WC-S-5309, WC-S-5310, WC-S-0547, WC-S-0860, WC-S-0549), WC-C-024 (WC-S-0495, WC-S-0494), WC-C-026 (WC-S-0488, WC-S-0489, WC-S-5328), WC-C-028 (WC-S-0490, WC-S-0491, WC-S-0493, WC-S-0648), WC-C-017 (WC-S-0923), WC-C-043 (WC-S-0942, WC-S-0659), WC-C-052 (WC-S-0874, WC-S-0598, WC-S-0876, WC-S-0877, WC-S-5381), WC-C-054 (WC-S-0599, WC-S-5382), WC-C-055 (WC-S-0633, WC-S-0639), WC-C-057 (WC-S-5316), WC-C-060 (WC-S-0905), WC-C-075 (WC-S-0017, WC-S-0687, WC-S-0688, WC-S-0689), WC-C-078 (WC-S-0140), WC-C-089 (WC-S-0893, WC-S-0894), WC-C-107 (WC-S-5484 with WC-S-5485), WC-C-118 (WC-S-5462, WC-S-5465, WC-S-0964, WC-S-0963).
- The index excerpts WC-S-0635 and WC-S-0636 (WC-C-055) are held in new statements from their page, re-read under rule 5 (the list of EU countries after WC-S-0635; what "that location" is in WC-S-0636).

13. `https://woocommerce.com/document/woocommerce-shipping-and-tax/woocommerce-tax/`, held in `evidence/product-class/runs/20261010T235357Z-q1-woocommerce-sources/items/047-woocommerce.com/` (capture of 2026-10-10, dateModified 2026-08-21), read in full with `quote_check.py --text` on 2026-10-27, under rule 5.
14. Statements S02-WC-108 to S02-WC-123 (new): readme.txt lines 33-34; the Store Address fields (class-wc-settings-general.php lines 135-177); the WooCommerce Tax page (item 13). S02-WC-124 to S02-WC-159 (new): class-wc-countries.php (item 9). The three long lists, each recorded whole as one statement under rule 7 with its start and its docblock cited: the address formats (S02-WC-143, lines 754-796, 3,561 characters with whitespace collapsed), the default address fields (S02-WC-147, lines 928-1009) and the country locale (S02-WC-151, lines 1078-1899, 12,831 characters).
15. `woocommerce-11.2.1:i18n/states.php`: docblock (lines 1-17) and start of the array read 2026-10-27; its country keys (108) and empty arrays (39) listed with a script. `woocommerce-11.2.1:i18n/locale-info.php`: lines 1-60 and the 'BG' entry (lines 352-364) read; its 248 entries and their keys listed with a script. `woocommerce-11.2.1:i18n/postcode-validation-rules.json`: read in full (117 lines). Statements S02-WC-160 to S02-WC-168.
16. Held pages read with `quote_check.py --text` on 2026-10-27, from this repository's capture runs, instead of routing gaps to the founder (rule 9) or because an index excerpt was too short (rule 5); each is cited by its live URL:
    - `https://woocommerce.com/document/configuring-woocommerce-settings/general/` (run 20261010T235357Z-q1-woocommerce-sources, item 024; dateModified 2026-10-09), read in full;
    - `https://woocommerce.com/document/woopayments/compatibility/countries/` (item 054; 2026-09-25), read in full;
    - `https://woocommerce.com/document/woopayments/startup-guide/` (run 20261012T104936Z-s01-sources, item 101; 2026-09-25), lines 25-100 of its text read, and searched for country, location, address and change;
    - `https://woocommerce.com/document/woopayments/our-policies/know-your-customer/` (item 068; 2025-08-15), read in full;
    - `https://woocommerce.com/document/woo-mobile-app-point-of-sale-mode/` (item 043; 2026-08-04), its Requirements and Supported countries read;
    - `https://woocommerce.com/document/woopayments/currencies/multi-currency-setup/` (item 058; 2026-09-25), lines 25-110 read;
    - `https://woocommerce.com/document/woopayments/in-person-payments/` (item 065; 2026-09-26), lines 30-56 read;
    - `https://woocommerce.com/document/woocommerce-shipping/` (item 048) and `https://woocommerce.com/document/woopay-merchant-documentation/` (run 20261011T084016Z-q1r-woocommerce-more, item 018; 2026-05-20), searched for country, U.S., currency and location, and the lines found read.
    Statements S02-WC-169 to S02-WC-204.
17. Not held, so not read: `https://woocommerce.com/document/setting-up-shipping-zones/` and `https://woocommerce.com/document/woocommerce-setup-wizard/` (`held_index.py`, 2026-10-27).
18. terms.tsv: 30 terms, each citing quotes already written (and two new citations: the Store Address section title, class-wc-settings-general.php lines 127-130; the customer address field Country / Region, class-wc-countries.php lines 950-952). No translation is recorded: none of the material read gives the platform's own translation of a term.
19. Read under rule 5 on 2026-10-27, with `quote_check.py --text`: `https://woocommerce.com/document/setting-up-taxes-in-woocommerce/` (run 20261010T235357Z-q1-woocommerce-sources, item 039; dateModified 2026-08-07), lines 25-160 of its text (the index excerpt WC-S-0878 doesn't show how rates are set by location); `https://woocommerce.github.io/woocommerce-rest-api-docs/` (item 099), its Tax rates, Shipping zones and Shipping zone locations sections found by search (the index excerpts WC-S-0681, WC-S-0687 and WC-S-0688 don't show what a rate or a zone location holds). Statements S02-WC-205 to S02-WC-212.
20. `corpus_search.py woocommerce verify verified verifies verification --with country countries "business location" "store address" --max 25`, run 2026-10-27: 16 documents, none stating who verifies the store's or account's country; it lists the release's WooPayments onboarding code (src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsService.php, WooPaymentsRestController.php; a `business_verification` step and a `kyc_session` route), which the brief doesn't name and which wasn't read.
21. `https://woocommerce.com/document/woopayments/fees/` (item 059; dateModified 2026-09-25), read under rule 5 on 2026-10-27: lines 25-150 of its text (factors, definitions, notes for all countries, Countries in Europe). Its per-country fee tables (from line 150 to about line 2350 of the text) were not read or copied. Statements S02-WC-213 to S02-WC-215.
22. `corpus_search.py woocommerce "shipping zone" "shipping zones" --with "single zone" match matched "geographic region" regions --max 15`, run 2026-10-27 for an (e) gap (what a zone is, how many a shopper or store holds): 15 documents. Read, since they could state it (rule 9): `woocommerce-11.2.1:includes/admin/settings/views/html-admin-page-shipping-zones.php` lines 15-30, 48-64 and 84-90; `includes/admin/settings/views/html-admin-page-shipping-zone-methods.php` lines 40-50; `includes/class-wc-shipping-zones.php` lines 70-92. The others are the language template's entries for the same strings, the zone data store, the legacy shipping methods, `class-wc-shipping.php` (a debug notice) and an admin bundle. Statements S02-WC-216 to S02-WC-220; the term "Shipping zones" takes the definition from line 87.
23. For the (a) and (b) gaps (where the WooPayments account's country is held; who checks or changes it), read on 2026-10-27, starting from the documents the corpus search of item 20 listed: `woocommerce-11.2.1:src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsRestController.php` lines 70-80 and 888-905; `src/Internal/Admin/Settings/PaymentsProviders/WooPayments/WooPaymentsService.php` (searched with grep for country and location only); and, reached from them, `src/Internal/Admin/Settings/Payments.php` lines 19 and 240-290, `src/Internal/Admin/Settings/PaymentsController.php` lines 136-150 and `src/Internal/Admin/Settings/PaymentsProviders/WooPayments.php` lines 316-382. Statements S02-WC-221 to S02-WC-227.
24. `https://woocommerce.com/document/woopayments/currencies/currencies-overview/` (item 057), searched on 2026-10-27 for a limit on currencies and for countries: none found.

## Gaps and absences

- gaps.tsv: S02-WC-G01 (a, where the residence and the WooPayments account's country are held), G02 (b, who checks the country), G03 (b, conditions on changing the store's Country / State), G04 (e, how many zones or currencies a store can hold), G05 (f, where the values of locale-info.php and the postcode rules apply). Bullets c, d and h have every part stated; g needs no gap.
- absences.tsv: header only. No complete list read was used to record an absence.

## What couldn't be read

- Not held, and live pages are outside what the brief allows for woocommerce: `https://woocommerce.com/document/setting-up-shipping-zones/`, `https://woocommerce.com/document/woocommerce-setup-wizard/`, `https://woocommerce.com/contact-us/` (held_index.py, 2026-10-27). They are named in gap routes.
- Release files named in gap routes and not read: the WooPayments onboarding service and REST controller in full (G02); the files that use locale-info.php and postcode-validation-rules.json (G05).

## Problems with the method (continued)

- Lists recorded whole as one statement each (rule 7), with their start and their docblock cited: address formats (S02-WC-143), default address fields (S02-WC-147), country locale (S02-WC-151, 12,831 characters), postcode rules (S02-WC-168), the tax rate properties (S02-WC-209, S02-WC-212). Two lists are not copied whole because of their size: `i18n/states.php` (108 countries' states, about 94,000 characters) and `i18n/locale-info.php` (248 country entries, about 96,000 characters); their docblocks, the first locale entry (with the keys every entry holds) and counts are recorded (S02-WC-160 to S02-WC-166). The per-country fee tables of the WooPayments fees page are not copied either (item 21).
- Items 22 and 23 read release files that the brief doesn't name, because a corpus search run for a gap listed them (rule 9 has a "searched, not found" gap read each listed document that could state it), or because those documents led to them. The brief limits woocommerce to the recorded statements and the files on countries; the coordinator may judge whether these reads, and statements S02-WC-216 to S02-WC-227, stay.
- Rule 5's re-reads (items 10, 11, 13, 16, 19, 21) record new statements that hold an index excerpt, with the index citation kept as a further citation; the excerpts themselves are then not copied as separate statements.

## Check

- `python3 -I method/check_subject.py` on a copy (`/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/s02/wc/check/S-02`, output in `.../check/out`), 2026-10-27: 227 statements, 5 gaps, 291 quotes found, no error. One warning: S02-WC-C024's quote is 313 characters, a copied index citation (WC-S-5377) that rule 5 keeps unchanged. One review line: two claims of absence (G01, G03) await phase A3. 36 web sources listed for capture.
- The commit 31bedd3a (2026-10-27 01:43) holds this folder as it stood after the first 60 statements; the working files supersede it.
