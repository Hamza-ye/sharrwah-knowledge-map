# Held pass, Zid, batch ZD-CH: notes

42 entries of `dashboard-page-index` (items.jsonl lines 59 to 100: settings.communications to logistics.shipment-transactions), at other-product-class@0d79b794f. 52 lines: 51 on capabilities, 1 new, none out.

Sources read: the items; `zid/structures/dashboard-page-index/source.js` for each page's permission, sidebar badge and listing condition; the modules that source.js imports for those conditions, held in run 20261028T143118Z-dashboard-code (`fetch.warc.gz`, records `use-is-ngo-store-SFG8ijPH.js`, `use-feature-flag-npDDBet2.js`, `automatic-discount-pilot-list-BzTPcabc.js`, `gift-2-line-Dg_SogQX.js`); the store's feature flags answer (20261028T144855Z-dashboard-routes-en, `answers/hermod.zid.sa/v1/managers/store/feature-flags/e8462761….json`); and, to clarify entries only, the run steps that `index/ledger/dashboard-routes.tsv` joins to each path.

## The listing conditions, as scope

All of them come from source.js and the modules it imports (facts at the commit):
- `use-is-ngo-store false`: the module `use-is-ngo-store` returns `storeBusinessData.business_type===ngo || isCharitableDonationStore`. source.js leaves out, for such a store, Stock notifications, Bundle offers and the whole Logistics group, children included (`...s?[]:[...]`). So entries 38 to 42 carry it as their scope.
- `customer_wallets`: Customer wallet and Cashback offers are listed only where `customerWallets` is set. That is `feature_flags.customer_wallets` in `use-feature-flag`, true on the demo store.
- `show_new_zones`: Zones is listed only where `showNewZones` is set (`feature_flags.show_new_zones`, false on the demo store). The demo store's page reads 'This feature is not enabled for your store.' (20261028T160128Z-dashboard-routes-rest-en/steps/169.text.txt, line 31).
- `automatic-discount-pilot-list`: Automatic discounts is listed only for a store id in that list, and the module held is `var e=[],t=t=>e.includes(t)`: the list is empty. So the page is listed for no store at capture (a reading). I placed it `core` with the list as its scope. If the coordinator reads an empty pilot list as "not released", it is `shows`. The cell is `core` either way, from its staff permission.
- Qitaf: `rt(e,t)=>nt.includes(e)&&t`, where `nt` lists 41 store ids, and `t` is `isQitafEnabled&&!isMoneyHashQitafEnabled`. Where rt holds, the page is `marketing/qitaf`, with no badge (entry 31). Otherwise it is `marketing/new-qitaf`, with the badge new (entry 30). MoneyHash appears only in a flag's name, so it is no filler.
- Mokafaa's condition is a permission, not a store condition: `xe` is `checkOne(MOKAFAA.viewHome)`, in `gift-2-line`. It is in the reading, and the scope is empty.

The permissions (`permission: {one|any|all: …}`) and the badges are in each line's reading. The pulse dots (`hasPulseDot`) on Marketing and Whatsapp are marks, also in the readings.

## New things

