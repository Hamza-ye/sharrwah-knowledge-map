# The held pass's dry run, review part R5a: ZD-1, lines 63 to 103

**What this is.** Part R5a of the review the brief `studies/class-model/briefs/H-review.md` (at `f0dd52bd`) sets: ZD-1's placements at `33946dbc`, lines 63 to 103. These are the dashboard-page-index's entries 59 to 100, from Communications to the shipping Transactions log. Line 103 is the first of entry 100's two lines; its second, line 104, belongs to R5b. The rows are in `review-H-R5a.tsv`. The review was read at `max`.

**Pins:**
- H-held.md and `held/selection.tsv` at `dc1e6414`;
- the model at `13205959`;
- other-product-class at `0d79b794f`.

**Abbreviations in the rows:**
- `source.js@N` is the character offset N in `other-product-class@0d79b794f:zid/structures/dashboard-page-index/source.js`. That file is the source `meta.json` names: sha256 `b950901d…`, 36,136 bytes, one line.
- `rest-en#N`, `gaps-en#N`, `en-2#N` and `en-3#N` are `zid/raw/runs/<run>/steps/NNN.text.txt`, with the run labels ZD-1's notes define.
- "ledger" is `zid/index/ledger/dashboard-routes.tsv`.

Every claim below that isn't a quoted fact is a reading.

## Counts

| Verdict | Rows |
| --- | --- |
| stands | 40 |
| missing line | 10 |
| missing scope | 4 |
| can't tell | 1 |
| **all** | **55 rows on 41 lines** |

Every line holds its capability. 13 of the 41 lines carry a miss.

**The misses by cause and effect:**

| Cause | Effect | Rows | Lines |
| --- | --- | --- | --- |
| care | column | 8 | 66, 69, 71, 72, 75, 82, 87, 102 (a second capability whose cell already holds core) |
| care | filler | 2 | 91, 92 (CM-PAY-012 gains the fillers Mokafaa and Qitaf) |
| brief | column | 4 | 76, 85, 100 (a store flag as scope); 91 (Saudi Arabia, from the page) |
| evidence | column | 1 | 100 (whether `showNewZones` is released) |

No miss changes a count, a kind or a capability. The lines that change a count are right:
- lines 67 and 97 make CM-SUP-002 and CM-NTF-003 held on Zid;
- line 87 gives CM-MKT-006 its core;
- lines 95 and 96 give CM-SUP-004 its core;
- line 102 gives CM-SHP-017 its core.

The checker prints each of these as CHANGES, and each stands.

**Thirds.** ZD-1's 143 lines split into thirds at about line 49 and line 96.
- Lines 63 to 96, in the middle third: 12 miss rows on 34 lines.
- Lines 97 to 103, in the last third: 3 miss rows on 7 lines.

They show no growth toward the batch's end.

**Omissions not counted as verdicts.** The source lists seven pages only where the store's donation condition is unset (see "Store conditions"): lines 80, 86, 99, 100, 101, 102 and 103. Their readings don't say so. A reading that leaves a condition out isn't untrue, so these aren't `wrong reading`. Under the ruling below, each is a `column` miss of care. Each row's `why` names it.

## The leads

Of the 40 lines on a capability, the right cap_id is among the leads `show --candidates` prints now on 21. It is missing on 19:
- lines 63, 67, 68, 73, 77, 78, 83, 84, 87, 88, 91, 92, 94, 96, 97, 98, 99, 100, 103;
- 8 entries print no lead at all: the containers Communications, Store, Whatsapp and Logistics, and Automatic replies, Message logs, Settings and Zones.

Of the 10 missing lines, 4 capabilities were leads the agent didn't place: CM-ACC-004 (69), CM-ACC-007 (71), CM-MKT-022 (75) and CM-SHP-009 (102). The other 6 were not leads: CM-NTF-002, CM-STF-002, CM-MKT-002, CM-NTF-001 and CM-PAY-012 twice.

## The cases

