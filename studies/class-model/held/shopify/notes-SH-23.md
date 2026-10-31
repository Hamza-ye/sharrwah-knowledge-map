# SH-23: notes

**The batch:** Shopify, 130 entries of four structures, in observed-sh at `e38dc17e3`, at effort `high`:
- `checkout-editor-pages`, the checkout and accounts editor's page picker (10, all);
- `collaborator-access-permissions`, the sections of the Dev Dashboard's Request access form (18, all);
- `dev-dashboard-nav`, the Dev Dashboard's navigation, on its own pages and an app's (17, all);
- `dev-dashboard-scopes`, the Dev Dashboard's scope picker for an app (85, the first of 200). SH-24 holds the rest and hasn't run yet: the coordinator aligns the two.

**Counts:** 130 entries in 139 lines. By entry, 125 `capability`, 2 `new`, 3 `out`. By line, 107 `core`, 20 `shows`, 8 `extension-point`, 1 `own-service`.

No earlier batch had placed these structures, so `held_entries.py earlier` found nothing on their keys but the label Log out (SH-2's line 60, which I kept). The rules below are mine, numbered for the coordinator to check and for SH-24 to keep for `dev-dashboard-scopes`.

## The rules I set

### The checkout editor's page picker (R23.1 to R23.3)

The picker is the dialog of the editor at `settings/checkout/editor/profiles/9408086312` on capture-plus (run `20261004T111454Z-journey-theme-editor`, step 20; `steps/020.aria.yaml`, lines 207 to 228). It lists three headings, each over a list of buttons, then a last list with Online store theme. CM-CHK-003 is the editor (its route `checkout-accounts-editor`), and its note sends 'customer accounts themselves' to CM-CUS-010.

- **R23.1. A page the picker offers is the editor's own page for it:** CM-CHK-003 `core`, a part of the editor (rule 3). That covers Checkout, Thank you, Sign-in, Orders, Order status and Profile.
- **R23.2. A heading is a container (M-13), on the capability its title names.**
  - Checkout goes on CM-CHK-001, and Customer accounts on CM-CUS-010.
  - Post purchase names pages after the purchase, which no cell's reading holds as the platform's own (CM-CHK-004's Post-purchase UI is apps' extension type). So it goes on the capability of the page it is on, the editor's, CM-CHK-003 (M-13's fallback).
  - A page under a heading is a kind of what the heading names, so it takes the heading's line too (M-6 refined). Checkout takes CM-CHK-001. Sign-in, Orders, Order status and Profile take CM-CUS-010: the buyer's account pages, which the cell holds through the Customer Account API's scopes for the customer's own orders and data.
  - Order status isn't CM-ORD-003: that capability's note keeps the order status page apart, as a homonym.
- **R23.3. Online store theme takes the capability its words name, CM-SFR-001.** The button states no target. The editor's address carries an `exitPath` to `/admin/themes/190246945064/editor`, the theme editor, from whose template picker the run opened this editor (step 19). That it returns there is a reading, and the place it opens is another place (rule 2), so it takes no CM-SFR-002 line.

The lines take no scope. The picker is held on one store, and its source states no condition. I named the store in `reading`, as SH-1 and SH-2 did for one store's admin.

### The collaborator request's sections (R23.4)

**R23.4. A section's checkbox is a section of the admin that a collaborator asks for.**
- **What an entry is:** each entry is one section's own checkbox, unlabelled (`data-node-id` `<section>_group`). Its section's permissions name it as their `data-parent-id`. Its title and count are in the mark before it ('Orders 0/19', `items.jsonl`). The form is the Dev Dashboard's Request access (`dev.shopify.com/dashboard/239421532/stores/collaborations/new`, run `20261007T010009Z-journey-partner-dashboard`, step 91: 'Permissions', 'Select all', then each section).
- **How it is placed:** each is `shows`, by the dry run's S7 (the selection row's note), as a container (M-13) on the capability its title names. I mapped the titles as SH-3 and SH-4 placed the staff permissions' categories.
- **Two lines:**
  - Home is the Home, which SH-2's N3 reads as two things, CM-ANL-003 and CM-ONB-004. SH-3 placed the staff permission Home > Home so.
  - Checkout and customer accounts names two things: CM-CHK-001 and CM-CUS-010.
- **Where no capability is the title's:**
  - Content takes CM-CNT-002, the line SH-2 gave the navigation's Content (SH-E-4e6c685e: no capability is its title's, so its page, Metaobjects).
  - Store settings takes CM-ACC-006, where SH-18 put the router's settings containers (SH-E-66492d29, SH-E-39a1431f).
  - Quick sale takes CM-POS-001, whose cell keeps the admin route `quick-sale`.
  - Finance takes `new:Finance`, the name earlier batches gave the admin's Finance section (the router digest, section 4).
