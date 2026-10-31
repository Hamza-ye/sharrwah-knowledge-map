# Notes: held pass, Salla, batch SA-28 (`onboarding-missions`, rest; `onboarding-status`; `partners-portal-header`; `partners-portal-navigation`, first part)

## What I read

- The brief, `H-held.md`; the evidence map; the coordinator's rulings, `held/review-H-rulings.md`, to its last section; B-extent.md's "Cells and evidence" and "Conventions from the dry run".
- observed-sa (at `b0bd0b16`): `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`; the `structures/REGISTER.tsv` rows of my four structures; `index/ledger-summary.tsv` and `index/ledger/portal-app.tsv`.
- The four structures' `meta.json` (`show --meta`) and their `selection.tsv` rows: all four are `where`; `onboarding-missions` by the rule `nested:completed,pending,uncompleted,available,missions,tasks;drop:statistics,steps`, `onboarding-status` by `nested:steps,items,data`.
- SA-27's notes and placements (its rules O1 to O5 and the coordinator's check); SA-34's, SA-35's and SA-36's notes (their rules 1 to 12, rule 5 on the portal's admin, the rules on layout-mf, and their coordinator's checks) and their lines for the routes the header and the menu open.
- **Sources:**
  - `onboarding-missions @public-demo@en`: `source.json` (`raw/runs/20261009T021126Z-journey-public-demo-entry-en/responses/0044.json`, step 3), the missions at `/missions/completed/9` to `/12` and their tasks, with each task's `config` (labels, `meta.template`, `helpCenterArticle`, empty for all 20) and the missions' `statistics`.
  - `onboarding-status @merchant@ar`: `source.json` whole (`raw/runs/20261008T122729Z-sweep-merchant-menus-ar/responses/0013.json`, step 1), and the page of the same step, `raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/001.text.txt`, lines 1 to 25, where the home page shows the checklist; the demo store's English answer of the same endpoint, `raw/runs/20261008T133523Z-sweep-demo-store-en/responses/5131.json`, for the untranslated titles.
  - `partners-portal-header`: both labels' `items.jsonl` and `source.html` (the `nav` of `raw/runs/20261008T114611Z-partners-portal-dashboard/steps/001.html` and `raw/runs/20261008T123118Z-sweep-partner-portal-ar/steps/003.html`), read for each link's icon and nesting.
  - `partners-portal-navigation @partner@ar` and `@partner@en`: `items.jsonl`, lines 1 to 14; `portal-apps/prod/items.jsonl`, line 3 (layout-mf at `/` and `/conversations.*`).

## The structures' split with other batches

- **`onboarding-missions`:** SA-27 holds its first 37 entries, and I hold the last 24 (missions 151, 152, 153 and 168 with their 20 tasks). I kept SA-27's O1 to O5 throughout. Two applications of O4 to words SA-27 didn't meet:
  - **`core` where the description states the feature doing it itself:** 'تذكير تلقائي يوصلهم…' (abandoned cart reminders, CM-MKT-022); 'كيف تطلق إعلانك بنفسك عبر إعلانات سلة' (Salla Ads, CM-MKT-010); 'تطبيق سلة يوصلك إشعار فوري بكل طلب جديد' (CM-SRF-001, CM-NTF-002); 'تطبيق محلي يجمع منتجات تجار سلة في مكان واحد' (Mahally, CM-CHN-002). Every such cell already holds `core`, so none of these lines changes a cell. A task that only describes what a feature lets the buyer do once turned on (guest checkout, the quick-buy button, the top bar) I kept `shows`, as SA-27 did for free shipping and e-payments.
  - **SA-27's CM-SRF-001 line for its own Salla app task (SA-E-c97a8313) is `shows`, and mine (SA-E-97efd95e) is `core`.** Mine states what the app does; SA-27's description didn't. The coordinator may align them.
- **`onboarding-status`:** no batch had placed it. I placed it whole (13 entries).
- **`partners-portal-header`:** no batch had placed it. I placed it whole (41 entries, both languages).
- **`partners-portal-navigation`:** no batch had placed it. I hold its first 4 Arabic entries: the logo, لوحة التحكم, تطبيقاتي and the group الثيمات. **SA-29 holds the rest and hasn't run.** The coordinator aligns the two. The rules my lines follow are below, for SA-29.

## Rules my lines follow

### Missions and tasks: SA-27's O1 to O5

No scope on a mission, the task's `plan` as its scope, and each thing a title or description names on its own capability. The `meta.template` of a task (a coupon, a bar, a reminder that Salla's dashboard creates for the merchant) is cited in `reading` with its values. They are the template's defaults, not qualities.

### The setup checklist (`onboarding-status`)

