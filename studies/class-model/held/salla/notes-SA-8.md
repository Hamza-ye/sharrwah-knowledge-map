# Held pass, Salla, batch SA-8: notes

104 entries of `dashboard-app-routes` (items.jsonl lines 154 to 1156: the apps localization, gamification, feedback, devstore, chat, ai-agent, the Salla Ads apps (youtube, xio-v2, utils-v2, tools, tiktok-v2, snapchat-v2, smart-campaigns, payment, meta-v2, manageads, google-v2, dashboard-v2, dashboard, campaigns-v2), abandoned_carts, and `salla-search-provider-package`). Evidence at observed-sa@b0bd0b163.

**Placed:** 61 entries on capabilities, in 70 lines; 0 `new`; 43 `out`, in 8 lines. Twelve entries take two lines (1, 5, 25, 36 to 39, 43 to 46, 58); entries 11 to 14 share one line. 78 lines in all. Every line supports `core` but one: 58's line on CM-MKT-008, `shows`. No `own-service`, no `extension-point`, no quality. Scope on six entries: `salla_chat` (18, 19, 20, 24) and `plan not basic` (31 to 33). Fillers are the ad platforms the entry's words name (youtube, snapchat, tiktok, google, meta), as CM-MKT-010's cell holds them from its plan line.

Entry numbers below are the batch's order (`held_entries.py show --batch SA-8`). Bundles are cited by their record in `raw/runs/20261008T115555Z-dashboard-bundles/fetch.warc.gz`, with offsets from that run's `fetch.cdx`.

## How I read the entries

I kept SA-7's eight rules. Two of them did most of the work here:
- **Rule 3: what the route renders.** Each catch-all `*` route of a Salla Ads v2 app renders that app's main page, so it goes on the app's capability, as CM-MKT-010's or CM-MKT-020's cell already cites the app.
- **Rule 4: breadcrumb label objects** (keys: `label`): the youtube app's `/brand-reach`, `/video-views` and `/campaign/reciept`, the tools app's `/snapchat` to `/meta` and `/snapchat/authenticate`, and the ads dashboard's `/home` and `/dashboard`. Each goes where its route goes. Here every label has its route in the same app.

Rules 5 and 6 gave two new kinds of line:
- **Store gates read from the bundle, as scope (rule 6):**
  - the chat app wraps `/channel/chat/*`, `/manage-agents` and `/bots/*` in the guard `S9({feature:L3.APP_CHAT,mode:"page"})`, where `APP_CHAT="salla_chat"`, and embeds `/channel/whatsapp/*` with `feature:"salla_chat"`. Their scope is `salla_chat`, CM-SUP-004's released flag;
  - the YouTube app sends a store whose plan is `basic` to `/billing` (`getStoreInfoDetails?.data?.plan==="basic"&&r5("/billing")`). I wrote its routes' scope as `plan not basic`, a reading: the source names only the plan it excludes. The labels 28 to 30 sit outside that gate, so they carry no scope.
  - No other app in this batch has a route gate in its bundle (I searched every bundle for `feature:` guards and `plan===`).
- **Staff permissions stay in `reading` (rule 6):** abandoned carts' `forget_cart_rule` and `forget_cart_management`.

**Objects that are not routes** (the register says such objects are listed too):
- 26, the ai-agent app's `/`: a cookie helper's default option, `{path:"/"}`;
- 27: a progress bar's class names;
- 35, 48, 50, 53 and 60: a mapper that turns an ad platform's targeting interests (`IN_MARKET`, `AFFINITY`) into `{id, name_en, name_ar, path:"/", parentId, source}`;
- 69 to 104: the request paths of the Algolia API client that `salla-search-provider-package` bundles. Its user agent is 'Algolia for JavaScript', and its paths are `/1/abtests`, `/1/indexes/*/queries`, `/1/incidents` and the like.

All of these are `out`, as the software's own bookkeeping: none names a place of Salla's. That is the nearest of the brief's out kinds; a third party's API paths aren't listed among them by name.

**A checker point for SA-9 to SA-14:** a reading must hold no double quote (`"`). My first write quoted bundle code with its double quotes, and the checker read those rows as broken, leaving 57 entries unplaced. So a quote from a bundle has to be a part without `"`, as SA-7's were.

