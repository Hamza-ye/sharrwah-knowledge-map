# Zid: what is not held yet

Each row: what Zid shows or publishes that this folder does not hold, why, and how it can be held.

| Not held | Why | Route |
| --- | --- | --- |
| The dashboard routes the ledger marks `not opened` ([index/ledger/dashboard-routes.tsv](index/ledger/dashboard-routes.tsv)) | not reached yet | a run that opens them in English on the demo store, one run at a time |
| The routes whose path takes an id (`:id`, `:code`, `:token`, …: 112 of the manifest's 437) | each needs an item of the store | journeys that open an item of each kind (a product, an order, a customer, a market, …) |
| The dashboard's API calls as items (method name, HTTP method, path) | the module is held as bytes (`assets/api-resources-<hash>.js`, run 20261028T143118Z-dashboard-code); its calls are minified and need a JavaScript parser to read | a structure read with acorn |
| The dashboard's original source | Zid answers every source map address with an empty map (`/assets/nope.json`, run 20261028T145949Z-dashboard-source-maps) | none: Zid does not serve it |
| Sign-up: what it asks, and the countries a new store can take | the demo signs in to an existing store | the sign-up journey on `dashboard.zid.sa/en-sa/register` with a capture email address |
| A store outside Saudi Arabia: its checks, its contract and the tax on Zid's fees | the demo store is Saudi | a store made at sign-up with another country, as far as Zid lets it go; the contract and the tax only Zid can state |
| Zid's own storefront themes as a buyer sees them (cookie banner, language and country control, footer contact details) | the demo storefront shows a landing page whose text is not the store's data (run 20261028T145325Z-storefront-first-visit-en) | the demo store's theme switched to a Zid theme for a journey, then back |
| The older dashboard (`web.zid.sa`), which the demo offers to go back to | not opened | a journey from the demo's "Back to the old dashboard" |
| Zid's other surfaces: help.zid.sa, docs.zid.sa, zid.sa, the app and theme markets, the partner dashboard, the mobile apps | not captured here; sharrwah-knowledge-map holds some of their pages (`evidence/product-class/`) | fetch runs from their sitemaps, and journeys |
