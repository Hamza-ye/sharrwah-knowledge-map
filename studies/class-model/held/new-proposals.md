# The held pass's new things: proposals across the platforms

Written by the agent of `briefs/N-new.md`, 31 October 2026, for the coordinator's decisions in `held/new.tsv`. One row per new thing per platform is in `held/new-proposals.tsv`. Its `reading` column holds, for each thing: the facts first, each cited; the count of lines and their supports, and the entries; then the group's grounds. A fact is traced to its source at a commit (a placement line `batch:line`, whose entry gives the evidence repository and commit, or a file named). A reading says so.

## What is listed

- **84 new things in 426 lines**: Shopify 40, Salla 22, Zid 14, WooCommerce 8. They are every `new:<name>` of `held/<platform>/placements-*.tsv` as the files stand now, less:
  - BigCommerce's five things decided in `held/new.tsv` (Display, Share, URL structure, Extensions, Professional Services). No other platform's new thing is any of them, so none is listed.
  - Zid's two things decided there (Customer Referrals, Similar products). Salla's Recently Viewed Products (N65) is proposed onto CM-MKT-023, where Similar products was decided, but it isn't the same thing.
  - The calibration batches BC-CH, BC-CX, ZD-CH and ZD-CX. They "aren't listed in `batches.tsv`, so they never reach the model" (`held/calibration.md`). Their new things are BigCommerce's Social sharing (the decided Share again) and Throttler, and Zid's Customer Referrals again. BC-1 places Throttler's entry on CM-ACC-006 and CM-ORD-001.
- **Shopify's batches still running.** SH-27, SH-90 and SH-91 hold no placements yet. SH-89's file holds 7 lines of N04's Earn 1% back, listed as they stand. Any new thing those batches name is the coordinator's to add.

## How the decisions were made

- **A new capability** where at least one platform gives the thing a place of its own (B-extent's kinds, as Q3M-6 sets them out) and no capability's definition or cells hold it. The domain and area follow the seed's areas. The amendment part is `<domain>-amend`. A-amend, C-amend and F-amend don't exist yet. B-amend, D-amend, E-amend and G-amend do. The next numbers given are provisional: the coordinator numbers.
- **An existing capability** where its definition holds the thing (its words are quoted in the row), or, for a thing with no place of its own, the nearest capability. Where the definition holds the thing only once widened, the row says how, and the widening is the coordinator's.
- **Out** where the thing has no place of its own and is no thing of the class, or is a title that names only a grouping of other capabilities' pages (the ruling after SA-28), or is the admin's own frame (the ruling after SH-37).
- **Joins across platforms** are by what the thing is. A join on role is marked as a reading.

## The groups that join platforms (8)

**N01, Search in the admin.** New, domain G, area SRF (admin surfaces and navigation), no parent, G-amend.
- Members: Shopify's Admin search (25 lines) and Saved views (7), Zid's Search (1) and Salla's quick search (1).
- Places of its own: Zid's dashboard route `search` (`zid/structures/dashboard-route-manifest/items.jsonl` line 413 at other-product-class@0d79b794f). Shopify's app tab 'Search the app' (`structures/shopify/mobile-app-navigation/tabs-and-more/items.jsonl` line 44 at observed-sh@e38dc17e3).
- Grounds:
  - The ruling after SH-37 keeps the admin's search and its saved views as new things, to be decided with Zid's and Salla's.
  - Shopify's own post puts 'Filters, search, and saved views ... in one bar' (SH-35:24). So saved views are part of the admin's search here, not a capability apart: they have no place of its own.
  - A reading: Zid's 'Ctrl + K' search, Salla's '⌘ + F' quick search and Shopify's command+k search are one thing.
- Not CM-SFR-013, which is buyers' search on the storefront.

**N02, Admin interface language.** New, domain G, area SRF, no parent, G-amend.
- Members: Shopify's Admin languages (9) and Salla's العربية / English (3).
- Places of its own: Shopify's app settings item 'Language settings' (SH-82:21, SH-82:23). Salla's Partners portal language menu (SA-28:67) and its Your profile item 'English (Beta)' (SA-49:34).
- Grounds: the ruling after SA-49 makes this one new thing across the platforms. The coordinator's note on SA-E-69216074 keeps it because it bears on a market.
- Alternative: CM-ACC-001's child in domain A, since Salla puts it in Your profile.
- No Zid, BigCommerce or WooCommerce statement or held line names the admin's language. The concern map holds none on any platform (searched: admin language; display language; interface language; English (Beta); لغة لوحة التحكم).

**N03, Store speed and caching.** New, domain G, area OPS, parent CM-OPS-003 (hosting of the store), G-amend.
- Members: Zid's Extended caching (1), WooCommerce's speed (7), Cache Product Objects (2) and Clear Customer Sessions When Empty (2), and Shopify's Web performance dashboard (4).
- Place of its own: Zid's plan policy `extended_caching` (`store-plan-policies` line 154). The other platforms' lines have no place: a card's line, unreleased flags, an Editions card with no route held (SH-55's notes).
- Grounds, a reading: caching is there to make the store load faster, so the caching and the speed reports are one thing. WooCommerce's flags state as much: 'Speeds up your store by caching product objects', and 'improving page caching performance'.
- Not CM-API-012, which caches the API's responses.
- Leads for the amendment: Salla's plan line تفريغ الكاش (SA-C-002/decides/SA-S-2092), now on CM-ACC-006; BigCommerce's Cloudflare CDN (BC-C-082/where/BC-S-0448), now on CM-TRU-014 and CM-TRU-015 as `outside`.
- Left out: Unified block editor assets (N31) is the admin editor's own loading, not the store's speed.