## The CHANGES lines

- **CM-ONB-004@salla becomes held, core** (3, `/gamification/*`). The app is the merchant's setup tasks: 'Your success path', 'Keep moving forward and complete tasks that drive you toward ongoing success.' (`20261008T141131Z-sweep-merchant-en/steps/160.text.txt`), and its locale, 'Kickstart your business with a guided path that helps you achieve your first 5 orders through clear steps and simple tasks.' CM-ONB-004 names 'the setup tasks'. SA-7 made the same cell held, from `/persona/*`, and the coordinator hasn't applied it yet, so the checker shows it again. Kept.
- **CM-MKT-008@salla becomes held, by a `shows` line only** (58, `/marketing/ads/manageads/utm-builder/:id?`). The UTM Builder is Salla Ads' own tool, so its `core` line is on CM-MKT-010. Its page says 'UTM parameters are tracking codes used by tools like Google Analytics to identify website traffic from specific sources.' That is the input to attribution; no held statement says orders are credited to marketing. So the line is `shows`, and the cell stays without a placement. Kept, unsure. The alternative is no CM-MKT-008 line at all.

## Entries I couldn't tell, and what would settle each

- **1 and 2, `/localization/*` and `/localization/settings`.** CM-MKS-008's Salla cell (languages) cites the app `@salla.sa/ui-merchant-localization` at `/localization`. But what the app shows is markets and branches, not languages:
  - its page on the Pro demo store is Multi-Warehouse Management ('Bring your store closer to your customers', `20261008T133523Z-sweep-demo-store-en/steps/111.text.txt`);
  - on the Special store the same route is Multi Market (`20261028T153241Z-journey-markets-public-demo-en/steps/005.text.txt`);
  - its locale holds `basic_branch_management` and `advanced_store_management` (markets).

  I placed 1 on CM-INV-005 and CM-MKS-001, and 2 on CM-MKS-001. The coordinator may want CM-MKS-008's evidence row for the app read again: a market's languages are set there, which CM-MKS-008's note allows.
- **15 to 17, `/store-dev/*`.** Placed on CM-DVT-004, whose cell cites the app. What the pages state:
  - the first page shows terms, among them 'الموافقة على شراء هذا المتجر من خلال منصة الشركاء والمتاجر المتوفرة' (`structures/salla/dashboard-translations/en/devstore.json`);
  - the checkout pays with `source:"transfer_store"`, by card or Apple Pay;
  - the payment page reads 'التاجر لديه متجر من قبل'.

  So the app is where a merchant agrees to and pays for taking over a store from the Partners platform. That is a lead for CM-DVT-005 (ready stores), whose note says who buys a ready store isn't stated. A statement naming the store the merchant pays for would settle it.
- **18, `/channel/chat/*`.** Its landing says 'Salla Chat is no longer available for new subscriptions.' (`20261008T133523Z-sweep-demo-store-en/steps/063.text.txt`; the journey `20261008T223648Z-journey-salla-chat-demo` found no subscribe control).
  - I kept `core`: the routes are Salla's own, for subscribers, with agents, bots and notifications.
  - The alternative is `shows`, by the ruling after WC-5 (an offer stated unavailable where it is listed). The statement is a run step's, so it isn't the line's scope (SA-7's rule 7).