- **No CM-STF-005 line:** I gave no section a line on CM-STF-005, collaborator access itself. A staff permission takes none on CM-STF-002 (the ruling after ZD-7), and CM-STF-005's note leaves the partner's own side to domain F. The form as a whole, the partner's request, has no entry.
- **Scope, terms and counts:** no line takes a scope. The terms are the node and section ids, the only words of the entry's own text. The count (0/19) is the form's state and its number of permissions, not a quality, so it goes in `reading`.

### The Dev Dashboard's navigation (R23.5 to R23.8)

- **R23.5. The Dev Dashboard is the platform's own dashboard for developers, CM-PTN-001 `core`** (E151, since the cell holds the Partner Dashboard's Home and its Dev dashboard item, SH-I-2085 and SH-I-2094). An item goes on the capability its title names, as the cells' readings show, with the Partner Dashboard's items as twins:
  - **Home** takes CM-PTN-001.
  - **Stores** takes CM-DVT-003, as the Partner Dashboard's Stores (SH-I-2086). It takes a second line, CM-DVT-004 `core`: its page lists the organization's stores, each of Type 'Dev', with 'Create store' (`derived/step-text-from-html/20261004T174545Z-journey-dev-dashboard-app/021.html.txt`), and E151 places the dashboard's dev stores there.
  - **Catalogs** takes CM-AIA-005 `extension-point`. Its page configures a catalog over 'All Shopify' or 'Specific stores' (`022.html.txt`). A later run's page previews a `search_catalog` call with a `ucp-agent` profile, beside 'Agent identity' (`raw/runs/20261007T010009Z-journey-partner-dashboard/steps/092.text.txt`, line 66). That is the catalog developers' commerce agents search, which E122 places so. It isn't CM-B2B-003, whose lead is by the word only.
  - **Apps** takes CM-PTN-001, as a part of the dashboard (rule 3). No narrower capability holds a developer's own apps.
- **R23.6. An app's pages in the dashboard:**
  - **Overview, Logs and App settings** take CM-PTN-001 `core`, as parts of the dashboard. They follow the Editions' cards on watching an app in the Dev Dashboard (SH-E-802a7c4b, SH-E-244b9ce2, SH-E-6343ce1c).
  - **Two homonyms are left aside:** CM-OPS-005, the store's own logger (WooCommerce Logs), and CM-APP-010, parameters a developer defines for each store (SH-66's notes).
  - **Versions** takes `new:App versions` `core`: the name SH-53 gave, now with a place of its own in the dashboard's navigation.
- **R23.7. The frame is `out`** (SH-2's N4; the ruling after SH-37). That covers the mark '$ shopify dev', linking to the Home, and the app's back link, named by the app's own name.
- **R23.8. The popover is the account's menu, CM-ACC-001 `core`, as SH-2 placed the admin's user menu.**
  - **The button:** 'M My Store' is a container (M-13), named by the organization's own name. It opens a popover over a list not yet loaded ('Loading...'), the signed-in user and Log out.
  - **Its two items:** the signed-in user, named by their name and email and linking to `accounts.shopify.com`, and Log out each take CM-ACC-001 `core` (SH-E-cffdd30d, SH-E-180b7e86).
  - **Its class:** the source classes the popover's rows `developer-dashboard-next-store-switcher`.

### The scope picker (R23.9 to R23.11), for SH-24 to keep

The picker is the dialog Select scopes of Create an app (run `20261004T174545Z-journey-dev-dashboard-app`, step 4). Each resource is a heading with no parent, then the API that grants it, then its scopes, each with that heading as `parent`. The concern map cited all 174 scope names from this file (`citations.tsv`, source `structures/shopify/dev-dashboard-scopes/…/items.jsonl`) and placed 41 of them. So the entries are the frame, the headings and the APIs under them.

The picker lists the Admin API's resources first, alphabetically. My part ends at Locations, and every resource in it has only the Admin API under it. The Customer Account, Storefront and Shop APIs' resources come later, under headings of their own (Customer and Checkouts recur there).

- **R23.9. A resource heading is a scope group of the API's own list.** It goes on the capability where the model places its scopes: the picker's own scope where the model placed it (`SH-S-0940` read_analytics on CM-ANL-001, and the like), else the cell whose terms hold its scope names. Its support is the one the model gives the same picker's scopes in that cell. Its terms are the heading.
  - **The support:** that is `core` (rule 4), except three resources, which take `extension-point`. The model places their picker scopes so: App Proxy (read_app_proxy, SH-S-0943, CM-SFR-004), Cart Transform Api (write_cart_transforms, SH-S-0950, CM-CHK-006) and Cart And Checkout Validations (write_validations, SH-S-0953, CM-CHK-005). See "Rule 4's two clauses" below.
  - **Headings no cell's terms hold:** I placed four by reading:
    - Checkout Kit Enhanced Buyer Events on CM-MKT-009: the buyer's events, the cell's event family;
    - Custom Fulfillment Services on CM-SHP-011, as the admin's 'Custom order fulfillment' anchor (SH-E-9f58e598);
    - Custom Pixels on CM-MKT-009, whose cell holds custom pixels' staff permissions;
    - Inventory Shipments, Inventory Shipments Received Items and Inventory Transfers on CM-INV-006, Shopify Transfers and inventory shipments.
  - **A title that names an API** (Cart Transform Api, Discovery Api, Locales GraphQL Admin Api) is the group its cell holds, so it takes no CM-API-001 line (E157).
- **R23.10. An API under a resource states that apps reach that resource's scopes through that API.**
  - It is the API's group for the resource, which the resource's capability holds. So it takes that capability's line alone (E157), with the heading's support, and its term is the API's name.
  - For SH-24: an API whose scopes the model keeps on the API's own capability goes there instead, by the same test (where the model places that API's scopes for the resource). Examples are the Customer Account API's `customer_read_orders` on CM-CUS-010 and the Storefront API's `unauthenticated_read_product_listings` on CM-SFR-012.
