# Held pass, Zid, batch ZD-1: notes

153 entries: the dashboard's own index of its pages (`dashboard-page-index`, entries 1 to 119, all its items) and the first 34 routes of its route manifest (`dashboard-route-manifest`, items 2 to 35, the routes outside a store: subscription, access requests, store creation, payment links, password reset, sign-in by token, registration, suspended store). Evidence at other-product-class@0d79b794f.

**Placed:** 152 entries on capabilities (in 143 lines; entries 45, 50, 52 and 100 each take two lines), 1 entry `new`, 0 `out`. Every placement supports `core` except entries 12 and 13 (`extension-point`, apps' embedded pages). No `own-service`: no entry names Zid's company as a maker. Slot fillers: ZATCA (54), Mokafaa (87), Qitaf (88, 89), WhatsApp (91).

**How I read the entries.** A page-index entry gives only a pageKey, a path and a title. Where that left the thing unclear, I read:
- the item's source, `zid/structures/dashboard-page-index/source.js`, for each page's permission, its sidebar badge (`new`, `beta`) and the condition it is listed under (cited in readings as "source.js");
- the page as a run opened it, through `zid/index/ledger/dashboard-routes.tsv`. Readings cite it as "page text <run>#<step>", meaning `zid/raw/runs/<run>/steps/<NNN>.text.txt`. The run labels are:
  - `rest-en`: 20261028T160128Z-dashboard-routes-rest-en;
  - `gaps-en`: 20261028T150740Z-settings-gaps-en;
  - `en-2`: 20261028T145901Z-dashboard-routes-en-2;
  - `en-3`: 20261028T145905Z-dashboard-routes-en-3;
  - `api-en`: 20261028T155108Z-markets-api-en.

  The Settings landing page (gaps-en#2) gives a one-line description of each setting, and I placed the settings entries by those descriptions.
- for routes no run opened (or that only redirected the demo store), three namespaces of `zid/structures/dashboard-locales/items.jsonl`: `access-request`, `subscription` and `onboarding-wizard`/`home`. Selection marks the locales structure as not read (`read: no`). I used it only to read these entries, never as an entry. See "Problems" below.

Each of these readings is marked as one in its line.

## The new thing

**`new:Customer Referrals`.** Its entry is 86, ZD-E-381f5c01.
- **What it is:** a program in which each customer gets a referral code, and both the customer and the friend they invite are rewarded when the friend orders. The rewards are cashback (a percentage or a fixed amount) or loyalty points, released after a holding period. The rules include a minimum order value and a first order only (page text rest-en#195). Sidebar badge `beta` (source.js).
- **Its place of its own:** an admin route. The page index names it: pageKey `marketing.referrals`, path `marketing/referrals`. The route manifest also has `marketing/referrals` and `marketing/referrals/program` (ledger, opened rest-en#195 and #116; those routes fall in a later batch).
- **Proposed home:** domain D, area MKT, parent CM-MKT-005, following Zid's grouping under Marketing. LOY under CM-LOY-004 is the alternative, since its rewards are cashback and points.
- **Names:**
  - English: Customer Referrals (the page heading is "Customer referrals program");
  - Arabic: برنامج دعوات العملاء.
- **Searched:**
  - with `class_slice.py caps`: referral; referrals; refer a friend; دعوات العملاء; إحالة; الإحالة; دعوة صديق; invite; invitation; refer; referred; دعوة; دعوات; برنامج دعوات العملاء; ادع صديق;
  - with `search --platform zid`: referral; دعوات العملاء; إحالة.
- **What the searches found:** only CM-MKT-013, CM-MKT-014 (affiliates: partners promoting the store for commission, which is not buyers inviting buyers) and CM-PTN-008 (referral of the platform's plans), and no Zid statement.

## Entries I couldn't tell, and what would settle each

- **4, Zid Insights / نبض زد.** Placed on CM-ANL-001. Its page sells an analytics service on a 3-month free trial ("Ask your store data"; analyses such as Market Pulse and Competitor Watch). Three places are possible:
  - CM-ANL-005, Smart analytics (Salla's, undefined);
  - CM-AIA-001, AI tools;
  - a new capability.

  To settle: whether the coordinator joins Salla's undefined Smart analytics on role, and whether Zid Insights is billed apart from the plan (its trial suggests it is). The billing would show on the subscription or add-ons pages.
- **2, All analytics.** Placed on CM-ANL-003 from its pageKey `analytics.overview` and its permission, which requires every analytics view. Its page (`analytics/:tab?`) was not opened. A run opening `/analytics` would settle it.
- **39, llms.txt.** Placed on CM-AIA-005 (buyers' discovery through AI) by the page's words. It sits under SEO, so CM-CNT-007 is the alternative.
- **42, Settings, and the other containers.** I placed each container on the capability that its children's thing makes it:
  - 1 Analytics on CM-ANL-001;
  - 42 Settings on CM-ACC-006;
  - 59 Communications on CM-NTF-001;
  - 64 Store on CM-ACC-006;
  - 77 Marketing on CM-MKT-005;
  - 96 Logistics on CM-SHP-001;
  - 102 Payments on CM-PAY-002;
  - 109 Channels on CM-CHN-001;
  - 117 Apps on CM-APP-001;
  - 91 Whatsapp on CM-NTF-004;
  - 26 Online store on CM-SFR-001.

  The brief has a rule for what sits under a container, but none for the container itself. 42 is the weakest: Settings holds every setting, and I placed it on CM-ACC-006 only because Salla's "Settings" is in that capability's terms. `out` is the alternative.
- **50, Orders and products properties.** Two lines: CM-ORD-001 for its order properties and CM-CAT-001 for its product properties. Its order toggles also fit CM-ORD-010: minimum and maximum order, and automatically setting paid orders to "completed", which is Salla's own term there.
- **56, API integrations.** Placed on CM-APP-009 (the cell's direct API connection, خدمة الربط المباشرة (APIs)). The page generates a manager token "to connect Zid with other systems", so CM-API-002 (app authorization) is the alternative.
- **62, Product question notifications.** Placed on CM-NTF-001 as notification settings. CM-SUP-001 (product questions) is the alternative.
- **83, Automated Messages.** Placed on CM-MKT-006 (it is under Marketing, with "from a welcome to recovering an abandoned cart"). CM-NTF-001 is the alternative.
- **84, Marketing campaigns.** Placed on CM-MKT-007, not CM-MKT-005 whose name it shares, because its source item's permission is `SMS_CAMPAIGNS.manage` and its page lists SMS and WhatsApp campaigns to a segment.
- **106, Bank accounts.** Placed on CM-PAY-030, bank transfer. Its page says "These bank accounts will appear as payment methods for customers on your store. Manage your payout bank account separately", under the permission `PAYMENT_OPTIONS`. This contradicts the CM-PAY-030 cell's reading that the bank accounts page is the payouts page cited in CM-PAY-005. The coordinator may want to move ZD-C-004's page there.
- **133, reset-password, and 138, login/impersonate/:token.** Placed on CM-TRU-001 as sign-in routes. Neither was opened. For 133, CM-ACC-001 is the alternative. For 138, who impersonates is not stated: Zid's staff would make it CM-STF-005, a partner would make it `shows`.
- **143, 146, 147, register OTP routes.** Placed on CM-ACC-001 as the merchant's registration. No capability holds merchant sign-up as such (searched: sign up; register; registration; create store; التسجيل; إنشاء متجر; verification code; OTP; رمز التحقق). CM-TRU-001 is the alternative.
- **120, 142, 144, subscription routes.** Placed on CM-PLN-001. The checkout routes are paying for a plan, so CM-PLN-005 is the alternative.
- **121, 125, 137, access-request.** Placed on CM-STF-005 with `core`, because the locale strings name Zid's own technical team as the requester, not a partner. The brief's S7 rule (a partner's access is `shows`) would apply if the requester were a partner. A run that opens an access request would settle it.
- **122 to 124, 127 to 132, 134, 136, 139 to 141 and 145, create-store.** Placed on CM-ONB-004, the onboarding questionnaire. 130 and 131 (current-platform, platform-switch) may also bear on CM-MIG-005, but they are questions, not a migration service.
- **Badges.** Several pages carry the sidebar badge `new`, and 86 carries `beta`. The brief says how a flag that isn't released is placed, but has no rule for a route with a badge. I kept `core` and put the badge in the reading.

## A structure whose items and source disagree

**`dashboard-page-index`.** Its source holds 137 pageKey objects, but its items hold 119. The extractor drops these 18 (other-product-class@0d79b794f:zid/structures/dashboard-page-index/source.js):
- `dashboard`, `orders`, `orders.all`, `orders.manual`;
- `catalog`, `catalog.products`;
- `customers`, `customers.all`, `customers.groups`;
- `analytics.sales-reports`, `analytics.customer-reports`, `analytics.products`;
- `settings.general`;
- `channels.marketplaces`;
- the computed app entries `apps.${e.id}`, `apps.categories`, `apps.categories.${e.id}` and `apps.categories.${e}.${t.id}`.

**Why they were dropped.** Most have a conditional title (`t ? ngoTitle : title`, for charity stores) or a computed path or title. `dashboard` (empty path) and `settings.general` (an `alternativePaths` key before its title) are simple and still missing.

**What the items also leave out.** They don't carry each page's permission, badge or listing condition. The conditions include `mustUseMarketsPricing`, `hasNewGifting`, `customerWallets`, `showNewZones`, the blog's `is_enabled`, the Qitaf flags and the charity-store flag. Several readings depend on them (47/48, 51, 72, 81, 88/89, 97, 41).

**Route manifest.** Its item 1 (`root`, no path) is not an entry; the batch's manifest entries begin at its line 2. That is consistent with the ledger.

## Qualities seen on the pages but not in the entries

The brief takes a quality only where the entry states it, so I left these out. They belong to other structures or cells:
- Mokafaa's and Qitaf's earning and redeem rates by Zid plan (Rise 8.5% / 15%, Growth 8% / 13%, Professional 7% / ...; rest-en#35, #196);
- Zid Financing:
  - eligibility, sales over 40,000 in 3 months;
  - up to 10m;
  - a 10-25% annual profit margin;
  - 5-36 months (rest-en#156);
- Zid Insights' free trial of 3 months (rest-en#163);
- inventory addresses, "4 out of 6 available for activation" in the plan (gaps-en#34);
- the suspended store's "Your store information will be stored for 2 years" (dashboard-locales, `subscription:suspended.dialog.storeInformation`), a lead for CM-TRU-016.

The product feed's named platforms (Snapchat, TikTok, Google, Meta, X, OpenAI; rest-en#91) are on the page, not the entry, so I recorded no filler for 38.

## Problems with the brief or the script

- **What may be read to clarify an entry.** The brief says to read an entry's item at the source `entries.tsv` gives. For the page index, that source (a JavaScript module) states only titles, permissions and conditions. What a page is had to come from the run steps the ledger names, which the brief lists under `index/`, and, for unopened routes, from the locales that selection marks `read: no`. I took both as allowed for reading, never as entries. The coordinator should confirm this, since most readings of this batch rest on them.
- **No rule for a container entry itself**, nor for a route's release badge (`new`, `beta`). See the entries above.
- **Store-flag conditions and `scope`.** Several pages are listed only when a store flag is set. Since the entry states no plan or store, I left `scope` empty and put the condition in the reading. A rule would make the batches consistent.
- **The script:** the checker printed no problem besides the missing notes, which this file supplies.

## Corrections after the review (the coordinator, 30 October 2026)

The review (`held/review-H.md`, parts R4, R5a and R5b) and the coordinator's rulings (`held/review-H-rulings.md`) corrected this batch. 46 verdicts were applied as they stand; the coordinator's hand pass did the rest. Line numbers below are the review's, at `33946dbc`.
- **Zid Ads and Zid Voice (lines 13, 14):** `shows` on what each app does, since no maker and no gate are stated, and `core` on CM-APP-007 as the dashboard's page for an app (M-10).
- **Scope:** every store condition the source lists a page under is the line's scope, in the source's identifiers (M-11): `not an NGO store` (the charity store), `showNewZones`, `hasNewGifting`, `not hasNewGifting`, `mustUseMarketsPricing`, `customerWallets`, `hasPos or subscription.is_trial`, and `suspended store`.
- **Lines added:** the second capability a page names, on CM-NTF-002, CM-ACC-004 (twice), CM-ACC-007, CM-STF-002, CM-MKT-022, CM-MKT-002, CM-NTF-001 and CM-SHP-009; CM-INV-001 for the Inventory container; CM-PAY-012 for Mokafaa and Qitaf, whose points pay.
- **Moved:** reset-password to CM-ACC-001.
- **Readings corrected:** All analytics' permission (five named views); Zid Insights' missing maker statement; the POS reports and cashiers pages; where the registration's verification words are.
- **Not taken:** "Saudi Arabia" as Mokafaa's scope, read from a run page (M-12). R5b's CM-SHP-002 line for line 104 already existed at line 103.
- **Customer Referrals** stays new. Its parent is CM-LOY-004, since Zid's marketing page files it under loyalty and rewards (R5a), not CM-MKT-005.
- **Kept as placed, can't tell,** with what would settle each in the review's rows:
  - the online store's settings page and zones, shown only under `showNewZones`;
  - the platform-switch and where-do-you-sell routes;
  - who signs in by the impersonate token.

**The coordinator, after SA-2 (30 October 2026):** this batch's llms.txt line on CM-AIA-005 is `shows` now, and the entry takes CM-CNT-007 `core`. A store's llms.txt is a file the platform writes for AI platforms to read the store; it gives buyers no channel and no purchase, and Zid keeps it in its SEO section (`review-H-rulings.md`, the ruling after SA-2).