**Containers.** In this part: Communications (63), Store (68), Marketing (81), Whatsapp (94) and Logistics (99). All five stand.
- A container is a place of its own, by B-extent's "What a place of its own is". The source marks each `type:group`, with its own title, path and children.
- By B-extent, a place whose thing a capability's cells already hold is that capability's evidence.
- A container's thing is what its title names. Where the title names only a grouping, its thing is the page its own path opens. The source gives containers a path:
  - Communications opens `settings/communications/orders`, the Order notifications page, on CM-NTF-001, whose cell already cites التواصل (ZD-I-0145);
  - Store opens `settings/information`, the store's details, on CM-ACC-006;
  - Marketing is CM-MKT-005's own term;
  - Whatsapp is in CM-NTF-004's terms (واتساب زد);
  - Logistics is the first step of CM-SHP-001's cited route (لوحة التحكم > اللوجستيات > طرق الشحن, ZD-S-0836).
- A container that names no capability's thing by its title or its path would be `new:<title>`, `shows`, with its children in the notes.
- This stays within B-extent. It is fix F3.

**Pages with a release badge.** In this part, badge `new` on 76, 83, 85, 87, 91, 92 (the `new-qitaf` path) and 96, and `beta` on 90. The agent kept `core` and put each badge in the reading; every reading here names its badge. That stands.
- B-extent makes `shows` only of a flag stated as not released (`"released": false`).
- A route the source lists to the stores with a badge is the platform's own route, released to them. The demo store can activate Customer referrals: "Activate" (rest-en#195).
- H-held.md rule 4 sends a help page's release marker to the reading. Its flag clause also counts "a beta" as not released, which reads two ways for a route.
- This stays within B-extent. It is fix F4.

**Store conditions.** The source lists several pages only under a store condition:
- `customerWallets` (76, 85, source.js@24586, @26023);
- `be(storeId)` (84, @25853);
- `xe()` (91, @26821);
- the Qitaf choice (92): the path `qitaf` is listed only for stores in a fixed list of store ids, `nt` (@5771), whose `isQitafEnabled` is set and `isMoneyHashQitafEnabled` isn't (`rt`, @6052), and `new-qitaf` otherwise;
- `showNewZones` (100, @28209);
- the condition `s` (`N()`), under which orders read `navbar:donations`, customers `navbar:donors` and products `navbar:donationOpportunities` (locales: "Donations", "التبرعات"). Under it, stock notifications (@25239), bundle offers (@26202) and the whole Logistics section (@27925) aren't listed.

