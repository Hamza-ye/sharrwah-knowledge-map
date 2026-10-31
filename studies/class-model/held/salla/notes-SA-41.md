# Held pass, Salla, batch SA-41: notes

85 entries (effort high), evidence at observed-sa@b0bd0b16:
- 1 to 21: the last of `portal-help-center-article` (`partner@en`), the articles of three categories, by their line in `structures/salla/portal-help-center-article/partner@en/items.jsonl`:
  - 1 to 4: Influencers Service Information (line 11);
  - 5 to 9: Influencers Services Listing (line 12);
  - 10 to 21: Ready Stores (line 13), a category with no entry of its own (SA-39's check: the concern map cites it).
- 22 to 85: the first 64 of `portal-help-center-resource` (`partner@en`), the Partners Resources tree at `/help/resources`, by its line in `structures/salla/portal-help-center-resource/partner@en/items.jsonl`:
  - 22 to 38: Get Started (line 1), its resource and all its sections and articles;
  - 39 to 61: Apps Support (line 2), all of it;
  - 62 to 77: Themes Support (line 3), all of it;
  - 78 to 84: Services Support (line 4), its resource and its sections 0 and 1 with their articles;
  - 85: the resource Influencers Support (line 5).

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-41`).

`portal-help-center-article` is now placed whole (SA-39 to SA-41).

**`SA-42` holds the rest of `portal-help-center-resource` and hasn't run.** Its entries are Services Support's sections 2 to 4 (`SA-E-c778e872`, `SA-E-ffdee408`, `SA-E-a5848f14`, `SA-E-0b2e8f84`) and every section and article of Influencers Support (`SA-E-0366d867` to `SA-E-c8bc71c0`). The batch files put the resource Influencers Support (85) in SA-41 and its sections in SA-42. The coordinator aligns SA-42 with the rules below, which my lines follow.

**Placed:** 84 entries on capabilities and 1 on a new thing (42), in 99 lines. No entry is `out`. 21 entries take more than one line. Nine lines each group two entries: a card and its one link (or post), which hold the same words.
- **Supports**, by line (a line of two values counted in each): 33 `core`, 29 `extension-point`, 39 `shows`. One of the `shows` is the new line. There is no `own-service` and no `outside`.
- **Fillers** are on 2 lines, from entry 3: the social media platforms, on both influencer cells, as SA-40's entry 71.
- **Qualities** are on 4 lines, from three entries:
  - 11: a Plus or Pro plan without cost while a ready store is set up (on CM-DVT-005 and CM-PLN-001);
  - 12: Salla's themes and the App Store's apps free of charge for a ready store;
  - 19: no limit on the number of ready stores a partner can develop and list.
- **Scope:** entry 11's two lines carry `Plus;Pro`, the plans its answer names. No other entry states a plan, country or store.

**Sources read:**
- the brief and what it names;
- SA-39's and SA-40's notes, with the coordinator's checks, and their placements;
- the rulings, with their last section;
- the evidence map, and B-extent's "Cells and evidence" and conventions;
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and the register's rows for the two structures;
- the selection rows and `show --meta`;
- both structures' `source.json` and `meta.json`, and the concern map's citations of the FAQ (SA-S-5107 to SA-S-5113, SA-S-5131, SA-S-5137) and of the portal's navigation (SA-S-1945, the Help Center's Partners Resources);
- the cells of every lead, and of every capability the entries' words name;
- for alignment, SA-35's, SA-37's and SA-44's lines on private apps (CM-APP-009).

`held_index.py` finds none of the tree's salla.dev links held: the blog, the tutorials, the posts on trusted IP, private apps' payment, shipping apps' payment cycle and ready stores. The YouTube videos aren't held either. The docs.salla.dev links are held only as the docs' page itself (below, for the second stage).

## Rules my lines follow

### The articles, 1 to 21

SA-39's and SA-40's article rules hold throughout. An article's question and answer are read together, by what they say the platform does. On top of those:

1. **Influencers' articles take both CM-MKT-015 and CM-PTN-009** (SA-39's rule 3, SA-40's rule 4):
   - the influencer's profile and its switches and sections, its services list and its additional services are `extension-point` (2, 5 to 9);
   - the categories an influencer markets for, and service terms and requirements, are `shows` (1, 4);
   - the social media platforms are `extension-point`, each a filler, as SA-40 placed the same list (3).

   Entry 5's 'Facebook 5 posts for 1000 SR' is an example, so it has no quality and no filler.
2. **Ready stores go on CM-DVT-005,** the partner's side and the platform's rules together:
   - the partner creating, editing, developing and listing ready stores in the portal, and preparing them in the store's own dashboard, is `extension-point` (10, 15, 16, 19), as SA-34 to SA-37 placed the portal's Ready Stores routes;
   - Salla's review and re-approval, its free plans and free themes and apps during setup, its showcase and promotion of ready stores, and the purchase through the platform are `core` (11, 12, 14, 15, 17, 18);
   - who sets the price, and the store being the buyer's after purchase, are terms: `shows` (13, 20, 21).
3. **A thing an answer names beside the ready store takes its own line:**
   - the partner account as a condition is CM-PTN-002 `shows` (10), as SA-40's rule 5;
   - the plans Plus and Pro, given free during setup, are a plan policy for a kind of store: CM-PLN-001 `core`, scope `Plus;Pro` (11);
   - Salla's themes go on CM-SFR-001 (12, below), and the App Store's apps on CM-APP-002 `shows` (12);
   - the store's plan, theme design and products, named only as what the partner customizes (16) or the buyer may edit (20, 21), go on CM-PLN-001, CM-SFR-002 and CM-CAT-001 `shows`. The apps the buyer may edit go on CM-APP-001 `shows` (20, 21). 'settings', 'content' and 'text' name no one capability and take no line.

### The resources, 22 to 85: rules for SA-42

The tree is the Partners portal's page Partners Resources (`/help/resources`), which the CM-PTN-001 cell cites as the Help Center's Partners Resources (SA-S-1945). It holds four levels:
- a resource is a tab of the page;
- a section is one of four types: `article-list`, `card-horizontal`, `card-horizontal-full` or `card-vertical`;
- a subsection is titled with one post;
- an article is a link, with an empty title and content, whose entry carries its section's (or subsection's) title and description.

Subsections have no entries of their own. Their titles are in their section's entry and in their article's entry.

1. **A resource is a container** (M-13). It goes on the capability its title names, `shows`, since a help centre's grouping names a topic (SA-39's rule 3):
   - Apps Support: CM-APP-002;
   - Themes Support: CM-SFR-003;
   - Services Support: CM-PTN-005;
   - Influencers Support: CM-MKT-015 and CM-PTN-009.

   Get Started names no capability, so it goes on the capability of the page it is a tab of, CM-PTN-001 (22). A resource takes no line for the Partners Resources page it sits under.
2. **An `article-list` section is a container**, `shows`, on the capability its title names: Public Apps on CM-APP-002, Private Apps on CM-APP-009, Shipping Apps on CM-SHP-015, APIs Documentation on CM-API-001, Themes Basics on CM-SFR-003, Twilight Themes Documentation on CM-SFR-002, and the two service sections on CM-PTN-005. A section titled as its resource is goes where its resource goes (23).
3. **A subsection with no article** is named only in its section's entry, so it takes its line there, read as a post's title. Two such subsections are in this batch:
   - 'How to customise Themes for Salla stores' (30), CM-SFR-002 `shows`, a guide; its Arabic names متجر الثيمات, so it also takes CM-SFR-003 `shows` (the ruling after SA-4);
   - 'How to create and update Private Apps' (43), CM-APP-009 `extension-point`, beside the section's `shows`.
4. **A post, or a card that stands for one post, is read as a help page's title** (the brief's rule 4; SA-39's and SA-40's rules):
   - `core` where it names the platform's own feature or tool: the partner account (24), ID verification (25), Twilight (27, 64, 65, 69, 71), the Salla CLI (55, 70), the App API (51), the Merchant API (52), private apps' payment (44) and shipping apps' payment cycle (47);
   - `extension-point` where developers or partners build, publish or offer through the platform: a first app (26, 41), private apps (43, 44), publishing themes (66), themes made with custom components (71), offering services (80, 81), and the shipping apps' API (46, 50; as SA-40 placed shipment services integrating with Salla);
   - `shows` where it gives only a guide or a topic: shipping app search (48), an app's popularity (53), theme promotion (67), completing service details (83, 84), and a video with no title (32).

   A release marker ('is here', 'now!', 'New', 'has arrived') goes in `reading`. A card and its single link hold the same words, so they share one line.
5. **The platform's own channels for partners are `core` on CM-PTN-001.** These are the blog (28, 29), the tutorials (30, 33), the developer community on Telegram ('You still have more questions?', 34, 35, 57, 58, 73, 74), the Telegram help channel (36, 37, 59, 60, 75, 76) and the support email (38, 61, 77). The CM-PTN-001 cell holds the Help Center's Partners Resources and Support, and 'dedicated technical and commercial support for all partners' with email as an official channel (SA-S-5098). This is the partners' side of the platform's learning for merchants, which is CM-ONB-003's (the ruling after SA-2 and SA-5). Telegram is where the group is, so it isn't a filler.
6. **Homonyms:**
   - 'support' (CM-SUP-005) is a store's ticket system, not Salla's support for partners;
   - 'blog' (CM-CNT-004) is a store's blog, not the partners' blog;
   - 'service provider' (CM-TRU-013, CM-TRU-015, CM-PAY-004) means a data processor or a payment processor, not a partner offering services;
   - 'promotion' (CM-MKT-001, CM-MKT-003) is a store's promotion, not a theme's;
   - 'collection' and 'categories' (CM-CAT-003) are a store's product groupings;
   - 'marketing campaigns' (CM-MKT-005) are a store's campaigns, not Salla's own promotion of ready stores.
7. **Terms** are the entry's own words, in both languages where the entry gives both. Links aren't held, so they clarify nothing.

## New things

1. **Trusted IP Address**, entry 42, `shows`.
   - What the entry states: a post of the section Public Apps, 'Secure your Apps with the Trusted IP Address now!' (the Arabic title is the same English).
   - Place of its own: none held. The entry is only a post's title. The app's own record carries a field `trusted_ip` (an empty list) in `structures/salla/portal-app-scopes/partner@en/source.json`, the partner's app as the portal answers it. That is a field, not a place of its own, and I didn't read it beyond the field's name.
   - Proposed: domain F, area API, parent CM-API-002 (app authorization: a restriction on where an app's calls may come from). CM-APP-002 is the alternative, as a setting of a developer's app.
   - Names: Trusted IP Address (English only; the Arabic field repeats the English).
   - Searched: trusted IP; IP address; whitelist; allowlist; trusted; IP; security; secure; app security; authorization; OAuth; app keys; client secret. The hits (CM-API-002, CM-API-003, CM-TRU-001, CM-TRU-018, CM-SFR-010 and others) don't hold it.

## Entries I couldn't tell, and what would settle each

- **31: CM-ONB-004 (a `CHANGES` line).** 'How to create Salla stores' / 'خطوات تأسيس متجرك الإلكتروني' (the steps to set up your online store) is a YouTube video, not held, among the partners' tutorials. I placed it `shows` on store setup as the thing it most plainly names. CM-ONB-004's Salla cell holds nothing: no statement showed a wizard, profile or tasks, and this title doesn't show them either. A `shows` line makes the cell held with no placement. The alternatives are CM-ONB-003 (learning for merchants), CM-ACC-001 (the merchant account and sign-up) or CM-DVT-003 (a partner's stores). The video would settle it.
- **12: CM-SFR-001 `core` or `own-service`.** 'any Salla-developed theme' names Salla as the themes' maker. I read it as the platform building the storefront's theme itself, as the cell reads Salla's store design and Shopify's cell reads its own themes. The words name 'Salla', not one of the group's companies (the checker's `GROUP` list, CM-ACC-002), and M-1 asks for a statement naming the company. If the coordinator reads 'Salla-developed' as maker evidence and a theme as a separate product, the line is `own-service`, and on CM-SFR-003 rather than CM-SFR-001.
- **44: CM-PTN-003 or CM-APP-003.** 'Get paid for Private Apps with Salla' is the developer's side, the platform paying a partner, so I placed it on partner payouts. CM-APP-003's note leaves the developer's payout to area PTN. If the post shows the platform billing the merchant for a private app, CM-APP-003 takes a line too. The post would settle it.
- **47: CM-PAY-031 or CM-PTN-003.** 'Payment Cycle Automation for Shipping Apps': CM-PAY-031's note reads the shipping apps' managed settlement (labels withheld from the wallet and settled with the carrier) as its own, so I placed it there `core`. Partner payouts is the alternative. The post would settle it.
- **50: CM-SHP-015 alone, or CM-SHP-009 too.** 'Shipment APIs' / '… لتطبيقات الشحن': the Arabic names the shipping apps, so I kept the one element on CM-SHP-015 (the ruling after SA-4). CM-SHP-009's cell holds the developer section Shipments & Fulfillment APIs as `shows`. The docs' navigation id (below) would settle it.
- **71, 72: CM-SFR-002 or CM-SFR-005.** 'Custom Components, Your Home Page Upgrade Tool', with a post on the single product page with Twilight themes. I read it as the Twilight engine's components (CM-SFR-002 cites the Twilight docs folder Components). CM-SFR-005 is component bundles published in the Theme Marketplace, `extension-point`. The post would settle it.
- **22: CM-PTN-001 `shows` or `out`.** Get Started's sections are several capabilities' pages: the partner account, apps, Twilight and the partners' channels. The ruling after SA-28 makes a title naming only a grouping over several capabilities `out`. The coordinator's message calls the five resources containers, and its title names the partner's start in the programme, so I placed it on the page it is a tab of. Entry 23, the section of the same title, follows it.
- **16, 20, 21: the store's features named in passing.** I gave plan, theme design, products and apps `shows` lines (rule 2's "every thing it names"). They change no cell. A coordinator's rule that a store's features named only as what can be edited take no line would drop seven lines.
- **51: CM-APP-010 for 'App APIs'.** The App API holds an app's Settings (CM-APP-010), Subscriptions (CM-APP-003) and App Details Builder (CM-APP-002). I placed it where the cell cites 'the extension point App API'.
- **11, 12: the qualities.** 'without any cost to you' and 'completely free of charge' are prices in the answer's words, as SA-39 gave registration 'free'. A reading that a waiver isn't a price would drop them.
- **17: the ready stores' showcase.** 'a dedicated platform accessible from Salla’s main page' (the Arabic: 'قسم مخصص داخل منصة سلة', a dedicated section inside Salla's platform) could be a place of its own, a marketplace of ready stores for merchants. It isn't held, and CM-DVT-005's note says who buys a ready store isn't stated. Entries 17 and 18 now state it: merchants buy them through the platform.

## Items against sources

- **Both structures:** `items.jsonl` and `source.json` agree: the five resources and the three article categories are equal, but for the capture's `position`.
- **Missing entries:**
  - the subsection 'Get paid for Private Apps with Salla' holds the same link twice (articles 629223846 and 1486630979); only the first has an entry (44);
  - the subsections 'How to customise Themes for Salla stores' and 'How to create and update Private Apps' hold no article, so they have no entry (30, 43 place them).
- **Duplicates:** the Ready Stores question 'Can I edit the store after purchase?' is held twice (articles 10 and 11, entries 20 and 21), with answers that differ by one comma. One line places both.
- **Salla's numbers recur** (observed-sa's `docs/READING.md`):
  - the subsections of the section Get Started carry the FAQ's category ids: 2080834032 (Influencers Service Information), 318898285 (Influencers Services Listing) and 1176306442 (Ready Stores);
  - the resource Influencers Support's id, 1731593753, is the section Blogs' id too.

  An equal number links nothing across these lists.

## For the second stage: what the sources state that no entry holds

- **`trusted_ip`**, a field of the partner's app record (`structures/salla/portal-app-scopes/partner@en/source.json`), for the new thing Trusted IP Address.
- **The docs.salla.dev links** (50 to 52, 69, 70: `?nav=01HNA8MH78MVX1S0DRXDHE3A1K`, `01HNA8M216X4HFNGWM9TWSTCKQ`, `01J1Y9KTRRDA57Q8ZSW95TTVDB`, `01HNFTD5Y5ESFQS3P9MJ0721VM`, `01HNA8QHCPJTCY5VSEZ616JCAK`). `held_index.py` resolves each to the docs' page itself (`structures/salla/docs-sidebar/merchant-api@20261008T095742Z`; `raw/runs/20261008T095742Z-stage0-entry-points/fetch.warc.gz@398441`), since the query is the docs' own navigation. The nav ids would name the folders (Shipment APIs, App APIs, Merchant APIs, Twilight, Salla CLI) in `docs-navigation`. That would settle 50 and 51.
- **Not held** (`held_index.py`):
  - salla.dev's blog and tutorials, and the posts on trusted IP, private apps' payment, shipping apps' payment cycle and ready stores;
  - the YouTube tutorials.

  They would settle 31, 42, 44, 47, 71 and the ready stores' showcase (17).

I read no run step beyond the entries.

## The checker's lines, read again

- **`CHANGES` CM-APP-009@salla gains `extension-point` and becomes held** (lines 61, 62: entries 43, 44, private apps). These are SA-35's changes, which the coordinator's check accepted and SA-39 noted; the cell isn't amended yet. My lines follow the same reading, so I kept them.
- **`CHANGES` CM-ONB-004@salla becomes held** (line 51: entry 31). This is a `shows` line from a video's title (above). I kept it as the plainest place and listed the alternatives.
- **`NOTE` core on a product named with the platform's brand** (lines 43, 54, 74, 75, 81, 86): 'Salla Partners Account', 'Salla Partner Telegram group', 'Salla CLI', 'Salla Developers'. Each names Salla's own partner account, community, CLI or theme engine, which the cells already hold as the platform's own (`core`). No line rests on a maker.
- **`NOTE` new thing whose entry has leads** (line 60, entry 42). The leads are CM-APP-002 (by public apps, the section), CM-PTN-001 and CM-SUP-005 (by support, the resource's name) and CM-API-008 and CM-API-009 (by address). I read each cell: none holds a trusted IP address.
- **`NEW`:** Trusted IP Address, 1 line.
- No quote prints 'found nowhere held'. I quoted only within a line of the source, since several answers hold line breaks.

## Problems with the brief or the script

- **A section entry carries all its subsections and articles,** so a section's text names its children's titles. I read those titles as the children's, which have entries of their own, except where a subsection has no article (rule 3 above).
- **The batch boundary splits a resource from its sections** (85 here, its sections in SA-42), and leaves Services Support's last three sections to SA-42 while this batch holds the resource and its first two.
- **Leads by 'support'** come from every resource's name ('Apps Support', 'Themes Support'), which each article entry carries in its `category`. They point to CM-SUP-005, a homonym, on 25 entries.

The checker's last line, for SA-41: `85 of 85 entries placed; 0 problems`.
