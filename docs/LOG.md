# Log

Dated record of the work: what was decided, what was measured.

## 2026-10-28

- The founder: Zid's evidence, and later BigCommerce's, WooCommerce's or any other platform's, is held here, one
  folder per platform (Shopify stays in observed-sh, Salla in observed-sa). Recordings are in English from first step
  to last; the Arabic pass is work of its own. Evidence is held and pushed as observed: no masking or holding back for
  tokens, cookies or passwords. Any of the capture email addresses may be used where a step needs one.
- Zid's demo, `https://dashboard.zid.sa/<lang>/demo`, signs any visitor in to the merchant dashboard as the owner
  (role `store.owner`) of Zid Demo Store, store 127604, on the Professional plan (`new_professional.yearly`, to
  2026-11-05); every visitor shares the store. `/en-sa/` paths give the dashboard in English (page `lang` en). The
  sign-in call (`POST hermod.zid.sa/v1/managers/login`) answered 429 once, in run
  20261028T144855Z-dashboard-routes-en, and the step stayed on the login page.
- The dashboard is a React Router application: its shell page names `assets/manifest-<version>.js`, the route manifest
  (437 routes; version 28c22f5b, then 48694231 within an hour). Every code file names a source map; each `.map`
  address answers 301 to `/assets/nope.json`, an empty map. The entry module states the 79 locale namespaces of each
  language, English and Arabic, with their versions. One module states the dashboard's page index (119 pages).
- The store's feature flag `must_use_markets_pricing` is false (feature-flags answer): the settings page leaves out
  Markets (the page index puts it behind that flag), while the plan policy `markets_management.active_markets` is
  enabled with a limit of 5 and `/settings/markets` opens, with no market and a Create button. Languages & currencies
  holds one currency per country (Saudi Arabia, default; Kuwait, Bahrain, UAE, Oman active).
- The storefront `https://zid-demostore.com/` declares an address per language and country (hreflang ar-sa at the
  root, en, ar-kw, en-kw, ar-ae, en-ae, ar-bh, en-bh, ar-om, en-om). On `/en/` its page text is Arabic, a landing page
  for a shaving kit with a footer giving a phone, a VAT number and the handle @rsmstoresa.
- The demo store refuses changes. The dashboard's create-market route sends a store whose `must_use_markets_pricing`
  is false back to Settings (its loader, `assets/markets_.create-<hash>.js`). `POST hermod.zid.sa/v1/markets`, sent
  from the dashboard page with the dashboard's own headers and the create form's body, answered 403 "Authentication
  credentials were not provided."; a save of Checkout page options answered 403 "This action is not allowed on demo
  store"; the dashboard's own `POST /v1/analytics/sales-over-time` answered 403 `DEMO_STORE_WRITE_BLOCKED`. The demo
  shows the store; a store with markets needs a store of our own.
- Route sweeps: a page takes 25 to 80 seconds to settle (the dashboard keeps connections open, so the network-idle
  wait runs its full 10 seconds), and the machine was shared with other capture work (load 16 to 28 on 4 cores). With
  three sweeps at once (one in the profile's window, two in fresh-context windows), run
  20261028T144855Z-dashboard-routes-en lost its step 18 screenshot to the 30-second limit; the sweeps were closed after
  their current step (30 routes held) and the routes are taken one run at a time.
