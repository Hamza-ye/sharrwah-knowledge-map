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
- Zid's public sign-up: email, then personal information (name, phone with a country list of 207 codes, Yemen among
  them), then store details. The emailed code expires fast: typed after about two minutes it answered "Verification
  code has expired"; the founder typed a resent one by hand and it passed. The phone step answers "Verification code
  is sent to your whatsapp number"; no message reached the founder's Yemeni numbers.
- Zid's Partner Dashboard (`partner.zid.sa`) registers a partner with no phone code (country list of 242 entries),
  confirms the email by a link, and makes a development store in one step (name and password). The development store
  is on `new_professional.lifetime`, has a primary market made with it (Saudi Arabia, SAR) and the flag
  `must_use_markets_pricing` false, like the demo. On it, `POST v1/markets` with the create form's body answered 201;
  the market could be published, listed, read and removed in the dashboard, and no settings page showed a market.
  Its country list on Business address has 162 entries; changing the store's country to Kuwait asked only for a
  district and a street, and left the currency (SAR) and the primary market (Saudi Arabia) as they were.
- The tracking apps (Google Analytics, Google Tag Manager, Meta pixel, TikTok pixel) each take one account code for the
  store in their App market page, with a second market present; Google Analytics accepted a G- code, not a UA- one.
- Zid's subscription checkout, read with the development store's country set in turn: the price is in the country's
  currency and the VAT line, labelled "VAT %15" in every answer, is 15% for Saudi Arabia and Syria, 14% for Egypt and
  0 for Kuwait, the UAE, Oman, Bahrain and Qatar; every checkout links zid.sa's terms. zid.sa's and zid.eg's terms
  name AlQudrah AlTaqniyah for Technology and Communication Company LLC (CR 1010365366) and Saudi law; their pricing
  pages give its VAT number. The address page's country list can select an option on the click that opens it (it
  opens over the field); the address can be set through the call its form makes (POST
  v1/managers/store/business-place).
- Route sweeps: a page takes 25 to 80 seconds to settle (the dashboard keeps connections open, so the network-idle
  wait runs its full 10 seconds), and the machine was shared with other capture work (load 16 to 28 on 4 cores). With
  three sweeps at once (one in the profile's window, two in fresh-context windows), run
  20261028T144855Z-dashboard-routes-en lost its step 18 screenshot to the 30-second limit; the sweeps were closed after
  their current step (30 routes held) and the routes are taken one run at a time.

## 2026-10-29

- The founder's go for BigCommerce and WooCommerce, ten questions first (`docs/PLAN.md`, Next 4); each platform is
  pushed when done, with the knowledge map's branch. The capture tools now keep the IP a platform's edge reports whole
  (the founder, 2026-10-28: no masking in any repository); `capture/jstep.sh` drives a live journey in one command and
  `RUN_ADOPT_PAGE` lets a run take over a tab a person left (a ticked CAPTCHA).
- BigCommerce's trial sign-up asks no country, only where the store is hosted (North America, the default; Europe;
  Asia-Pacific). Through the VPN this machine sends BigCommerce's domains through (seen from GB), `create-store`
  answered 427 and then 422 `{"pass":false}`, for a scripted form after the founder's reCAPTCHA tick and for the
  founder's own hand-typed form, with two email addresses; the page said "An error has occurred, please contact
  support." With BigCommerce sent through the Yemeni network (seen from YE, Cloudflare's Muscat edge) the founder's
  hand-typed form made the store. Its "Default country" (Localization, `store_country`) came out as Oman, its currency
  OMR, a shipping zone named Oman; units KGS/Centimeters and date "24th Jul 2020" are what "Set standard formats for
  Oman" gives (the same for the UK, Saudi Arabia, Yemen and Japan; the US and Germany differ), and the time zone is
  London (GMT), which no country's button changed except Germany's. The default country saves to any of 245 countries
  with no check and changes neither currency nor formats. A trial store has online payments off ("Please switch to a
  paid plan").
- BigCommerce adds tax to its own plan fee by the billing contact's address: on the Core annual checkout ($348.00),
  $34.80 Sydney, $69.60 London, $66.12 Berlin, $22.96 Austin, $30.89 New York, $36.71 Seattle, and $0.00 Los Angeles,
  Toronto, Tokyo, Singapore, New Delhi, Riyadh, Dubai, Sana'a and Muscat. Its terms name the contracting entity by
  the merchant's country of residence (US, UK, EU, Australia, any other) and state that all fees exclude taxes, which
  the merchant pays. Its invoice article: a payment fails with "MAX 7" when the device's IP location is too far from
  the billing address, a VPN included.
- BigCommerce Payments (powered by PayPal) is for paid-plan stores located in the UK or the US with a UK or US PayPal
  Business account; its KYC status appears in the account's Actions. Multi-storefront: a storefront's store profile
  (name, address, email, phone), default country, language and formats can be its own, and one payment provider can
  be set up with several merchant accounts assigned per channel; more storefronts need a paid plan. Automatic tax
  applies where the merchant targets a provider by country and subdivision, Basic Tax elsewhere.
- WooCommerce: a test store on this machine (Docker; WordPress 7.1.4, since WooCommerce 11.2.1 asks for 7.0) reached
  through a Cloudflare quick tunnel (Claude Code's auto mode refused to start the tunnel until the founder allowed its
  command). WooCommerce's set-up filled "Where is your store located?" with Yemen, where WordPress.com places this
  browser, but its list matched no entry for Yemen; choosing another country brings "It looks like you're located in
  Yemen. Are you sure you want to create a store in ...? Setting up your store in the wrong country may lead to ...
  Tax and duty obligations, Payment issues, Shipping issues", which does not stop the set-up. The set-up saves the
  country (`woocommerce_default_country`, country and state in one option) and sets currency and units from it; its
  free features follow the country (WooPayments for the US, the UK and the UAE, not for Saudi Arabia, Oman, Yemen or
  Egypt). Settings > Payments has a "Business location" of its own, held per user (`woocommerce_payments_nox_profile`,
  else the store's country), and WooPayments' `supported` follows it, not the store's country: true for the US, the
  UK, the UAE and Japan, false for Saudi Arabia, Oman, Yemen and Egypt. Changing the store's Country / State with two
  orders and two tax rates saved with only "Your settings have been saved."; currency, rates and orders stayed as they
  were. WooPayments' own code reads its account country from the account data WooPayments' server returns
  (`wcpay_account_data`, United States when there is none). WordPress.com answered the store owner's connection with
  "Confirm you are human", so a WooPayments account and its verification wait for the founder.
