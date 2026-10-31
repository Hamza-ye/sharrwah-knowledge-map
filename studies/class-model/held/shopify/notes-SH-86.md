# Notes on SH-86 (shopify, effort high)

130 entries of four structures, read at observed-sh `e38dc17e3`:
- `partner-api-client-permissions` (2): the Create API client form's marks, at `settings/partner_api_clients/new` (run `20261007T010009Z-journey-partner-dashboard`, step 135). Its four permission sets are the concern map's (SH-I-1133 to SH-I-1136).
- `partner-dashboard-nav` (12): the Partner Dashboard's navigation before and after the business email was verified (steps 24 and 25). Home, Stores, Sales, App distribution, Catalogs, Themes, Payouts, Partner settings, Organization and Dev dashboard are the concern map's (SH-I-2085 to SH-I-2094).
- `partner-focus-options` (5): the sign-up's question “What’s your main focus as a Shopify partner?” (step 9).
- `partners-dashboard-routes` (111): the bundle label's path literals 0 to 110 (`partners.shopify.com@20261007T065956Z-published-partners-dashboard-js`). The other 12 path literals and the 128 routes of the label `@source-maps` are SH-87's and SH-88's.

Placements, by entry:
- 117 on a capability alone;
- 5 on a new thing alone;
- 1 on both (SH-E-f9bc62db, App versions and CM-APP-006);
- 7 out.

That is 144 lines: 131 on a capability, 6 new, 7 out.

## The rules this batch sets (R86), for the coordinator to check and SH-87 and SH-88 to keep

The admin router digest's rules are taken where they fit; where they don't, the rule says so.