- **C1.** Each step is CM-ONB-004 `core`: a step of Salla's own setup checklist, the store's setup in the admin, the cell's thing as SA-27's missions are.
  - Its `status`, `status_label` and the answer's `subscription` (`is_launched: false`) are the store's state, in `reading`.
  - `parent_step` (general, settings) is a group named only by its slug, with no entry of its own. It goes in `reading`.
  - No scope: the answer states no plan or condition. The store is the merchant store, its home page badged بيسك (`001.text.txt`, line 9).
- **C2.** Six steps' titles are translation keys the answer leaves untranslated (`onboarding::steps.kyc.title`), in Arabic and in the demo store's English answer. Their terms are their slugs. Their readings quote the home page's own title for the step, from the same run and step (`001.text.txt`, lines 14 to 25), a source the brief allows for clarifying an entry.
- **C3.** Each thing a step names takes a line, `shows`: the step only has the merchant do it.
- **C4.** A step that names only the checklist's start or end (initial, close), or the cell's own thing (persona-questions, the onboarding profile; create-store), takes C1 alone.

### The portal's top bar (`partners-portal-header`), and for SA-29's menu

- **H1. A link to a portal route** takes the capability and support that SA-34 to SA-36 gave the same route, citing that line:
  - /account, /settings/profile, /settings/change-password on CM-PTN-002 `core`;
  - /help/faq and /dashboard on CM-PTN-001 `core`;
  - /apps on CM-APP-002 `extension-point`.

  The route's gate isn't stated by the menu. It goes in `reading`, never `scope`. None of my links has one.
- **H2. A menu's toggle is a container (M-13).** It goes on the capability its heading or its children name:
  - the notifications bell ('2') on CM-PTN-001, the Message Center;
  - the avatar ('Salem avatar') on CM-PTN-002, the account menu;
  - the side menu's group الثيمات (href #) on CM-SFR-003 `extension-point`, the support SA-35 gave its child My Themes.
- **H3. The language menu** (href `#dropdown-grouped`) is a container whose title, the chosen language, names no capability and whose href opens no page. It is `new` and `core` (M-13). Its two items, English and العربية, are a list of languages: `out` as market data.
- **H4. The Message Center's parts** (its heading, its tabs Notifications, Messages, Updates, the button View All Notifications) go on CM-PTN-001 `core`, with SA-35's route /message-center.
  - `out`: the counts ('2 New'), the tab 'All (2)' and 'Read All', which name no kind or place.
- **H5. A notice in the Message Center** goes on the capability of what it states. Each notice also takes CM-PTN-001 `core`, the portal's own notice.
  - The offer of help to publish an app: CM-PTN-001 `core`, Salla's own support, and CM-APP-002 `extension-point`, the partner's app on Salla's App Store, as SA-35's My Apps.
  - The account's creation: CM-PTN-002 `core`.

  These notices are what the held account received. I placed what they state of the platform; see "Entries I couldn't tell".
- **H6.** An empty link with only an icon is `out`, a layout node that names nothing: the side menu's toggle (feather-menu), the display toggle (feather-moon), the empty tabs' icon (sicon-bell-off).
- **H7.** The logo link to `/` goes on CM-PTN-001 `core`: the registry serves `/` by layout-mf, the portal's own home.
- **H8. Logout** goes on CM-PTN-002 `core`. It ends the partner account's session, whose /login route SA-35 placed there, as the merchant's sign-out routes are CM-ACC-001's (SA-E-7797ef68, SA-E-df24bba0).

**For SA-29**, the rest of the side menu: keep H1, H2, H6 and H7.
- **Groups with href '#'** (My Services, Affiliates, Influencer, Marketing Tools, My Subscriptions, Stores, Payments, Help Center) are containers, on the capability their title names, with the support SA-34 and SA-35 gave their children's routes.
- **'Others'** names only a grouping, over Webhooks Log, Chats, Message Center and the Help Center. M-13 makes such a section `new` and `core` where no capability is named, and the ruling after SA-22 makes a container over several sections of the admin with no title of its own `out`. 'Others' has a title, so I read M-13 as governing. The coordinator decides.
- **A 'NEW' badge** in an item's text is `core`, the badge in `reading` (D1).
- **The empty link at position 1** of both labels is the same kind as H6's.

## Each new thing

