# Plan and status

Where the work stands, so it can be resumed or extended; updated at every checkpoint. What is not held for a
platform, with its route, is in `<platform>/GAPS.md`; what is unusual about a run, in `<platform>/index/run-notes.tsv`.

## Status (2026-10-28)

- Zid: the dashboard's route manifest, page index and locales (English and Arabic) are structures; its code is held
  in run 20261028T143118Z-dashboard-code. On the demo store, the manifest's routes are opened in English
  (`zid/index/ledger/dashboard-routes.tsv`). The demo store refuses changes and is not offered Markets.
- A development store of our own (3277610, from the partner account) holds Markets as far as Zid offers them to a
  store with `must_use_markets_pricing` false (`zid/GAPS.md`). The public sign-up stops at its WhatsApp phone code.
- Browsers: `capture-profile` on port 9230 (the demo), `capture-profile-signup` on port 9240 (the partner account and
  the development store). Ports 9231 and above, other than 9240, are observed-sa's.

## Status (2026-10-29)

- BigCommerce: a trial store of our own (`bigcommerce/README.md`). The six questions are answered as far as a trial
  store and BigCommerce's own terms and Help Center go; what needs a paid plan (BigCommerce Payments' onboarding and
  KYC, a second storefront, an invoice) is in `bigcommerce/GAPS.md`.
- WooCommerce: a test store of our own on this machine (`woocommerce/README.md`): where it holds its country, what a
  country change does with orders and tax rates, the set-up's and the Payments page's checks of the country, the code.
  With the WordPress.com connection: WooPayments' test account, a country change with it, and the live verification's
  requirements for the US, the UAE and the UK; Stripe's later screens need a phone in the account's country
  (`woocommerce/GAPS.md`).
- Browsers: port 9250 BigCommerce (`capture-profile-bigcommerce`), 9251 WooCommerce (`capture-profile-woocommerce`),
  9222 the capture inbox (observed-sh's profile). The WooCommerce store's containers (`woocommerce-capture`) and its
  tunnel run on this machine; the tunnel's address is `SITE_URL` in `.env`.

## Next

1. Zid: the development store's storefront, page by page (theme, cookie banner, language and country control,
   footer), and the routes that take an id, item by item.
2. Zid: the dashboard's API calls as a structure, read from `assets/api-resources-<hash>.js` with a JavaScript parser.
3. Zid: the new Partners Dashboard (`partners.zid.sa`) and the older merchant dashboard (`web.zid.sa`).
4. BigCommerce and WooCommerce: the founder's go of 2026-10-29, ten questions first (each can change the knowledge
   map's S-02 analysis); each platform is pushed when done, with the knowledge map's branch.
   - BigCommerce, on a trial store: (1) the documents or checks BigCommerce Payments' KYC asks for, and whether they
     differ by the store's country; (2) whether anything checks the store's country (Store profile and Locale, the
     sign-up country, the hosting region); (3) the taxes BigCommerce adds to its own fees, and what decides them;
     (4) whether a new store's units, date format and time zone follow its default country; (5) whether a storefront
     or channel can sell through an entity other than the merchant, or a merchant of record; (6) what sets the
     store's tax obligations by its country (the automatic tax settings).
   - WooCommerce, on a test store with WooPayments in test mode: (1) where the store's country and WooPayments'
     account country are held; (2) what changing the store's Country / State does once there are orders, tax rates
     or a WooPayments account; (3) whether any of those countries is checked beyond the form; (4) the documents
     WooPayments' verification asks for, and whether they follow the country.

## Starting new work

1. What is held: `README.md`, then the platform's `README.md`.
2. What is not held: the platform's `GAPS.md`; `docs/OPERATING.md` for the browser, journeys and fetches.
3. After the runs: `docs/OPERATING.md`, "After any run"; then this Status.
4. Resuming: `git log --oneline -5`, then this Status.
