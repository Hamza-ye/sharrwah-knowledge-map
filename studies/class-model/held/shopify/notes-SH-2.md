# SH-2: notes (Shopify, the last 14 entries of `admin-home-setup` and the first 66 of `admin-main-nav`)

Batch SH-2, effort `high`, read under `briefs/H-held.md` and the coordinator's rulings to the one after SA-56. Evidence: observed-sh at `e38dc17e3`. 80 entries, 97 lines in `placements-SH-2.tsv`:
- 77 entries placed on capabilities, 3 `out`, none `new`;
- 94 capability lines, 3 out lines.

**SH-1's split.** The 14 `admin-home-setup` entries are the new trial store's Home cards (`ibx5bt-xy`, both states). They follow SH-1's rules A1 and H1 to H15, which the coordinator kept, and SH-1's lines for the same cards on other stores (its lines 13 to 44, 115, 116, 158 to 161, 189 to 194). **SH-3 hasn't run.** It holds the last 6 entries of `admin-main-nav` (the new store's Inbox link, Pin to your navigation, Apps, Add, Settings and its trial link). The rules below are the ones my lines follow, so that the coordinator can align the two.

## What `admin-main-nav` is

Three navigations, each the `nav` element of one step's HTML (`source.html` beside each `items.jsonl`):
- the development store's on its Users page (`demo-fake-dev-store@settings-organization-account`, run `20260930T103225Z-sweep-dev`, step 363);
- the trial store's on its plan page (`fake-demo-sharrwah@settings-subscribe-select-plan`, run `20260930T002940Z-sweep-trial`, step 100);
- the new trial store's on its Home (`ibx5bt-xy@home`, run `20260930T074710Z-m0-account`, step 3).

The element holds the sidebar, the top bar's Alerts Feed and the user menu, and the trial store's plan link.

The concern map read the trial store's sidebar links 2 to 32 (SH-S-1506 to SH-S-1536, Q1's inventory SH-I-0742 to SH-I-0772), and the development store's Shipping labels and Abandoned checkouts. So those have no entry. My entries are the same links on the other two stores, with the top bars.

## The rules my lines follow (for SH-3)

- **N1. A link takes the capability of the page its address opens.**
  - The page is the router's route for the address, with the store's prefix stripped (`derived/admin-routes-resolved.tsv`), such as `draftOrders` at `draft_orders`.
  - Where the concern map placed the same link on the trial store's navigation, I kept its capability and cite its statement (SH-S-1507 Orders to SH-S-1534 Sales channels).
  - Scope is empty: every sidebar link here is on both the development store and a trial store. A route's gates on the store are the route entries' scope (SH-8 to SH-10), not a link's.
