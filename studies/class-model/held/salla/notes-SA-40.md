# Held pass, Salla, batch SA-40: notes

81 entries (effort high), all of `portal-help-center-article` (`partner@en`), evidence at observed-sa@b0bd0b16: the articles of eight categories, by their line in `structures/salla/portal-help-center-article/partner@en/items.jsonl`:
- 1 to 4: Access Token (line 3);
- 5, 6: Webhooks (line 4);
- 7 to 9: Apps Testing (line 5), a category with no entry of its own;
- 10: Shipping Apps (line 6);
- 11 to 37: Twilight Themes Engine (line 7), a category with no entry of its own;
- 38 to 62: Services Support (line 8), a category with no entry of its own;
- 63 to 78: Influencers (line 9), a category with no entry of its own;
- 79 to 81: Influencers Basic Information (line 10), a category with no entry of its own.

Entry numbers below are the batch's order (`held_entries.py show --platform salla --batch SA-40`).

**Placed:** all 81 entries on capabilities, in 128 lines. No `new`, no `out`. 34 entries take more than one line: the 19 influencers' articles take CM-MKT-015 and CM-PTN-009 each, and entry 5 takes ten. Supports, by line (a line of two values counted in each): 45 `core`, 43 `extension-point`, 42 `shows`. There is no `own-service` and no `outside`.
- **Fillers** are on 8 lines. Entry 71 names the social media platforms (Facebook, Instagram, Snapchat, X, Youtube, TikTok, Linkedin). Entries 79 to 81 name the General Authority of Media Regulation. Each of the four entries puts its filler on both influencer cells.
- **Qualities** are on 8 lines, from six entries:
  - 3: the access token is valid for 14 days;
  - 15: a developer can create any number of themes, with no limit;
  - 17: a theme's minimal price is 150 SAR;
  - 44: a service's review takes 3 to 4 working days;
  - 63: an influencer has 3k+ followers;
  - 66: an influencer profile takes no more than 5 minutes to set up.

  63 and 66 put their quality on both influencer cells.

**Sources read:** the brief (it changed during the batch: the reading of `dashboard-translations` feature content and `marketplace-apps`, and the portal rows of `permission-gates`, neither of which bears on this structure) and what it names. That is:
- SA-39's notes, with the coordinator's check, and its placements;
- the rulings, the evidence map, and B-extent's "Cells and evidence" and conventions;
- observed-sa's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, and the register's row for the structure;
- the selection row and `show --meta`;
- the cells of every lead and of every capability the entries' words name.

To align with SA-34 to SA-39, I also read their placements for the partners' portal's pages for themes, services, influencers, demo and development stores, webhook logs and store management. I read the concern map's citations of the same FAQ (`studies/concern-map/platforms/salla/citations.tsv`, SA-S-5107, 5108, 5110, 5111, 5113, 5131, 5137) and the merged evidence rows that cite them, to see which cells already hold an article. I compared `items.jsonl` with `source.json` for the eight categories: titles and contents are identical, and each article's `section`, `url` and `icon` are null.

## Rules my lines follow

SA-39's six article rules hold throughout. An article's question and answer are read together. An answer is `core` where it names the platform's own place, rule or feature, and `extension-point` where developers or partners work through what the platform provides. It is `shows` where it gives only a term, a guide or a topic. Every thing an answer names takes a line, and the homonyms are kept apart. On top of those:

1. **Access tokens and Twilight are the platform's own tools for developers:** `core`. The access token belongs to Salla's own authorization (CM-API-002). Twilight is the theme engine (CM-SFR-002, the cell's Twilight Engine). Twilight's endpoints and `salla.product.fetch` are the storefront API (CM-SFR-012, the cell's Twilight JS SDK). The Salla CLI and its `preview` commands are CM-DVT-002's. This follows the brief's rule 4: the platform's own API for its own feature is `core`, and so is a guide addressed to developers. A guide to writing a theme's code is `shows`: skills (13), tools (14), GitHub (28), converting HTML (29), forms (32), product cards (33), product pages (34).
2. **Developers' themes go on CM-SFR-003, as apps go on CM-APP-002.**
   - Building, publishing, selling, republishing and installing themes on one store is `extension-point`: entries 12, 15, 16, 18, 24, 25, 26, 30, 35, as SA-35 placed the partner's My Themes.
   - Salla's own review before a theme is published is `core`, so entry 23 is `core;extension-point`.
   - A theme's price (17) and its tags (31) are terms: `shows`. The minimum price is a quality, and the cell already cites the Arabic answer.
3. **Services go on CM-PTN-005:**
   - the partner's own pages and tools in the portal are `extension-point`, as SA-34 to SA-38 placed My Services: the service details page, preview, gallery, additional services, plans, access, Orders Center and Service Provider Portfolio. The services marketplace's categories are `extension-point` too, by the ruling after SA-25 (47, 'Others');
   - Salla's own review (44, with its duration) and its rules on cancelling a service order (57, 58) are `core`;
   - who sets the price, the delivery time, service terms and requirements, keywords, FAQs and conditions are `shows`.
4. **Influencers' articles take both CM-MKT-015 and CM-PTN-009,** as SA-34 and SA-38 placed the influencer pages and SA-39 the influencer categories:
   - the influencer's profile, campaign orders and conversations in the portal are `extension-point` (after SA-44's check);
   - the rule that a merchant can't cancel a started campaign is `core` (78), as 57 is for service orders;
   - statuses, durations, guides, the sectors and the Mawthooq licence are `shows`. The CM-MKT-015 cell already cites the Arabic statuses (SA-S-5137) as `shows`. The CM-PTN-009 cell already cites the Arabic Mawthooq answer (SA-S-5113) as `shows`, with the authority as its filler.
5. **A thing the answer names beside its own thing takes its own line:**
   - the partner account and its verification or eligibility (CM-PTN-002: 12, 24, 40, 44; `shows` for the account as a condition, 14);
   - Salla's support for partners (CM-PTN-001: 58, 70);
   - a partner's request for store access (CM-STF-005 `shows`, 54, by the ruling on what a partner asks of a merchant; the cell cites the Arabic answer so);
   - the store's languages (CM-MKS-008 `shows`, 20, 27);
   - demo stores (CM-DVT-004: 7, 8, 18, 19, 35);
   - App Events and app pricing plans (CM-APP-004, CM-APP-003: 8).
6. **Webhook categories (5).** The answer names ten categories. Each one that names a feature takes a `core` line on its capability, as the platform's own webhook topics for its own feature (the brief's rule 4), and each such cell already holds Salla's topics as `core`:
   - Order: CM-ORD-001;
   - Products: CM-CAT-001;
   - Shipping Companies: CM-SHP-015;
   - Customer: CM-CUS-001;
   - Category: CM-CAT-003;
   - Brand: CM-CAT-005;
   - Store: CM-ACC-006;
   - Cart: CM-CHK-002;
   - Special Offer: CM-MKT-003.

   Miscellaneous names only a grouping and takes no line.

## New things

None. Before deciding, I searched with `caps --terms`: Twilight; storefront API; theme preview; theme tags; web components; product card; GitHub; refresh token; access token; Postman; OAuth; theme price; theme review; private theme; theme install; component; Salla Services; service store; service terms; service requirements; keywords; service gallery; service orders; services store; متجر الخدمات; service provider; مزود الخدمة; conversation; محادثات; chat; campaign order; طلبات الحملات; social media; منصات التواصل; Mawthooq; موثوق; licence; رخصة; followers; hooks; JavaScript events; language files; ملفات اللغة; preview; معاينة; theme details; partner rating; تقييم الشريك; delivery date; Twig; HTML template; the webhook topics. Every thing an entry names falls inside a held cell's thing.

## Entries I couldn't tell, and what would settle each

- **9, CM-DVT-005 or CM-DVT-004.** The answer names 'the Development store feature in the [Partners Portal]'. The question asks how merchants preview a store 'before purchasing the store?' ('قبل بيعها للتاجر', before selling it to the merchant). SA-35 and SA-37 placed the portal's Development Stores routes (`/store`, `/stores`, permission manage-development-stores) on CM-DVT-005, which is the stores a partner prepares for merchants. The demo stores (CM-DVT-004) are for testing. The linked article (t.ly) isn't held; it would settle it.
- **5, Store and Cart.**
  - The entry doesn't say which topics the category Store holds. CM-ACC-006 is where it most plainly belongs. The model holds `store.branch.created` in CM-INV-005, which the entry's words don't name.
  - The model holds Salla's `abandoned.cart` topics in CM-CHK-007. I followed the entry's word, Cart (CM-CHK-002).

  Both cells are `core` already. The docs' webhook events (bit.ly, not held) would settle both.
