# SH-12: Shopify's admin router, 86 entries of CustomerAccounts, CustomerEvents, Customers, Discounts, Domains, EmptyTest, Extensibility and Finances (notes)

**What this batch is.** The fifth held-pass batch on `admin-router`, after SH-8 to SH-11. Its 86 entries are the manifest's items at lines 500 to 613 of `structures/shopify/admin-router/items.jsonl` (observed-sh at `e38dc17e3`), less the routes the concern map already cites. Those include `customerAccountsSettings:parent` (SH-S-5136), `customerAuthenticationSettings:parent`, `identityProviders:auth`, `customer-events-settings:pixel` (SH-S-5138), `customer`, `customer:create`, `customer:bulk-edit`, `customer-segments`, `customer:merge`, the store credit routes, `customer-subscriptions:show`, `customer-payment-methods:show`, `customer:mobile:edit-marketing-status`, `discounts:root` (SH-S-5150, SH-S-5151), `domains:inactive` (SH-S-5152), `domains:inactive:transfer:prepare_for_transfer` (SH-S-5154), `domains:root` (SH-S-5155), `domains:buy` (SH-S-5156), `email:create`, `emptyPage:parent`, `extensions-dev:parent`, `money` (SH-S-5158), `finance` and `finance:dashboard` (the Help Center's links, SH-S-6331 and others), `finance:risk` (SH-S-5163), `finance:risk:disputes` and `finance:payout-reconciliation-report` (SH-S-5165, SH-S-7103).

- **Entries:** 86. By placement, counting each entry once: 80 on capabilities only, 2 on a capability and a new thing, 2 on a new thing only, 2 `out`.
- **Lines:** 101, since 12 entries take two lines or more (`customerAccountsSettings` takes seven). By support, counting each entry of a line: 77 `core`, 12 `shows`, 7 `core;extension-point`, 2 `extension-point`, 1 `core;own-service`, 2 `out`.
- **The checker's last run:** no problem. Three cells change (section 4). Three new names (section 3).
- **`held_entries.py earlier`** printed no earlier line for any key of the batch.
- **Ancestors' gates** aren't looked up, as the coordinator asked. A route's own store gates are its `scope`: `sellsOnShopifyPlatforms` and `customDomains` on the Domains routes, `financesOverview and beta 747a1ad6` on Finance's risk lists and rules. Gates on the user are named in `reading`. The Gift cards anchor's own gate is its line's scope (C1). The coordinator's script names the ancestors' gates, such as `customerAccountsSettings:parent`'s customers.accountSettingsAccess, `customer-events-settings:pixel`'s storefront.enabled, `customer-segments`' customerSegmentation, `discounts:root`'s discountCodes, `domains:root`'s and `domains:inactive`'s, and `money`'s beta 8c7faba1 with financesOverview.

