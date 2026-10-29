# WooCommerce: what is not held yet

Each row: what WooCommerce or WooPayments shows that this folder does not hold, why, and how it can be held.

| Not held | Why | Route |
| --- | --- | --- |
| WooPayments' live verification as the onboarding shows it, for each country: the fields and documents its embedded Stripe onboarding asks for | the WordPress.com connection and a test account are made (US; `wcpay_account_data` country US, run 20261029T090847Z-db-after-test-account); Activate payments asked business location (39 countries), legal entity and goods or services, then opened Stripe's onboarding, whose login popup answered an hCaptcha challenge (run 20261029T090147Z-wpcom-connect-en) | the founder solves the challenge; then the US fields, a reset (onboarding/reset deletes the account "if possible"), the UAE (test-marked documents in `capture/woocommerce/files/`) and the UK |
| WooCommerce Tax's automated rates by country | WooCommerce Tax works through the WordPress.com connection | as above |
| The set-up's country list as items (which countries and states it offers; it matched no entry for Yemen) | held as the page and the code (`i18n/countries.php`, `i18n/states.php` in woocommerce.11.2.1.zip) | a structure read from the code |
| The structures in [structures/REGISTER.tsv](structures/REGISTER.tsv) marked backlogged, as items | held as answers and code | read each into `items.jsonl` |