- **`new:العربية / English`**, the Partners portal's language menu: SA-E-6d6dc9bf (39, Arabic) and SA-E-aa1a3006 (61, English), `core`.
  - **What it is:** a menu in the portal's top bar, href `#dropdown-grouped`, titled by the language chosen ('arالعربية' / 'enEnglish', a flag image and the name), over two items, English and العربية. It is the language a partner reads the portal in. That is a reading; the menu's own words are only the language names.
  - **Place of its own:** a container of the portal's top bar, not an admin section with its own title or path. M-13 makes such a container `new` and `core`. If the coordinator reads the language choice as a toggle of the page, it has no place of its own, and both lines go `out` with their items.
  - **Proposed domain, area and parent:** domain F, under CM-PTN-001, the partners' portal. Or, if the class holds an admin's interface language for merchants too, domain A, beside CM-ACC-006. No capability holds one: CM-MKS-008 is the store's languages for buyers.
  - **Names:** Arabic العربية, English English; the menu has no name of its own.
  - **Searched:** language; اللغة; لغة; languages; multilingual; translation; admin language; interface language; لغة الواجهة; preferred language; locale. Only CM-MKS-008 (store languages), CM-MKS-006 (currencies), CM-NTF-001 and CM-PLN-004 matched.

## Entries I couldn't tell, and what would settle each

- **The Message Center's notices** (50, 51, 70, 71) are what the held account received, and "one account's own data" is `out` by the brief. I placed them because their words state what the platform does for partners:
  - it notices an app created and not published, and offers help, 'لقد لاحظنا أنك حاولت إنشاء تطبيقك خلال الأيام القليلة الماضية ، لكنك لم تنشره بعد';
  - it welcomes the new account to 'منصة شركاء سلة'.

  If the coordinator holds a received notice to be the account's own data, the six lines go `out`. No cell changes either way: CM-PTN-001, CM-PTN-002 and CM-APP-002 already hold these supports.
- **35, the step launch (تدشين المتجر), on CM-ACC-009 `shows`**, the CHANGES below.
  - The cell's thing is the store's coming-soon mode and its launch, WooCommerce's Launch your store. The step and the home page's heading 'واصل خطواتك الأولى لتدشين متجرك' name Salla's store launch, and the answer holds `is_launched: false`.
  - Nothing held in my sources says what launching does to the storefront. observed-sa's `docs/GAPS.md` says the merchant store's storefront answered 'ترقَّب إطلاق المتجر' (run `20261009T084616Z-journey-storefront-order-public-demo-en`), which would show a coming-soon page. I didn't read that run's step: a lead for the second stage.
  - CM-ACC-007 (maintenance mode) is kept apart by the cell's note.
- **31, موقع استلام الشحنات, on CM-SHP-001 `shows`:** a reading of the step as the location carriers collect the store's shipments from, part of the store's shipping setup. CM-INV-005 (branches and warehouses) is the other lead. The step's own page, not opened by the run, would settle it.
- **28 and 29, store identity and customer service channels, on CM-ACC-006 `shows`:** the cell cites SA-C-231/boundary/SA-S-5147, the store data a merchant updates, which lists 'هوية المتجر' and 'قنوات خدمة العملاء' among them. That the step store-identity is the same identity is a reading: its title is an untranslated key, and the home page's title is 'هوية المتجر'.
- **11 and 13, the merchant's daily posting on TikTok and Instagram and in Telegram and X communities,** take O2 alone. They are the merchant's own actions on other platforms, and no capability of the model is organic social posting. **19, a pinned ad tweet in an influencer's account on X,** I placed on CM-MKT-015 `shows`, since it names an influencer, with no interface of Salla.
- **22, from receiving the order to shipping, on CM-SHP-009 `shows`:** the task names an order's fulfilment and attaches a guide. If the coordinator reads it as advice only (O5), the line goes.
- **24, asking the customer's opinion after receipt,** takes O2 alone, as SA-27's like task (SA-E-c7d44f5a). Its label 'اطلب رأي عميلك' is a lead for review requests, CM-SUP-002.
- **4, the quick-buy task:** its plan is basic, while CM-CHK-008's cell holds the button as a Salla Plus plan line, with its flags on plus, pro and special. This supports SA-27's O3: a task's `plan` isn't stated to be the feature's gate. The feature list (`dashboard-features`, quick-purchase) for the public demo would settle what the plan is.
- **42, the moon icon,** I read as a light or dark display toggle, from its icon class only. It names nothing, so it is `out`.

## Structures whose items and sources disagree

- **`partners-portal-header`:**
  - The items nest 'View All Notifications' under 'Read All' (`parent: 18`), and '2 New' under 'Message Center'. In `source.html`, 'Read All' and the button are siblings in the menu's footer `li`. So the checker's NOTE that 'Read All' / 'قراءة الكل' is a container (lines 82 and 102) follows the items, not the source. The source governs: 'Read All' is a UI string, `out`.
  - `parent` names an item by its text, so 'arالعربية', the Arabic language item (41), shares its text with the menu that holds it (39). The checker's container NOTEs on lines 68 and 91 come from that. The containers themselves are lines 67 and 90.
  - The English items repeat the two notices (positions 14 and 15 repeat 12 and 13): the tabs All and Notifications each list them. Each notice is one entry.