**What I read:**
- the brief, SH-8's, SH-9's, SH-10's and SH-11's notes with the coordinator's checks (SH-11's was added while I worked; it changes none of these lines), and `review-H-rulings.md`;
- B-extent.md's "Cells and evidence" and "Conventions from the dry run", the evidence map, and `held/selection.tsv`'s router rows;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv`'s router, betas and titles rows, `index/ledger-summary.tsv` and `index/ledger/admin-route.tsv`;
- the structure's `meta.json` and `items.jsonl`, lines 499 to 614, with each item's modules and intent (which `show` leaves out). I also read `source.jsonl` for `discounts:details:create`;
- `structures/shopify/admin-betas/` for both held stores, and `derived/intents.tsv`;
- the run steps the ledger joins to the routes:
  - `derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/` steps 210, 211, 220, 226, 230, 234, 240 to 252, 255 to 257, 259 and 260;
  - `derived/step-text-from-html/20261004T092454Z-sweep-instances/` steps 019 and 024;
  - `raw/runs/20261007T215203Z-journey-admin-router-new-routes/` step 6;
- the concern map's router statements for these sections (`studies/concern-map/platforms/shopify/statements.tsv`; `class_slice.py key` and `search`), and its review log's lines on `money`;
- the cells of CM-CUS-001, CM-CUS-002, CM-CUS-004, CM-CUS-010, CM-CUS-011, CM-MKT-009, CM-CNT-002, CM-LOY-001, CM-LOY-002, CM-RET-003, CM-PAY-022, CM-PAY-014, CM-SEL-001 and CM-B2B-002;
- the cells of CM-SRF-001, CM-SFR-008, CM-SFR-009, CM-PAY-005, CM-PAY-023, CM-PAY-024, CM-PLN-005, CM-MKT-001 to CM-MKT-004, CM-MKT-007, CM-NTF-004, CM-SHP-001, CM-ORD-006, CM-ANL-003, CM-APP-006 to CM-APP-009, CM-DVT-001 and CM-DVT-002.

## 1. Lines by capability

- **Customer accounts:** CM-CUS-010 (the settings page, with its anchors Customer accounts, Login links and Customer account URLs, and Sign in with Shop as `own-service`; the Authentication page) and CM-CUS-011 (Multipass, Authentication, a provider's connection, the identity provider routes). The page's other anchors go on their own capabilities: Self-serve returns (CM-RET-003), Saved payment methods (CM-PAY-022), Gift cards (CM-LOY-002, `shows`), Store credit (CM-LOY-001) and Subscription management (CM-SEL-001).
- **Customer events:** CM-MKT-009, the app pixel's details as `extension-point` (SH-S-5028) and the legacy redirect as `shows`.
- **Customers:** CM-CUS-001 (the list, and the customer's page as `core;extension-point` for its documented intent), CM-CUS-002 (segments and segment templates), CM-CNT-002 (the five metafield routes, the app-controlled one `core;extension-point`), CM-B2B-002 (a customer's company locations), CM-CUS-004 (the merge redirect, `shows`), and `new:Email customer` with CM-SRF-001.
- **Discounts:** CM-MKT-001 (the list, the container, the discount's page and the creation routes, five with documented intents), CM-MKT-002 (a discount's codes) and CM-MKT-004 (an app's discount).
- **Domains:** CM-SFR-008 (27 routes), CM-SFR-009 (the two DNS Settings routes and the automatic set-up's return), and CM-PLN-005 (the domain's payment authentication).
- **EmptyTest:** both `out`.
- **Extensibility:** CM-APP-006 (the extension preview routes and the admin's hosts for apps' UI), CM-DVT-002 (the CLI's preview page), CM-SRF-001 (the mobile preview), and `new:Data Sharing Preferences`.
- **Finances:** `new:Finance` (Money and a finance transaction), CM-ORD-006 (risk lists and rules, `shows`), CM-PAY-005 and CM-PAY-024 (two loader-only redirects, `shows`).

## 2. Rules I followed for kinds of route the rules don't cover

These are for the coordinator to align with SH-13 to SH-18. Each is a reading.

- **C1. An anchor with its own eligibility** takes its own line, with its own gate as its scope (the ruling after SH-69), and its own beta decides its support. The anchor Gift cards of `customerAccountsSettings` (`gift_card_visibility`) carries `betas [94a07d98]`, `entitlements [giftCards.enabled]` and `permissions [GIFT_CARDS]`. The beta is false in both held stores, so the line is `shows` on CM-LOY-002, scope `beta 94a07d98 and giftCards.enabled`. The route's other lines keep their empty scope.
- **C2. An intent with its own eligibility.** `discounts:details:create`'s intent `create shopify/Discount`, which the Intents API documents, carries `eligibility: {excluded: {betas: [6645261e]}}`. The beta is true in both held stores, so the intent isn't offered there. I wrote a second line on CM-MKT-001 under the intent's condition: `shows`, scope `not beta 6645261e`, written as SH-8's 2.5 writes an exclusion. The route's own line stays `core`. The typed creation routes carry the same intent with no exclusion, and are `core;extension-point`. No cell changes either way.
- **C3. A loader named for a redirect beside a page's component.** `discounts:details:create` loads `redirect-loader` and renders `DiscountDetails`, the discount form, with a form and an action. I kept it `core`, not redirect-only, its reading naming the loader.
  - SH-8's 2.4 lists `redirect.loader` among names that make a route redirect-only. The routes it was read from have no component: `balance:inactive:redirect-statements`, `shopify-balance:onboard-redirect` and `credit:account:index`.
  - SH-10's `checkout-settings:theme-content` had both its loader and its component named for a redirect.
  - Later batches hold more routes with a redirect loader and a page's component: `growth:automations`, `growth:automation-summary:flow`, `marketing` and `marketing:automations` (items 648 to 730). The coordinator may align them.
- **C4. Native-only routes.** A route for the native client whose own id or path names mobile takes a CM-SRF-001 line, as that cell's three routes do. `mobile-email-customer:show` is the case, as the cell's `customer:mobile:edit-marketing-status` is.
  - A native-only route whose words don't name mobile names its client in `reading` only (SH-8, 2.5): `customer-company-locations:show`, the App Bridge modal and `extensibility/intents`. The module's name (`MobileCompanyLocations`, `MobileIntents`) isn't the route's words, since 2.3 reads a module's name only for an untitled route with no words of its own.
  - `extensions-dev:mobile` is a web route. Its path names mobile and its page offers 'Open in Shopify Mobile' (capture-advanced step 243), so it takes the line too.
- **C5. A title that names a redirect on a page with content of its own.** `domains:automatic-redirect`, 'Automatic redirect' (component `AutomaticRedirect`), shows 'Successfully updated DNS records' and 'Your domain is now connected to Shopify.' (capture-advanced step 234). It is the return from the domain provider's automatic set-up, not a router redirect, so it is `core`. I placed it on CM-SFR-008 and, by its page (SH-11's B3), on CM-SFR-009.
- **C6. The admin's hosts for apps' UI.** The section Extensibility's pickers, extension host, intents host and legacy host, and the `extensions-dev` preview routes, are the admin's own routes, named for apps' UI in general. I placed them `core` on CM-APP-006, as SH-8's 2.4 places the admin's pages for apps in general. Each reading rests on the path and the module's name, since nothing rendered on any visit.
  - The `extensions-dev` page reads 'Run shopify app dev and click on the preview url.' (capture-advanced step 242), so it takes CM-DVT-002 too.
  - An extension previewed there may be a checkout, customer account or POS extension, whose capabilities are those surfaces' (CM-APP-006's note). The page doesn't say which.
- **C7. An app's discount.** `discounts:details:create:app` (`new/app`, 'Create discount') takes `extension-point` on CM-MKT-004, whose cell holds only `extension-point`, as SH-10's A3 places the checkout rules. It also takes `core` on CM-MKT-001 for the admin's discount form.
- **C8. A test page.** `emptyPage`, 'Empty Page Test Section', has a title and a path. Its own title names a test, and its page shows only that heading (capture-advanced step 240). I placed it `out` as a scaffold the code holds for no place (rule 2). `cached-web-view` is `out` by SH-8's 2.9.
- **C9. A list or detail page with modal children** is a container by its children (the checker's note). I kept it on its own capability and named its modals in `reading`: `domains:list`, `domains:inactive:list`, `domains:edit`, `domains:inactive:edit` and `domains:renew`.
- **C10. A payment authentication titled for another capability's thing.** `domains:complete_payment_authentication`, 'Domain Payment Authentication', takes CM-SFR-008 for the domain its title names. It takes CM-PLN-005 for completing the payment authentication, as SH-9's rule 6 places the charge approval's authentication step. Both lines take the route's own scope.

## 3. The new things

- **`new:Email customer`** (SH-E-b3247925, `mobile-email-customer:show`).
  - **What it is:** staff emailing a customer from the customer's page. It is a modal at `customers/:id/mobile_email_customer`, for the native client only, and loads the customer page's loader.
  - **Its place of its own:** this admin route, a modal with its own path. The Orders section holds the same thing, `order:mobile:email-customer` (named in SH-S-5145's note), in a later batch, for the coordinator to align.
  - **Proposed:** domain D, area CUS, parent CM-CUS-001. Another reading puts it under CM-NTF-001, beside CM-NTF-004.
  - **Its name:** the platform's id, in English only, since the admin isn't held in Arabic (`docs/GAPS.md`).
  - **Terms searched:** 'email customer; contact customer; customer email; send email; mobile admin; merchant mobile app; email; contact; message customer; communication; inbox; chat; conversation; write to customer'. They found campaigns (CM-MKT-007), automatic notifications and their delivery (CM-NTF-001, CM-NTF-004, whose Shopify side is the SMS sender ID), chat (CM-SUP-004) and consent (CM-CUS-007). None of them is a staff member writing to one customer.
- **`new:Data Sharing Preferences`** (SH-E-45c78bb1, `extensibility/app-bridge-data-sharing-preference-modal`).
  - **What it is:** a modal of App Bridge, for the native client only, titled Data Sharing Preferences. What is shared, and with whom, isn't stated, and the web sweeps answered “There's no page at this address”.
  - **Its place of its own:** the route, a modal with its own path, under the container Extensibility.
  - **Proposed:** domain F, area APP, parent CM-APP-006, or CM-API-004 if it bounds an app's access to data.
  - **Its name:** English only.
  - **Terms searched:** 'data sharing; sharing preference; share data; app permissions; app access'. They found nothing. The leads by 'preferences' (CM-ACC-006, CM-API-009) match the staff permission PREFERENCES, not this.
  - The mobile app's capture would settle it (`docs/GAPS.md`: the phone).
- **`new:Finance`** (SH-E-f18a277e, `money:home`, 'Money'; SH-E-b9245d10, `finance:transaction`, 'Finance Transaction Details').
  - **Alignment:** this is SH-39's `new:Finance` (SH-E-44c35194, the changelog post on the redesigned Finance section, 'one place to view all your money products'). SH-39 isn't checked yet.
  - **Its place of its own:** the router's section Finances. Its dashboards are `money` (actionType `dashboard`, loader `FinancesMoneyHome-loader`) and `finance:dashboard`, titled Finance, which the Help Center links as Finance (SH-S-6331 and others).
  - **Proposed:** domain C, area PAY, no parent: a container over CM-PAY-005 and CM-PAY-023 to CM-PAY-027.
  - **What every held visit showed:** 'Money' answered “There's no page at this address”. `money`'s gate is beta 8c7faba1, false in both held stores, with the feature financesOverview. The finance transaction needs an instance, and no run opened it.
  - **Another reading:** CM-PAY-023's reading cites the help's 'The finance suite is built into your Shopify admin' (SH-S-0454) as the money account's evidence. The coordinator may read the Finance section as CM-PAY-023's place. SH-39's line and these two would then move together.
  - **Terms searched:** 'finance; money; financial; finances overview; risk; fraud; wallet'. They found each money product's own capability, and the analytics overview (CM-ANL-003), which is the store's performance, not its money.

## 4. The `CHANGES` lines

- **CM-CUS-001@shopify gains `extension-point`** (line 21, SH-E-76ea82b5, `customer:show`, 'Customer Details'). Its intent `edit shopify/Customer`, release `public`, has Intents API pages (`derived/intents.tsv`: `admin-extensions`, `app-home` and `app-home-ui-extension`, in each page's Customer table). Kept, by the ruling after SH-8, as the coordinator kept SH-10's catalog and collection intents: an app opens the admin's own customer page.
- **CM-CUS-010@shopify gains `own-service`** (line 2, SH-E-0671696f, the anchor Sign in with Shop). Kept. Shop's things are `own-service` (the ruling after SH-34), and SH-34, SH-35, SH-37, SH-39, SH-50 and SH-51 placed Sign in with Shop or Shop's one-tap sign-in on CM-CUS-010 so. The cell doesn't hold them yet because those batches aren't amended.
- **CM-SFR-009@shopify becomes held, with `core`** (lines 54 and 73: `domains:inactive:dns` and `domains:dns`, 'DNS Settings'; line 65: `domains:automatic-redirect`). A reading. CM-SFR-009 is the DNS records of the store's domain, managed from the platform. Salla's name for it is إدارة إعدادات DNS, DNS settings management. The cell's reading says no Shopify statement defines DNS management. These routes are Shopify's admin routes of their own, titled DNS Settings, for one domain (`domains/:id/dns`, module `DomainEditDns`). Kept, with two cautions:
  - no run opened a DNS Settings page (needs an instance), so which records the merchant can edit isn't held. The domain page's capture shows only 'Domain target and type' (`derived/step-text-from-html/20261004T092454Z-sweep-instances/024.html.txt`, line 134);
  - line 65 rests on the automatic set-up's page, 'Successfully updated DNS records' (C5). There the domain provider updates the records, and the platform asks for it and shows the result. If the coordinator reads that as the provider's work, line 65 goes, and lines 54 and 73 still make the cell held.

## 5. Entries I couldn't tell, and what would settle each

- **Saved payment methods** (anchor of `customerAccountsSettings`): CM-PAY-022 by the words, payment methods kept for a customer. CM-PAY-014, saved checkout details, is the other reading. No held page shows the section: capture-advanced's, capture-plus's and capture-grow's pages at `settings/customer_accounts` lack it. A capture of a store with Shopify Payments would settle it.
- **Authentication's CM-CUS-010 line** (SH-E-09ec7732). The page holds the buyers' sign-in options, Shop among them, beside the third-party connections (CM-CUS-011). If the coordinator reads the page as CM-CUS-011's alone, the CM-CUS-010 line goes. No cell changes either way.
- **`discounts:details:create`** (C3). A visit to `discounts/new` would settle whether its redirect loader sends the request on.
- **`finance:transaction`**: which product's transaction (`:product`). A visit with an instance would settle it, and might move it to that product's capability (CM-PAY-023, CM-PAY-005 or CM-PAY-026).
- **`money:home`'s support.** It is `core` by its own words and has no gate of its own, but no held store shows the page (section 3). Whether a route under an ancestor's beta that is false everywhere stays `core` is the coordinator's, with the ancestors' gates.
- **The Extensibility hosts** (C6) rest on the modules' names. Nothing rendered on any visit.
- **'Customer account URLs'** stays in CM-CUS-010's line. Its page offers 'Change customer accounts domain', a domain for customer accounts, which may also be CM-SFR-008's (section 7).

## 6. The checker's `NOTE` lines, answered

- **`own-service` on CM-CUS-010:** section 4.
- **The new things whose entries have leads:**
  - line 31: CM-MKT-007, CM-NTF-004, CM-API-004 and CM-CUS-007. I read their cells, and none is staff emailing a customer;
  - line 89: CM-ACC-006, CM-API-009 and CM-CHK-004, which match by 'preferences' and 'extensibility' only;
  - lines 94 and 95: CM-ANL-003, CM-PAY-005, CM-PTN-001 and CM-PTN-003. Their cells are other things (section 3).
- **Containers:**
  - `discounts:details`, `domains:inactive:edit:parent`, `domains:edit:parent` and `extensibility:parent` name their children;
  - the list and detail pages with modal children name them too (C9);
  - the other container notes (lines 13, 14, 21, 23, 24, 26, 37, 48 and 57) compare relative paths across sections, as SH-9 to SH-11 found, and are set aside.

## 7. Item text that reads as instructions

The intents of seven routes carry two tools, `updateForm` ('Update forms on the page with the given data') and `getFormValues` ('Get the values of the forms on the page'). They are `customer-segment:create` and `customer-segment:update`, `discounts:details:show`, `discounts:details:create` and the four typed creation routes (`items.jsonl`, lines 521, 522, 541 and 543 to 547; also `customer:create`, line 516, outside the batch).

`discounts:details:show`'s intent (line 541) also tells its reader how to write an identifier: 'Accepts a bare ID (treated as the canonical gid://shopify/DiscountNode/{id}) or a discount GID. Use gid://shopify/DiscountNode/{id} as the canonical value; for a method-specific GID, match it to the discount method'.

These describe tools for an agent that fills the admin's forms, as SH-10 and SH-11 found. I read them as the routes' data and followed none of them. They are a lead for the admin's own AI assistant on these pages.

## 8. What sources state that no entry holds, for the second stage

These are not placed (M-12).

- **The Customer accounts page** (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/210.html.txt`):
  - lines 145 and 146: 'Self-serve returns and cancellations', 'Set conditions and fees with return and cancellation rules'. The anchor's title names returns only; the page adds the buyer's self-serve cancellation, a lead for the orders' cancellation;
  - line 98: 'account.myshopify.com will become the primary domain for customer accounts, including the Order status page.' A lead for CM-SFR-008 and CM-CUS-010;
  - line 102: 'Legacy customer accounts are no longer maintained or updated. Customers will lose access to these features: Passwordless sign-in', with 'No-code customizations with apps Store credit Self-serve returns'. A lead for CM-CUS-014, apps' customer account UI, and for CM-RET-003's and CM-LOY-001's condition, which CM-LOY-001's cell already states for store credit;
  - line 140: 'Configure apps, branding, and features for checkout and customer accounts'.
