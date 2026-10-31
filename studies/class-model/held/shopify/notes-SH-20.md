# SH-20: notes (Shopify, the held pass)

**The batch:** 130 entries of four structures, read at observed-sh `e38dc17e3`:
- `admin-router-versions`, entries 1 to 9: the routes only the later router holds (`router-dd413330f40a`);
- `admin-settings-nav`, entries 10 to 50: the admin's settings navigation on demo-fake-dev-store (22) and fake-demo-sharrwah (19);
- `app-install-consent`, entries 51 to 79: the install dialogs of Collabs and Search & Discovery and Marketplace Connect's grant page;
- `app-store-built-in-features`, entries 80 to 130: the first 51 of 201, the pages Abandoned checkout recovery, Automated privacy settings, B2B, Customer accounts, Customer segmentation and Domains, and the six headings the pages share.

**Counts:** 122 entries on capabilities, 8 `out`, no `new`; 164 lines (136 `core`, 17 `shows`, 5 `own-service`, 1 `extension-point`, 6 `out`).

**Effort:** high, as the message names.

## `admin-router-versions` (entries 1 to 9)

- **Its twins.** Each of the nine routes is a route the later version adds, so no router batch placed it. SH-19 placed each one's change row in `admin-router-changes` (its lines 79 to 93). I placed each route by the digest's rules (`held/rules/admin-router.md`), and each takes its change row's line.
  - The terms are the title, then the id; an untitled route takes its id and its own path (the digest's rule 4).
  - Each reading names the change row it agrees with.
- **One correction to SH-19's reading.** SH-19's line 84 (`market:managed:biggest`, SH-E-c699983c) says 'no run opened it'. A run did:
  - run `20261007T215203Z-journey-admin-router-new-routes`, step 3, opened `markets/managed/biggest/` on fake-demo-sharrwah;
  - it landed on `markets`, as every `markets/managed*` route does on the held stores (`docs/GAPS.md`).

  I kept SH-19's `core` on CM-MKS-003. The landing reads as the store not being eligible (R14.1), not as the loader's own redirect, and the digest's rule 11 keeps a loader-only route whose names don't say redirect `core`. The other reading is that the visit shows the loader sending elsewhere (rule 11's exception), which would make it `shows` on `markets`' capability, CM-MKS-001. Neither changes a cell. A visit from a store eligible for Managed Markets would settle it.
- **The same run's other steps agree with SH-19's `shows` lines.** Steps 1, 4 and 5 (payments_summary, market-picker, market-picker-changes) all met “There's no page at this address”, as the betas false on both held stores predict.

## `admin-settings-nav` (entries 10 to 50): the rules I set

The coordinator's message for this batch asked me to take each twin's line from SH-97's `settings-panel` lines (S97.1 to S97.4). Every line here does, and names the twin's SH-97 line. I'd place none of them differently.

- **R20.1: a settings navigation item takes its twin's line.** The model places ibx5bt-xy's items of the same id (SH-S-1481 to SH-S-1503). Another store's item of that id is the same settings page, `core` on the same capability.
  - It has no scope. The item's `scope` (SHOP or ORGANIZATION) states the setting's level, not a condition on the store, so it goes in `reading` (a reading).
  - The store and the item's address (`<store>.myshopify.com/admin/settings/…`) are in `reading`.
  - The terms are the title, and the id where it differs from the title.
- **R20.2: Users is a container** (M-13; S97.4), `core` on CM-STF-001, the capability its title names. Roles and Security nest under it. They aren't kinds of users, so they take no CM-STF-001 line (M-6 refined); each is placed by its own entry (CM-STF-002, CM-TRU-001).
- **R20.3: every thing a title names takes a line** (rule 2; S97.2). 'Taxes and duties' takes CM-TAX-008 beside CM-TAX-001, on both stores. 'Shipping and delivery' and 'Metafields and metaobjects' are each one capability's own name, so they take that one line.
- **Homonyms the leads raised** (as SH-97 found):
  - CM-PTN-002's organization is the Partner Dashboard's;
  - CM-APP-003's Billing is its API group;
  - CM-APP-002's Shipping and delivery is an App Store category;
  - CM-PAY-014, CM-API-011, CM-SHP-018 and CM-SHP-019 matched only words.

## `app-install-consent` (entries 51 to 79): the rules I set

The sources are three steps of run `20261007T131249Z-journey-shopify-apps-2`:
- step 013: Search & Discovery's dialog, over `apps/search-and-discovery`;
- step 019: Collabs' dialog, over `apps/collabs`;
- step 038: Marketplace Connect's grant page at `app/grant`, which its App Store listing's Install opened.

The items agree with each step's `text.txt` and HTML.

- **R20.4: the dialog and the grant page 'Install app' are the admin's own install step,** `core` on CM-APP-001 (entries 51, 52 and 69). CM-APP-001's cell holds the admin's grant routes app/grant and oauth/request_grant as `core` (SH-S-5035, SH-S-5039), and step 038 is the route app/grant's own page. The dialog is a container (M-13) on the capability its title names.
  - The checker notes these lines: 'the dry run's S7 makes it shows'.
  - I read S7 (the brief's rule 4) as covering what the app asks for, not the platform's own install step. That covers the access categories and their texts, which I placed `shows` (R20.5).
  - If the coordinator reads the whole consent as `shows`, the two lines become `shows` on CM-APP-001. No cell changes either way.
- **R20.5: what the app asks for is `shows`** (the brief's rule 4; the dry run's S7; `selection.tsv`'s note):
  - the heading 'This app needs access to:' and the categories 'View staff and contributor data' and 'View and edit store data', with their texts, go on CM-API-003, the access scopes the merchant grants. Its cell holds that merchants approve the scopes when they install an app (SH-S-0755);
  - 'View customer data' and 'Sensitive data, device and activity data' go on CM-API-004, protected customer data, the narrower capability;
  - the data a category lists (customers, products, orders, store owner, staff members, blog contributors) takes no line (the ruling after SA-41). The terms of those list texts are left empty, so the words don't become CM-API-003's terms.
- **R20.6: the line 'Shopify' under each app's name is the app's developer, a maker statement** (entry 57; a reading). Two things support it:
  - the consent ends “Why do apps need data access? Check the developer's privacy policy.”, and that link opens https://www.shopify.com/legal/privacy;
  - the line is shown to merchants at install, as a store listing's developer is (the ruling after SH-2), so it is a maker field merchants are shown (the ruling after WC-4).

  In the HTML the line is a subdued text under the app's heading (`steps/038.html`), with no label of its own. The entry takes CM-APP-011 (apps made by the platform's company), `own-service`. Each app's region, icon and heading then take that app's own feature's capability, `own-service` (the ruling after SH-55):
  - Collabs: CM-MKT-015. Its maker is also stated by 'our creator platform' (SH-E-709b37e4) and by its publisher Shopify Inc. (SH-S-2760). CM-MKT-014's affiliate sales aren't named by the dialog, so no line there;
  - Search & Discovery: CM-SFR-013. Its maker is also stated by the changelog's 'we' post (SH-E-e612d2b5; SH-38, SH-39 and SH-41's own-service lines);
  - Marketplace Connect: CM-CHN-003. No other maker statement is held (see CHANGES).

  None of the three dialogs links the app's admin page, so none takes a CM-APP-007 line.
- **R20.7: the buttons 'Close', 'Cancel' and 'Install', and the text '.', are UI strings: `out`.** The install itself is the dialog's line.
- **R20.8: the link 'privacy policy' takes two lines** (entry 65):
  - CM-API-004 `shows`: the developer's privacy policy shown at install, as that cell's `shows` row holds;
  - CM-TRU-013 `core`: the page the link opens is Shopify's own Privacy Policy, whose legal page the cell holds as `core` (SH-I-1376). A second line follows the page (the ruling after SA-19).

  The checker notes the `core` line under S7, as it does R20.4's. CM-TRU-005, CM-TRU-006 and CM-CNT-008 are the store's own privacy settings and policies, other things.

## `app-store-built-in-features` (entries 80 to 130): the rules I set, for SH-21 and SH-22 to keep

Each page is one feature 'Included with Shopify' (B2B: 'Included with Shopify Plus'). Its layout:
- the title (h3), cited by the concern map where it is cited;
- the badge (span) and a tagline (h4);
- How it works: points (h5), each with a paragraph;
- What’s in the box: a section heading (h4) with a paragraph and a link to an App Store category, then a list heading (h5) over groups (h6) of items marked Supported or Not supported;
- Do more with Shopify tools: cards (h4), each with a paragraph and a link into the admin;
- Learn more: links.

Only h3, h4, h5 and span are entries (`selection.tsv`). The paragraphs, list items and links are read as each entry's words.

- **R20.9: the badge 'Included with Shopify' takes one line per page** (entry 80, SH-E-1b715d89, which stands for 28 pages). Each line is `core` on the capability the page's title names. This is how the model places B2B's 'Included with Shopify Plus' (SH-S-7211, CM-B2B-001 `core`).
  - 27 lines: the two Shopify Magic pages share CM-AIA-003, so they take one line.
  - Each reading names the page, its title and the cell evidence it agrees with.
  - Where the page is a separate product of the platform's whose own features are `own-service` (Shopify Capital), the inclusion stays `core`, as a plan line that includes it does (the ruling after SH-55; the digest's section 3).
  - A line takes a scope only where the page names a market: Shopify Tax's three pages take 'EU', 'United Kingdom' and 'United States', each in its own page's words.
  - SH-21 and SH-22 meet these pages' own entries. The pages' features, as I placed them:

    | Page | Capability |
    | --- | --- |
    | draft-orders | CM-ORD-005 |
    | gift-cards | CM-LOY-002 |
    | inventory | CM-INV-001 |
    | magic-* | CM-AIA-003 |
    | managed-markets | CM-MKS-003 |
    | markets | CM-MKS-001 |
    | metafields-and-metaobjects | CM-CNT-002 |
    | order-tracking | CM-SHP-017 |
    | payments | CM-PAY-001 |
    | product-variants | CM-CAT-002 |
    | shop-pay-installments | CM-PAY-015 |
    | shop-pay | CM-PAY-014 |
    | shopify-balance | CM-PAY-023 |
    | shopify-capital | CM-PAY-026 |
    | shopify-payments | CM-PAY-002 |
    | shopify-shipping | CM-SHP-002 |
    | shopify-tax-* | CM-TAX-002 |
    | shopify-theme-store | CM-SFR-003 |
    | sidekick | CM-AIA-002 |
    | store-credit | CM-LOY-001 |
- **R20.10: a tagline, point, section heading, list heading or card goes on the capability of the feature it is about, `core`,** read with its paragraph, and its card's link where it has one (rule 1).
  - Where its words or its paragraph name a narrower or another thing, that thing takes its own line (rule 2: what a description names), for example:
    - company profiles: CM-B2B-002;
    - catalogs: CM-B2B-003;
    - the B2B buyer's self-serve storefront: CM-B2B-007;
    - returns from the account: CM-RET-003;
    - store credit: CM-LOY-001;
    - the account pages' branding and customization in the checkout and accounts editor: CM-CHK-003;
    - apps extending the account: CM-CUS-014, `extension-point`;
    - automated emails: CM-MKT-006;
    - a discount's segment eligibility: CM-MKT-001 and CM-CUS-002;
    - the store's privacy policy configured by the feature: CM-CNT-008.
  - What a paragraph lists in passing takes no line (the ruling after SA-41). Examples are the catalogs, quantity rules and pricing of 'Customized buying experiences', and the attributes a segment uses.
  - A claim of effect names its topic `shows`: 'Enhanced SEO with a personalized domain' takes CM-CNT-007 `shows`.
  - A point that names Shop's sign-in takes `own-service` for it (the ruling after SH-34): 'Easy logins for your customers' is `core;own-service` on CM-CUS-010.
  - A point that names its own plan takes it as that line's scope (the ruling after SH-69): 'Support B2B buyers', 'Shopify Plus plan'. It takes the lines the model gives its paragraph (SH-S-7213): CM-B2B-007 `core`, CM-B2B-002 `shows`.
  - A shared point stands for several pages, and takes one line per page. 'Easy setup and management in your Shopify admin' stands for three: CM-MKT-022, CM-SHP-017 and CM-TAX-002 (United States).
- **R20.11: the headings every page's template repeats are the page's own frame: `out`.** They are 'How it works', “What’s in the box”, 'Do more with Shopify tools' and 'Learn more', which name no feature (the coordinator's message: a page's frame is `out`). Each point, section and card under them is placed by its own entry.
- **R20.12: the B2B page's lines take 'Shopify Plus' as scope,** the plan its badge 'Included with Shopify Plus' states for the page's whole feature (SH-S-7211; rule 5). The page's paragraph says the same: 'Your Shopify Plus plan gives you everything you need to run your wholesale business' (SH-S-7212).
- **Homonyms the leads raised:**
  - CM-NTF-001 for the recovery emails, which the page's Get started opens in marketing automations;
  - CM-ANL-001 for the recovery's own analytics;
  - CM-CHK-002 and CM-CHK-007 for 'Abandoned cart features';
  - CM-MKS-008 for the privacy features' own translation;
  - CM-ACC-004, the store's own business entity, for B2B's companies;
  - CM-ORD-001, the merchant's order management, for the buyer's self-serve;
  - CM-MKT-011, ad platforms' audiences, for segments' 'targeted audiences';
  - CM-OPS-004 (see NOTE).

## CHANGES, with what I decided

- **CM-CHN-003@shopify gains own-service, by line 69** (Marketplace Connect's region, icon and heading on its grant page). It rests on R20.6 alone. The grant page names the app's developer 'Shopify', and its developer's privacy policy is Shopify's.
  - Without this line Marketplace Connect has no maker statement held. `held_entries.py makers` finds only the changelog post SH-E-619edc55, whose 'our' names the Help Center. So its earlier lines are `shows` (the ruling after SH-43; SH-53's and SH-58's lines).
  - I kept `own-service`. The grant page is a statement merchants are shown, naming the developer as a store listing does (the ruling after SH-2).
  - If the coordinator holds that a developer line with no label of its own isn't a maker statement, the line becomes `shows`, and R20.6's other lines keep their own support: Collabs and Search & Discovery have other maker statements held.
  - This decides whether Marketplace Connect's lines in other batches are aligned to `own-service`.
- **CM-SFR-013@shopify gains own-service, by line 72** (Search & Discovery). It has maker statements held besides the dialog: the changelog's 'we' post SH-E-e612d2b5, which SH-38, SH-39 and SH-41 already placed `own-service` on this cell. The cell's reading predates them ('no statement names that app's maker'). I kept it.
- **CM-CUS-010@shopify gains own-service, by line 136** ('Easy logins for your customers': the buyer's Shop account). The digest's section 3 places Sign in with Shop `own-service` on CM-CUS-010, and SH-12's line 2 gave the route `core;own-service`. The cell isn't yet amended from them. I kept it.

## The checker's NOTE lines, answered

- **'core on a partner's or an app's permission (app-install-consent)', three times:** R20.4's two lines (the install dialog, and the grant page at app/grant) and R20.8's CM-TRU-013 line (Shopify's Privacy Policy). None is a permission the app asks for. Each is the platform's own step or page, as their cells hold them `core`.
- **own-service on CM-MKT-015, CM-APP-011, CM-CHN-003, CM-SFR-013 and CM-CUS-010:** R20.6 and the CHANGES above.
- **line 12 (Users), a container:** R20.2.
- **line 114 ('Do more with Shopify tools'), first lead CM-OPS-004 (tools) holds nothing:** that capability is a store's system status report and tools, which the heading doesn't name. The heading is the page's frame (R20.11), and its cards are placed by their own entries.

## New things

None.

## Entries I couldn't tell, and what would settle each

1. **`market:managed:biggest`** (SH-E-e4fb6db4): its loader's landing on `markets`. See above. A visit from a store eligible for Managed Markets would settle it.
2. **The install dialog's support** (R20.4): `core` as the admin's own install step, or `shows` as part of the app's consent. No cell changes. The coordinator's reading of S7's reach settles it.
3. **Marketplace Connect's maker** (R20.6; CHANGES).
4. **The badge's 27 lines** (R20.9) decide the capability of 22 pages that SH-21 and SH-22 place by their own entries. If either places a page's feature elsewhere, the badge's line for that page moves with it.

## Items and sources that disagree

- **Three settings items have no entry and no statement of their own.** They are fake-demo-sharrwah's `billing` ('Billing', SHOP), its `user_permissions` ('Users', SHOP), and ibx5bt-xy's `markets` ('Markets', settings/markets). The concern map's settings statements (SH-S-1481 to SH-S-1503) hold none of them, and SH-S-1494 doesn't exist. A reading: the build counts them cited because their keys match statements of other sources (`markets` is an identifier of five help pages' statements, SH-S-6310 among them).
  - Their twins' lines would be CM-PLN-004, CM-STF-001 and CM-MKS-001.
  - No cell loses a thing: each holds these pages already.
- **The consent's categories each have a 'Show more details' button** (`accessibilitylabel`, `steps/038.html`). The details weren't expanded, so neither the ARIA tree, `text.txt` nor the HTML holds them.

## What a source states that no entry holds (leads for the second stage)

- **The built-in features pages' lists of features, marked Supported or Not supported** (`li`, not selected). Each 'Not supported' is the platform stating what the built-in feature doesn't do, a statement of absence for the feature's cell:
  - Abandoned checkout recovery (`…_abandoned-checkout-recovery/items.jsonl`, lines 21 to 45). Cart recovery: 5 supported, 9 not: Exit pop-ups, Retargeting ads, SMS notifications, Web push notifications, Multi-channel messaging, Cross-device carts, Opt-in pop-ups, Time-limited offers, Games and contests. Display options: 10 supported;
  - Automated privacy settings (lines 19 to 54). Display options: 12 supported, A/B testing not. Privacy compliance: 3 supported; Accessibility compliance, Auto-blocking, Consent expiration and Cookie scanner not. Regulation: 14 supported;
  - B2B (lines 21 to 50). Pricing options: 14 supported, Pre-orders not. Order management: 13 supported, Order form not;
  - Customer accounts (lines 21 to 42). Customer login: 6 supported. Account management: 5 supported; Tagging and Activation link not. Access control: 6 supported, Secret link not.
- **The paragraphs under the What’s in the box sections, and their links to App Store categories.** Each names apps that offer more:
  - abandoned cart apps (`categories/marketing-and-conversion-marketing-abandoned-cart`);
  - cookie consent apps (`categories/store-design-internationalization-cookie-consent`);
  - wholesale apps (`categories/finding-products-sourcing-options-wholesale`);
  - account and login apps (`categories/store-management-security-accounts-and-login`).

  These are `extension-point` leads for CM-MKT-022, CM-TRU-006, CM-B2B-001 and CM-CUS-010.
- **The page behind the install dialogs** (steps 013 and 019): 'You don't have this app installed', with each app's card, its rating and tagline:
  - Collabs: '4.2 Attract new customers when influencers recommend your products';
  - Search & Discovery: '2.6 Customize search, filtering, and product recommendations'.

  The register's other apps installed with no consent step (Translate & Adapt, Bundles, Inbox, Subscriptions, Planet) hold no dialog.

## Problems with the brief or the scripts

- **`held_entries.py earlier` finds no twin across structures,** as the coordinator's message said. SH-97's `settings-panel` twins and the concern map's `admin-settings-nav` statements were found by `class_slice.py key` and `merged/evidence.tsv`.
- **The checker's S7 note fires on every `core` line of `app-install-consent`,** the platform's own install step and pages included (R20.4, R20.8).

## The coordinator's check

Measured: 23.7 million tokens over 102 requests, about 182,000 an entry. The checker prints no problem.
- **Kept:** R20.1 to R20.12, every `CHANGES` line, the settings navigation's lines (each its SH-97 twin's), and the app consent's `core` lines on CM-APP-001 and CM-TRU-013 that the checker's S7 note names.
- **R20.6, accepted:** the install page's 'Shopify' under the app's name, with its developer's privacy policy Shopify's, names the app's developer, as a store listing does (the rulings after SH-2 and WC-4). So Marketplace Connect's maker is held, and its own features are `own-service` (the ruling after SH-43). Seven lines that had it `core` or `shows` for want of a maker are aligned: SH-41:33, SH-53:19, SH-53:98, SH-55:69, SH-55:72, SH-58:75 and SH-58:78. SH-55:74 stays `shows`, a case study's claim.
- **SH-19's line 84:** its reading said no run opened `market:managed:biggest`. The run this batch names opened it and landed on markets; the reading is corrected and the line stands.
- **The build's settings items:** three items with neither an entry nor a model statement (fake-demo-sharrwah's `billing` and `user_permissions`, ibx5bt-xy's `markets`) go to `amendment-notes.md` for the omission review; each cell already holds those pages.