- **R86.1: support.** Every Partner Dashboard route is the platform's own route for partners, `core` on its capability, unless a rule below says otherwise (the digest's rule 9, for partners.shopify.com).
- **R86.2: a route's words.** A bundle entry holds only a path, its bundle and its offset. Its element and module are named by its twin in the label `@source-maps` (`items.jsonl`), the same route in the same file and order, cited as "the source map, position N". The mapping is:
  - entries 20 to 45 are positions 0 to 25 (the partners app's and the dashboard's Router.tsx, Signup's Routes.tsx);
  - entries 47 to 50 are 94 to 97 (PartnerLeads);
  - entries 51 to 100 are 33 to 82 (Apps);
  - entries 101 to 104 are 101 to 104 (Payments);
  - entries 105 to 109 are 26 to 30 (Ads' route configs);
  - entries 110 to 127 are 105 to 122 (Settings).

  The element names stand where the digest's rule 2 puts a module's name, as a reading. They aren't the entry's text, so `terms` take only the path's own segments; an index (`/`) or a parameter takes none. The routes' visits are the runs `index/runs.tsv` joins to them: `20261007T070336Z-journey-partner-dashboard-routes`, `20261007T213930Z-journey-partner-dashboard-routes-from-source` and the partner run. Where this differs from the digest: the dashboard's routes have no title, resource, actionType or eligibility, so its rules 22 to 31 have nothing to read.
- **R86.3: apps managed in the Dev Dashboard.** `AppsRoutes` (the source map's `sections/Apps/routes/Routes.tsx`) renders NotFound, or goes to a Dev Dashboard address, for an app whose path `app.dev_dash_app_allowed_routes` doesn't allow. That is a condition on the partner's own app, written in `reading`. A route with its own page component keeps its own capability and support, whatever its visit landed on, as R14.1 has it. Only a route whose own element is a `Navigate` (SH-88's `sandbox_organizations/new`) would be a redirect, `shows` on its target.
- **R86.4: containers.** A section's wrapper (`/:orgId/<section>/*`, a pathless wrapper, an element over a `<Routes>`) goes on the capability its navigation title names, as the cells hold it:
  - App distribution: CM-APP-002;
  - Payouts: CM-PTN-003;
  - Partner settings: CM-PTN-002;
  - Sales: CM-PTN-008;
  - Stores: CM-DVT-003.

  Failing a title, it goes by its own words. Its children are named in `reading`. A route whose path only begins its siblings' paths, each its own `Route` in one `Routes`, keeps its own line (the digest's rule 8: "a container by its path alone keeps its own support"). This covers `/:orgId/` (Home), `/:appId/extensions`, `/:appId/versions` and `:registrationId`, which the checker notes as containers.
- **R86.5: catch-alls.** A catch-all at `*` whose element is `NotFound`, or Signup's `<div>Not Found</div>`, is `out` (R18.1).
- **R86.6: a partner's tool takes the support of what it does** (the rulings after SA-44 and SA-30). These are what the routes do, not what a partner or a store does with them.
  - `core` where the platform does the thing for the partner: its programme and dashboard (CM-PTN-001), the partner's account and team (CM-PTN-002), payouts (CM-PTN-003), billing (CM-PTN-004), referrals (CM-PTN-008), the Partner API (CM-PTN-001), the CLI (CM-DVT-002), GraphiQL (CM-DVT-001), the developer's monitoring of its own app (CM-PTN-001, as SH-23's R23.6), the App Store's registration and its ads (CM-APP-002, E86), and the charges it bills merchants for apps (CM-APP-003).
  - `extension-point` where the partner, a third party, does the thing through the platform's marketplace or interface:
    - an app's distribution on the App Store (the ruling after SA-30; SH-7's MANAGE_APP_LISTING) and by custom link (CM-APP-009);
    - its extensions (CM-APP-006), functions (CM-APP-005), carrier services (CM-SHP-004), fulfillment services (CM-SHP-011) and navigation in the admin (CM-APP-007);
    - its place in the Partner Directory (CM-PTN-005).
  - `shows` for what an app asks of the platform: the API access requests, protected customer data, and the scopes and APIs behind approval (the ruling after the dry run's S7, as SH-23's R23.4 placed the collaborator request).
- **R86.7: moves to the Dev Dashboard.** A page that says its thing moved to the Dev Dashboard keeps its own capability, the move in `reading`: CLI tokens ('CLI tokens are now managed in Dev Dashboard, where you can create and rotate tokens.', step 45), and an app's API health, insights and performance (step 115).
- **R86.8: gates.**
  - **A section gated by the partner's beta flag** (`useFlags`) whose page renders nothing for the held partner is `shows` on its line, the flag as its scope in the source's words: `FLAG_PAYMENTS_PARTNER_CERT_MGT` (PartnerCertificates). The routes inside it name the flag in `reading` and take `shows`, by the digest's rules 28 and 29.
  - **A gate on the partner's user** (`rbacPermitted`, `rbacPermittedOrLegacyOwner`, an Ads config's `canAccess` and `permission`) goes in `reading`. Examples are view_partner_financials on billing, develop_apps on Activity, and view_partner_ads and manage_partner_ads on Ads.
  - **A condition on the organization's kind** that only picks which page renders (PartnerLeads' `prmOrganization` and `prmMembership`, Referrals against PRMReferrals) is no gate, and goes in `reading`.
- **R86.9: path literals that aren't routes.** The extractor takes any `path:` literal (`capture/structure_jsroutes.py`, by the register). There are three kinds:
  - **A component's match pattern** (AppsNav's `/:orgId/apps/:appId/*`) is a container of the pages it matches.
  - **A third party's widget path** (Hyperwallet's `rest/widgets/transfer-methods`, script `hyperwallet-src`) is that party's thing: `outside`, the party its filler.
  - **A link to the platform's docs on Built for Shopify's category criteria** (`docs/apps/launch/built-for-shopify/requirements#…-apps`) takes CM-APP-002 `core;extension-point`, Built for Shopify marking third parties' apps (as SH-E-c3291129). It also takes the category's capability, `extension-point`: product bundles apps on CM-SEL-006 and subscription apps on CM-SEL-001.

  SH-87 holds the other twelve such links: discount, product reviews, returns and exchanges, invoices and receipts, fulfillment services, carrier services, affiliate program, analytics, ads, email marketing, forms and SMS marketing apps.
