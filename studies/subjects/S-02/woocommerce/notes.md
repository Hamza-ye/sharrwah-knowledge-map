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