Ruling:
- **Where the source names the condition,** it is the line's `scope`, in the source's words: `customerWallets`, `showNewZones`. B-extent gives a released flag "its plan or store as its scope", and a page listed under a store's flag is stated for the stores that have it.
- **Where the source computes it without a name** (`be`, `xe`, the `nt` list, `s`), it goes in `reading`.
- **Where the observed store's page says the feature isn't enabled** (Zones: "This feature is not enabled for your store", rest-en#169), `core` against `shows` can't be told. Under B-extent's flag convention it hangs on whether the flag is released, which nothing held states (line 100).

B-extent speaks of flags, not of a page's listing condition. So this is **a method ruling** for the coordinator. It is fix F5. Under it, the Qitaf group (line 92) keeps one line: its condition is computed and goes in reading.

**Customer Referrals (line 90).** The `new` stands.
- **Its thing.** Customers get a code, and both they and the friend they invite are rewarded with cashback or points after a holding period (rest-en#195). No cell's reading holds buyers inviting buyers. CM-MKT-013 and CM-MKT-014 are affiliates and creators. CM-PTN-008 refers the platform's plans. CM-LOY-004's cells hold points programmes.
- **What the notes didn't name.** CM-MKT-013's Salla cell holds `marketing/referrals`, but only as one path of the affiliate app `@salla.sa/ui-merchant-partner-marketing` (SA-S-3550), beside the unreleased flag `affiliate-referral` (SA-S-3454). Whether Salla's page is a customer referral programme isn't in the concern map. Salla's dashboard routes in observed-sa would settle whether the new capability has a Salla cell: an item for the coordinator.
- **Its place of its own.** An admin route: the page index's `marketing.referrals`, and the manifest's `marketing/referrals` and `marketing/referrals/program` (ledger: rest-en#195, #116).
- **Its supports.** `core`, its `beta` badge in reading (the badge ruling above).
- **Its parent.** The notes propose CM-MKT-005, "following Zid's grouping under Marketing". Zid's marketing page groups its tools more finely, and puts "Customer referrals … Loyalty and rewards … Beta" beside Cashback offers (rest-en#212). Under B-extent's `parent` convention ("the platforms' own grouping"), that puts it in area LOY, under CM-LOY-004, which the notes give only as the alternative. The page index's Marketing holds CM-LOY-003 and CM-LOY-004 too, so the coarser grouping doesn't decide the area.
- **Its names.** English "Customer Referrals" (the page's heading reads "Customer referrals program"); Arabic "برنامج دعوات العملاء".
- **My searches.** `caps --terms`: referral; referrals; refer a friend; customer referrals; invite friends; referral code; دعوات العملاء; برنامج دعوات العملاء; إحالة; الإحالة; دعوة صديق; ادع صديقك. Only CM-MKT-013 and CM-PTN-008 come up. `search --platform salla` and `--platform shopify` give no customer referral programme.

**The notes' other "couldn't tell" items in this part:**
- **62, Product question notifications.** CM-NTF-001 stands against CM-SUP-001: the page's two toggles are both notifications. The description also names the merchant's notification, so a second line on CM-NTF-002 is due (line 66).
- **83, Automated Messages.** Both: CM-MKT-006 stands, and the page's "keep your customers informed about their orders" adds CM-NTF-001 (line 87).
- **84, Marketing campaigns.** CM-MKT-007 stands.

**Mokafaa and Qitaf (lines 91, 92).** This is a difference with the model the notes didn't see. CM-LOY-004's own note reads: "Homonym: Salla's مكافأة الراجحي (SA-C-119, a payment method, domain C) isn't a store's reward". CM-PAY-013's note lands that concern in CM-PAY-012.
- Zid's pages state both sides. Customers earn the bank's or STC's points when they shop, at earning rates set by the Zid plan, which is a reward the store funds: CM-LOY-004. Customers also pay with the points: CM-PAY-012.
- So each takes a second line, on CM-PAY-012, with its filler.
- `core` holds against `extension-point` and `outside`. By B-extent's clause, "the platform itself does it for the merchant": Zid's own page activates the programme at Zid's own rates. The bank and STC run the points and are the slot's fillers.

**Readings that rest on a file beyond the item and its source.**
- 39 of the 41 lines cite a run's page ("page text …"), reached through the ledger. Lines 68 and 101 cite only `source.js` and the cell. None in this part cites `dashboard-locales`.
- H-held.md rule 1 names only the item and its source. Its reading list names `index/`, where the ledger names the steps, but not `raw/runs/`.
- The checker already searches "the platform's run pages" for a reading's quotes (`held_entries.py`, `run_text`). So the tools allow what the brief doesn't name.
- Of the 10 missing lines:
  - 66, 72, 87 and 92 rest on the pages alone: the settings landing gaps-en#2, which the agent quoted, or the page itself;
  - 91 rests on its page and on CM-LOY-004's note;
  - 69, 71, 75, 82 and 102 hold on the item and its source alone, by the cells' terms, the title key or permission, and the leads. The pages only confirm them.

This is fix F1.

## Fixes to H-held.md, the build and the checker

| # | Fix, in words the coordinator can paste | Within B-extent? | Checker test |
| --- | --- | --- | --- |
| F1 | Rule 1: "To read what an entry is, you may also read the page as a run opened it, through the ledger's steps (`index/ledger/…`), and, for a route no run opened, the locale strings it names. Cite them in `reading`. The entry's `scope`, `filler` and `quality` come from the entry and its source only" (or the coordinator rules that the page's words may give them; line 91's Saudi Arabia and the notes' rates hang on this). | Yes | The quote test already reads run pages. A note for each line whose reading cites a page while its scope is empty and the page names a country would catch 91. |
| F2 | Rule 2, after "write two lines": "Before you write one line, read the leads and the cells of the capabilities the page's words name. Where a cell's reading cites the same page or the same term for its capability, as CM-ACC-004's cites بيانات المتجر, the entry is that capability's too." | Yes | Print each lead matched by the entry's whole title, in either language, or by its title key's last word, where no line of the entry places it. Catches 69, 71, 75 and 102; not 66, 72, 82, 87, 91 or 92. |
| F3 | Rule 3: "A container (a section with children, such as Settings, Marketing or Logistics) is a place of its own. Place it on the capability whose thing its title names; where its title names only a grouping, on the capability whose page its own path opens; failing both, `new:<title>`, `shows`, with its children in your notes." | Yes | None while the items don't carry `sidebar.type`. With it, print each container line for a second reading. |
| F4 | Rule 4, flags: "A page or route the source lists with a badge (`new`, `beta`) supports `core`, with the badge in `reading`. `shows` is only for a flag the platform states isn't released (`released: false`, `is_experimental: true`)." | Yes | None while the items don't carry badges. With them, check that a line on a badged entry names its badge. |
| F5 | Rule 5, scope: "A page the source lists only under a store's condition takes the condition as its `scope`, in the source's words (`customerWallets`). A condition the source computes without a name goes in `reading`. Where the observed store's page says the feature isn't enabled, list the line under 'couldn't tell'." | **Method ruling**: B-extent's flag convention speaks of flags, not of a page's listing condition | None while the items don't carry conditions. With them, check that each conditioned entry states its condition in scope or reading. Catches 76, 85 and 100, and the omissions on 80, 86 and 99 to 103. |
| F6 | Rule 2: "Read the placed capability's note. Where it names a homonym whose words the entry holds, such as CM-LOY-004's مكافأة الراجحي, place the entry where the note sends it." | Yes | Print each line whose capability's note holds "Homonym" with a term the entry's text holds, once folded. Catches 91, not 92. |
| F7 | The build: carry each page object's `permission`, `sidebar.badge`, listing condition and conditional title into `dashboard-page-index`'s items, or into the entries, so the entries state them. | n/a (the build) | Makes F3 to F5 testable. |

## What the batch never placed

These are things the source states between `source.js@20876` (`settings.communications`) and `@29006` (`payments`), the stretch that holds this part's items, that no entry holds.

1. **The donation store's titles.** Six of the 18 page objects the extractor drops lie here:
   - `orders`, `orders.all`, `orders.manual` (@23623 to @23949);
   - `customers`, `customers.all`, `customers.groups` (@24239 to @24722).

   For a store whose condition `s` is set, their titles are:
   - `navbar:donations` "Donations" / التبرعات;
   - `allDonations`, `manualDonations`;
   - `donors` "Donors" / المتبرعون;
   - `donorsGroups` (locales lines 7282, 7339 to 7341, 7397, 24134, 24193 to 24195, 24252).

   With them goes the catalog's `donationOpportunities` (`ot()`, @9713). The manifest holds their routes, `orders`, `orders/drafts`, `customers` and `customers/groups` (ledger), but no titles, and no Zid entry names a donation (`held/zid/entries.tsv`). **So the evidence map's reading that "the model loses nothing" fails here.** CM-SEL-007, Donations, is `none-held` on Zid; its cell's only hit is "a charity (جمعية خيرية) as a type of business". A reading: Zid's own admin titles a donation store's orders, customers and products as donations, donors and donation opportunities. That supports `core`, and would make the cell held. The build left it out: the extractor drops a conditional title. R4 tests the 18 pages as a whole.
2. **What a donation store isn't given:** stock notifications, bundle offers and the Logistics section (@25239, @26202, @27925). No entry states it. It would change readings or scopes only (`column`), but with (1) it is part of what Zid shows for donation stores. Left out by the build, which doesn't carry conditions, and by the agent's readings.
3. **Each object's permission, badge and condition.** The evidence map already names these. In this stretch, the permissions are the dashboard's constants for the staff permissions the cells hold, such as `ABANDONED_CARTS.view`, `COUPONS.view`, `SMS_CAMPAIGNS.manage` and `ZIDSHIP.viewShipment`. None would change a cell here: each cell cites the matching staff permission or holds `core` already.
4. **The computed objects** `x` (Zid Voice), `O` (catalog), `b` (Zid Ads), `A` (online store) and `j` (analytics) are defined elsewhere in the module. Their items are R4's, except catalog, which is dropped (see 1). Nothing else here is a thing: icons, `analyticsEvent` names and `hasPulseDot` are the interface.

**The rendering against the item.** Item 70's `title_ar` ends in a carriage return, `رابط المتجر الالكتروني\r`, which the rendering drops. No term or placement changes.

## The notes' claims, for this part

| Claim | Verdict | Why |
| --- | --- | --- |
| Customer Referrals: what it is | stands | rest-en#195, as quoted |
| Customer Referrals: its place of its own | stands | page index `marketing.referrals`; manifest `marketing/referrals`, `/program` (ledger) |
| Customer Referrals: searched terms, and "only CM-MKT-013, CM-MKT-014 … and CM-PTN-008" | stands, short | My searches find the same. The claim leaves out that CM-MKT-013's Salla cell holds `marketing/referrals` as an affiliate app's path (SA-S-3550). |
| Customer Referrals: proposed parent CM-MKT-005, "following Zid's grouping under Marketing" | doesn't stand | Zid's own tool category is "Loyalty and rewards" (rest-en#212): area LOY, parent CM-LOY-004. |
| 62: CM-NTF-001, CM-SUP-001 the alternative | partly | NTF-001 holds; the description and the page also name the merchant's notification: CM-NTF-002 too (line 66). |
| 83: CM-MKT-006, CM-NTF-001 the alternative | both | A second line on CM-NTF-001 (line 87). |
| 84: CM-MKT-007, not CM-MKT-005 | stands | SMS and WhatsApp campaigns to a segment, under `SMS_CAMPAIGNS.manage` |
| The containers 59, 64, 77, 91 and 96, each on its children's capability | stands | By the container rule above. The rule rests on each container's title or own path more than on its children. |
| Badges: `core`, badge in reading | stands | The badge ruling above (F4) |
| Store flags left out of scope, put in reading | ruled otherwise, as a method ruling | Named conditions go in scope; computed ones in reading (F5). |
| What may be read: run steps and locales, for reading only | confirmed as the brief's gap | F1. The checker already reads run pages for quotes. |
| The page index drops 18 of 137 objects; the items leave out permission, badge and condition | confirmed in this stretch | Six of the 18 lie here, with the donation titles the manifest can't give back (see above). |
| "Several readings depend on them (47/48, 51, 72, 81, 88/89, 97, 41)" | stands, short | Of this part's entries, 76, 82 and 96 to 100 also sit under a condition (donations) their readings don't state. |
| Qualities seen on the pages: Mokafaa's and Qitaf's rates by plan | stands | rest-en#35: Rise 8.5 % and 15 %, Growth 8 % and 13 %, Professional 7 % and 10 %; rest-en#196 likewise. F1 decides whether a page may give them. Not listed: Team members 0/20 (gaps-en#28), which CM-STF-001's cell holds already from the plan line (ZD-S-0939). |
| Differences from the model's cells: 63 SUP-002 none-held; 92 no chat of Zid's own; 99 a place for tracking the cell lacked | stands | Lines 67, 95 and 102. |
| Differences the notes don't name | — | Line 97 makes CM-NTF-003 held on Zid. Line 73's words answer CM-STF-003's reading, which says no statement gives roles to a team group. Lines 91 and 92 meet CM-LOY-004's homonym note. |

The notes number entries by their place in the batch: entry 63 is line 67, entry 92 is line 95, and entry 99 is line 102.