- **R86.10: the navigation's secondary links.** The icons beside an item (`Polaris-Navigation__SecondaryAction`, an aria_label only, `target=_blank`) take their item's line. Where the address's page is a second thing, they also take its line (the ruling after SA-19): the Dev Dashboard's Stores, whose Dev stores give CM-DVT-004 (R23.5).
- **R86.11: the navigation before verification.** It holds items the later navigation drops: Shopify POS, Partner docs, Product docs, Support, Team and Settings. After verification their addresses land on the Home (`pos_dashboard`, both docs, `support`), on the Dev Dashboard's Stores (`stores`), or on the admin organization's Users (`memberships`), as run `20261007T022232Z-journey-partner-dashboard-earlier-nav` shows. Each item is placed by its title. A landing on another capability's page through a redirect takes `shows` on the target: Team on CM-STF-001, and `memberships/*` by R14.4.
- **R86.12: the sign-up's focus options.**
  - Each option is a value of a field of the partner organization that the platform's own sign-up asks, 'to recommend resources, training, and more': CM-PTN-002 `core`. This follows WooCommerce's onboarding profile fields (WC-E-30807e24).
  - Each also takes a line on the work it names. It is `extension-point` where that cell holds third parties doing the work through the platform:
    - Build apps: CM-APP-001;
    - Build themes for the Shopify theme store: CM-SFR-003;
    - Provide services for existing businesses: CM-PTN-005.

    Otherwise it is `shows`: Build new Shopify stores for clients, on CM-DVT-003. Making it `extension-point` would have changed CM-DVT-003's cell on a reading the option doesn't state.
  - Other is `out`.

## New things

- **`new:Bug Bounty`** (SH-E-2a714fdd, `/:orgId/bugbounty`):
  - **What it is:** 'Bug Bounty', 'Find vulnerabilities. Get paid.', “Shopify’s Bug Bounty program is our way to reward security researchers for finding serious security vulnerabilities in our core application.”, with 'Report Vulnerabilities' (`20261007T070336Z-journey-partner-dashboard-routes/steps/001.text.txt`).
  - **Place of its own:** the Partner Dashboard's route `/:orgId/bugbounty`, element Bugbounty, in the route manifest its bundles declare.
  - **Proposed:** domain F, area PTN, parent CM-PTN-001, a programme the platform offers in the partner's dashboard. Domain A, area TRU, is the other reading, by its subject, the platform's own security.
  - **Name:** in English only, as the dashboard isn't held in Arabic.
  - **Searched:** caps --terms bug bounty; bugbounty; vulnerab; security researcher; HackerOne; responsible disclosure; security program. `search` and the held lines found nothing.