**`new:Customer Referrals`** (ZD-E-381f5c01, `core`):
- **Its place of its own:** the page index's entry `marketing.referrals` (path `marketing/referrals`, sidebar badge beta), and the route manifest's `marketing/referrals` and `marketing/referrals/program`. Both were opened, 20261028T160128Z-dashboard-routes-rest-en steps 195 and 116.
- **What it is:** a programme in which the store's customers invite friends and both are rewarded: 'Your customers gets a code, and when a friend they invite orders, both get rewarded.' (step 195, line 47).
- **Names:** English Customer Referrals; Arabic برنامج دعوات العملاء.
- **Proposed placement:** domain D. Area MKT, parent CM-MKT-013, or area LOY, parent CM-LOY-004. Zid's own marketing page lists Customer referrals under the tool group "Loyalty and rewards" (step 212, line 88). Salla's dashboard app @salla.sa/ui-merchant-partner-marketing holds a `marketing/referrals` beside affiliates (SA-S-3550, cited in CM-MKT-013). Whether Salla's referrals are customers' referrals isn't stated in that cell. If they are, this is that capability's, and the coordinator could make one capability of the two.
- **Terms searched:** referrals; referral; customer referrals; دعوات العملاء; refer a friend; برنامج دعوات العملاء; دعوة; إحالة; الإحالة; ادع صديق; invite friends; refer; referral code.
  - The only hits were CM-MKT-013 (Salla's path), and CM-PTN-008, the platform's plans' referral, another thing.
  - The checker's leads CM-CUS-001, CM-STF-002 and CM-MKT-005 matched on "customer" and "marketing". Their Zid cells hold customer records, staff permissions and campaigns, not referrals.

## Entries I couldn't tell, and what would settle each

- **Automated Messages, ZD-E-5388c35e:** placed on CM-MKT-006, which is CHANGES (the cell gains `core`).
  - The page calls its items automations, 'Create First Automation' (step 118, line 74), sent 'based on events you specify' (line 45). Zid's marketing page offers them 'from a welcome to recovering an abandoned cart' (step 212).
  - CM-NTF-001, "the messages the store sends automatically to customers", also fits its words. The settle: whether the coordinator reads Zid's Automated Messages as marketing automations or as notifications. Zid lists them under Marketing, not under Settings > Communications.
- **Mokafaa and Qitaf, ZD-E-51f6c7ae, ZD-E-b13ec16b and ZD-E-5eb861c2:** each on CM-LOY-004 (a loyalty programme, as the pages call it) and CM-PAY-012 (the buyer pays with the points).
  - I followed CM-LOY-004's note, that Salla's مكافأة الراجحي is a payment method, domain C, and CM-PAY-013's note, that Salla's SA-C-119 lands in CM-PAY-012. But CM-PAY-012 is "third-party wallets", and points aren't plainly a wallet.
  - What would settle it: the coordinator's ruling on where a third party's points used to pay belong, CM-PAY-012, CM-PAY-017 or a capability of their own.
  - Al Rajhi Bank and STC are named only by the run steps (208, line 45; 196, line 45), so they are in the readings, not in `filler`. The second stage could write them as slot fillers from those steps.
- **Live chat and Automatic replies, ZD-E-6ca60383 and ZD-E-7e7d8e0c:** on CM-SUP-004, which is CHANGES (`core` added to `extension-point`).
  - They are Zid's own pages, under `services/whatsapp`. No app's address and no maker is stated.
  - Live chat needs WhatsApp activated (step 123, line 28), a condition on the store's own data, so it is in the reading.
  - Automatic replies' own page broke on the demo store ('Oops! Something broke', step 042). So the reading rests on the WhatsApp settings page's 'Replies flow' (step 137).
  - Automatic replies could instead be CM-NTF-004's, as a part of Zid WhatsApp. A capture of `services/whatsapp/settings/auto-replies` that renders would settle it.
- **Shipments tracking, ZD-E-9d3c8885:** on CM-SHP-017, which is CHANGES (`not-stated` becomes `core`).
  - It is the dashboard's own page, titled تتبع الشحنات, the very term the cell's help-centre entry held. It lists shipments with a tracking number (step 115, line 37).
  - A second line goes on CM-SHP-009, by its title key `navbar:shipments`.
  - The page is gated by Zid Ship's permissions (`ZIDSHIP.view`, `ZIDSHIP.viewShipment`). So its shipments may be only those of Zid Ship's labels (CM-SHP-002); a store with shipments would show it.
- **Transactions log, ZD-E-f2eb9f97:** on CM-SHP-002, the charges of the platform's labels.
  - Its page also holds 'COD settlement' (step 032, line 33), which bears on CM-PAY-029. That is a lead, not placed.
  - The lead CM-PAY-020, an order's payment transactions, is a homonym.
- **Discounts, ZD-E-f622dfae:** a second line goes on CM-MKT-002 (coupons), by its title key `navbar:coupons` and its permission `COUPONS.view`, though its English and Arabic titles say Discounts. If a title key isn't the entry's words, that line goes.
- **Hours of operation, ZD-E-0fa9b23d:** on both CM-ORD-010 and CM-ACC-007, since both cells already cite this settings place (ZD-S-0970).
- **Legal pages, ZD-E-5e2ff3fb:** one line, on CM-CNT-008. Its path is under the online store's pages (`channels/online-store/pages/legal`). If the coordinator reads that path as naming the store's pages, CM-CNT-003 takes a line too.
- **Groups, ZD-E-4d70e67d:** on CM-STF-003, with a second line on CM-STF-001, because its Arabic title مجموعات فريق العمل names the team.
- **A parent's line from the pageKey alone:** I took none. Examples are `orders.` for Abandoned carts, `customers.` for the customers' pages, `marketing.` for the marketing pages, `logistics.` for the logistics pages and `whatsapp.` for Live chat.
  - I read rule 2's "the parent's thing where the entry's own words name it" as the title's words, not the pageKey's prefix. Groups is the one entry whose title names its parent's term.
  - If the pageKey counts, each of those entries takes a line on CM-CHK/ORD, CM-CUS-001, CM-MKT-005, CM-SHP-001 or CM-NTF-004.
- **Store, ZD-E-e0c2feef:** a container (its own sidebar group), though the checker doesn't flag it as one, since its children's pageKeys don't begin with `settings.store.`.
  - Its title "Store" names CM-ACC-006, by that cell's term Store. Its path opens Store information. So it is placed on CM-ACC-006.
  - Its children are Store information, Legal pages, Hours of operation, Team, Groups and Domains list.

## Containers

- **Communications** (ZD-E-b2f66cda) is on CM-NTF-001. Its children are Order notifications, Abandoned cart reminders, Product question notifications and Product review notifications.
- **Store** (ZD-E-e0c2feef) is on CM-ACC-006, with its children as above.
- **Marketing** (ZD-E-8775d13b) is on CM-MKT-005. Its children are Discounts, Bank discounts, Automatic discounts, Cashback offers, Bundle offers, Automated Messages, Marketing campaigns, Loyalty program, Customer Referrals, Mokafaa program, Qitaf and Affiliates.
  - source.js also lists `zidAdsPage` (`b`) in it, an entry the items leave out.
- **Whatsapp** (ZD-E-4a0d6399) is on CM-NTF-004. Its page is 'Zid WhatsApp' (step 166). Its children are Live chat, Automatic replies, Message logs and Settings.
- **Logistics** (ZD-E-6cd309e3) is on CM-SHP-001. Its children are Zones, Shipping methods, Shipments tracking, Transactions log, and Prepaid packages (`logistics.labels`, the batch after this one).

## Items against their source

- The items leave out each page's permission, badge and listing condition, as the brief and the evidence map say. They also leave out these page objects in this stretch of source.js:
  - `dashboard`, whose path is empty;
  - `orders`, `orders.all`, `orders.manual`, `customers`, `customers.all` and `customers.groups`, whose titles are conditional (`e(s?…:…)`, the NGO store's Donations / Donors titles);
  - the computed `zidVoicePage` (`x`, under Orders), `zidAdsPage` (`b`, under Marketing), and the catalog group `O`, which comes from another function.

  All are known (evidence map, R4).
- **Legal pages:** its path `channels/online-store/pages/legal` is no route of its own in the route manifest. The ledger holds its five children (`…/legal/privacy-policy`, `terms-and-conditions`, `exchange-and-returns`, `complaints-and-suggestions` and `licenses`), each opened, and `channels/online-store/pages` itself is `redirected`. So the page index names a path that no manifest route matches exactly.
- **Qitaf:** two items share the pageKey `marketing.qitaf`, at two paths. They are alternatives under the condition rt. Both are kept, as two entries.
- **Domains list:** its Arabic title is رابط المتجر الالكتروني, the store's online link, where the English is "Domains list". The source's title key is the same for both (`settings:landingPage.domains.label`), so this is the locales' wording, not a disagreement.

## Leads for the second stage: what run steps state that no entry holds

Run 20261028T150740Z-settings-gaps-en:
- **steps/027.text.txt, lines 21 and 29:** 'Manage your store closure or stop receiving orders', and 'Stop receiving orders'. These are for CM-ORD-010, whose reading says Zid doesn't say the hours govern when orders are received.
- **steps/028.text.txt:**
  - line 20, 'Team members (0/20)': a limit on CM-STF-001 (quality);
  - line 26, 'Authenticator app': the team's sign-in, a lead for the staff security cells.
- **steps/029.text.txt, line 27:** 'Assign permissions easier to your team members'. This defines CM-STF-003, whose reading says no statement defines a team group.
- **steps/050.text.txt:** for CM-ACC-006, whose reading says no statement lists the store's details:
  - line 24 onward: the store's details, Store name, Email and Phone;
  - line 36: 'Social media account management moved', with the social accounts now under Channels \ Online Store \ Brand.
- **steps/033.text.txt:** for CM-SFR-008:
  - line 23, 'You can connect more than one domain, but you can activate only one.', a quality;
  - line 38, 'Request a free domain from Zid';
  - a link to the Saudi Business Center's domain verification.
- **steps/049.text.txt, line 21:** order status messages aren't to be used for marketing, 'To ensure compliance with communication authority regulations'. This is for CM-NTF-001, and a law or regulator as a slot filler.

Run 20261028T160128Z-dashboard-routes-rest-en:
- **steps/040.text.txt, lines 19 and 50:** 'Recharge reminder credits' and 'Automatic reminder', for CM-MKT-022: reminders paid from credits.
- **steps/079.text.txt, lines 21 and 25:** automatic notifications to the customer after a reply, and to the merchant on a new question. These are for CM-SUP-001 and CM-NTF-002.
- **steps/183.text.txt, lines 34 and 66:** 'Manage reminders' and 'Send reminder' on the abandoned carts list, for CM-MKT-022.
- **steps/213.text.txt, lines 43 and 60:** the customer wallets' overview: Cashback ROI, held and pending balances, 'Balance expiring'. These are for CM-LOY-001 and CM-LOY-003.
- **steps/109.text.txt, line 48:** stock notifications sent by email and by WhatsApp, counted separately, for CM-MKT-016.
- **steps/197.text.txt, line 48:** the Discounts page holds 'coupons, automatic discounts, progressive offers, and free shipping', and the demo store's automatic discounts are listed there. This is for CM-MKT-003 and a free-shipping offer.
- **steps/212.text.txt:** the marketing page's tool list, with its groups "Bigger baskets", "Loyalty and rewards" and "Reach and engagement":
  - line 74: 'Free shipping offer';
  - line 80: 'Zid Business WhatsApp';
  - line 88: Customer referrals;
  - line 93: Bank discounts, 'Offer a discount to holders of specific bank cards'.
- **steps/118.text.txt, lines 47 and 56:** WhatsApp balance, SMS balance, 'Buy sender name', 'Sender name: Zid'. These are for CM-NTF-004.
- **steps/128.text.txt, line 49:** campaigns by SMS and WhatsApp, each to be activated, for CM-MKT-007.
- **steps/195.text.txt, lines 56 and 58:** the referral programme's rewards (cashback, a fixed amount or loyalty points), its holding period, and its abuse rules (minimum order value, first order only, caps). These are for `new:Customer Referrals`.
- **steps/193.text.txt, lines 49 and 69:** 'set commissions, attribute orders, and track payouts', and 'Manage redemption methods', for CM-MKT-014.
- **steps/208.text.txt:** for CM-LOY-004 and CM-PAY-012:
  - line 45: Mokafaa is Al Rajhi Bank's, a slot filler;
  - line 59 onward, 'Mokafaa rates by plan': Rise earning 8.5 %, redeem 15 %; Growth 8 %, 13 %; Professional 7 %, 10 %. These are qualities, the fees by plan;
  - lines 79 and 81: 'Every 1 SAR earns 10 points' and 'Every 250 points convert to 1 SAR'.
- **steps/196.text.txt:** for the same two capabilities:
  - line 45: Qitaf is STC's;
  - line 59 onward, 'Qitaf rates by plan': the same rates as Mokafaa;
  - lines 79 and 81: 'Every 1 SAR = 0.1 points' and 'Every 5 points = 1 SAR'.
- **steps/219.text.txt, line 47:** the old Qitaf page says activation requests are suspended.
- **steps/166.text.txt, lines 49 and 55:** Zid WhatsApp's activation, through a Meta business account, 'connects your store to WhatsApp Business API'. This is for CM-NTF-004, whose cell holds the same from other statements.
- **steps/137.text.txt:** WhatsApp settings: line 40, Quick replies; line 43, Tags; line 47, Store widget, a WhatsApp button on the storefront; line 52, Unsubscribe from messages, the buyer's opt-out by keyword. These are for CM-SUP-004 and CM-CUS-007.
- **steps/155.text.txt:** the Logistics page:
  - line 32: 'Shipping rate calculator';
  - line 33: 'Order your packaging and shipping needs now', for CM-SHP-021, packaging;
  - line 40: Local delivery, for CM-SHP-008;
  - line 52: 'Pickup in Store settings relocated', to the inventories page, for CM-SHP-007;
  - line 75: 'Explore integrations with alternative fulfillment and shipping providers.'
- **steps/032.text.txt, lines 31 and 33:** Shipping fees and 'COD settlement', for CM-PAY-029.

Run 20261028T145901Z-dashboard-routes-en-2:
- **steps/005.text.txt, lines 24 and 27:** reviews auto-approved above a minimum rating, and the time a customer may edit a review. These are for CM-SUP-001, as qualities or settings.

## The checker's other notes

- Line 7 (Product question notifications): its first lead, CM-API-009 (webhooks set up in the admin), holds nothing on Zid. It matched only on the word "notifications". The page notifies customers and the merchant of questions (step 079), and subscribes no address to events, so no line names it.

## Problems with the brief or the script

- The checker spots a container only by a pageKey prefix. So `settings.store` (Store), a sidebar group whose children's keys are `settings.information` and the like, isn't flagged. It is placed as a container all the same.
- Rule 2's "the parent's thing where the entry's own words name it" doesn't say whether a pageKey's prefix is the entry's own words. My reading is above. A ruling would make batches agree.
- The listing conditions sit in modules that source.js imports, not in source.js itself: the NGO test, the feature flags, the pilot list and Mokafaa's permission. The brief names only source.js. I read the modules from the dashboard-code run's WARC to resolve the identifiers.