- **N2. A link whose words name a grouping is a container (M-13):**
  - **on the capability its title names:** Orders, Products, Customers, Growth (CM-MKT-005, 'Shopify Growth' in its name), Markets, Analytics and Sales channels;
  - **Settings is CM-ACC-006.** 'Settings' is in its name (Salla's term), and its address, route `settings`, opens Settings > General (`20260930T103225Z-sweep-dev` step 170 landed on `settings/general`, `index/ledger/admin-route.tsv`). Salla's Settings link (SA-E-0bfa5b40) and Zid's Settings index (ZD-E-5155bc0d) are placed the same way. It is not the whole admin, and it has a title of its own.
  - **failing a title's capability, on the page its own address opens:** Content opens `/content/metaobjects`, Metaobjects, so it is CM-CNT-002. Its section `content:parent` is gated by `metaobjects.enabled`. 'Content' names a part of the platform, so it isn't the ruling after SA-28's grouping, such as 'Others' or 'More'.
  - **a second line where its page is a second thing:** Analytics opens `analytics:dashboard-details`, which SH-8 also placed on CM-ANL-003 (SH-E-b16b7f2a).
- **N3. Home is CM-ANL-003 and CM-ONB-004.**
  - Its page `route:home` is the Home, whose own capability is CM-ANL-003: SH-1's H13, the staff permission Home > Home, and the development store's dashboard metrics.
  - It also holds the store's setup tasks and guides: SH-1's H2 and H6, and this batch's lines 1 to 14 for `ibx5bt-xy`. That is a page which is itself two things (the ruling after SA-19).
  - Q1 had left Home out as 'the admin's landing page; it gathers other concerns rather than holding one' (SH-I-0742). SH-1's kept rules place its contents, so the link follows them.
- **N4. The Shopify logo is `out`.** It is the frame's mark linking to the Home, like a breadcrumb or a back button (the ruling after SH-37). The Home link places the page.
- **N5. A sidebar group gives its links no line, but Sales channels does.**
  - The groups Orders, Products, Customers, Growth, Content, Markets and Analytics say where a link sits, so their children take no line for them (M-6 refined): Attribution has no CM-MKT-005 line, and Reports no CM-ANL-001 line.
  - Sales channels lists the channels installed on the store, each one a sales channel, as Bank deposit under OFFLINE PAYMENT METHODS is an offline payment method. So Online Store, Agentic and Inbox, button and link alike, each take CM-CHN-001 `core` beside their own capability.
  - The Online Store item's buttons Edit theme (CM-SFR-002) and View your online store (CM-SFR-001) are a channel's controls, not channels, so they take no CM-CHN-001 line.
- **N6. The channels' own capabilities:**
  - **Online Store** is CM-SFR-001: the route `themes`, section OnlineStore.
  - **Agentic** is CM-AIA-005 `extension-point`, the support the cell gives the same route. `apps/agentic`, route `agentic:list`, is open only to `APPLICATIONS` or `LIMITED_APPLICATIONS` (SH-S-5027, SH-S-5028; B-extent's convention). See 'Entries I couldn't tell'. It is the admin's own route section, not `apps:app_handler`, so I gave it no CM-APP-007 line.
  - **Inbox** is CM-SUP-004 `own-service`. The app is `shopify-inbox`, and the cell's own maker evidence is Shopify Inbox's Google Play publisher, Shopify Inc. (SH-S-2758; M-1; the ruling after SH-37).
  - **For SH-3, the Inbox link** (`apps/shopify-inbox`) would take the same two lines (CM-SUP-004 and CM-CHN-001), and CM-APP-007 `core` for the app handler's page (SH-8's SH-E-55ef27b1, visited as `apps/shopify-inbox`).
- **N7. The top bar:**
  - **the Alerts Feed** (its button, its filter View unread only and its alerts) is CM-NTF-002 `core`, as SH-51 placed the Winter '23 Edition's alerts feed (SH-E-7184be60). The unseen count is the store's own.
  - **the user menu** (`data-admin-user-menu` in `source.html`) is a container on CM-ACC-001, the merchant's account. That covers its button, named by the user's own name, and the signed-in user's entry, with the person's name and email. Salla's partner account menu, under the user's avatar, is placed so (SA-E-6b95baaa).
  - **the menu's stores and Create store** are CM-ACC-003, the owner's several stores and the move between them, as SH-51 placed the account drawer's 'list of stores to add and switch between' (SH-E-c5d17b7b). The stores' names and their organization's name (`parent-org-suffix`) are their own data.
  - **Log out** is CM-ACC-001, as Salla's dashboard sign-out (SA-E-7797ef68).
  - **The development store's badge 'dev'** (`s-internal-badge` in its `_DevStoreName_` element) is CM-DVT-004 `shows`: a badge is no place, plan line or definition.
- **N8. The plan link and the alert, under a store's own condition:**
  - **the trial store's plan link** 'Trial ends in 2 days, select a plan' is CM-PLN-001 `core`, with the store's label as scope (SH-1's H11). Its days left are its own.
  - **the alert** 'Your free trial of POS Pro ends in 3 days', 'Your account will automatically switch to POS Lite.' takes three lines:
    - CM-NTF-002, as an alert of the feed;
    - CM-POS-001, POS Pro's trial and the move to POS Lite, with `ctcbwa-r1` as scope, the store its address names. The feed is the trial store's, but the page it opens is that store's;
    - CM-APP-007, since its address is the Point of Sale channel's app page (`apps:app_handler_with_route_star_path`, SH-8's SH-E-30ffb42d).
- **N9. The Home cards follow SH-1's H2 to H5.**
  - 'Start with a free theme' is CM-SFR-001 `core` (the ruling after SH-53).
  - 'Get $20 back' on the domain card (the card `add_domain_card`) follows H12's reading: a second CM-SFR-008 line, with the store's labels as scope and `domain offer: Get $20 back` as its quality, beside the domain task's own line, which has no scope (the ruling after SH-69).

## New things

None.

## The cells that change, and why

- **CM-ONB-004, `holds nothing`, would become held, `core`** (the checker's CHANGES, lines 2, 6, 11, 15, 18, 24 and 76). SH-1's 54 lines on it aren't amended yet, so mine show the same change. Each was read again:
  - lines 2, 6, 11, 15 and 18 are the setup task cards and headings of the new store's Home, under SH-1's H2;
  - lines 24 and 76 are the Home links' second line (N3).

  They are kept.
- **No other cell changes.** Every other capability's Shopify cell is already `core` where my lines are `core`. CM-AIA-005 already holds `extension-point`, and CM-SUP-004 `own-service`. CM-DVT-004's `shows` leaves it `not-stated`.

## Entries I couldn't tell, and what would settle each

- **Agentic (SH-E-1fc6f03c, SH-E-7664c7ba), `extension-point` or `core`.**
  - I followed the cell's own reading of the route under B-extent's convention.
  - Shopify's changelog says 'Agentic Storefronts now has its own page in your Shopify admin' (SH-34, SH-E-2178ade3, `core;extension-point`) and 'Knowledge base is now built into your Shopify admin at Sales channels > Agentic > Knowledge base' (SH-36, SH-E-a50b68cc, `core`).
  - What would settle it: the coordinator's reading of the convention for a section of the admin's own router at `apps/<name>` that is open only to the apps permissions.
  - Either way the cell keeps both values.
- **The user menu as a container on CM-ACC-001 (SH-E-3a2e510d, SH-E-704ea5fd, SH-E-cffdd30d, SH-E-ca4d4277).**
  - Its labels are the person's own name and email, so it could be read as `out`, as one account's own data.
  - I read it as the account's menu (rule 3: a container is never `out`), as Salla's account menu is placed.
- **Inbox `own-service` (SH-E-4c631fa5).**
  - This rests on the cell's Google Play publisher for Shopify Inbox.
  - That the admin's Inbox channel (`apps/shopify-inbox`) is that app is a reading from its handle.
  - What would settle it: a held App Store listing of the admin app (`apps.shopify.com`) naming its maker. Without it, the line would be `shows`, and CM-APP-007 `core` on the link (M-10; the ruling after SH-36).
- **The Sales channels items' CM-CHN-001 lines (N5).** If the coordinator reads Sales channels as a sidebar group like the others, the six lines go, and no cell changes.
- **'Get $20 back' (SH-E-35ba470e, SH-E-52a66965).**
  - What it is paid back on, and how, isn't held. The card says only that, over 'Claim your store's web address'.
  - What would settle it: the domain purchase page on that store, or a held help page on the offer.
- **The POS alert's scope, `ctcbwa-r1` (SH-E-129293e5).**
  - The alert stands in the trial store's feed, and links to another store's POS subscriptions.
  - What would settle it: whether the alerts feed is the account's or the store's. A held statement on the feed's reach would.

## A structure whose items and sources disagree

`admin-main-nav`'s items give the user menu's entries 'Alerts Feed - 0 unseen alerts' (and '1') as their `parent`:
- the button with the user's name, the account's stores, Create store and the signed-in user;
- the lines involved are the development store's 37 to 41, and the trial store's 36 to 40.

That is the list nesting the extractor read. The source puts them in the user menu's own popover (`s-popover id=":r2q:"`, which the button with `aria-label="Demo-name demo-last-name"` controls, `data-admin-user-menu="true"`, `demo-fake-dev-store@settings-organization-account/source.html`). The source governs, and my lines read them as the user menu's.

## What the sources state that no entry holds (for the second stage)

- **The Home's own names for its setup tasks** (for CM-ONB-004):
  - the card handles `add_product_card`, `customize_theme_card`, `activate_payments_card`, `add_domain_card` and `review_shipping_card`, and the cards' ids `gid://shopify/HomeCard/<handle>`;
  - in `20260930T071154Z-m0-instruments/steps/002.html` and `20261001T023324Z-trial-watch/steps/004.html`.
- **The alerts feed's 'Mark all as read'**, an `s-internal-button` that the extractor doesn't take (`fake-demo-sharrwah@settings-subscribe-select-plan/source.html`). It is a control of CM-NTF-002's feed, and no cell needs it.
- **The page the POS alert opens**, `apps/point-of-sale-channel/locations/manage-subscriptions` on `ctcbwa-r1`: POS Pro's subscriptions by location, a lead for CM-POS-001's POS Pro. I didn't look for its visit.

## Problems with the brief or the script

- **`held_entries.py earlier` finds no line for a navigation link.** Its keys are the full address with the store's handle (`/store/demo-fake-dev-store/draft_orders`) and the query (`appLoadId=…`). SH-8 to SH-10 and the concern map cite routes by their own paths (`draft_orders`). I looked them up in `derived/admin-routes-resolved.tsv`, in the concern map's citations of the trial store's navigation, and by grep. Stripping `/store/<handle>/` and the query from an address key would find them.
- **The checker's first-lead note** (lines 25 and 77, CM-PAY-032) counts only a line's `cap_id`, not a reading that names the lead as a homonym. Both readings name it.
- **The checker's container note** matches a parent by its name across labels. The new store's collapsed Products 'holds 5 other entries', but those are the development store's.
- Nothing in this brief read differently from B-extent.md for these entries.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem. Its one `CHANGES`, CM-ONB-004, repeats SH-1's, kept.
- **N1 to N9 stand for SH-3, with two alignments** (the rulings after SH-2):
  - **Agentic is `core`,** lines 93 and 95. The changelog states its section part of the admin: 'Agentic Storefronts now has its own page in your Shopify admin'. A held statement outranks the convention that reads a route under the apps permission as an app's page. The anchor's `extension-point` on that route is read again at Shopify's amendment.
  - **Shopify Inbox is `own-service`,** as line 97 has it. Its Google Play publisher is Shopify Inc. (SH-S-2758), a maker statement whatever channel sells the app, as the cell reads it. SH-50's, SH-52's, SH-53's and SH-54's eight Inbox lines are aligned. The check after SH-54, which kept them `core`, is corrected. SH-3's Inbox link takes this batch's suggestion: CM-SUP-004 `own-service`, CM-CHN-001 and CM-APP-007.
- **The open lines stand as marked readings:** the user menu, a container on CM-ACC-001 over the person's own account; the POS alert's scope, the store its address names; 'Get $20 back', H12's reading.
- **The tools:** `held_entries.py earlier` now reads a store's admin link (`/store/<handle>/orders?…`) as the router's route 'at orders', and skips an ARIA name that is one capitalized word (Search), which is a label, not a key.
- **The structure's items and its source disagree** on the user menu's items' parent. The source governs (`evidence-map.md`).
- **Cost:** 16.4 million tokens over 87 requests, about 205,000 an entry. The context reached about 363,000 tokens.
