# Held pass, Zid, batch ZD-6: notes

87 entries: the last 13 routes of Zid's `dashboard-route-manifest` (the sign-in, registration, store list, root and demo routes, all children of `root`), then all 74 entries of `plans-offered`, the plans the dashboard's API offered the demo store. Evidence at other-product-class@0d79b794f.

**Placed:** 86 entries on capabilities, 1 `new`, none `out`, in 105 lines. Every line supports `core`. No `own-service`: no entry names Zid's company as a maker (Zid Payments, Zid POS Go, Zid Financing and Zid Academy carry the brand in their names only, which names no maker; each is `core` as a plan line that includes it, M-9). No `extension-point` and no `outside`. Slot fillers: Apple Pay (the Apple Pay lines) and WhatsApp (the free WhatsApp lines), each named in the entry's own words, as the model's other cells take them.

## How I read the entries

**The routes.** A route entry gives only its id, parent, path and index flag. As ZD-1, ZD-4 and ZD-5 did, I read the route's item in `zid/structures/dashboard-route-manifest/items.jsonl` (lines 425 to 437) for its module and imports, the ledger `zid/index/ledger/dashboard-routes.tsv` for what a run did with it, the run steps it names, and, for the routes no run rendered (the demo redirected them to the store), the dashboard's own strings in `zid/structures/dashboard-locales/items.jsonl`, cited by namespace and key. Run labels in the readings:
- `signup-en`: 20261028T155912Z-signup-en (register, register/otp, register/info opened);
- `en`: 20261028T144855Z-dashboard-routes-en (login at step 1; the plans page at step 18);
- `rest-en`: 20261028T160128Z-dashboard-routes-rest-en (steps 236 to 247, these routes, nearly all redirected to the store).

I kept to the earlier batches' placements: the registration routes on CM-ACC-001 (ZD-1's phone and email codes, ZD-4's mobile, details, location and complete steps), the sign-in routes on CM-TRU-001 (ZD-4's one-time link, ZD-1's impersonate), the account's own password recovery on CM-ACC-001 (the review's move of ZD-1's reset-password), and the store's root on CM-ANL-003 (ZD-4's and ZD-5's store routes). No module of these routes imports a guard, so no route line has a scope.

**Containers (rule 3).** The checker notes `register` and `login` as containers by path: `register` holds `register/store`, `register/info`, `register/otp` here and `register/phone-otp`, `email-otp`, `mobile-otp`, `mobile`, `details`, `location`, `complete` in ZD-1 and ZD-4; `login` holds `login/password`, `login/passkey`, `login/otp`, `login/2fa` here and `login/otl/:token`, `login/impersonate/:token` in ZD-1 and ZD-4. Each has a page of its own, whose thing its title names: the registration (CM-ACC-001) and the sign-in (CM-TRU-001). Their lines are on those.

**`plans-offered`.** One answer, `zid/raw/runs/20261028T144855Z-dashboard-routes-en/answers/hermod.zid.sa/v1/managers/purchasables/core-packages/packages/07336273fc4c2e535482483dc38d715602955483228508c9d673d97b8282e506.json`, read whole; the page it fed, 'Select your plan', is `en` step 18 (`steps/018.text.txt`).
- **The variants** (monthly, yearly) are the billing period: CM-PLN-002, with `parsable_duration` as the quality.
- **The packages** are plans: CM-PLN-001, with the price and the monthly price as qualities; CM-PLN-005 for `payment_methods`, the means the plan is paid with (credit_card; bank_transfer and credit_card on the yearly Growth and Professional); CM-PAY-007 for `zidpay_rates`, Zid Pay's rates by plan, on Growth and Professional (Rise's list is empty).
- **An advantage** is a plan line of its package. Its scope is its package's `code` (`rise.monthly`, `new_growth.monthly`, `rise.yearly`, `new_growth.yearly`, `new_professional.yearly`), the source's identifier for the plan and its period, so the monthly and yearly Rise lines stay apart. Each is placed on the capability whose cell already cites the same plan card from Zid's public plans page (ZD-S-0361 to ZD-S-0387, ZD-I-0389 to ZD-I-0405), as the readings say. Where an advantage names two things, it takes two lines: Apple Pay (CM-PAY-012, CM-CHK-008, as the model's cells do for ZD-S-0362); inventory management across branches (CM-INV-001, CM-INV-005); counting, transfer and display by city (CM-INV-003, CM-INV-006, CM-INV-010); external systems via API (CM-APP-009, CM-API-001); coupons discounts (CM-MKT-002 and its parent CM-MKT-001, M-6).
- **The common advantages** are `common_advantages`, the advantages common to all the answer's packages: their scope lists the five codes.

## The new thing