- **21, `/channel/chat/error`.** Placed on CM-SUP-004, as SA-7 placed `/auth/error` on its app's capability. `out` is the alternative.
- **24, `/channel/whatsapp/*`.** Its breadcrumb reads Sales channels > Whatsapp, and it embeds `/services/whatsapp` under the feature `salla_chat`. I placed it on CM-SUP-004 only: the cell cites the chat app's path `whatsapp`, and Sales channels is where it sits. The page showed nothing but the breadcrumb, so whether it is WhatsApp as a sales channel (CM-CHN-001) isn't shown.
- **25, `/channel/chat/notifications`.** Its breadcrumb is 'Whatsapp Notifications', with customer, order, employee, product, abandoned cart and receipt notifications. I gave it two lines: CM-SUP-004 (the chat app's page) and CM-NTF-004 (delivery by WhatsApp). I gave no line to CM-NTF-001, the parent.
- **36 to 39, and 43 to 46, the ads tools' platform routes and their labels.** Each takes two lines:
  - CM-MKT-010, linking the store's ad account: the page 'Connect and manage your ad accounts, tracking pixels, and product catalogs across multiple platforms.';
  - CM-MKT-009, the pixel: the bundle names each route `routeToPixel`.

  The ad platform is the filler of both lines. The leads CM-OPS-004 and CM-PTN-009 came from the word "tools" and are no leads.
- **51, `ui-merchant-ads-smart-campaigns`.** Placed on CM-MKT-010, whose cell cites the app. Its locale isn't held, so what a smart campaign is isn't stated.
- **59, `/marketing/ads/manageads/invoice`.** Placed on CM-MKT-020 (the ads wallet): 'Used balance', 'Available balance', 'Amount Due', 'Next billing date'. CM-PTN-004 (partner billing) was the lead, from the word "invoice": not this.
- **33, 55, CM-MKT-012 as a lead.** Not Salla Ads: no held statement says it is paid per conversion, or run in Salla's own channels.
- **68, `/marketing/carts/bulk`.** The bulk reminder sent to the selected abandoned carts. I placed it on CM-MKT-022 (recovery); its parent route `/marketing/carts/*` is CM-CHK-007's.

## What a source or run step states that no entry holds (for the second stage)

- **CM-SUP-002:** the reviews settings' 'Request store review', 'Request shipping review', 'Request product reviews' (`20261008T133523Z-sweep-demo-store-en/steps/164.text.txt`). The same page holds many settings for CM-SUP-001, such as 'Allow attachments in reviews' and 'Hide customer name', and 'Show reviews in the store app', 'Display customer reviews inside your store app built with the App Maker.'
- **CM-SUP-004:** the Salla Chat FAQ (`index/run-notes.tsv`, `20261008T223648Z-journey-salla-chat-demo`):
  - 'Yes, Salla Chat is available only for Salla merchants.';
  - 'Yes, there are three monthly plans with a certain number of agents to access Salla Chat.' (a plan or price lead);
  - '… or by subscribing using the Salla apps' store.' (Salla Chat sold in Salla's app store: who makes it isn't stated, a maker gap for CM-APP-011);
  - connecting WhatsApp by signing in with Facebook.
- **CM-MKS-001, CM-INV-005:**
  - the activation's warning, 'Once enabled, it cannot be disabled except by contacting the Account Manager.' (`20261008T165800Z-journey-localization-demo`, run note);
  - the market wizard's countries (`20261028T153241Z-journey-markets-public-demo-en/steps/007`);
  - the locale's 'special_label' 'Available on' 'Special' (`localization.json`), a plan lead.
- **CM-ONB-004 and the payments cells:** the success path's tasks name instalments 'For Plus plan' and Salla Point: 'سلة بوينت تساعدك تستقبل مدفوعات تابي او تمارا داخل محلك التجاري بسهولة' (`20261008T141131Z-sweep-merchant-en/steps/160.text.txt`). This is a lead for the in-person payment and instalment cells.
- **CM-MKT-010:**
  - the new-campaign page's objectives: 'Website visits … 🚧 Unavailable', 'Application promotion', 'Interaction', and 'New' 'Sponsored Ads', 'Ads shown in Chat Feed will open full-screen when tapped.' (`20261008T133523Z-sweep-demo-store-en/steps/187.text.txt`);
  - the dashboard's 'Switch to v2.0' (`…/steps/026.text.txt`);
  - the TikTok banner offering matching ad credit up to 37,500 SAR (`20261008T181051Z-journey-salla-ads-demo`, run note), a quality or offer lead;
  - the xio-v2 bundle's 'Daily billing, cancel anytime', 'Daily budget must be at least {{min}} SAR' (`fetch.warc.gz@24882847`).
- **CM-MKT-020:** the ads dashboard's 'Store credits', 'Low balance', 'Top up' (`20261008T133523Z-sweep-demo-store-en/steps/190.text.txt`).
- **CM-MKT-009:** 'With Pixel + CAPI integration, you'll get precise data …' for Snapchat, and 'Meta Pixel and Conversions API' for Meta (`…/steps/179.text.txt`, `…/steps/183.text.txt`). Third parties' features connected by Salla: a lead for an `extension-point` reading by M-8, if the coordinator reads them so.
- **CM-MKT-011:** the audience manager's `showAIAudience` (AI audiences), and the targeting interests `IN_MARKET` and `AFFINITY` that the v2 ads apps map (entries 35, 48, 50, 53, 60).
- **CM-SFR-013 (storefront search):** `salla-search-provider-package` is an Algolia client (agent 'Algolia for JavaScript'), and its locale holds 'Trending searches', 'Search suggestions', 'Recent searches' (`structures/salla/dashboard-translations/en/salla-search-provider-package.json`). Where Salla uses it, and whether it is Salla's search provider, isn't stated (a maker and provider gap). observed-sa's docs/READING.md calls algolia.mahally.com 'the search behind Salla's marketplace': the capture's wording, not Salla's.
- **CM-DVT-005:** the devstore terms above, and 'سلة غير مسؤولة عن تشغيل واعداد المتجر او اي من خصائصه.' CM-DVT-004's cell already cites that sentence.

## A structure whose items and sources disagree

None in the values. The items keep only keys. As SA-7 found, a route's element, redirect, guard and permission are in the bundle alone, as are the objects that aren't routes (26, 27, 35 and the rest, 69 to 104).

## Problems with the brief or the script

- **A reading can't hold a double quote.** The checker reads such a row as malformed, and its message ('9 tab-separated fields, no quoting (it has 9)') doesn't say why. The brief's rule 7 says a quote is copied exactly. Code from a bundle almost always holds `"`, so only a part of it can be quoted. The brief, or the checker's message, could say so.
- **Leads from a common word:**
  - CM-OPS-004 (tools, status), CM-PTN-009 (marketing, tool), CM-API-007 (batch), CM-STF-001 (manager), CM-PTN-004 (invoice);
  - CM-AIA-005 for every chat route (by name: channel, chat);
  - CM-API-003 for `no-access`.

  None is the entry's thing.
- **The selection's rule keeps non-routes.** `dashboard-app-routes`' rule drops word lists and catch-alls by path, but keeps a library's API paths. The 36 Algolia paths alone are a third of this batch; a rule dropping the `salla-search-provider-package` items would spare a later pass.

## The coordinator's check (30 October 2026, after the batch)

- **Salla Chat's routes are `shows`.** The chat app's landing says 'Salla Chat is no longer available for new subscriptions.' (`20261008T133523Z-sweep-demo-store-en/steps/063.text.txt`), and the journey `20261008T223648Z-journey-salla-chat-demo` found no control to subscribe. So a store that subscribes now finds the app listed but unavailable, which the ruling after WC-5 places `shows`. All nine lines of the chat app's eight routes take it (18 to 25, with 25's CM-NTF-004 line), not only the four the guard scopes: the statement is the app's, whatever the route.
- **CM-SUP-004's Salla cell is read again at Salla's amendment.** It is `core` from its link, its dashboard apps, the released flag and its page (SA-S-5138). The same statement may make the cell `shows`.
- **CM-MKS-008's Salla cell is read again at the amendment too.** Its evidence row cites the app `@salla.sa/ui-merchant-localization` as languages, and the app's pages are markets and branches (entries 1 and 2).
- **`/store-dev` is a lead for CM-DVT-005** in the second stage: the devstore app is where a merchant agrees to and pays for a store taken over from the Partners platform (entries 15 to 17).
- **The Algolia client's 36 paths are all in this batch.** SA-9 to SA-14 hold none, so the selection needs no change for them.
- **A double quote now has its own message.** The checker said '9 tab-separated fields, no quoting (it has 9)', and the agent's first write lost 57 entries to it. It now says the row holds a double quote and how to quote without one (`method/held_entries.py`).
- **The cells this batch changes stand:** Salla's setup tasks (CM-ONB-004), as from SA-7's `/persona/*`, and CM-MKT-008, held by a `shows` line only.
- **Cost:** 15.5 million tokens over 83 requests, about 149,000 an entry. The yield is one cell beyond SA-7's.
