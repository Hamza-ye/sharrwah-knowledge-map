# Held pass, Zid, batch ZD-CX: notes

**The batch:** 42 entries of `dashboard-page-index` (items.jsonl lines 59 to 100 at other-product-class@0d79b794f): Settings' groups Communications and Store with their pages, then Orders > Abandoned carts, five Customers pages, the Marketing group, the Whatsapp group and the Logistics group up to Transactions log. Worked from the brief `studies/class-model/briefs/H-held.md` at commit 657cd861, effort xhigh. A calibration batch: no other batch's placements or notes, and no review file, were read.

**Read:** the evidence map; other-product-class `README.md`, `zid/README.md`, `zid/GAPS.md`; `zid/structures/REGISTER.tsv` (rows of dashboard-page-index, dashboard-route-manifest, dashboard-locales); the structure's `meta.json`, `items.jsonl` and `source.js`; the Zid rows of `held/selection.tsv`; `zid/index/ledger/dashboard-routes.tsv` for each entry's route and steps; the run steps it joins, to clarify entries only; the model's cells for every lead and for each placement; B-extent.md, "Cells and evidence" and "Conventions from the dry run". Every run step cited below is under `other-product-class@0d79b794f:zid/raw/runs/`.

**Counts:** 42 entries: 41 placed on capabilities, 1 `new`, 0 `out`, in 55 lines (13 entries take a second line).

## What source.js adds to the items

The items leave out each page's permission, badge and listing condition. `source.js` (one line; offsets are characters) holds them, and they are read into the lines as the brief says:
- **Listing conditions, written as `scope` in the source's identifiers:**
  - `use-is-ngo-store` (imported as `N`, offset 1088; `s=N()` in `ht`, offset 23110): Stock notifications (offset 25229), Bundle offers (26192) and the whole Logistics group with its children (27915) are listed only where it is false: scope `not use-is-ngo-store`;
  - the flags of `use-feature-flag` (offset 1500; `{customerWallets:c,showNewZones:l}=P()`, 23259): Customer wallet (24586) and Cashback offers (26016) need `customerWallets`; Zones (28202) needs `showNewZones`. The demo store's feature-flags answer (`20261028T144855Z-dashboard-routes-en/answers/hermod.zid.sa/v1/managers/store/feature-flags/e8462761….json`) has `customer_wallets` true and `show_new_zones` false, and Zones answered 'This feature is not enabled for your store.' (`20261028T160128Z-dashboard-routes-rest-en/steps/169.text.txt`, line 31);
  - `be(Number(t))` of `automatic-discount-pilot-list-BzTPcabc.js` (offsets 1843, 23319, 25846): Automatic discounts, for the stores in a pilot list;
  - `rt(Number(t),!!(i&&!a))` (offset 23227), where `rt=(e,t)=>nt.includes(e)&&t` (6053), `nt` a list of 41 store ids (5771), and `i`, `a` the store's `isQitafEnabled` and `isMoneyHashQitafEnabled` (23179): the old Qitaf page (marketing/qitaf) is listed where it holds, the new one (marketing/new-qitaf, badge new) where it doesn't. The demo store, 127604, is not in `nt`;
  - `p=!!xe()` (offset 23310), `xe` being export `n` of `gift-2-line-Dg_SogQX.js` (offset 1908): Mokafaa program (26814). See "Couldn't tell".
- **Badges,** in `reading`: new on Customer wallet, Bank discounts, Cashback offers, Automated Messages, Mokafaa program, the new Qitaf page and Automatic replies; beta on Customer Referrals.
- **Permissions,** in `reading` only: no line rests on a permission alone (see "Problems").

## New things

