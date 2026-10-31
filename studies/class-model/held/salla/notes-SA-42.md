# Held pass, Salla, batch SA-42: notes

130 entries (effort high), evidence at observed-sa@b0bd0b163. Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-42`).
- **1 to 16: the last 16 of `portal-help-center-resource`** (`partner@en`), the Partners Resources tree at `/help/resources`, by its line in `structures/salla/portal-help-center-resource/partner@en/items.jsonl`:
  - 1 to 4: Services Support (line 4), its last three sections (order 3 to 5), the cards 'You still have more questions?', `https://t.me/SallaDev` with its link, and `Support@salla.dev`;
  - 5 to 16: every section and article of Influencers Support (line 5), whose resource SA-41 placed (its 85).
- **17 to 130: the first 114 of `portal-menu-definitions`**:
  - 17 to 121: `layout-mf@prod`, `items.jsonl` lines 1 to 89 and 94 to 109, both menus of layout-mf v0.0.337: the admin's (`admin: true`, lines 1 to 56, but for the partner's Dashboard and Home at lines 2 and 3) and the partner's (lines 57 to 109). Lines 90 to 93 (the partner's group Domains and its items Domains Management, Transfer Domain, Domain Assignment) have no entries: the concern map cites them (SA-S-5116, SA-S-5117, SA-S-5153, SA-S-5154), and the selection reads "the items not cited";
  - 122 to 130: `ui-partners-portal-layout@prod`, lines 1 to 9, the first items of the other bundle's admin menu (array `Li`): Dashboard, the group Users and its five items, the group Apps and All Apps.

**`portal-help-center-resource` is now placed whole** (SA-41, SA-42).

**No batch had placed `portal-menu-definitions`. `SA-43` holds the rest of it and hasn't run:** `ui-partners-portal-layout@prod` lines 10 to 109 (100 entries), from Apps Requests to the partner's Support. The rules my lines follow are below, for SA-43; the coordinator aligns the two.

**Placed:** 121 entries on capabilities, 4 on earlier batches' new things (19, 24, 29, 127), 5 `out` (17, 22, 114, 122, 125), in 158 lines. 31 entries take more than one line. Five lines group two entries each: a card and its one link (2 and 3; 11 and 12, three lines; 14 and 15).
- **Supports over the 149 capability lines:** 94 `core`, 44 `extension-point`, 11 `shows`. The four new lines are `core`. No `own-service`, no `outside`.
  - the resource tree: 21 lines, 7 `core`, 6 `extension-point`, 8 `shows`;
  - the menu: 137 lines, 87 `core`, 38 `extension-point`, 3 `shows` on capabilities, with the 4 new and the 5 `out`.
- **No filler and no quality:** no entry names a third party doing the thing, a limit or a price.
- **Scope** on 17 lines, each the menu item's own `feature`: `app-store-ads` (63), `influencer_packages` (80), `expert` (82), `advanced-affiliate-marketplace` (88), `affiliate-active-merchants` (89, 91), `affiliate-orders` (90), `development_store` (104), `store-management` (105), `invoices` (109, 110), `temp-unified-reviews-page` (111, 112), `partner_resource` (119).

## Sources read

