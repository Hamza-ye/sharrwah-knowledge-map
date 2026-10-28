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

## Next

1. Zid: the development store's storefront, page by page (theme, cookie banner, language and country control,
   footer), and the routes that take an id, item by item.
2. Zid: the dashboard's API calls as a structure, read from `assets/api-resources-<hash>.js` with a JavaScript parser.
3. Zid: the new Partners Dashboard (`partners.zid.sa`) and the older merchant dashboard (`web.zid.sa`).
4. BigCommerce, WooCommerce: when the founder says.

## Starting new work

1. What is held: `README.md`, then the platform's `README.md`.
2. What is not held: the platform's `GAPS.md`; `docs/OPERATING.md` for the browser, journeys and fetches.
3. After the runs: `docs/OPERATING.md`, "After any run"; then this Status.
4. Resuming: `git log --oneline -5`, then this Status.