- **The Authentication page** (`…/211.html.txt`, lines 120 to 123): 'Sign-in options' with Shop, and 'Available connections' Google and Facebook. Google's connection page reads 'Sign in with Google', set up 'In the Google Cloud Console' with a client ID and secret (`derived/step-text-from-html/20261004T092454Z-sweep-instances/019.html.txt`, lines 119 and 124). Leads for CM-CUS-011's fillers, Google and Facebook, which the routes' own words don't name.
- **Segment templates** (`…/220.html.txt`, lines 124 and on): Shopify's own templates, grouped 'Target email behavior' and 'Target storefront behaviors'.
- **The domains page** (`…/230.html.txt`, line 92): 'This development store uses a developer preview and can't be transferred to a new account owner. Domains purchased for this store can be transferred to a new store from the Domains page.' A lead for CM-SFR-008, a domain moved between stores.
- **The automatic set-up's page** (`…/234.html.txt`, line 122): the merchant is asked to press 'Verify DNS Records' after the connection.
- **Discount types in the intents** (`items.jsonl`, lines 541 and 544 to 547), which the selection drops from the entries:
  - 'Amount off products', 'Discount specific products or collections of products';
  - 'Amount off order', 'Discount the total order amount';
  - 'Buy X get Y';
  - 'Free shipping', 'Offer free shipping on an order';
  - and 'gid://shopify/DiscountAutomaticNode/{id} for automatic discounts'. A lead for CM-MKT-003, automatic discounts, whose Shopify cell holds nothing.
