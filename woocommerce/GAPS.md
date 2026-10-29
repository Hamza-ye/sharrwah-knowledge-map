# WooCommerce: what is not held yet

Each row: what WooCommerce or WooPayments shows that this folder does not hold, why, and how it can be held.

| Not held | Why | Route |
| --- | --- | --- |
| Stripe's verification screens after the first, for each country, and its answers to a submitted verification | the first screen is held for a US individual and each account's requirements for the US, the UAE and the UK (run 20261029T101705Z-stripe-onboarding-us-en); the forms ask a phone "required to be in the country of your account" and, in the US, a full SSN or ITIN, which this capture does not have (a made-up number could be a real person's); Stripe refused its sign-in while this capture's browser automation was attached (captcha_try_again_later_support_error, run 20261029T090147Z-wpcom-connect-en) and took the founder's own | a phone in the account's country; the UAE's documents can be the test-marked images in `capture/woocommerce/files/`; the founder signs in to Stripe by hand with no run attached, then a run adopts the tab |
| WooCommerce Tax's automated rates by country | WooCommerce Tax works through the WordPress.com connection | as above |
| The set-up's country list as items (which countries and states it offers; it matched no entry for Yemen) | held as the page and the code (`i18n/countries.php`, `i18n/states.php` in woocommerce.11.2.1.zip) | a structure read from the code |
| The structures in [structures/REGISTER.tsv](structures/REGISTER.tsv) marked backlogged, as items | held as answers and code | read each into `items.jsonl` |
