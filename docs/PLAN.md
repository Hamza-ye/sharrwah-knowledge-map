# Plan and status

Where the work stands, so it can be resumed or extended; updated at every checkpoint. What is not held for a
platform, with its route, is in `<platform>/GAPS.md`; what is unusual about a run, in `<platform>/index/run-notes.tsv`.

## Status (2026-10-28)

- Zid: the dashboard's route manifest, page index and locales (English and Arabic) are structures; its code is held
  in run 20261028T143118Z-dashboard-code. On the demo store, 57 of the manifest's routes are opened in English
  (`zid/index/ledger/dashboard-routes.tsv`), the settings pages sharrwah-knowledge-map's S-02 asks about first.
- The demo store refuses changes and is not offered Markets (`zid/GAPS.md`); a store with markets needs a store of our
  own.
- The capture browser is `capture-profile` on port 9230, signed in to Zid's demo. Port 9231 is observed-sa's.

## Next

1. Zid: the sign-up journey with a capture email address (what it asks, the countries a new store can take), and, if
   Zid offers it to the new store, Markets: a market's pages and every settings page again with a second market.
2. Zid: the dashboard's remaining routes (`zid/index/ledger/dashboard-routes.tsv`, status `not opened`), one run at a
   time.
3. Zid: the dashboard's API calls as a structure, read from `assets/api-resources-<hash>.js` with a JavaScript parser.
4. BigCommerce, WooCommerce: when the founder says.

## Starting new work

1. What is held: `README.md`, then the platform's `README.md`.
2. What is not held: the platform's `GAPS.md`; `docs/OPERATING.md` for the browser, journeys and fetches.
3. After the runs: `docs/OPERATING.md`, "After any run"; then this Status.
4. Resuming: `git log --oneline -5`, then this Status.