- **A later router version gates `money` by region:** the repository's own journey intent reads 'Route changed: money (Finances overview), its eligibility now adds regions [US]' (`raw/runs/20261007T215203Z-journey-admin-router-new-routes/actions.jsonl`, step 6). These are the repository's words, not the platform's. A lead for SH-19 (`admin-router-changes`).
- **For the amendment:** CM-SFR-009's note says 'Shopify's statements hold nothing under the terms searched'. These routes are such statements (section 4).

## 9. Homonyms

- **'subscription'** in a domain's Manage subscription and `domains/subscriptions/:id` is the domain's renewal. It isn't the store's plan (CM-PLN-001) or a buyer's subscription (CM-SEL-001). Subscription management in customer accounts is the buyer's (CM-SEL-001).
- **'permissions'** in Manage permissions (`customer-company-locations:show`) is a B2B customer's permissions at company locations, not staff permissions (CM-STF-002).
- **'Authentication'** is buyers' sign-in. It isn't the admin's sign-in security (CM-TRU-001, a lead by name) or app authorization (CM-API-002).
- **'redirect'** in Automatic redirect is the domain provider's return. It isn't a router redirect or the storefront's URL redirects (CM-CNT-009).
- **'checkout'** in `domains:checkout` and `plan-checkout-return` is paying for a domain or a plan, not the store's checkout (CM-CHK-001).
- **'Lists' and 'rules'** in Finance's risk are risk lists and rules (CM-ORD-006), not segments or checkout rules (CM-CHK-005).
- **'wallet'** in `addToWallet` is a card added to a digital wallet, not buyers' wallets (CM-PAY-012) or store credit (CM-LOY-001).
- **'extension'** in Extensibility is an app's UI extension, not BigCommerce's Extensions (M-2) or the platform's own apps (CM-APP-011, a lead by name).
- **'transaction'** in `finance:transaction` is a money product's, not a partner's payout (CM-PTN-003).
- **'Money' and 'dashboard'** aren't payouts (CM-PAY-005) or the analytics overview (CM-ANL-003).
- **'preferences'** in Data Sharing Preferences isn't the staff permission PREFERENCES.
- **'Gift cards'** in customer accounts is the gift card's visibility in the account (CM-LOY-002), not gifting (CM-LOY-006).
- **'free shipping'** in `discounts:details:create:free-shipping` is a discount's type (CM-MKT-001), not the store's shipping rates (CM-SHP-001, a lead by the term).

