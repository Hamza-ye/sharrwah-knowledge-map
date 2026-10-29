# WooCommerce

What WooCommerce (and WooPayments, its payments extension) states and shows about itself, captured at the source, in
English.

## The instrument

A test store of our own: WordPress 7.1.4 with WooCommerce 11.2.1, WooPayments 11.2.0 and WooCommerce Tax 3.7.3, run on
this machine in Docker (`capture/woocommerce/compose.yaml`) and reached through a Cloudflare quick tunnel
(`https://<name>.trycloudflare.com`; the address changes when the tunnel restarts). WooCommerce is open code that runs
on the merchant's own site, so the store's database and the plugins' code are held beside its pages: a database run
holds `wordpress.sql` and `options.tsv`, and run `20261029T023950Z-plugin-code` holds the three plugins as WordPress.org
serves them. Its facts, each with the run it comes from, are in [index/instruments.json](index/instruments.json).

The site is registered with WordPress.com (Jetpack, site 258291858); the store owner's WordPress.com connection, which
WooPayments needs before a test account or verification, was answered with a human check
([GAPS.md](GAPS.md)).

## Where to start

| To find | Read |
| --- | --- |
| The set-up (store location, its Yemen warning, the free features), WooCommerce's Payments page and WooPayments' onboarding answer | run `20261029T020454Z-store-setup-en` (`answers.jsonl`: `wc-admin/onboarding/...`, `wc-admin/settings/payments/...`) |
| Where the store's country, currency and units are held, and the payments business location | runs `20261029T023002Z-db-after-setup`, `20261029T023745Z-db-after-country-change` (`options.tsv`; `wordpress.sql` for `wp_usermeta`) |
| What a change of the store's Country / State does with orders and tax rates, and which country decides WooPayments' support | run `20261029T023051Z-country-change-en` |
| The set-up's free features by country | run `20261029T024814Z-free-extensions-en` |
| The code (where WooPayments reads its account country, its supported countries, the business location) | run `20261029T023950Z-plugin-code` (`fetch.warc.gz`; `capture/warcbody.py` writes a zip out) |
| Every run, and what is unusual about one | [index/runs.tsv](index/runs.tsv), [index/run-notes.tsv](index/run-notes.tsv) |
| Every self-description seen, held or not | [structures/REGISTER.tsv](structures/REGISTER.tsv) |
| What is not held yet, and how it can be | [GAPS.md](GAPS.md) |