- **R23.11. The frame:**
  - 'Select scopes', the title, is a container (M-13) on CM-API-003, access scopes, `core`.
  - The filter 'API type', its option 'All APIs' and the search 'Search for scopes' are controls of the list, on CM-API-003, as SH-2 placed the alerts feed's filter on its feed (SH-E-b7a44753).
  - The filter's options that name an API go on that API's capability: Admin API on CM-API-001, Customer Account API on CM-CUS-010 and Storefront API on CM-SFR-012 (the router digest's rule 34). Shop API goes on CM-CHN-002 `own-service`, Shop being Shopify's own consumer app (the ruling after SH-34).
  - Cancel is `out`.

**For SH-24, the model's placements of the picker's later scopes:**
- read_marketing_integrated_campaigns: CM-MKT-005 `core`;
- read_merchant_managed_fulfillment_orders: CM-SHP-009;
- read_online_store_pages and write_online_store_pages: CM-CNT-003;
- read_orders: CM-ORD-001;
- read_privacy_settings: CM-TRU-006;
- read_shipping: CM-SHP-004; write_shipping: CM-SHP-001;
- read_shopify_payments_accounts: CM-PAY-002;
- read_shopify_payments_bank_accounts and read_shopify_payments_payouts: CM-PAY-005;
- unauthenticated_read_bundles: CM-SEL-006;
- unauthenticated_read_shop_pay_installments_pricing: CM-PAY-015;
- write_packing_slip_templates: CM-ORD-009;
- write_payment_terms: CM-PAY-008;
- write_product_feeds: CM-CHN-004;
- write_products: CM-CAT-001;
- write_returns: CM-RET-003;
- write_theme_code: CM-SFR-002;
- all of the above `core`;
- write_payment_customizations: CM-PAY-019 `extension-point`;
- unauthenticated_write_checkouts: CM-CHK-002 `shows`. Read that one before taking its support for a scope group.

## New things

- **`new:Finance`** (SH-E-b38da03f, `shows`): the admin's Finance section as a section of the collaborator request.
  - It is the name SH-12, SH-19, SH-39 and SH-60 gave it, decided in `held/new.tsv`.
  - **Place of its own:** the admin's section Finances (the router digest, section 4), and here a section of the Request access form. Its permissions span several capabilities: billing details, plan, app billing, Shopify Payments payouts, payment settings, Balance bank accounts and Shopify Credit transactions. So it is the section itself, not one of them.
  - **Proposed:** domain C, payments, with the router digest's alternative, CM-PAY-023's place.
  - **Names:** English only. The Dev Dashboard isn't held in Arabic.
  - **Searched:** Finance; Finances (only CM-APP-003's words matched).
- **`new:App versions`** (SH-E-c14d6233, `core`): an app's versions in the Dev Dashboard, where the run released the app's first version and opened Create version (steps 11, 18 and 20).
  - **Place of its own:** the dashboard's navigation item Versions, at `/dashboard/238086467/apps/431413264385/versions`.
  - **Proposed:** domain F, under CM-DVT-001 or CM-PTN-001.
  - **Names:** English only.
  - **Searched:** app versions; versions; app version. Only CM-API-006, the platform's API versions, matched: a homonym.

## Entries I couldn't tell, and what would settle each

- **Rule 4's two clauses** (R23.9). Rule 4 says a scope group of this list is `core`, 'as the model places the same scopes'. The model places three of this very picker's scopes `extension-point`: App Proxy, Cart Transform Api and Cart And Checkout Validations, whose things are apps' extensions and app-written logic.
  - **What I did:** I followed the model's placement for those six lines (lines 69, 70, 77, 78, 79 and 80), so that a heading doesn't contradict its own scopes.
  - **What core would change:** it would add `core` to CM-SFR-004, CM-CHK-005 and CM-CHK-006, three cells that hold only `extension-point`.
  - **The model's own split:** it places the function scopes of CM-SHP-013, CM-SHP-014 and CM-SHP-019 `core` from the same picker (SH-S-0978, SH-S-0990, SH-S-1009). The class is split on the same kind of scope.
  - **What would settle it:** the coordinator's ruling on the support of a function's scope group, applied to all six cells.
- **The Dev Dashboard's Apps and an app's pages** (R23.5, R23.6). I put them on CM-PTN-001 by E151. Two other readings exist:
  - CM-DVT-001 `core`: the platform's own tool for building apps. The Apps page says 'Extend Shopify's functionality and access all app capabilities using Shopify CLI.' (`derived/step-text-from-html/20261004T174545Z-journey-dev-dashboard-app/001.html.txt`, line 13).
  - CM-APP-002 `extension-point`: Salla's batches put the partners portal's apps list there (its `apps-list` route, a partner's tool for the app marketplace).

  A coordinator's choice of where a developer's own apps belong would settle it, for both platforms.
- **The popover 'M My Store'** (R23.8). Its rows' class names a store switcher. If its unloaded list is the organizations or stores, CM-ACC-003 (Shopify Organization and its stores) fits the button, as SH-2 placed the admin's list of the account's stores. A capture with the popover opened would settle it.
- **The signed-in user and Log out** (R23.8). Salla's partners portal puts its account menu and sign-out on CM-PTN-002 (SA-E-6b95baaa, SA-E-29ba3c4f). I kept SH-2's CM-ACC-001: the link opens the Shopify account at `accounts.shopify.com`, and this capture's organization, My Store, holds the merchant's own dev stores. On a partner organization's dashboard (239421532, Capture Partner Studio) the same menu might be read as CM-PTN-002's.
- **Shop API** (SH-E-5dee4f43, `own-service` on CM-CHN-002). What the API does for apps isn't stated here. Its one resource, O Auth Access (`shop_app:oauth`), is in SH-24's part. If it is Sign in with Shop, CM-CUS-010 fits better (the Editions digest's rule 11). Its shopify.dev page would settle it.
- **Checkout Kit Enhanced Buyer Events** (SH-E-88d2d694, SH-E-57271085, CM-MKT-009). No cell holds its scope. It may instead be CM-CHK-001's, where SH-E-df9ac94c put Checkout Kit. The scope's page on shopify.dev would settle it.
- **Online store theme** (R23.3). It may be CM-SFR-002, the theme editor, if the button opens it. A run that clicks it would settle it.
- **The Home section's CM-ONB-004 line** (line 18, a CHANGES line). It stands or falls with SH-3's line on the staff permission Home > Home (SH-E-092b7b88), which SH-3's notes flagged.
- **Post purchase** (R23.2): CM-CHK-003 by M-13's fallback. If the coordinator reads the thank-you page as the checkout's own, CM-CHK-001 fits, as Checkout's heading does.

## Items against their sources

- **`dev-dashboard-nav`:** the items list the signed-in user and Log out as siblings of the button 'M My Store', with no `within`. The source puts them inside that button's popover (`altair-popover`, rows classed `developer-dashboard-next-store-switcher`, `source.html` of both labels). The source governs, and my lines read them as the popover's, as SH-2 found for the admin's user menu.
- **`collaborator-access-permissions`:** an entry's text holds only its checkbox's ids, since its title is a separate mark item ('Home 0/1'). The entries could carry the mark before them. The terms can only be ids, and the title stays in `reading`.

## What the sources state that no entry holds, for the second stage

- **The Apps page:** the Shopify CLI's command '$ npm init @shopify/app@latest' (CM-DVT-002) and 'Get API credentials' (CM-API-002) (`derived/step-text-from-html/20261004T174545Z-journey-dev-dashboard-app/001.html.txt`, lines 13 to 15).
- **An app's Overview** (`012.html.txt`):
  - Growth's Install events and Uninstall events, line 36: an app's statistics for its developer, `new:App statistics` in Salla's SA-39;
  - Operations' GraphQL and REST error rates, Webhook failure rate and response time (CM-API-008, line 75) and Function error rate (CM-APP-005, line 81);
  - Admin performance (CM-APP-002, as SH-E-802a7c4b, line 91);
  - 'Install your app on a dev store to test OAuth, scopes, extensions, and app behavior' (CM-DVT-004, line 100);
  - Credentials and Versions.
- **App settings** (`019.html.txt`):
  - Credentials, with Client ID and Client secret (line 25) and the rotation's 'New installs that authenticate with the auth code flow will automatically start using the new client secret.' (line 31), for CM-API-002;
  - webhook delivery through Google Cloud Pub/Sub (line 34) and Amazon EventBridge (line 40), for CM-API-008.
- **Logs:** its filters, among them Cart/checkout token (`017.html.txt`, line 36).
- **Stores:** each row's Type, Plan and Organization, with Log in and Delete store (`021.html.txt`, line 36), for CM-DVT-004.
- **The Home:** 'Portfolio summary' (`023.html.txt`, line 16) and the developer changelog's latest posts with 'View all developer updates' (line 37), for CM-API-006's change log.
- **Catalogs:** the catalog's fields (`raw/runs/20261007T010009Z-journey-partner-dashboard/steps/092.text.txt`): Ships from (line 32), Min rating (line 60) and Agent identity Locked, Verify to unlock (line 66), for CM-AIA-005.
- **The Request access form:** 'To protect merchants, verify your identity before requesting store access' (`091.text.txt`, line 14) and the Store URL field, for CM-STF-005 and the partner's identity verification (CM-PTN-002).
- **The checkout editor's Checkout page:** its sections Header, Main, Order summary and Footer, with Add block and Hide section (`raw/runs/20261004T111454Z-journey-theme-editor/steps/020.aria.yaml`, lines 27 to 188), for CM-CHK-003.

## The checker's lines, read again

- **CHANGES CM-DVT-004 gains core** (lines 41 and 54, Stores' second line): kept. Its page lists the dashboard's dev stores, and E151 places them so. SH-67's SH-E-6055c1ba makes the same change.
- **CHANGES CM-ONB-004 becomes held** (line 18): kept, by SH-2's N3, with the doubt above.
- **NOTE own-service on CM-CHN-002** (Shop API): Shop's maker is held (the ruling after SH-34). The cell is already `own-service`.
- **NOTEs on first leads that hold nothing:**
  - CM-OPS-004 for Order status: a lead by the word status, not its thing;
  - CM-OPS-005 for Logs and CM-APP-010 for App settings: homonyms, named in each line's `reading`.
- **NOTEs on containers:** each scope heading holds the API under it. It is placed as a scope group on its scopes' capability (R23.9), and the API takes its own line (R23.10).

## Problems with the brief or the scripts

- **Rule 4's two clauses diverge** on this picker (above): 'is `core`' against 'as the model places the same scopes'.
- **The Dev Dashboard run's text:** `20261004T174545Z-journey-dev-dashboard-app` predates `text.txt`. Its text is in `derived/step-text-from-html/`, the saved markup's text, which includes text the page didn't show. I cited those files.

## The coordinator's check

Measured: 28.8 million tokens over 123 requests, about 222,000 an entry. The checker prints no problem.
- **Kept:** R23.1 to R23.11, which SH-24 keeps (R23.9 to R23.11 for the scope picker), both `CHANGES` lines and both new things (Finance `shows`, App versions `core`, whose supports are decided with each thing).
- **The scope groups' support:** a scope group takes the support the model gives the same scopes, as placed. The model's split follows the Editions digest's rule 17: an app proxy and the Function APIs (Cart Transform, Cart and Checkout Validations) are apps' work, `extension-point`; the shipping scopes the platform's own resources, `core`. The brief's rule 4 says the same in its parenthesis, so it holds no contradiction, and SH-24 keeps it, checking `unauthenticated_write_checkouts`'s `shows` as the notes say.
- **The entries left open** (the Dev Dashboard's Apps and app pages, the popover, the account and Log out, the Shop API, Checkout Kit's buyer events, Online store theme, Post purchase): kept as placed.