**N04, Credits and cashback on the merchant's sales.** New, domain A, area PLN, parent CM-PLN-004 (platform billing), A-amend.
- Members: Shopify's Earn 1% back on all sales as subscription credits (68) and Zid's cashback campaigns (2).
- Place of its own: Shopify's plan table row 'Earn 1% back on all sales' (SH-76:124).
- Grounds:
  - The amendment notes ask whether CM-PLN-001 already holds it, by the concern map's SH-I-1141. It doesn't. CM-PLN-001's note makes each plan line evidence for the capability it names, and no cell cites SH-I-1141 (`merged/evidence.tsv`).
  - A reading on role: Zid's strings pair cashback with campaigns only for Zid's offer to merchants, 'earn a free year subscription and / or cashback' (ZD-7's notes). That is the platform's reward to the merchant for its orders, as Shopify's credit is.
- Alternative parent: CM-PLN-006, the prepaid balance, for Zid's wallet.
- Not CM-LOY-003, which is buyers' cashback. Zid's nd2026 (N59) may belong here (see the open cases).

**N05, Shipment received by another person.** New, domain C, area SHP, parent CM-SHP-001, C-amend.
- Members: Zid (1) and Salla (2).
- Place of its own: Zid's plan policy `shipment_receipt_by_different_consignee` (line 340). Salla's is one switch of its invoice settings, which names the delegated recipient, المستلم المفوض.
- Grounds: SA-26 already read Salla's as Zid's thing.
- Not gifting (CM-LOY-006). CM-CHK-009 is the alternative parent.

**N06, Order limits.** New, domain C, area CHK, parent CM-CHK-002 (cart), C-amend.
- Members: Zid's Minimum and maximum order limit (2) and Shopify's Quantity rules (5).
- Place of its own: Zid's two plan policies (lines 338 and 339).
- Grounds, a reading on role: a minimum or maximum the buyer's order must meet. Zid's limit may be on value or on quantity; that isn't stated. Shopify's quantity rules set minimums, maximums and increments per product for B2B buyers.
- Not CM-ORD-010's daily order limit, nor CM-CHK-005's app-written validation (ZD-11's notes).
- A lead for the amendment: Shopify's setting Add-to-cart limit (SH-C-046/decides/SH-S-7483) is cited on CM-CHK-002. It is this thing's.
- Alternative for Shopify: CM-B2B-003, since its rules are set in catalogs.

**N07, Sales credited to staff.** New, domain A, area STF, parent CM-STF-001, A-amend.
- Members: Shopify's Staff sales attribution (20) and Zid's employee commission (1).
- Place of its own: Zid's POS plan policy `zidpos.employee_commision` (line 569). Shopify's role permission and POS tile aren't B-extent's kinds.
- Grounds, a reading on role: Shopify's attribution is for 'reporting and staff commission' (SH-41:109), and Zid's key names the commission.
- CM-POS-001 stays beside each POS line. Not CM-MKT-008, which credits orders to marketing (a homonym).

**N09, Trying the platform before signing up.** New, domain A, area ONB, no parent, A-amend.
- Members: Zid's Demo store (1) and Shopify's Store preview (3).
- Place of its own: Zid's route `:lang/demo` (line 437).
- Grounds, a reading on role: 'Explore the demo, then launch yours' (Zid), and building a store 'before signing up, and keep what you create when you’re ready to sell' (Shopify).
- Salla's Demo Stores are partners' stores (CM-DVT-004), not this. No BigCommerce or WooCommerce statement holds a demo store.
- Alternative: apart. Zid's demo store alone as the capability, and Shopify's store preview on CM-ONB-004.

## New capabilities of one platform (9)

| Group | Thing | Domain, area, parent | Place of its own | Grounds |
| --- | --- | --- | --- | --- |
| N08 | Zid employee attendance | A, STF, CM-STF-001 | POS plan policy, line 568 | A reading from the key alone; no string names it |
| N10 | Shopify Tipping (15) | C, CHK, CM-CHK-001 | checkout settings' anchor Tipping (admin-router line 358); POS settings item Tips | 'Show tipping options at checkout'; at the POS too |
| N11 | Shopify 3D Secure (2) | C, PAY, CM-PAY-001 | plan feature 'Fraud protection and 3D Secure checkout' (pricing line 85) | BigCommerce's BC-C-022/reason/BC-S-0130, on CM-PAY-022, a lead for its cell |
| N12 | Shopify Bug Bounty (2) | A, TRU, none | Partner Dashboard route bugbounty | a trust thing of the platform itself (a reading) |
| N13 | Shopify Sandbox organizations (4) | F, DVT, CM-DVT-003 | Partner Dashboard route sandbox_organizations | what it is, read from the modules' names |
| N14 | Shopify App versions (16) | F, APP, CM-APP-001 | Dev Dashboard item Versions; Partner Dashboard route versions | not CM-API-006, the API's versions (a homonym) |
| N15 | Salla Transfer Requests (10) | F, PTN, CM-PTN-001 | portal admin route and menu item | an app's ownership moved between partners |
| N16 | Salla Product certificates (3) | B, CAT, CM-CAT-001 | route /products/certificates and its navigation item | 'Certificate templates'; what a certificate is isn't stated |
| N17 | Salla Gift a Salla plan (1) | A, PLN, CM-PLN-001 | Store plan's settings item gift-a-plan | a plan bought as a gift; alternatives CM-PLN-001 or CM-PLN-005 |

## Things proposed onto existing capabilities (38 things, 38 groups)

Each row's `reading` quotes the definition's words. The ones that need the definition widened are named here:
- CM-ORD-013 (N20, Shopify's Timeline events): 'on an order' to 'on an order and the store's other records'.
- CM-NTF-001 (N21, Email customer): 'automatically' to 'automatically or by its staff'.
- CM-SHP-008 (N24, Salla's Bullet Delivery): 'the store's own delivery' to delivery 'by its couriers or by carriers'.
- CM-STF-002 (N26, Staff access restrictions): 'and the records each may reach'.
- CM-PTN-010 (N18, VIP Partners): its 'partner APIs' to 'APIs or its portal'.
- CM-AIA-003 (N32, Tinker by Shopify): text to text and images, in the admin or in an app of its own.
- CM-TRU-004 (N48, Web Bot Auth): 'at checkout' to the online store.

Eight things have a place of its own whose thing an existing capability already holds, so the place becomes that capability's evidence. B-extent: "A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not a new one." They are:
- Salla's VIP Partners routes (N18, CM-PTN-010, a reading on role);
- Shopify's Plus trial route (N19), under the Plus routes CM-PLN-001 cites;
- the Timeline events API group (N20);
- the Email customer route and template (N21);
- Salla's Bullet Delivery route (N24);
- Salla's custom fields route (N25), on CM-CNT-002 now that the held pass defines the fields, which Q1's U-005 lacked;
- Shopify's Data Sharing Preferences route (N49), the nearest capability, since its thing isn't stated;
- Salla's app category أتمت عملياتك اليومية (N62, CM-AUT-001).

The other thirty have no place of their own and go to the nearest capability. Among them are WooCommerce's Direct Debit (CM-PAY-001) and test account (CM-PAY-003), and Shopify's Planet (CM-SHP-001) and Commerce Components (CM-SFR-011).

## Out (16)

- **Titles that name only a grouping** (the ruling after SA-28):
  - Shopify's Finance (N22), over Capital, Credit, Balance, Payments, Bill Pay and Taxes. CM-PAY-023's note already says no capability holds the Finance suite.
  - Zid's Services (N23).
  - Salla's app_impact category حوّل الزوار إلى مشترين (N61), an outcome over several capabilities' apps, as WooCommerce's category Conversion is.
- **The admin's frame** (the ruling after SH-37): WooCommerce's Unified block editor assets (N31) and Shopify's Rich text editor (N50).
- **No thing of the store:**
  - Shopify's Storefront Signage Maker (N51);
  - Salla's National Day banners (N60), which advertise the platform to its merchants;
  - Salla's team task app (N63);
  - Zid's es pushdown (N56).
- **Nothing held says what the thing is:** Shopify's Beacons (N52), Seller health (N53) and Review modal (N54), and Zid's hermes, vitrin, collection moderators presenter and nd2026 (N55, N57 to N59).

## Supports, once each thing is decided

The amendment notes list supports that differ between batches: Staff sales attribution, Tipping, Saved views, Admin search, Admin languages, App versions, Sanity integration and Finance. A proposal, a reading: once the thing is a capability, each line's support is what its entry shows, by the brief's supports rules. Several lines are `shows` only because the thing had no place of its own, the brief's rule for a new thing. Those become `core` where the platform's own words say it does the thing, such as SH-36's 'search has been improved' and SH-35's saved views. Tinker's and Planet's `own-service` stand on their maker statements (the rulings after SH-2 and SH-35). Finance's lines go to the capabilities of the pages they name, or are dropped with the group.

## Leads for the amendment (facts, each now cited elsewhere or nowhere)

- Salla's تفريغ الكاش plan line (SA-C-002/decides/SA-S-2092), on CM-ACC-006: N03's.
- BigCommerce's Cloudflare CDN (BC-C-082/where/BC-S-0448), on CM-TRU-014 and CM-TRU-015: N03's, as `outside`.
- Shopify's Add-to-cart limit (SH-C-046/decides/SH-S-7483), on CM-CHK-002: N06's.
- BigCommerce's 3D Secure (BC-C-022/reason/BC-S-0130), on CM-PAY-022: N11's BigCommerce cell.
- Shopify's SH-I-1141, 'Earn 1% back on all sales', uncited: N04's.
- Shopify's help section SH-I-2109, 'Setting up tipping options for online orders', uncited: N10's.
- Salla's Merchant API folder Order Histories (SA-C-040/boundary/SA-S-1018), on CM-ORD-001: N20's widened CM-ORD-013.
- BigCommerce's 'IT IS SOLELY YOUR DUTY AND RESPONSIBILITY TO BACKUP' (BC-C-083/boundary/BC-S-0459), uncited: N29's CM-OPS-001, as `shows`.
- Bin locations (N43): SH-22's and SH-36's lines put bins on CM-INV-001. They align with the proposed CM-INV-005, or the proposal aligns with them.

## The cases I couldn't settle, and what would settle each

1. **N03, what Zid's extended caching caches.** Possibilities: the storefront's pages, its assets or its API. What would settle it: a label or a plans-page row for the policy in either language. Also, whether Salla's clear-cache line moves from CM-ACC-006.
2. **N06, whether Zid's limit is on an order's value or its quantity, and whether Shopify's quantity rules join.** What would settle it: Orders and products properties opened with the limit enabled, showing its field and unit. If the limit is on value, Shopify's quantity rules may better stay on CM-B2B-003, and the Add-to-cart limit decides the join.
3. **N07, whether Zid's employee commission is commission on sales credited to staff.** What would settle it: a label, a help article or the cashier's page for `zidpos.employee_commision`. N08's attendance has the same gap.
4. **N09, whether a demo of the admin and a preview store are one thing.** The join is on role. What would settle it: the coordinator's reading. If they are apart, Zid's demo store is a capability alone and Shopify's store preview goes to CM-ONB-004.
5. **N18, whether VIP Partners are CM-PTN-010's thing.** The definition rests on partner APIs, and Salla's tool is a portal's. What would settle it: a held page that shows how a VIP partner's stores are created and billed. The alternative is new, under CM-PTN-001.
6. **N24, whether express delivery by carriers Salla selects is the store's local delivery.** What would settle it: a statement that ties Bullet Delivery to Branch Delivery Zones, or one that sets it apart. The alternative is a new child of CM-SHP-006.
7. **N22, Finance: out or CM-PAY-023.** What would settle it: the coordinator's reading of the finance home ('Money', money:home). Every held visit answered "There's no page at this address" (SH-12:94).
8. **N17, gifting a plan: new, CM-PLN-001 or CM-PLN-005.** What would settle it: the gift card's terms (giftcards.resal.me, not held), which say whether a third party sells a plan or a balance.
9. **N16 and N13, definitions not held.** What a product certificate is: the certificate templates page with a template opened. What a sandbox organization is: its pages for a partner with access. Both now answer only their titles or "not found".
10. **N49, Data Sharing Preferences: what App Bridge's modal shares, and with whom.** What would settle it: the modal opened in the native app. It is proposed on CM-APP-006 as the nearest.
11. **N52 to N59, things named only by a key.** What would settle each: a held statement of what it gates or does. Those statements are BEACONS's and MANAGE_SELLER_HEALTH's titles, and the review modal's text. For Zid: hermes, vitrin and collection moderators. nd2026 may be Zid's National Day 2026 offer to merchants, which would make it N04's.
12. **N61 and N62, Salla's app_impact categories.** One is proposed out, the other onto CM-AUT-001. What would settle it: whether the coordinator reads a category by outcome as a place of its own. If it is one, N61 becomes a new conversion capability with WooCommerce's Conversion category, and N62 stays on CM-AUT-001.
13. **N32, Tinker.** CM-AIA-003 widened, or each tool on its output's capability (product shots on CM-CAT-007) with the tools for no store out. What would settle it: the coordinator's choice between the app's grain and its tools' grain.
14. **N20, Timeline events: CM-ORD-013 widened, or a capability of its own** over every record's events. What would settle it: whether the coordinator wants a record's history outside orders as a capability. Its place of its own, an API group, would carry it.
15. **N69, Trusted IP Address: what the trusted address restricts.** What would settle it: the salla.dev post, not held.
