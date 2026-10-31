# SH-14: notes (Shopify, `admin-router`, entries 1 to 81: Markets, MerchantCheckout, MetafieldDefinitions, Notifications, OnlineStore)

Effort `high`. Evidence: observed-sh at `e38dc17e3`; the router's items are `structures/shopify/admin-router/items.jsonl`, lines 734 to 830.

## 1. What I read

- The brief, the digest `held/rules/admin-router.md` and the last section of `held/review-H-rulings.md`; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md` and `structures/README.md`, the register's rows for `admin-router` and `admin-betas`, `index/ledger-summary.tsv` and `index/ledger/admin-route.tsv` (by route id), the selection rows and `show --meta`; the evidence map.
- Earlier batches' notes, only where the digest sends me to a case:
  - `notes-SH-9.md`, rule 11 (lines 67 to 69) and its table (lines 26, 29): the POS Pro offer in the subscribe flow;
  - `notes-SH-10.md`, A7 and A8 (lines 57, 58): metafield lists and app-controlled metafields;
  - `notes-SH-11.md`, B1 and B4 to B7 (lines 44 to 50): redirects whose target no run shows, read-only metaobject entries;
  - `notes-SH-12.md`, C9 (line 55): a page with modal children;
  - `notes-SH-13.md`, D1, D3 to D5 and D10 (lines 32 to 48): redirects and legacy twins.
- Earlier lines: SH-11's lines 28 to 30 (Content's URL redirects, the twins of my `redirects` routes), SH-9's 'Try POS Pro' lines, and the lines on Shopify Email and on the sender email (SH-34 to SH-55), by grep.
- `makers` wasn't run: the only first-party products my routes name, Shopify Email (now Shopify Messaging) and POS Pro, are in the digest's section 3.

## 2. Count

81 entries, 84 lines, every entry on a capability: no `new`, no `out`. Supports: `core` 58, `core;extension-point` 12, `shows` 14.

By capability: CM-CNT-002 17, CM-NTF-001 10, CM-CNT-004 9, CM-MKS-003 8, CM-MKS-001 6, CM-CNT-003 6, CM-CNT-005 5, CM-SFR-001 4, CM-SFR-002 4, CM-CNT-009 4, CM-SHP-001 2, CM-PLN-001 2, CM-NTF-004 2, CM-CUS-007 2, CM-POS-001 1, CM-MKT-007 1, CM-CAT-001 1.

Second lines: Settings > Notifications (SH-E-4a6be307) takes CM-CUS-007 for its anchor Marketing consent and CM-MKT-007 for Shopify Email open tracking; Customer notifications (SH-E-6e0f3042) takes CM-CUS-007 for its anchor Marketing double opt-in confirmation.

## 3. New things

None.

## 4. The `CHANGES` line

- **CM-CNT-003@shopify gains `extension-point`** (lines 78 and 79: SH-E-70e42a11 `page:create`, SH-E-9d4a6792 `page:update`). Their intents, create and edit `shopify/Page`, release public, have Intents API pages (`derived/intents.tsv`, the table's Page row). By the ruling after SH-8 and the digest's rule 19 they are `core;extension-point`, as SH-10 placed Catalog's and Collection's. The concern map holds the admin's create page intent as `core` (SH-S-7241). Kept.

While line 41 read `own-service` (section 5, R14.6), the checker also printed 'CM-MKT-007@shopify gains own-service'. It now reads `core`, and that line is gone.

## 5. Rules I followed where the digest is silent (for the coordinator to add)

- **R14.1. A page route that sends ineligible stores back to its section is no redirect.** Managed Markets' routes at `markets/managed/*` have components of their own (ManagedMarketsApply, ManagedMarketsActivate, ManagedMarketsDeactivate, ManagedMarketsConfiguration, ManagedMarketsLanding). Six stores' sweeps were sent on to `markets`. `docs/GAPS.md` records Managed Markets answering INELIGIBLE with MISSING_SHOPIFY_PAYMENTS on capture-us-plus. I read the landing as the store not being eligible, so the routes stay `core` on CM-MKS-003, the landing in `reading`. The digest's rule 11 covers loader-only routes, and rule 10 needs a redirect marker. A staff user's sweep met 'You need permission to view this feature', a gate on the user.
- **R14.2. A callback whose component is named for a redirect, but whose page does work of its own, is `core` on its page's capability.** `notification-settings:email-domain-connect-callback` (EmailDomainRedirect, with the email domain page's action) shows 'Completing authentication' and 'Shopify is starting email domain validation.' (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/559.html.txt`). A trial store's visit was then sent on to `email-domain`, 'Propagation in progress'. This extends rule 12, "a page titled for a redirect with content of its own is `core`", to a component named for a redirect.
- **R14.3. A route rendered inside its parent's component is `core` on its title's capability, where none of its names says redirect, even if its visit didn't render.** These routes have no loader or component of their own, so the Online Store's frame renders them: `link` and `link-list` ('Navigation'), `online-store` ('Online store'), `online-store:preferences` and the `themes` routes.
- **R14.4. A container whose own loader a visit shows sent elsewhere keeps its own support,** `shows` on its target's capability (rule 8's "keeps its own support", with rule 11). `menu`, titled 'Navigation', has `menus-loader` only, and a visit was sent to `content/menus`. `articles:redirect`, `blogs:redirect` and `blogs:redirect:id` are the same, their ids naming a redirect.
- **R14.5. Two betas in one eligibility object are joined with ` and `** (rule 24): `beta 4e79d5b1 and beta 2847a1c7` for `editor:labs`. Both are false in both held stores, so the line is `shows` (rule 29).
- **R14.6. A settings anchor titled with a first-party app's brand is the admin's own route.** 'Shopify Email open tracking' is an anchor of Settings > Notifications. I placed it `core` on the app's capability, CM-MKT-007, as the digest keeps Credit's admin routes `core` (its section 3, 'routes `core`; own features `own-service`'). The other reading is `own-service`, by the ruling after SH-37 (every line about Shopify Messaging, formerly Shopify Email). The changelog batches' `own-service` lines on CM-MKT-007 make that cell change anyway.
- **R14.7. A notification template, or a group of templates, is CM-NTF-001's alone.** That covers the in-store receipt and Customer notifications' anchors such as 'Local delivery notifications' and 'Return notifications'. A notification of a return is no kind of return (M-6 refined), so the subjects' capabilities (returns, gift cards, local delivery, POS) take no line. An anchor whose own words name another thing takes that thing's line: Marketing consent and Marketing double opt-in confirmation go on CM-CUS-007.
- **R14.8. A legacy Online Store address with its own loader and component is `core` on its twin's capability,** as SH-13's D1 and D10 placed Marketing's legacy twins. `redirects`, `redirects/new` and `redirects/:id` (RedirectList, RedirectCreate, RedirectEdit) stayed at their addresses in the sweeps. They take CM-CNT-009, as SH-11 placed the `content/redirects` routes (SH-E-cf0ec94a, SH-E-4f41355b, SH-E-1962e785).

## 6. Entries I couldn't tell, and what would settle each

- **SH-E-1c154999, `market:update:eea-compare-at`** (a modal at `markets/:id/compare-at`, EEACompareAtPriceModal). I placed it on CM-CAT-001: a compare-at price is a price the product record keeps, as the corrections after SH-41 read unit pricing. No capability holds compare-at prices by name (`caps --terms` 'compare-at; compare at price; compareAtPrice; sale price; omnibus'; `search` 'compare-at'). The other readings:
  - CM-MKS-001: a market's own setting on its details page;
  - CM-CAT-013, product pricing: its Shopify cell holds only App Store categories, so `core` would change it.

  The modal's page, opened in a market of the EEA, would settle it. No run opened it (it needs an instance).
- **SH-E-1e14b3d0, `option-definition:update`** ('Edit shipping option'). I placed it on CM-SHP-001, by its title. The concern map places the same eligibility, on the twin `option-definition:create`, on CM-MKS-001 (SH-S-5205, 'shipping option definitions need the store feature marketDrivenShipping'). A CM-MKS-001 line here would rest on the gate's feature alone (rule 6), so I gave none. The coordinator may align the two.
- **SH-E-81133e5f, `merchant-checkout:subscribe:pos-pro`.** I placed it on CM-POS-001 alone, as SH-9 placed the 'Try POS Pro' routes. Its page shows the selected plan beside the add-on. A CM-PLN-001 line would rest only on the resource `subscription`, which the section's routes share (rule 3), so I gave none.
- **SH-E-1809c717, SH-E-e3a4646d and SH-E-19d3a4c4, the in-store receipt.** I placed them on CM-NTF-001 alone. Their template, 'POS and mobile receipt', is POS's receipt, so a CM-POS-001 line is the other reading.
- **SH-E-8a12b226 and SH-E-a5eec54e, Email domain authentication.** I placed them on CM-NTF-004: delivery by email, whose name holds the sender name and whose Shopify cell holds the SMS Sender ID. The other reading is CM-NTF-001, where SH-34 placed the sender email. No cell changes either way.
- **SH-E-4a70ec11 and SH-E-706da674, `links/*` and `link_lists/*`.** I placed them `core` (R14.3). With no loader or component, they may be legacy addresses that the Online Store's frame sends on, as `menus/*` went to `content/menus`. A visit that renders would settle it.
- **SH-E-6a1e0fdd, `editor:labs`.** It is `shows` by its betas. The concern map's `editor` (`themes/:id/canvas`, SH-S-5211), with the same component and betas, is `core` on CM-SFR-002 ('editor route behind THEMES permission and betas'). By the digest's rule 29 it would be `shows`. It is for Shopify's amendment.

## 7. What run steps state that no entry holds (for the second stage, M-12)

- **Market details,** `raw/runs/20261027T202345Z-journey-checkout-address-per-country/steps/078.text.txt`. A market's other customizations, each another capability's:
  - Catalogs (line 42), Currency (48), Domain / language (52);
  - Taxes and duties (56), Returns and cancellations (58);
  - Checkout and accounts (62), Parent market (64);
  - Customer privacy, 'Cookie banner, Data sharing opt-out' (67), Policies (69).
- **The subscribe flow on a trial store,** `raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/`:
  - **POS Pro** (`322.text.txt`): 'POS ProAdd-On' (line 40), 'Unlimited staff roles & permissions' (44), 'Customer loyalty insights' (46), 'In-store pickup & flexible delivery' (48), '$79' and '/mo after trial' (50 and 51). These are POS Pro's price and features, for CM-POS-001's qualities.
  - **The checkout** (`323.text.txt`): 'Build without bills' (26), '0.5% back on sales' (28), '$20 USD back for domain' (29), and the renewal line (44).
  - **The plan picker** (`321.text.txt`): the plans' trial prices and lines.
- **Customer notifications,** `raw/runs/20261007T102602Z-journey-notifications/steps/001.text.txt`: 'Shopify Messaging', 'Installed' (lines 157 and 158), and 'Remarketing with Shop' (160) with its Cart reminder (162), Back in Stock (165), Price drop (168) and Browse abandonment (171). These are Shop's own reminders, `own-service` by the ruling after SH-34.
- **Settings > Notifications,** `raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/332.text.txt`, line 61: a public domain such as Gmail can't send as the store, and customers see a shopifyemail.com address. This is a statement for CM-NTF-004.
- **Online Store > Preferences,** `derived/step-text-from-html/20261004T115543Z-storefront-page-types/001.frame-0.html.txt`, five sections:
  - Store access (line 4), the storefront's password;
  - Social sharing image and SEO (17), CM-CNT-007;
  - Automatic redirection (34), CM-MKS-004;
  - Spam protection (42);
  - Crawler access (48).
- **Text written for the admin's agent** (the digest's rule 41), leads for the admin's AI assistant. All three are in `items.jsonl`:
  - `market:update`'s intent tools deleteShippingOption, createShippingOption, editShippingOption, updateForm and getFormValues (line 736);
  - the Sender email anchor's intent tools (line 782);
  - `themes:theme-editor`'s `metadata.sidekick.navigationReadiness` (line 800).

## 8. Problems with the brief or the scripts

- **`earlier` matched route ids as words.** It matched `themes`, `link`, `menu`, `page`, `redirect` and `online-store` across hundreds of lines, such as CM-PLN-001 ×182 for `page`, and none of these were twins. I read them by route id (the digest's rule 44). It didn't find my real twins, SH-11's `content/redirects` routes: I found them by the routes' titles.
- **The checker's container notes.**
  - It notes a path `:id` under another parent as a container: lines 69 and 75, `menu:redirect:id` and `redirect:update`. Both are set aside, by the digest's rule 8.
  - It didn't note some routes whose paths begin their siblings' paths. I named their children in `reading`:
    - `metafield-definitions:edit`, over `bulk-edit`;
    - `metafield-definitions-index`, over `metafields-ownertype`;
    - `market:update`, over `:id/shipping` and `:id/managed`;
    - `page:update`, over the page metafield routes;
    - `themes:code-editor`, over `theme-editor` and `theme-settings`;
    - `themes`, over `editor`.
- **No structure's items and sources disagree.** The in-store receipt's routes land at `email_templates/store_receipt/…` (`index/ledger/admin-route.tsv`). That is the template's id, not a disagreement.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 81 of 81 entries, no problem. `method/held_router_gates.py SH-14 --apply` named the ancestors' gates in 49 lines.
- **The one `CHANGES` stands:** CM-CNT-003 `extension-point`. The page routes' create and edit intents have their Intents API pages (rule 19; the ruling after SH-8).
- **The rules R14.1 to R14.8 stand** and join the digest's section 6. R14.6, a settings anchor titled with a first-party app's brand being the admin's own route and so `core`, follows the ruling after SH-41: the admin's own routes for a separate product stay `core`.
- **For Shopify's amendment, two concern-map placements to read again:**
  - SH-S-5205, `option-definition:create`'s eligibility on CM-MKS-001. Its twin here stands on CM-SHP-001 alone.
  - SH-S-5211, `editor` `core` under betas false on both held stores. Rule 29 makes that `shows`.
- **The open readings stay as placed.** The EEA compare-at price is on CM-CAT-001, a price kept on the product, as unit pricing is.
- **`earlier` floods on route ids that are plain words** (`themes`, `link`, `menu`, `page`). It isn't changed: none of SH-15 to SH-18's ids floods.
- **Cost:** 20.4 million tokens over 101 requests, about 252,000 an entry. The context reached about 357,000 tokens.