- The brief, `H-held.md`, and what it names: the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run"; the coordinator's rulings, `held/review-H-rulings.md`, to its last section (the ruling after SA-41).
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the register's rows for both structures; `index/ledger-summary.tsv` and `index/ledger/portal-app.tsv`; `show --meta` and the two `selection.tsv` rows (`where`; the menu's note "the items not cited").
- **The batches before mine:** SA-41's notes and placements (the tree's rules, and the coordinator's check); SA-40's rule 4 and check (influencers' articles); SA-28's and SA-29's notes and lines for the rendered header and side menu (`partners-portal-header`, `partners-portal-navigation`); SA-30's and SA-31's notes and lines for `permission-gates`, whose portal rows are this structure's items read as gates (`derived/permission-gates.tsv` line 114 + position for layout-mf, 223 + position for ui-partners-portal-layout); SA-34's rule 5 and its check; SA-37's, SA-38's and SA-39's notes, with each check; and the lines SA-34 to SA-38 gave each route the items name, found by route name in their readings and by path in `entries.tsv`.
- **The structures' sources:** `portal-help-center-resource/partner@en/source.json` (the resources Services Support and Influencers Support, with every section, subsection and article) and `items.jsonl`; `portal-menu-definitions/layout-mf@prod/items.jsonl` (all 109 items, raw), `meta.json`, and `ui-partners-portal-layout@prod/items.jsonl` (all 109 items with their `words`), for each layout-mf item's twin and its English and Arabic words.
- The concern map's citations of `portal-menu-definitions` (`studies/concern-map/platforms/salla/citations.tsv`: SA-S-5116, 5117, 5153, 5154, layout-mf lines 90 to 93).
- **The model:** the cells of every capability I placed on (CM-PTN-001 to -005, -008, -009; CM-APP-002, -003; CM-SFR-003, -005, -008; CM-MKT-014, -015; CM-DVT-003 to -005; CM-STF-005; CM-API-008) and of the leads I set aside (CM-ONB-003, CM-SUP-001, CM-SUP-005, CM-B2B-002, CM-ACC-003, CM-OPS-005, CM-STF-001, CM-MKT-005, CM-MKT-010), with the names of the others; `caps --terms` for featured and recommended apps, app store ads, custom marketing, contracts, VIP partners and app transfers (English and Arabic), and for opportunities, influencer profile, campaign orders, payouts and Telegram.
- `held_index.py` for the influencer resource's six links, and a grep of observed-sa's `fetch.cdx` and `urls.txt` files: none is held.

I read no run step.

## Rules my lines follow

### The resource tree, 1 to 16: SA-41's rules 1 to 7, and the ruling after SA-41

1. **The channels' cards are `core` on CM-PTN-001** (SA-41's rule 5): the developer community on Telegram, 'You still have more questions?' (1, 13); the Telegram help channel, a card and its one link (2 and 3, 14 and 15); the support email (4, 16). Telegram is where the group is, so it isn't a filler. In Services Support and Influencers Support the 'You still have more questions?' card holds no link (`source.json`: no articles, `url` null), unlike the other resources' (SA-41's 35, 58, 74), so 1 and 13 stand alone.
2. **The influencer resource's `article-list` sections are containers,** `shows`, on CM-MKT-015 and CM-PTN-009, the two cells SA-41 gave the resource (85): 'Expand your Online Influence: Create Salla Influencer Profile Today' (5) and 'Grow your Opportunities as an Influencer' (8).
3. **Their posts are read as help pages' titles** (SA-41's rule 4, SA-40's rule 4), each on both influencer cells:
   - creating the influencer profile on Salla, the influencer working with merchants through the portal, is `extension-point` (6, the English blog post; 7, the Arabic tutorial);
   - a guide to growing an influencer's opportunities is `shows` (9, 10), as SA-41 placed the guides to an app's popularity and a theme's promotion.
4. **The card 'Campaign Orders and Payouts Process for Salla Influencers' and its link (11, 12)** name two things:
   - the campaign orders influencers receive for the services they offer merchants, `extension-point` on CM-MKT-015 and CM-PTN-009 (SA-40's rule 4);
   - the payouts to influencers, the platform paying a partner, `core` on CM-PTN-003, as SA-41 placed 'Get paid for Private Apps with Salla' (its 44).

   'create your influencer profile' in its description is the same two cells' thing, so it takes no further line.
5. **A resource gives the cards under it no line:** the support cards of Influencers Support (13 to 16) take CM-PTN-001 alone, as SA-41's support cards under Apps Support took no CM-APP-002 line.
6. **Homonyms,** as SA-41's rule 6: support (CM-SUP-005), help (CM-ONB-003, the merchants' learning), service provider (CM-TRU-013, CM-PAY-004), payouts (CM-PAY-005, a merchant's payouts), campaigns (CM-SEL-005, pre-orders).

### The menu, 17 to 130, and for SA-43

The items of `portal-menu-definitions` are the same items as `permission-gates`' portal rows (SA-30 and SA-31), which read each one as a gate (`decides`). Here each is read as the portal's place (`where`). SA-43's 100 entries are `ui-partners-portal-layout@prod` lines 10 to 109, whose rows SA-31 placed (its entries 24 to 123).

- **M1. Same item, same thing.** Each item takes the capability and support its address's lines give it, and each reading cites them:
  - the route (SA-34 to SA-39);
  - the rendered link (SA-28, SA-29), where the held partner's menu shows the item;
  - the item's permission row (SA-30, SA-31).

  layout-mf names a route (matched to its path through those batches' readings). ui-partners-portal-layout names a path (`to`) and carries its words in English and Arabic (SA-31's R1).
- **M2. The admin's menu** (`admin: true`; in the other bundle, the array `Li`, whose children carry no `admin`) keeps SA-34's rule 5: `core` where it manages a partner or marketplace thing. The admin's own Dashboard (`/admin/dashboard`) and Admins are `out` (17, 22, 122, 125).
- **M3. A permission is a gate on the portal's user.** It is named in `reading`, never a term, a scope or a line of its own (the brief's rule 5, on a gate on the user; the ruling after SA-22). So three second lines that SA-30 gave a container for its permission aren't taken here:
  - Themes, CM-SFR-005 for `manage-bundles` (74);
  - Marketing Tools, CM-APP-003 for `manage-coupons` (95);
  - the admin's Stores, CM-DVT-005 for `manage-development-stores` (52).

  Their children take those capabilities by their own words (76, 96, 53, 54). This is how SA-28, SA-29 and SA-31's R3 placed the rendered groups and the other bundle's. No cell changes either way.
- **M4. A second line stays where the page or the title is itself two things,** as the route's or the rendered link's lines have it:
  - Bundles Requests (CM-SFR-005), Salla Affiliate Products (CM-PTN-008), Merchants Live Products (CM-MKT-014) and the admin's Categories (CM-SFR-003), from SA-36's routes;
  - the Affiliate Marketplace (CM-MKT-014);
  - every influencer and agency item (CM-MKT-015 and CM-PTN-009);
  - My Subscriptions (CM-APP-003, CM-SFR-003) and Payments (CM-PTN-003, CM-PTN-004), by SA-29's N3.
- **M5. A child whose title makes it a kind of its group's thing takes the group's line too** (M-6, refined; SA-29's N4). The partner's Demo stores and Development Stores take CM-DVT-003 (103, 104), and so does the admin's Development Stores (53), which SA-30's row for it doesn't. Requests, store management, bundles and coupons aren't kinds of their groups' things.
- **M6. Scope is the item's own `feature`** (SA-30's Q5, SA-31's R4). A group's feature (My Services' `expert`, the other bundle's Domains' `domain-purchase`) isn't its children's scope: it goes in their `reading`.
- **M7. A route the code chooses goes in `reading`.** Where the code chooses a route by a feature or a computed condition (`temp-services-redesign`, `temp-affiliates-profile`, `temp-ready-stores`, `temp-payments-billing`, Dashboard's `No()`), the line takes the route the rendered menu opens (SA-30's Q6, SA-31's R6).
- **M8. Terms** are the item's title, its route names and its group's `name`. In the other bundle they are its key and its words in both languages. A permission is never a term.
- **M9. A layout-mf title that is a locale key** (help.helpCenter, agency.*, influencer.myProfile, influencer.campaignOrders, supportTools, settings) is read by its route and by its twin in the other bundle. The reading quotes the twin's words from `ui-partners-portal-layout@prod/items.jsonl`, and the key is the term. layout-mf's locale chunks aren't held (the register's note).
- **M10. A `tag: new` or `badge: navigation.new`** is a release badge with no limit stated (D1): `reading`, and the item keeps its support (SA-29's check).
- **M11. The header Others** (`header: Others`; the other bundle's `navigation.others`) is `out`, by the ruling after SA-28 (114).
- **M12. An item with `children` or `items` is a container** (M-13), on its title's capability with the support its children's routes took. A group with no permission of its own is still one (SA-31's R2: 123, 129).
- **M13. The partner's Store management stays `shows`** (the ruling on partner access requests) and Reviews & Ratings `shows` behind `temp-unified-reviews-page`. Domains stay `shows` (SA-37): for SA-43, the other bundle's group Domains (line 90) takes the scope `domain-purchase` and its three items (lines 91 to 93) none (M6).
- **For SA-43's other items:** SA-31's lines for the same rows hold, with M3 to M10 applied. In particular:
  - the admin's Ready Stores (line 35) takes CM-DVT-003 beside CM-DVT-005 (M5);
  - no SA-31 line on these items rests on a permission, since the other bundle's groups carry none;
  - their titles' words are in each item's `words`, which `show` prints.

## Each new thing

None of my own. Four entries take SA-34's new things, under the same names:
- **`new:VIP Partners`** (`core`):
  - 19, Home (route vip-dashboard, `/home`, permission `vip-home`);
  - 24, the admin's VIP Partners (`/admin/vip-partners`);
  - 127, its twin in the other bundle, 'VIP Partners' / 'الشركاء الـVIP'.
- **`new:Transfer Requests`** (`core`): 29, the admin's Transfer Requests (`/admin/applications/transfer-requests/`).

Their places of their own are those routes (SA-34, SA-36, SA-37). The names are the menu's own: VIP Partners / الشركاء الـVIP; Transfer Requests (its Arabic, طلبات نقل, is the other bundle's line 11, SA-43's). Searched again: VIP; VIP partner; الشركاء الـVIP; vip-home; app transfer; ownership transfer; طلبات نقل; نقل ملكية. No capability matched.

## Entries I couldn't tell, and what would settle each

- **52, 74, 95: the second lines not taken (M3).** If the coordinator wants this structure's lines to mirror the permission rows, the three come back: CM-DVT-005 `core`, CM-SFR-005 `extension-point`, CM-APP-003 `core`. Each cell already holds that support.
- **53: the admin's Development Stores on CM-DVT-003 too (M5).** SA-30's row for the same item has CM-DVT-005 alone. The title makes it a kind of the group's stores, as SA-29's N4 read the partner's. The coordinator may align the two either way; no cell changes.
- **11 and 12, CM-PTN-003.** 'Payouts Process for Salla Influencers' reads as Salla paying influencers what it owes. It could instead be merchants paying for a campaign through the platform, which no capability holds apart from the influencer cells. The post (salla.dev's `salla-influencers-campaign-payouts-and-statuses`, not held) would settle it.
- **9 and 10, `shows`.** 'Grow your Opportunities as an Influencer' reads as a guide. `extension-point`, influencers taking up opportunities through the portal, is the alternative. The posts (not held) would settle it.
- **111, supportTools, CM-PTN-005 `shows`,** as SA-31 placed it, by the ruling after SA-2: a heading over one capability's page. M-13's `new:Support Tools` with `core` is the alternative, as SA-31's notes say. The page behind it isn't held: the partner lacks `temp-unified-reviews-page` on 8 and on 28 October.
- **112, Reviews & Ratings:** opened for `manage-services` or `manage-influencers`. A second `shows` line on CM-PTN-009 (influencer reviews) is SA-37's alternative. The page would settle it.
- **68, Custom Marketing on CM-PTN-005:** SA-34 placed its route unsure. Its permission `manage-notifications` is a messaging permission, and where the content shows isn't stated.
- **64, App Store Ads on CM-APP-002:** whether partners buy placements in the App Store isn't stated (SA-30's notes). CM-MKT-010, a store's advertising, is a homonym.
- **18, Dashboard:** layout-mf chooses between `reports-dashboard` (`/dashboards`) and `user-dashboard` (`/dashboard`) by `No()`, from `Co`, which the item doesn't resolve. The other bundle chooses the same two addresses by `temp-home-page`. The held partner lacks it, and the rendered menu opens `/dashboard`.

## Structures whose items and sources disagree

- **The entries' text leaves out keys the items hold.** The left-out keys are `icon` (every icon of layout-mf) and `alert` (settings, line 101: `t=>!t.verified`). It also leaves out the expressions behind resolved values.
  - The source governs.
  - The icons name nothing.
  - The alert marks Settings while the partner account isn't verified. That is CM-PTN-002's own thing, so entry 113's reading names it and no line rests on it.
- **Influencers Support's two `article-list` sections both carry `order: 0`,** and so do their subsections. I number them by their place: section 0 (5), section 1 (8). Services Support's sections run 0, 1, 3, 4, 5, with no 2. My readings give a card's `order` as its section number, as SA-41's do.
- **A subsection's Arabic title is a typo of its English one:** 'Grow your Opportunities as an Influence' (9). The quote is copied as Salla spells it.
- **The two bundles title some items differently.** The rendered menu follows the second bundle:
  - Featured Apps / Recommended Apps;
  - Development Stores / Ready Stores, for the admin's and the partner's;
  - Theme Subscriptions / Theme Purchases;
  - Event Logs / Webhooks Log;
  - Conversations / Chats;
  - My Applications / My Apps;
  - My Themes Bundles / Bundles;
  - Coupons Admin / Coupons;
  - Messages Center / Message Center.

  Each reading names the other bundle's words where they help.
- **layout-mf's titles that are locale keys** have no words in this bundle (the register: the locale chunks v0.0.337 `locale-en.js` and `locale-ar.js` aren't held). Their twins' words are in the other bundle (M9).

## What the sources state that no entry holds (for the second stage)

- **The influencer resource's posts:** salla.dev's `blog/influencer-with-salla/`, `tutorial/arabic-influencer-with-salla/`, `blog/grow-your-opportunities-as-an-influencer/`, `tutorial/arabic-grow-your-opportunities/` and `blog/salla-influencers-campaign-payouts-and-statuses/`, and `t.me/SallaDev`. None is held: `held_index.py` finds none, and no `fetch.cdx` or `urls.txt` names one. They would settle 9 to 12.
- **The settings item's alert** (`layout-mf@prod/items.jsonl`, line 101): a lead for CM-PTN-002, on the partner's verification, as SA-31 noted.
- **Dashboard's condition `Co`** (`layout-mf@prod/items.jsonl`, line 2): what the partner's dashboard choice rests on in layout-mf.

## Problems with this brief or the script

- None that blocked.
- `show` renders a menu item without its `icon`, `alert` and expressions. The alert is a statement of its own, which a reader of the entry alone would miss.
- The checker prints no container `NOTE` for an item with `children` (as SA-30 found) or for a resource's sections. M12 places them as containers.
- The batch boundary splits `ui-partners-portal-layout` after its line 9: the admin's group Apps (129) and All Apps (130) are here, its other three items in SA-43.

## The checker's lines, read again

- **`CHANGES`:** none. Every line falls on a cell that already holds its support.
- **`NOTE` core on a product named with the platform's brand:**
  - lines 2 and 20, 'Salla Partner Telegram group' (1, 13): Salla's own community for partners, as SA-41 read it;
  - line 19, 'Salla Influencers' (11, 12): Salla's own payouts to partners;
  - lines 59 and 60, 'Salla Affiliate Products' (47): Salla's own packages that affiliates promote, CM-PTN-008's referral programme, as SA-30 and SA-36's check read them.

  Each is `core` by what the entry shows. No line rests on a maker.
- **`NOTE` first lead holds nothing,** lines 29, 152 and 153 (23, 123, 124): CM-B2B-002, Companies, is business buyers. These entries are the users and accounts of partners, CM-PTN-002's, as SA-30 and SA-34 found. A homonym.
- **`NOTE` new thing whose entry has leads,** lines 25, 30, 35 and 156 (19, 24, 29, 127):
  - CM-API-003 comes by the field `action: read`, which every item holds, so it is no lead;
  - CM-B2B-002 and CM-STF-001 (by users) are business buyers and a store's staff;
  - CM-APP-001 (by applications) is a store's installed apps;
  - CM-INV-006 (by transfer) is inventory transfers;
  - CM-PTN-001 (by name: partner) is the programme, not the VIP kind of partner.

  None of those cells is the new thing's.
- **`NEW`:** Transfer Requests, 1 line; VIP Partners, 3 lines. Both are SA-34's.
- No quote prints 'found nowhere held'.

The checker's last line, for SA-42: `130 of 130 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes.** The menu items keep the capabilities their addresses' earlier lines give them.
- **The rules M1 to M13 stand,** and SA-43 keeps to them.
- **M3 settles the difference with SA-30:** a permission is a gate on the portal's user, so it goes in `reading` (the brief's rule 5).
  - SA-30's three group lines that rested only on a group's permission are dropped. They were Stores on CM-DVT-005 for `manage-development-stores`, Themes on CM-SFR-005 for `manage-bundles`, and Marketing Tools on CM-APP-003 for `manage-coupons`.
  - Each group's remaining line names its permission in `reading`. SA-30's notes record this.
  - The children's own lines, such as My Themes Bundles on CM-SFR-005 and Create Coupons on CM-APP-003, stand. No cell changes.
- **M5 stands.** The admin's Development Stores takes CM-DVT-003 too.
- **Leads for the second stage:**
  - the Settings item's alert while a partner's account isn't verified;
  - the influencer posts and `t.me/SallaDev`, which aren't held.
- **Cost:** 25.4 million tokens over 92 requests, about 195,000 an entry. The context reached about 470,000 tokens, more than twice the brief's 200,000. Its 51 searches looked up earlier lines on the same addresses and permissions, which `held_entries.py earlier` now prints in one call. The agent started before that command existed.