## 10. This brief, B-extent.md and the scripts

- **B-extent.md:** no rule of the brief read differently from it on these entries.
- **`show` leaves out `intent` and the modules' names,** which C2, C3, C6 and the new things rest on. I read them from `items.jsonl` at each entry's locator.
- **The checker's container test** compares relative paths, as SH-9 to SH-11 found (section 6).
- **No problem with the checker.**

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 86 of 86 entries, no problem.
- **Ancestors' gates:** 52 lines of 42 routes now name them in `reading`, by `method/held_router_gates.py`.
- **The cell changes stand, each read again:**
  - CM-SFR-009 is held, `core`, from the admin's own two DNS Settings routes. Line 65 (`domains:automatic-redirect`, 'Successfully updated DNS records') is a marked reading beside them.
  - CM-CUS-001 gains `extension-point` from the documented intent `edit shopify/Customer`, by the ruling after SH-8.
  - CM-CUS-010 gains `own-service` from Sign in with Shop, Shop's thing, as SH-34 to SH-51 placed it.
- **New things:** Email customer (the mobile app's modal), Data Sharing Preferences, and Finance, under SH-39's name, decided with the others. Finance's two readings, a new thing or CM-PAY-023's place ('The finance suite is built into your Shopify admin', SH-S-0454), go to that decision.
- **C1 to C10 stand for SH-13 to SH-18.**
- **Agent instructions inside the evidence:** several intents carry tool descriptions and GID guidance written for Shopify's own admin agent. The agent read them as data and followed none.
- **Cost:** 25.9 million tokens over 120 requests, about 301,000 an entry. The context reached about 358,000 tokens, with 63 file reads.