**`new:Customer Referrals`:** entry ZD-E-381f5c01.
- **Its place of its own:** an admin route, the page index's page `marketing.referrals` (items.jsonl line 86) and the manifest route `$lang.stores.$storeId.marketing.referrals` (path marketing/referrals), opened in `20261028T160128Z-dashboard-routes-rest-en` step 195.
- **What it is,** from that step (a reading): the store's programme in which its customers get a code, and both they and the friends they invite are rewarded, 'Your customers gets a code, and when a friend they invite orders, both get rewarded.' (`…/steps/195.text.txt`, line 47).
- **Proposed:** domain D, area MKT. Its parent would be CM-MKT-013, Affiliate and creator marketing, by Salla's grouping: its dashboard app @salla.sa/ui-merchant-partner-marketing holds marketing/referrals beside marketing/affiliates (SA-S-3550, in CM-MKT-013's Salla cell). A reading. The alternative is CM-LOY-004, since the rewards include cashback and loyalty points (step 195, line 55).
- **Names:** Customer Referrals / برنامج دعوات العملاء (the page's heading: Customer referrals program).
- **Searched** with `caps`: referral; referrals; refer a friend; دعوات العملاء; برنامج دعوات العملاء; الإحالة; referral program; refer; invite; friend; إحالة; دعوة; ادع صديق; دعوات; word of mouth; customer referrals.
  - The hits are CM-MKT-013 (by its Salla path) and CM-PTN-008, the referral programme for the platform's own plans, another thing.
  - The checker's leads CM-CUS-001, CM-STF-002 (both by customer) and CM-MKT-005 (by marketing) were read: none holds a referral programme.
- **If the coordinator reads** Salla's marketing/referrals as this thing, the entry is CM-MKT-013's evidence instead.

## Choices made on the brief's rules (readings)

- **Containers (rule 3):**
  - Communications goes on CM-NTF-001, whose cell cites التواصل;
  - Store goes on CM-ACC-006, by its title Store (Merchant APIs > Account > Store) and the page its path opens;
  - Marketing goes on CM-MKT-005;
  - Whatsapp goes on CM-NTF-004, whose cell cites واتساب زد and Whatsapp;
  - Logistics goes on CM-SHP-001, whose cell cites لوحة التحكم > اللوجستيات > طرق الشحن.

  The own index pages of Marketing, Whatsapp and Logistics (steps 212, 166 and 155 of the rest run) show the same thing as their group (Marketing tools; Zid WhatsApp; the shipping setup), so none takes a second line.
- **The checker flags four containers, not Store.** `settings.store` is one too: `source.js` gives it a `children` array (offset 21789), but its children's pageKeys (settings.information, …) don't start with its own.
- **"The parent's thing where the entry's own words name it (its section is the parent's term)":** I read the section as the section of the title key. That gives these parent lines:
  - `settings:communications.abandonedCarts.label` takes CM-NTF-001;
  - `settings:landingPage.team.groups.label`, whose Arabic title مجموعات فريق العمل also names the team, takes CM-STF-001;
  - `navbar:whatsappMenu.liveChat` and `navbar:whatsappMenu.autoReplies` take CM-NTF-004.

  Every child's pageKey begins with its parent's key, so the pageKey prefix was not read as naming the parent. Otherwise every Customers page would take CM-CUS-001, every Marketing page CM-MKT-005, and every Store page CM-ACC-006.
- **A place a cell already cites takes the entry (rule 2):**
  - Store information is CM-ACC-004's, which cites Settings > Store > بيانات المتجر. It also takes CM-ACC-006, the store's details, which its words name;
  - Hours of operation is cited by both CM-ORD-010 and CM-ACC-007, so it takes both lines.
- **Notes followed:**
  - CM-CHK-007's note puts recovery messages in CM-MKT-022, so Abandoned cart reminders takes no CHK-007 line;
  - CM-MKT-001's reading puts Zid's bank and automatic discounts in its children, so they take no MKT-001 line.
- **Mokafaa and Qitaf:**
  - each goes on CM-LOY-004, as a loyalty programme the store offers (Zid lists them under Marketing, and their pages call them loyalty programmes);
  - each takes CM-PAY-001 too, since their points pay for purchases. The brief's own example says so of Mokafaa, and CM-LOY-004's note says Salla's مكافأة الراجحي is a payment method, cited in CM-PAY-001 (SA-C-119/decides/SA-S-1966);
  - the payment role rests on Zid's own pages, quoted in the lines (steps 208, 196, 219), not on Salla's cell;
  - the fillers are Mokafaa and Qitaf, which the entries name. Al Rajhi Bank and STC are known only from the pages, so they are in `reading`.
- **Whatsapp's filler:** the container's title names WhatsApp, the third party's service that carries the messages, so Whatsapp is its filler (a reading). The children name it only in identifiers (pageKey, path, title key), which, like a flag's name, make no filler.

## Couldn't tell, and what would settle it

- **The Mokafaa condition:** `xe()` is a minified export of `gift-2-line-Dg_SogQX.js`, a module the brief doesn't let me read. Its `scope` is written as the source's identifier, `xe() (gift-2-line-Dg_SogQX.js)`. Reading that module in run 20261028T143118Z-dashboard-code's `fetch.warc.gz` would settle what the condition is: a flag, a plan or a store kind.
- **Automated Messages (CHANGES):** I placed it on CM-MKT-006, marketing automations. Its alternative is CM-NTF-001, whose definition is 'the messages the store sends automatically to customers and staff'. I chose MKT-006 because Zid puts the page in Marketing, beside Communications, which holds the order notifications. What would settle it is the coordinator's line between marketing automations and notifications.
- **Automatic replies (CHANGES):** I placed it on CM-SUP-004 as one of the settings of chats with customers (its path is under services/whatsapp/settings). It has a place of its own (a page and a route), so it could be a new thing, an automated reply flow, if the coordinator holds that SUP-004 doesn't cover replies by a flow. Its page answered 'Oops! Something broke' (`20261028T160128Z-dashboard-routes-rest-en/steps/042.text.txt`, line 31). The WhatsApp settings page names the flow: 'Create an automated reply flow to guide customers to the right answer.' (`…/steps/137.text.txt`, line 35).
- **Live chat (CHANGES):** Zid's own chat with customers, CM-SUP-004 core. The cell's reading said no chat of Zid's own was held. It is built on Zid WhatsApp (NTF-004), whose page says 'Activation connects your store to WhatsApp Business API' (`…/steps/166.text.txt`, line 55).
- **Shipments tracking (CHANGES):** Zid's own page, so CM-SHP-017 core, plus CM-SHP-009 for the shipments list it shows. Its permission (`g.ZIDSHIP.view`, `g.ZIDSHIP.viewShipment`) ties it to ZidShip, CM-SHP-002's term. No line rests on that.
- **Transactions log:** I placed it on CM-SHP-002, from its page: shipping fees and COD settlement of labels bought through Zid. It could also be CM-SHP-009's (its key navbar:shipmentsTransactions; path under shipments), and its COD settlement is a lead for CM-PAY-029.
- **Discounts:** the second line on CM-MKT-002 rests on the title key navbar:coupons, which is in the entry's text.
- **Marketing campaigns:** its permission `E.SMS_CAMPAIGNS.manage` names SMS campaigns (CM-MKT-007), and its page shows SMS and WhatsApp campaigns (step 198). It takes no MKT-007 line, since the permission alone isn't the entry's words. If the coordinator reads a page's permission as naming its thing, MKT-007 takes a core line.
- **Legal pages:** its path channels/online-store/pages/legal opens the Legal Pages tab of the online store's Pages (`20261028T150740Z-settings-gaps-en/steps/054.text.txt`). It takes no CM-CNT-003 line; its words name the legal pages.
- **The checker's NOTE on line 8:** the first lead of Product review notifications that holds nothing is CM-API-009, webhooks set up in the admin, matched by "notifications". The entry is messages to customers, not webhooks, so no line names it. The same goes for the other notification entries.

## The structure against its sources

- **The items leave out** permissions, badges and listing conditions (known; brief, rule 1).
- **items.jsonl line 70** (settings.domains) has `title_ar` 'رابط المتجر الالكتروني' followed by a carriage return, which `entries.tsv` drops. The locale string carries it.
- **Two items share pageKey marketing.qitaf** (lines 88 and 89, ZD-E-b13ec16b and ZD-E-5eb861c2), with different paths and mutually exclusive conditions: one page listed two ways.
- **Pages with computed paths reach no entry,** the extractor's known fault (evidence map, R4): Zid Ads (`zidAdsPage`, `apps/${a}/embedded`, title navbar:zidAds), appended to Marketing's children at `...b?[b]:[]` (offsets 9385, 27257), and Zid Voice (`zidVoicePage`, offset 9519), appended to Orders' children at `...x?[x]:[]` (24222). Both are app pages for CM-APP-007 and their apps' cells, for a later batch or the second stage.

## What a run step states that no entry holds (for the second stage)

**`20261028T150740Z-settings-gaps-en/steps/`:**
- `027.text.txt`: lines 21 to 29, closing mechanisms 'Close store completely' and 'Stop receiving orders'. For CM-ACC-007 and CM-ORD-010.
- `028.text.txt`: line 20, 'Team members (0/20)'. A limit for CM-STF-001.
- `033.text.txt`: line 23, 'You can connect more than one domain, but you can activate only one.'; line 38, 'Request a free domain from Zid'. For CM-SFR-008.
- `050.text.txt`: lines 22 and 23, tabs Business details and Business address, for CM-ACC-004; line 36, social media accounts moved to Channels \ Online Store \ Brand.
- `049.text.txt`: line 21, order status messages not to be used for marketing, by the communication authority's regulations. For CM-NTF-001, and its slot filler هيئة الاتصالات.

**`20261028T160128Z-dashboard-routes-rest-en/steps/`:**
- `040.text.txt`: line 19, 'Recharge reminder credits'; line 44, reminder types by SMS, email and WhatsApp. For CM-MKT-022.
- `079.text.txt`: lines 20 and 24, automatic customer and merchant notifications on questions. For CM-SUP-001 and CM-NTF-001.
- `197.text.txt`: line 48, 'coupons, automatic discounts, progressive offers, and free shipping'. For CM-MKT-001 to 003.
- `212.text.txt`: line 45, Upcoming seasons; line 55, Marketing tools; line 74, 'Free shipping offer'. For CM-MKT-005.
- `208.text.txt`: lines 61 to 81, Mokafaa rates by plan (Rise: earning 8.5 %, redeem 15 %; Growth: 8 %, 13 %; Professional: 7 %, 10 %), and 'Every 1 SAR earns 10 points', 'Every 250 points convert to 1 SAR'. Qualities for CM-LOY-004 and CM-PAY-001.
- `196.text.txt`: the same rates for Qitaf.
- `219.text.txt`: line 47, 'Submitting requests to activate the Qitaf program is currently suspended.' (the old Qitaf page).
- `195.text.txt`: lines 55 and 57, the reward kinds and the anti-abuse rules of Customer Referrals.
- `213.text.txt`: lines 53 to 59, held balance, pending rewards and nearest expiry date. For CM-LOY-001.
- `137.text.txt`: lines 33 to 52, Replies flow, Quick replies, Tags, Store widget and 'Unsubscribe from messages'. For CM-SUP-004 and CM-NTF-004.
- `166.text.txt`: line 74, 'Messaging points are sold separately.' For CM-NTF-004.
- `155.text.txt`: line 32, Shipping rate calculator; line 40, Local delivery; line 52, Pickup in Store settings relocated; line 74, Other shipping providers. For CM-SHP-001, 006, 008 and 015.
- `032.text.txt`: line 33, COD settlement. For CM-PAY-029.

**`20261028T145901Z-dashboard-routes-en-2/steps/`:**
- `005.text.txt`: lines 24 to 28, reviews auto-approved by a minimum rating, and an editing window. For CM-SUP-001.
- `002.text.txt`: line 65, 'Purchase from Zid cashier' as a way to earn points; line 72, the points' validity; line 77, 'you can add up of 10' redemption methods. For CM-LOY-004.

## Problems with the brief or the script

- **What "section" means for a page-index entry** isn't stated in the parent's-thing rule. I read it as the title key's section (above). If the coordinator means the pageKey prefix, most children take a second line on their group's capability.
- **The brief doesn't say where a page's permission goes.** `scope` is for listing conditions, and `held_amend.py` keeps only the reading. I wrote permissions into `reading`.
- **A line with two listing conditions** has no stated separator. Zones' scope is `showNewZones, not use-is-ngo-store`, with a comma, because `;` separates values elsewhere.
- **The container check** keys on pageKey prefixes, so it misses `settings.store` (above).
- **A listing condition can be a minified function** (`xe()`) whose module the brief's reading list doesn't reach.
- **B-extent.md and this brief** read alike on every rule used here.
