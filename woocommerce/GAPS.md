# WooCommerce: what is not held yet

Each row: what WooCommerce or WooPayments shows that this folder does not hold, why, and how it can be held.

| Not held | Why | Route |
| --- | --- | --- |
| A WooPayments account (test account or sandbox): its country as WooPayments holds it (`wcpay_account_data`), and the verification it asks for, with the documents, for each country | the onboarding answer lists test_account and business_verification as needing the WordPress.com connection, and wordpress.com/jetpack/connect/authorize answered "Confirm you are human. We need to check you're not a robot before you can enter this site." (run 20261029T020454Z-store-setup-en, step 85) | the founder ticks the human check in the WooCommerce browser (port 9251), then the WordPress.com account (7amza.it+woo@gmail.com) is made, then WooPayments' test account and its verification for the US, the UK and the UAE (supported business locations), with test-marked values |
| A change of the store's Country / State with a WooPayments account | as above | the same, then the country changes of run 20261029T023051Z-country-change-en again |
| WooCommerce Tax's automated rates by country | WooCommerce Tax works through the WordPress.com connection | as above |
| The set-up's country list as items (which countries and states it offers; it matched no entry for Yemen) | held as the page and the code (`i18n/countries.php`, `i18n/states.php` in woocommerce.11.2.1.zip) | a structure read from the code |
| The structures in [structures/REGISTER.tsv](structures/REGISTER.tsv) marked backlogged, as items | held as answers and code | read each into `items.jsonl` |