**`new:Demo store`.** Entry ZD-E-de67267d, `:lang/demo` (`$lang.demo`).
- **What it is:** Zid's public demo of the merchant dashboard. The module imports `demo-credentials`. The registration page links to it, 'Browse demo store' / تصفح المتجر التجريبي (page text signup-en#1; dashboard-locales `common:demoStore`), and the dashboard shows the demo's visitor 'Experience the store, not the idea.. Explore the demo, then launch yours' with 'Launch your store today' (page text en#18; `home:demo.title`, `home:demo.actionButton`; Arabic 'عيش التجربة كاملة مع المتجر التجريبي، وبعدها خذ قرارك'). Opened again in rest-en, it landed on the sign-in page (step 247, 'Zid | Login').
- **Its place of its own:** an admin route of the manifest, `demo`.
- **Proposed home:** domain A, area ONB, beside the store's sign-up and setup (CM-ONB-001, CM-ONB-004), with no parent; or `out` if the coordinator reads a sales demo as no capability the platform gives merchants. Not CM-DVT-003 or CM-DVT-004, the stores a partner or developer keeps.
- **Names:** English Demo store ('Browse demo store'), Arabic المتجر التجريبي.
- **Searched:** `caps --terms "demo; demo store; متجر تجريبي; تجريبي; free trial; trial; public demo; try the dashboard; demo account; sandbox; preview the admin"`: only CM-DVT-003 and CM-DVT-004 (partners' and developers' stores) and CM-PLN-001, CM-APP-004, CM-SHP-010 (trials of plans, apps and a feature).

## Entries I couldn't tell, and what would settle each

- **ZD-E-c8cef1a0, `register/store`, its CM-ONB-004 line.** The step's own strings are 'Store Details', 'Tell us about your store', 'Create store'. The locales don't say which registration step asks which field; the store category, what the merchant sells and whether it sells on another platform are left to this step only by elimination (the info step asks name and phone, signup-en#15; the location step country and city, `registerNew.formCard.steps.location`). Business type ('Select your business type') may be on it too, which would give it ZD-1's second line on CM-ACC-004. This line makes CM-ONB-004 held (CHANGES), as ZD-1's create-store lines already would. Settled by: the step as a new account sees it, which the sign-up run didn't reach (no phone code arrived).
- **ZD-E-31b8d07e, `stores` (the account's stores).** Placed on CM-ACC-001, the account's store list, as that capability's note holds Shopify's. Its page wasn't seen: the demo account has one store and was sent to it. If the page lets an owner hold and move between several stores, it is CM-ACC-003's too, whose Zid cell holds nothing. Settled by: the route opened by an account with two stores.
- **ZD-E-8667f838, the dashboard's root (`:lang`, index).** Only a redirect (module imports `return-to-redirect`), placed on CM-ANL-003 as the store home it opens. `out` is the alternative, if the coordinator reads a redirect as naming no place of its own (the brief: a route's redirect names another place).
- **ZD-E-b3ca70b4, International Selling / البيع للعملاء من معظم دول العالم.** Placed on CM-MKS-001, as the root of selling across countries. It names no markets, no merchant of record (CM-MKS-003) and no shipping abroad (CM-SHP-020). Settled by: what Zid says this line includes, which no held source states.
- **ZD-E-2ad982c1, ZD-E-2f16f350, 'Segment customers for exclusive offers'.** One line, CM-CUS-002, as the cell holds the same card. Whether "exclusive offers" is a second thing (CM-MKT-001's discounts for a segment) isn't stated.
- **ZD-E-9c16494b, 'Profitability and cost reports'.** One line, CM-ANL-002. "Cost" doesn't say whose: CM-CAT-012 (product cost) takes a line only if it is the products' cost, which the line doesn't state.
- **ZD-E-c0c871c2, ZD-E-39760160, Zid Payments 'to accept Mada, Visa, and Mastercard'.** One line, CM-PAY-002, as the cell holds the same card. Mada, Visa and Mastercard are networks inside Zid Pay in the cell's reading (شبكات الدفع); no capability holds card networks as such, and whether mada is CM-PAY-017's local method isn't stated.

## The shipping rates differ from the model's

The dashboard's answer gives shipping rates starting from 12 SAR on Rise, 11 SAR on Growth and 9 SAR on Professional. CM-SHP-002's Zid cell cites Zid's public plan cards as 11 SAR on Rise and 8.5 SAR on Professional (ZD-S-0365, ZD-S-0380). Both are Zid's own statements, from different sources and dates; the lines keep the answer's values as their quality, scoped to the package codes, and the coordinator may want the cell's reading to say both.

## A structure whose items and sources disagree

- **`downgrade_information`** is in the answer but not in the structure's rule (`nested:variants,packages,features,advantages,common_advantages`), so no entry holds it. It lists, for plans `essential`, `business`, `rise`, `growth`, `new_growth` and `professional`, what a downgrade loses, such as 'Number of Users: three', 'Buy Now, Pay Later, with Tabby, Tamara, and MisPay', 'Selling and issuing wholesale invoices B2B', 'Multiple taxes by country', 'Personalized storefront via Theme SDK', 'Direct integration through Zid'. It names plans not offered here (essential, business, growth, professional). A lead for the second stage, for CM-PLN-001 and the capabilities each line names; the rule could take it.
- **The monthly variant has no Professional package**; Professional is offered yearly only, at 20000.01 SAR (1666.66 a month). The items hold the answer as it is; the page at en#18 shows Rise and Growth only, monthly.
- **The page and the answer list different common features.** The page's 'All plans include' (en#18) shows 'Vibrant Zid communities', 'High converting checkout experience', 'Customizable storefronts', 'Integrated payment & BNPL options' and 'Flexible shipping integrations', and its 'Features' table (Team management: '1 User', 'Up to 5 users', 'Up to 20 Users'; Discounted shipping policies; Instant payment activation), from the dashboard's `subscription:features*` and `subscription:featuresTable*` strings, not from the answer's `common_advantages`. No entry holds them.

## What a source or run step states that no entry holds (for the second stage)

- `signup-en` steps 1 to 21 and `en` step 1 (the registration and sign-in pages), lines 12 to 15 of `001.text.txt`: 'Enjoy an Extra Free Year', 'Complete 96 orders and unlock an additional year of your subscription on us!', 'Earn Cashback on Every Order', 'Complete 100 orders and get 0.25% cashback for every completed order.': a plan offer and a cashback, for CM-PLN-001 and CM-PLN-002 (whose cell holds the plan cards' cashback).
- The same pages: 'Sign up with Google' (signup-en#1) and 'Login with Google' (en#1): sign-in with an outside account, for CM-TRU-001.
- `dashboard-locales`, `auth:mfa.rememberDevice`: 'Remember this device for 30 days', a duration of the two-step verification, for CM-TRU-001's qualities; `auth:mfa.backupCodeDescription`: backup codes that each work once.
- `dashboard-locales`, `auth:registerNew.platforms_*`: the platforms the registration asks a merchant moving from (Salla, Shopify, ExpandCart, Makane, Other), for CM-MIG-005.
- `en` step 18, `018.text.txt`: 'Save 16%' on the annual plan (CM-PLN-002); the FAQ titles (such as 'Is there a fee charged on sales?', CM-PLN-003); and the footer '© Zid 2026 commercial registration number 1010365366', for CM-ACC-002.
- `dashboard-locales`, `subscription:featuresTable.*` and `subscription:faqs.*`: the plans' features table and FAQ answers, such as 'merchants receive a free domain for the growth and' (`faqs.questions.canIPersonalizeMyStoreDomain.content`), for the plan cells.
- The answer's `downgrade_information` (above).

## Problems with the brief or the script

- **The checker's brand note** flags every `core` line on Zid Payments, Zid POS Go, Zid Financing and Zid Academy (10 lines). Each is a plan line that includes the thing (M-9): `core`, the brand naming no maker (B-extent). Zid Financing's maker is stated elsewhere in its cell (ZD-S-0692), which this line doesn't repeat.
- **The checker's first-lead notes** were each read: CM-DVT-003 (a partner's stores) isn't the account's stores; CM-ACC-003 is led by "store management" in the team lines, which name team access, not several stores; CM-EVO-001 is led by the word "features" in `header_line`; CM-MKS-003 (merchant of record) and CM-APP-010 (an app's settings) aren't named by International Selling or Marketing Pixels integration.
- No rule of the brief read differently from B-extent.md for this batch.
- The checker's final line: see the report.

## The coordinator's check (30 October 2026, after the batch)

- **The four cells this batch makes held stand,** each from a plan line that includes it: 'Marketing Pixels integration' (CM-MKT-009), 'Similar Products' (CM-MKT-023, as ZD-4's Similar products was decided), 'Hosting unlimited visitors and data' (CM-OPS-003) and 'Free SSL Certificate' (CM-SFR-010).
- **The shipping rates differ by source, and both stand.** The dashboard's plans answer, as this structure holds it, gives label rates from 12 SAR on Rise, 11 on Growth and 9 on Professional. Zid's public plan cards, which CM-SHP-002's Zid cell cites, give 11 SAR on Rise and 8.5 on Professional (ZD-S-0365, ZD-S-0380). Each is a fact at its own source and capture. At Zid's amendment, the cell's reading states both, with their sources, and doesn't choose between them.
- **Demo store** waits for Zid's other new things (Search, Services). The model holds no public demo of a platform's dashboard. Salla's evidence holds a public demo store too (the `public-demo@en` label in observed-sa), so the decision is made with every platform's cells.
- **For the second stage:** `downgrade_information` in the source answer, with what each plan loses on a downgrade, and the plans page's `subscription:*` features, which no entry holds.