- **`onboarding-missions`:** the mission 'سوّق لمتجرك مجاناً ' ends in a space in the source, and its `name` holds two spaces, which `show` collapses. My quotes are copied from the source.
- **`onboarding-status`:** six titles and descriptions are untranslated keys (`onboarding::steps.*`), in both the Arabic and the English answer. The home page shows Arabic titles for them (`001.text.txt`, lines 14 to 25).

## What the sources state that no entry holds (for the second stage)

- **The home page's checklist** (`raw/runs/20261008T122729Z-sweep-merchant-menus-ar/steps/001.text.txt`):
  - its progress '7/8' (line 13);
  - its eight shown steps, of the answer's thirteen;
  - the button 'فعِّله الآن' on Salla Point (line 22);
  - 'توثيق' (line 24).
- **The onboarding answer's `subscription`** (`status`, `end_date`, `is_launched`, `renew`, `days_left`): the store's state. It is a lead only for what launching ties to the subscription (CM-ACC-009, CM-PLN-004).
- **The storefront's 'ترقَّب إطلاق المتجر'** (observed-sa `docs/GAPS.md`, run `20261009T084616Z-journey-storefront-order-public-demo-en`): a lead for CM-ACC-009's coming-soon page on Salla.
- **The tasks' templates**, in their entries' text: what the dashboard prefills for the merchant. They are leads for the settings these features hold:
  - a coupon's `is_apply_with_offer`, `free_shipping`, `show_checkout_coupon`, `show_thankyou_coupon`, `exclude_sale_products` and `marketing_active`, for CM-MKT-002;
  - a bar's `pages`, `applied_in`, `versions` and `style`, for CM-SFR-007;
  - a reminder's `cart_delay`, `min_cart_value_toggle`, `channels` and `expire_after`, for CM-MKT-022.
- **The top bar's display toggle** (`feather feather-moon`, `partners-portal-header/partner@en/source.html`): a lead, if a light or dark mode of the portal matters to anything.

## The checker's lines, read again

- **`CHANGES` CM-ACC-009 becomes held** (line 62; entry 35, the step launch, `shows`). Read again against the answer and the home page; see "Entries I couldn't tell". The cell gains a statement and no placement.
- **`CHANGES` CM-ONB-004 becomes held, with `core`** (the 37 lines of missions and checklist steps). This is the same thing as SA-7's ui-merchant-gamification and SA-27's 37 lines, which already change it. My lines add the store's setup checklist (`onboarding/status`) as its second source.
- **`NOTE` lines 98, 100 and 101, core on a product named with the platform's brand:** 'Salla App' and 'Salla Partners Portal' in the English notices. The lines are `core` by what the entry shows: Salla's own portal and its own notice. None is `own-service`, and the brand names no maker.
- **`NOTE` container lines:**
  - 67 and 90, the language menu: new (above);
  - 70, the bell: CM-PTN-001;
  - 71 and 92, the heading Message Center: CM-PTN-001;
  - 84, the avatar: CM-PTN-002;
  - 68 and 91, the language items, and 82 and 102, 'Read All': not containers in the source (above).
- **`NEW`:** العربية / English, 2 lines.
- No first lead whose cell holds nothing was left unnamed. CM-INV-010 (by عميل, منتج) and CM-AUT-001 and CM-APP-008 (by app, within, link) matched only common words.

## Problems with this brief or the script

- None that blocked.
- The checker reads `parent` by text, so an item whose text equals its container's, such as the selected language, is flagged as a container.
- The brief's list of `out` kinds doesn't say whether a notice an account received is that account's data or the platform's statement. I placed what the notices state (above).

## The coordinator's check (31 October 2026, after the batch)

- **The cells this batch changes stand:**
  - CM-ONB-004 gains the store's setup checklist as a second source, beside SA-7's and SA-27's lines;
  - CM-ACC-009 is held by the launch step's `shows`. The storefront's 'ترقَّب إطلاق المتجر' before launch (observed-sa `docs/GAPS.md`) is the second stage's lead.
- **A task line is placed by its own words.** SA-27's Salla app task, which doesn't say what the app does, stays `shows`; this batch's, which does, is `core`.
- **The portal's header stands,** placed by the routes SA-34 to SA-36 gave its links.
- **For SA-29:** the navigation group 'Others' is `out`, by the ruling after SA-28. It names only a grouping, over several capabilities' pages.
- **New thing:** the portal's language menu, `العربية / English`: the interface language of the platform's own portal or admin, which no capability holds. CM-MKS-008 is the store's languages for its buyers. It is decided with every platform's new things.
- **Cost:** 12.2 million tokens over 70 requests, about 149,000 an entry.
