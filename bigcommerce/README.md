# BigCommerce

What BigCommerce (bigcommerce.com; its terms now under commerce.com) states and shows about itself, captured at the
source, in English.

## The instrument

A free trial store of our own: "Capture Test Store NA", store `w5pamplexj` (id 1003524922), control panel
`https://store-w5pamplexj.mybigcommerce.com/manage/`, hosted in North America. BigCommerce's sign-up asks no country;
it made the store with the default country Oman and the currency OMR. The account is 7amza.it+bc-na@gmail.com. A trial
store has online payments switched off ("Please switch to a paid plan to activate online payments.") and one
storefront. Its facts, each with the run it comes from, are in [index/instruments.json](index/instruments.json).

The sign-up was refused (`create-store` answered 427 and 422 `{"pass":false}`) while this machine reached BigCommerce
through a VPN (seen from GB); the store was made once the founder sent BigCommerce through the Yemeni network (seen
from YE). The sign-up's reCAPTCHA and the form of the store that was made were the founder's own hand
([index/run-notes.tsv](index/run-notes.tsv)).

## Where to start

| To find | Read |
| --- | --- |
| The sign-up form, its region choice, and what BigCommerce answered to each attempt | runs `20261029T004315Z-trial-signup-en` to `20261029T011432Z-trial-signup-ye-hand-en` (their `answers.jsonl`: `/api/trials/...`) |
| Where the store's country is held (Localization's "Default country", `store_country`), the standard formats by country, Payments, Currencies, Tax and Shipping | run `20261029T012951Z-store-settings-en` |
| The plans, the tax BigCommerce adds to its own fee by billing address (15 places), and its fee disclosures | run `20261029T015915Z-plan-upgrade-en` |
| The channels a store is offered and what more storefronts need | run `20261029T023811Z-channels-en` |
| BigCommerce's terms (the contracting entity by the merchant's country), fees and billing (taxes), pricing, API reference | runs `20261029T024622Z-legal-pricing-docs`, `20261029T025119Z-fees-and-billing` (`fetch.warc.gz`; `capture/warcbody.py` prints a page) |
| BigCommerce's Help Center articles on payments, tax, localization, invoices and multi-storefront | runs `20261029T024758Z-help-center-en` and after |
| What each API answered | each browser run's `answers.jsonl` and `answers/` |
| Every run, and what is unusual about one | [index/runs.tsv](index/runs.tsv), [index/run-notes.tsv](index/run-notes.tsv) |
| Every self-description seen, held or not | [structures/REGISTER.tsv](structures/REGISTER.tsv) |
| What is not held yet, and how it can be | [GAPS.md](GAPS.md) |