- **57, 58, 78: `core` or `shows`.** These are the platform's rules on cancelling service orders and campaign orders. I read them as the platform's own order mechanism, as SA-39 read the App Store's rating rule (`core`). They could also read as terms (`shows`), as SA-39 read a condition of publishing. No cell changes either way.
- **73, `shows` or `core`.** 'Gettings approval for your Influencer Profile is easy' implies Salla approves profiles, but the answer gives only a link (not held). I kept it a guide.
- **71, fillers.** The social media platforms are where influencers market merchants. I gave them as fillers, as a venue is (M-3). The brief's 'doing it' could leave them in `reading` only.
- **28, 36, 37: GitHub.** The developer's theme code is held in GitHub ('push changes to your Github repo'). The entries name GitHub as a requirement and as the developer's repository, not as doing the theme's work, so it is in `reading`, not a filler. SA-36 placed the portal's `authorize/github` route on CM-PTN-002.
- **53, plans.** The partner limits a service to merchants' plans. The plans are only the service's audience, so I gave CM-PLN-001 no line.
- **30, a theme for one store.** No capability holds a store's own private theme. I kept it on CM-SFR-003, `extension-point`, where a partner installs a theme through the portal. If the coordinator wants a private theme as a thing of its own, entries 23 ('share it with a private store') and 30 are its evidence.

## Items against sources

None: `items.jsonl` and `source.json` agree for the eight categories. The concern map's citations name the categories' lines with an article id (SA-S-5110, 'line 5 (article 1131548349)'), which is the category Apps Testing's own id, not an article's. This is the same as SA-39 found for SA-S-5108.

## For the second stage

The FAQ's links aren't held (`held_index.py`: not held). Among them:
- salla.dev's posts on offering services, influencers, OAuth with Postman, publication standards, testing with demo stores, and the apps' events activity log;
- the docs' Twilight fetch page;
- the bit.ly, t.ly and rb.gy links.

They would show:
- the webhook categories' topics (5);
- the Development store feature (9);
- the influencer profile's approval (73);
- the theme publication standards (8).

I read no run step beyond the entries.

## The checker's lines, read again

- **No `CHANGES`.** Every line falls on a cell that already holds its support.
- **`NOTE` core on a product named with the platform's brand** (lines 17, 24, 26, 28, 34, 36, 37, 42, 44, 46, 64, 69, 70, 84, 85, 86). The names are 'Salla Partner', 'Salla CLI', 'Salla Team', 'Salla Themes', 'Salla Services', 'Salla support' and Salla's Twilight. Each names Salla's own portal, CLI, review, theme engine, services marketplace or support, which the cells already hold as the platform's own (`core`). No line rests on a maker.
- **`NOTE` first lead CM-CNT-001 holds nothing** (lines 51, 77, 78: entries 29, 51, 52). The lead comes by the word files: a theme's HTML files, and a service's design files and requirements. These are not a store's files, and each of the three readings says so.
- No quote prints 'found nowhere held'. One stray apostrophe ('influencers'') had paired with a quote and been printed as one; I reworded it.
- No `NEW` line.

## Problems with the brief or the script

- **The checker pairs apostrophes as quotes across a reading.** A plural possessive after a real quote ('for influencers'') was read as a quote's end.
- **A quote spanning the source's line breaks isn't matched.** Many answers hold `\n` and double spaces, which `show` prints collapsed, so I quoted only within a line.
- **Many lines per entry.** Each influencer article takes two lines (CM-MKT-015, CM-PTN-009), as SA-39's rule 3 did for the categories. A coordinator's rule to place an influencer article on one of the two would halve them.

The checker's last line, for SA-40: `81 of 81 entries placed; 0 problems`.

## The coordinator's check (31 October 2026, after the batch)

- **The article rules stand,** as SA-39 set them:
  - Salla's own tools for developers are `core`;
  - building and selling themes, services and influencer campaigns through the portal is `extension-point`;
  - Salla's own reviews and rules are `core`;
  - terms and guides are `shows`.
- **The qualities stand,** each a figure the answer states:
  - the access token's 14 days;
  - a theme's minimum price of 150 SAR;
  - a service review's 3 to 4 working days;
  - an influencer's 3k+ followers.
- **The webhook categories' lines (entry 5) stand,** each on its own capability. The Store and Cart events are read by the entry's own words. Both cells are `core`.
- **For SA-41:** a quote stays within one line of its source, since the test doesn't match across a line break. A plural possessive after a quote is reworded.
- **Cost:** 10.1 million tokens over 55 requests, about 125,000 an entry. No cell changes.