- **`new:Sandbox organizations`** (SH-E-6d4760a8, `/:organizationId/sandbox_organizations/*`):
  - **Its routes:** SandboxOrganizations, over an index and a creation page. Its `/new` sends a user with RBAC permissions back to the index (source-map positions 125 to 127, SH-88's).
  - **What it is:** organizations a partner creates as sandboxes, a reading of the modules' names. Both pages answer “The page you’re looking for could not be found” for the held partner (routes run, step 11; from-source run, step 5).
  - **Place of its own:** the route.
  - **Proposed:** domain F, area DVT, parent CM-DVT-003. Its leads CM-ACC-003 and CM-PTN-002 (by the word organization) hold an owner's several stores and the partner's own organization, not sandboxes; CM-DVT-004 holds free stores, not organizations.
  - **Searched:** sandbox; test organization; sandbox organization.
  - **What would settle it:** the page as a partner sees it where it renders.
- **`new:App versions`** (SH-E-09978ff2, SH-E-8ae46c23, SH-E-5d4e4055, SH-E-f9bc62db): the new thing SH-53 named and SH-23 placed for the Dev Dashboard's Versions (R23.6). Here its places are the routes `/:appId/versions`, `/versions/new` and `/versions/:appVersionId`, and an extension as a version holds it. All are `core`. SH-E-f9bc62db also takes CM-APP-006. It isn't CM-API-006, the platform's API versions, a homonym.

## The `CHANGES` lines, read again

- **CM-PTN-008 becomes held, `core`** (SH-E-d1dc0a27 `affiliate_program`; SH-E-ef912e56 `partner_leads/*` and its routes SH-E-2d959f95, SH-E-de2e8023, SH-E-bf18e7d4, SH-E-87454564).
  - The Leads page states 'Earn revenue by referring merchants to Shopify.': a one-time referral for an eligible Plus lead, a share of the merchant's monthly base platform fee and GMV, a POS Pro activation bonus, and B2B payments profit-share (step 30).
  - The Affiliate page states 'get rewarded for each qualified merchant you refer' (routes run, step 2).
  - This is the referral programme for the platform's plans and products. SH-7's VIEW_PARTNER_REFERRALS line is the same reading.
  - Kept.
- **CM-DVT-004 gains `core`** (SH-E-3a270daa, SH-E-fd879f29, second lines). The Dev Dashboard's Stores lists the organization's stores, with 'Create store' and a store of Type 'Dev' (step 87). The run made a Dev store from it (steps 64 to 71). This is SH-23's R23.5 and E151. Kept.
- **CM-APP-006 gains `extension-point`** (SH-E-3ace2bc5, SH-E-fc95e457, SH-E-764141b4, SH-E-5bbabef1, SH-E-44d56f2c, SH-E-f82673dc, SH-E-f9bc62db).
  - These are the app's extensions, which its developer builds on the platform's targets.
  - The routes name no surface. The extension types the dashboard manages include the admin's app_link and bulk_action (`DASHBOARD_EDIT_DISABLED_SPECIFICATIONS`).
  - The concern map places the help centre's App extensions and functions on CM-APP-006, the parent of CM-APP-007 and CM-APP-008, so the lines go there.
  - Kept. CM-APP-008 is the narrower reading for the admin's link and action types.
- **CM-APP-009 gains `extension-point`** (SH-E-c6f6bd00, second line). The app's distribution page offers 'Custom distribution', 'Generate custom install links for one store or one Plus organization.' (step 111). CM-APP-002's note leaves custom distribution to CM-APP-009. This is a partner's app made for one merchant through the platform's custom distribution. Kept.
- **CM-PTN-003 gains `outside`** (SH-E-845dd391, Hyperwallet's widget path).
  - The bundle's code at the offset loads Hyperwallet's transfer-methods widget (`HWWidgets.transferMethods`, script `hyperwallet-src`, v2_4_8) as the payout method's form.
  - The page states 'Payouts are handled by our third-party provider, Hyperwallet.' (step 42).
  - This is a third party behind the platform's own payouts, as Global-e is behind Managed Markets (the corrections after SH-41).
  - Kept, but `out` is the other reading, as the path isn't a route of the dashboard. The routes `/hyperwallet` and `/hyperwallet/verification` are `core` with Hyperwallet as filler (M-4: 'our third-party provider').

## Entries I couldn't tell, and what would settle each

- **Partner docs, Product docs and Support** (SH-E-28230e9b, SH-E-5c76987f, SH-E-2e56ce20, and the routes SH-E-c7982a76, SH-E-492b5eab, SH-E-5a476b92).
  - Their content isn't held: after verification each address lands on the Home.
  - They are placed by title: Partner docs and Support on CM-PTN-001, the programme's own docs and support for partners; Product docs on CM-ONB-003, the platform's help for its products.
  - CM-DVT-001 is the other reading for both docs.
  - The bootstrap's code names a Guide component for both, and a Partner Program Guide PDF (`partnerProgramGuidePdfPath`), not traced.
  - A partner page held before verification would settle them.
- **Shopify POS** (SH-E-33739a82; route SH-E-c13a76bf).
  - The section renders `pos-dashboard`, whose content isn't held, and the item is gone after verification.
  - It is `shows` on CM-POS-001, naming the topic.
  - The Leads page's Shopify POS lead (a POS Pro activation bonus) suggests a partner's POS referrals (CM-PTN-008), a reading not taken.
  - The page itself would settle it.
- **Activity** (SH-E-a9bc30c5).
  - Its element is AdsActivity, with the module activity-log, to a user with develop_apps; its page reads 'Activity is not available. Currently, not all events are tracked.'
  - It is placed CM-PTN-001 `core`, a part of the developer's dashboard, as SH-23 placed an app's Logs.
  - CM-TRU-003 is the store admin's audit log. CM-APP-002 would be the reading if it is the ads' activity, by the element's name.
- **App history** (SH-E-783322a3): placed CM-PTN-001. CM-APP-004 is the reading if it lists the app's lifecycle events in stores, which its cell holds through the Partner API's App events.
- **App audit** (SH-E-428625b9).
  - Its page shows 'Submitted requests', none found.
  - It is placed `shows` on CM-API-003, as the app's requests, which Shopify may audit.
  - CM-APP-002 (the App Store's review) and CM-TRU-003 (by the word audit) are the other readings.
  - A page with a submitted request would settle it.
- **Partner certificates** (SH-E-71776093 and its three routes).
  - They are CM-PAY-011 by the flag's name `FLAG_PAYMENTS_PARTNER_CERT_MGT`, a payments partner's certificates.
  - The payment processing request's 'certificate of compliance' for PCI (routes run, step 40) may be the same certificate, which would make it CM-TRU-018's partner side.
  - A partner with the flag would settle it.
- **Payment processing** (SH-E-bb0bc66b): placed CM-PAY-011 `shows`, a sales channel app processing card payments itself through the Checkout API. CM-CHN-001 (the sales channel) is the other thing its page names, not its path.
- **The API client's Name** (SH-E-3899cb42).
  - It is `shows`, as the structure's permission sets are, after the checker's note that the dry run's S7 makes this structure's lines `shows`.
  - The route that holds the form, `partner_api_clients/new` (SH-E-c61e4ac3), is `core`, the platform's own page for its Partner API.
  - The coordinator may prefer the field `core` with its page.

## What the structures and their sources disagree on

- **Path literals that aren't routes.** The bundle label holds path literals that aren't route definitions (R86.9): SH-E-04b4a3d8, AppsNav's match pattern; SH-E-845dd391, Hyperwallet's widget path; SH-E-e0f235d8 and SH-E-b1a17e2b, doc links, with twelve more in SH-87. The structure's shape reads "path literals of route definitions".
- **The navigation's group headings.** `partner-dashboard-nav` holds links and buttons only, so the groups Resources (Partner docs, Product docs, Support) and Admin aren't items: Payouts, Team and Settings before verification; Payouts, Partner settings, Organization and Dev dashboard after it. Both are in `source.html`. They are groups the items only sit under, and give them no line. A container line for Admin would go on CM-PTN-002 (the partner's account), and Resources on CM-PTN-001.
- **The checker's container note on line 9.** It ties the earlier navigation's Stores to the later navigation's secondary link by the name Stores. The link's parent is the later navigation's item Stores (SH-I-2086), so the note is set aside.
- **A visit that missed its route.** The routes run opened `/pending-invitations` without the prefix `/signup` (step 16), so that visit says nothing of `/signup/pending-invitations`.

## What a source or run step states that no entry holds (for the second stage)

- **CM-PTN-008's terms and rates**, on the Leads page (`20261007T010009Z-journey-partner-dashboard/steps/030.text.txt`):
  - Plus: 'Earn $2,500 USD one-time referral when you submit an eligible Plus lead', and 20% of the base platform fee plus 0.1% of eligible online GMV for 4 years;
  - POS: a POS Pro activation bonus and 20% Shopify POS payments profit-share for 4 years;
  - Plus B2B: 20% of B2B Payments profit for 4 years.

  The Referrals page (step 31) adds Enterprise. The Home (step 25) shows 'Registered Partner' and its program guide's tiers. The Affiliate Program is 'managed through Impact Radius' (routes run, step 2), a third party for the second stage.
- **App Store registration** (step 41): '0% revenue sharing (15% on additional sales over $1 million USD annually)' and 'One-time app store registration fee: $19'. These are qualities for CM-APP-002 and CM-APP-003. The CM-PTN-003 cell holds the revenue share already.
- **What partners are billed for** (step 43): registering and running ads; 'Ads are billed on a 30-day cycle, or when you hit your $100.00 USD billing threshold.'; a $100 ad credit once a card is added. This fills CM-PTN-004's stated gap.
- **App Store ads** (routes run, step 5): placements in search results, on the homepage and on category pages, device targeting and geotargeting, for CM-APP-002.
  - SH-7 placed the role permissions MANAGE_PARTNER_ADS and VIEW_PARTNER_ADS on `new:Partner ads` (`shows`, no place of its own).
  - This batch's Ads routes give partner ads a place of their own. I placed them on CM-APP-002 `core` by E86, the Editions digest's rule for developers' App Store ads.
  - The coordinator may fold `new:Partner ads` into CM-APP-002.
- **The access requests' conditions** (routes run, steps 33 to 40):
  - the Advanced DOM Events API in checkout 'limited to stores on Shopify Plus plans or above' (CM-MKT-009);
  - post-purchase extensions 'in beta and can be used freely with dev stores' (CM-CHK-004);
  - Chat UI 'Limited to public apps';
  - payment processing 'limited to PCI-compliant businesses only', through 'a payment service such as Stripe or Spreedly' or a certificate of compliance (CM-TRU-018, CM-PAY-011).
- **Protected customer data** (step 117): Shopify's review after the App Store Listing is submitted, and the data and fields an app selects (CM-API-004).
- **The partner's identity check**, a lead for CM-PTN-002, whose reading says identity verification isn't found for the partner:
  - the Dev Dashboard's catalog 'Agent identity Locked, Verify to unlock' and the identity check 'with Stripe', a photo ID and a selfie (steps 94 to 98);
  - 'verify your identity before requesting store access' (step 91);
  - the organization's Roles, 12, with Collaborator access in the category Partner (step 151).
- **The sign-up's other questions** (steps 12 and 13): the business location, with Yemen preselected and Region disabled (CM-ONB-001's partner side), and the business contact form. It reads 'This is how your business will appear to Shopify merchants.' and asks for agreement to the Partner Program Agreement (CM-PTN-001).
- **The embedded app navigation's retirement** (step 112): 'You can delete existing menus here until December 2024. After December 2026, they will be completely removed.' (CM-APP-007).

## Problems with the brief or the scripts

- **`show --code` prints nothing for this structure**, since its bundle items are only paths. The elements come from the other label's source maps (R86.2), and the code at each offset from the bundles. I read the bundles from their archive records with a reader of my own in my scratchpad, as `method/warc_text.py` failed on the PartnerLeads bundle: `gzip.decompress` raised on both its records, `20261007T065956Z-published-partners-dashboard-js/fetch.warc.gz@892444` and `20261007T205317Z-published-partners-dashboard-sections/fetch.warc.gz@620785`. Its output also starts with the record's HTTP headers, so offsets into it are shifted.
- **`earlier` matches bare paths** (`/new`, `/:id`, `/bills`, `/:payoutId`, `/:appId/overview`) to the admin's routes, another app's. The readings say so where they matched.
- **The checker's container note fires on sibling routes** whose paths begin others' (R86.4). The digest's rule 8 counts these as containers by their path alone, keeping their own lines.
- **No notes file is held for SH-23**, whose placements this batch follows (R23.4 to R23.8): `held/shopify/notes-SH-23.md` isn't in the tree.
