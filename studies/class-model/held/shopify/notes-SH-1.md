# SH-1: notes (Shopify, `account-organization` and the first 128 entries of `admin-home-setup`)

Batch SH-1, effort `high`, read under `briefs/H-held.md` and the coordinator's rulings to the one after SA-56 (nested gates joined with ` and `). Evidence: observed-sh at `e38dc17e3`. 130 entries, 193 lines in `placements-SH-1.tsv`:
- 114 entries placed on capabilities only, 2 on capabilities and a new thing, 14 `out`;
- 177 capability lines, 2 new lines, 14 out lines.

No batch had placed these two structures before. **SH-2 hasn't run.** It holds the last 14 entries of `admin-home-setup` (all from the new trial store `ibx5bt-xy`, SH-E-8863b63d to SH-E-4900f7ea) and the first of `admin-main-nav`. The rules below are the ones my lines follow, so that SH-2 can keep to them; the coordinator aligns the two.

## What the structures are

- **`account-organization`** holds the two links of the navigation of Shopify's account site (accounts.shopify.com, run `20261004T175650Z-journey-account`, step 1): General (`/accounts/<id>/personal`) and Security (`/accounts/<id>/security`). The step's page is the account's Security page, whose sections are Passkeys, Password, Secondary email, Two-step authentication, Authentication methods and Devices (`steps/001.aria.yaml`, lines 23 to 55).
- **`admin-home-setup`** holds the `main` region of the admin's Home in ten store states, each the ARIA subtree of one run step (`source.aria.yaml` beside each `items.jsonl`). An entry stands for the same node in every state it was held under (its labels). The region holds, by state:
  - a status button over the greeting, which the step's HTML names `data-onboarding-status-indicator`;
  - the greeting heading;
  - the Sidekick composer: its textbox, named by a suggested prompt, with Recents, Add files and more and Voice (the page's `complementary "Sidekick"` sits beside `main`);
  - the list of cards, named Home feed on some stores, each a button holding a heading, a description, an action and Dismiss card;
  - on the development store, the Home dashboard's metrics and Live visitors.

## The rules my lines follow (for SH-2)

- **A1.** Each link of the account site's navigation is the account's own page: General is CM-ACC-001 `core` (not CM-ACC-006, the store's general settings); Security is CM-TRU-001 `core`.
- **H1.** The Home's `main` region is read card by card, each entry with the card that holds it in its source (rule 1: an item read with the words its list gives it).
- **H2.** A card that sets up a thing of the store is a setup task: its card button and its heading take CM-ONB-004 `core`, and each also takes the capability of the thing the task sets up, with the support its words show.
- **H3.** A card's description takes the capability of what its words name as the card's own thing. Things it names only as examples or in a list take no line (the ruling after SA-41): 'card or digital wallet'; 'a title, a price, and a photo'; 'images, and pricing'.
- **H4.** A card's action link takes the capability of the page its address opens. Where its own words name another thing, it takes that line too, and the page's line comes second (the ruling after SA-19). Examples: Launch store, which opens `/themes`, is CM-ACC-009 and CM-SFR-001; Generate image, which opens `/products`, is CM-CAT-007, CM-AIA-002 and CM-CAT-001.
- **H5.** These are `out`, as UI strings that name no place or feature: Close, Dismiss, Dismiss card, and a generic action with no address (the Get started and Resume buttons, Watch now). An action button that has no address but whose words name a thing takes that thing's line, its target not held: Unlock store, Add digital product, Discover products to sell, Review delivery.
- **H6.** A guide of tasks (a card with 'N of M tasks completed') is a setup task, as H2. Its progress line takes CM-ONB-004 `core`, the count being the store's own. Its 'Next task: X' takes CM-ONB-004 and X's capability, and the guide's own capability where X is a kind of the guide's thing (M-6): Import your orders is a step of the migration guide.
- **H7.** A card that suggests an app without naming its maker (the Digital Products app, or 'a recommended app') is `shows` on the app's thing (the ruling after WC-3). The task's own line is CM-ONB-004 `core`. The maker is a gap.
- **H8.** A card that isn't a setup task takes only its own things' lines, without CM-ONB-004:
  - the lesson Learn the dropshipping basics is CM-ONB-003 `core`, the platform's own learning in its admin, and `shows` on its topic (CM-CAT-010);
  - the card for Sidekick's image generation is CM-AIA-002 and CM-CAT-007 `core`.
- **H9.** The greeting heading, and its words split around the store's name:
  - it takes CM-ONB-004 `core` where its words name the store's setup or progress: 'ready to sell', 'Let’s set up', 'is starting to take shape', 'is set up to take payments', 'What do you want to work on next?';
  - a greeting that names nothing ('Let’s continue growing your business.') is `out`;
  - the store's name in it (the buttons My Store and capture gb plus) is the store's own data: `out`.
- **H10.** The Sidekick composer on the Home is CM-AIA-002 `core`: its textbox and its controls Recents, Add files and more and Voice. Voice keeps SH-36's line on Sidekick Voice. The textbox's name is a suggested prompt, and what the prompt asks for (a product listing, a launch, an import) is named in passing, with no line.
- **H11.** The onboarding status indicator states the store's own state. Its scope is the store's labels (the brief's flag rule: 'the store's label where it names no plan').
  - In the trial state, 'Trial ends in 2 days' and 'Trial ends soon' are CM-PLN-001 `core` (the store's trial on its plan; its days left go in `reading`) and CM-ONB-004 `core` (the indicator).
  - On the paid store, 'Ready to sell' is CM-ONB-004 `core`.
  - The popovers are in the steps' HTML, not in the entries, so they clarify only (M-12).
- **H12.** The plan banner over the trial store's Home is CM-PLN-001 `core`, with the store's labels as scope: 'Get 3 months for $1/month', its offer a quality as the pricing batches wrote it (`paid trial: …`), and Select a plan (`subscribe/checkout`, as SH-9). For SH-2, a reading: the domain card's 'Get $20 back' on the same store is an offer listed for that store, so it would take CM-SFR-008 with the same labels as scope and the credit as its quality.
- **H13.** The Home dashboard is CM-ANL-003 `core` (the Home's own capability: its staff permission Home > Home, and SH-35's Home feed): its title Dashboard metrics (a container), its period Last 30 days, its channel filter All channels and each metric. The values are the store's own data, in `reading`. Live visitors is CM-ANL-004 (Live View, `/analytics/live`). The separator `·` and the illustrations' alt texts are `out`.
- **H14.** **Scope** is empty except in three cases:
  - a plan the entry's own words name: `Plus`, on the Plus guide;
  - a market they name: `EU`, on the guide for the EU right of withdrawal, whose options are 'for EU orders';
  - the store's own subscription state (H11, H12), where the scope is its labels.

  A card shown because of the store's own progress (no product yet, no domain yet) is shown on a condition of the store's own data, so the stores go in `reading` where they matter, never in `scope` (M-11). A text that stands for two cards under different conditions takes a line for each: '0 of 5 tasks completed' is on the Plus guide (`Plus`) and on the EU guide (`EU`).
- **H15.** The list Home feed is a container. By its title it is the Home page's feed, CM-ANL-003 `core`, as SH-35 placed the Home feed's insights (SH-E-578fcd32). Its items here are setup tasks, so it takes CM-ONB-004 `core` as a second thing of its own page.
- **The capabilities the cards name.** These follow the cells' own places:
  - Products: CM-CAT-001;
  - the theme: CM-SFR-001 (and SH-53's ruling makes the platform's free themes `core`, for SH-2's 'Start with a free theme');
  - payments: CM-PAY-001, `settings/payments`;
  - domains: CM-SFR-008, `settings/domains`;
  - shipping rates: CM-SHP-001, a shipping profile or a market's shipping section, the market's page taking CM-MKS-001;
  - the products import: CM-MIG-001, `products?modal=import`;
  - the launch and the password: CM-ACC-009;
  - the migration guide: CM-MIG-005;
  - B2B and DTC in one store: CM-B2B-001, the cell's blended store, SH-S-0740; B2B markets also take CM-MKS-001;
  - the checkout: CM-CHK-001 for the page `settings/checkout`, CM-CHK-003 for 'Customize your checkout';
  - the return and cancellation options and the route `settings/legal/cancel-return-rules/new`: CM-CNT-008, the cell's SH-S-7089, as SH-E-79642a2b's line placed Settings > Policies > Return and cancellation rules;
  - the EU right of withdrawal: CM-RET-004, its filler the law the entry names;
  - orders to fulfill: CM-SHP-009, its page Orders taking CM-ORD-001.

## The new thing

**`new:sales events`** (`shows`, scope `Plus`). Entries: SH-E-220db6fa, the Plus guide's card, and SH-E-3d1e9537, its description, 'Customize your checkout, enable sales events, and reach more shoppers with Plus-exclusive features.'
- **Place of its own:** none held. The card's line of text is its only place here, a line inside a card, and the guide's five tasks aren't held.
- **Proposed home:** domain D, area MKT, parent CM-MKT-005 (marketing campaigns and activities). This is a reading from the words alone: 'sales events' are events of selling that the merchant enables. Nothing held defines them.
- **Names:** English only, 'sales events'. The admin isn't held in Arabic (observed-sh `docs/GAPS.md`, Admin in Arabic).
- **Searched:** `sales event; flash sale; scheduled sale; event; Launchpad; Plus exclusive`. Only lifecycle events, webhooks and bookings came back. The checker's leads, CM-EVO-001 (Feature test drives on Shopify), CM-ORD-003 and CM-API-013, are leads by the words 'enable', 'completed' and 'one' only.
- **What would settle it:** the Plus guide's task list, opened from its Get started, or a held help page on Plus sales events.

'reach more shoppers' names no thing, so it takes no line.

## The cells that change, and why

- **CM-ONB-004 holds nothing, and becomes held, `core`** (54 lines). Its reading said no statement showed 'steps or a checklist the admin gives a new store'. This structure is that checklist: the Home's setup tasks and guides, the tasks' progress ('N of M tasks completed', 'Next task'), the Home feed holding them and the onboarding status indicator. The cell's own note names Shopify's 'home setup'. Each line rests on a card the platform shows in its own admin, so it is `core`.
- **CM-MIG-005, from `not-stated` to `core`** (6 lines). The migration guide 'Complete your migration to Shopify' reads 'Import your remaining data from your previous platform, including customers and orders. Then, connect your domain to your new Shopify store.' It has 6 tasks on the Plus store and 5 on the trial store, whose next task is 'Import your orders'. It is Shopify's own guide in its admin for moving a store from another platform. CM-MIG-001 keeps the imports, and CM-SFR-008 keeps the domain.
- **CM-RET-004: no change, by the checker.** `cells` prints its Shopify cell as 'placed core' while its reading says 'shows only … (derived not-stated)'. My lines put Shopify's own guide for the EU right of withdrawal there as `core` (SH-E-bec81020, SH-E-28bb0660, SH-E-7e9da2b2), and its help link and requirements as `shows`. If the cell is in fact `not-stated`, these lines change it: read them with that in mind. The guide's five tasks aren't held, so whether Shopify takes the buyer's withdrawal request itself, which is the capability's thing, isn't stated. What is held is the guide and its action, the Policies settings' new return and cancellation rule.

## Entries I couldn't tell, and what would settle each

- **SH-E-6b9e6be6, Recents:** placed on CM-AIA-002 as the composer's recent conversations. This is a reading, since what it opens isn't held. A step that opens it would settle it.
- **SH-E-9b7304ab, Pause activity globe:** placed `out`, as a control of the Home's look (the ruling after SH-37). If the globe is Live View's own display, it would be CM-ANL-004. Settled by a held statement naming the globe.
- **SH-E-688c493b, SH-E-f2a5d254, SH-E-993e055f, SH-E-7df6bdec, Review digital delivery options:** `shows` on CM-SEL-002, since who delivers digital products isn't stated and the button's target isn't held. The card follows the Digital Products app's. If the button opens a settings page of Shopify's own, the line is `core`, and it changes CM-SEL-002, whose cell reads 'No statement shows Shopify itself delivering digital goods'.
- **SH-E-59cfd801 and its parts, the Digital Products app:** `shows` (H7). The app's maker isn't stated anywhere held:
  - no earlier line names the app;
  - the App Store's sitemap ledger lists `https://apps.shopify.com/digital-downloads` as not-attempted, and whether that listing is this app isn't stated.

  A held listing naming Shopify as the maker would make these lines `own-service` (M-1), and would change CM-SEL-002.
- **SH-E-d3114ae2 and its parts, Discover products to sell:** `shows` (the ruling after WC-3), since the 'recommended app' is unnamed. The button's target would name it.
- **SH-E-70e7cdf9, Unlock store:** read as removing the store's password. The button's target isn't held.
- **SH-E-fd8fb9f8, Ready to sell:** placed on CM-ONB-004 alone, as the indicator. Its popover, 'You can sell, but your store isn't public', followed by 'When you're ready to reach customers, launch your online store.', also names CM-ACC-009's thing. The popover isn't an entry, so it is a lead below.

## A structure whose items and sources disagree

`admin-home-setup`'s items leave out every ARIA line that the YAML writes in single quotes. The source governs, and these nodes have no entry:
- the B2B guide's card button, 'button "3 of 6 tasks completed Sell B2B and DTC, in one place Next task: Create B2B markets … Resume Dismiss card"' (`capture-gb-plus@2026-10-07-plus-dev/source.aria.yaml`, line 110), and the same guide's '4 of 8 tasks completed …' button (`demo-fake-dev-store@2026-09-30/source.aria.yaml`, line 139);
- the lesson's second button, 'Watch now: Learn the dropshipping basics', in `ctcbwa-r1@2026-09-30` (line 143), `fake-demo-sharrwah@2026-09-30` (line 143), `@2026-10-04-paid-failed-bill` (line 141) and `@2026-10-05-staff-customer-support` (line 121).

Their texts are held in their parts' entries, so no cell loses a thing. The extractor (`capture/structure_aria_subtree.py`, by the register) could be fixed by its owner.

## What the sources state that no entry holds (for the second stage)

- **The onboarding status indicator's popovers** (`data-onboarding-status-indicator`), for CM-ACC-009 and CM-PLN-001:
  - 'Select a plan to keep building' (`20260930T071154Z-m0-instruments/steps/014.html`);
  - 'Subscribe for $1' with Select a plan (`20261001T023324Z-trial-watch/steps/001.html`);
  - 'You can sell, but your store isn't public', followed by 'When you're ready to reach customers, launch your online store.' (`20261004T235142Z-journey-paid-state/steps/005.html`).
- **The paid store's Home shows two prompts by the composer** that its ARIA source doesn't hold: 'Install a migration app' and 'Set up my import CSV' (`20261004T235142Z-journey-paid-state/steps/005.text.txt`, lines 26 and 27). They are leads for CM-MIG-005 (a migration app, which would be `extension-point` if apps do the moving) and CM-MIG-001.
- **The account's Security page's sections:** Passkeys Recommended, Password, Secondary email, Two-step authentication, Authentication methods, Devices and Logged in (`20261004T175650Z-journey-account/steps/001.aria.yaml`, lines 23 to 55). They belong to CM-TRU-001, which is already `core`. The General page (`/accounts/<id>/personal`) isn't in this structure's step: the register names the sweeps for it.
- **The Plus guide's and the EU guide's five tasks**, and the B2B and migration guides' other tasks, aren't held. Only each guide's first or next task and its action are held. The guides' pages would show them.

## Problems with the brief or the script

- **The `earlier` lookup matches on an entry's first word** (its key `name`): Add, Set, Get, Review, Choose and the like. In this structure that word is a verb, and its lines ('Add' on POS, 'Get' on Flow) are no lead. I filtered them out. Only 'Home feed' (a label), 'Voice', 'Live', 'Fulfill' and 'Select' gave a lead.
- **The checker's quote test doesn't read a structure's `meta.json`.** The account page's title, Shopify account profile, is held there (`source.title`), so I wrote it without quotes.
- **`cells` prints CM-RET-004's Shopify cell as 'placed core'** while its reading says it supports no placement. One of the two is stale.
- Nothing in this brief read differently from B-extent.md for these entries.
