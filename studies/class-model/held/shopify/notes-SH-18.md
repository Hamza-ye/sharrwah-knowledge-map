# SH-18: Shopify's admin router, its last 101 entries (notes)

**The batch:** Shopify's `admin-router` (observed-sh at `e38dc17e3`), entries 1 to 101: ShippingLabels (5), Sidekick (3), Taxes (69), TestIntent (3), Trust (1) and the 20 routes with no section, `settings-modal`, `settings`, `root` and `shopless-root` among them. Effort `high`. 113 lines: 92 entries placed on capabilities, 9 `out`, no new thing.

## 1. What I read

- **The rules:** the brief, the router digest (`held/rules/admin-router.md`, whole), the last section of `review-H-rulings.md`, B-extent's "Cells and evidence" and conventions, the evidence map, observed-sh's guides and its ledger summary.
- **Earlier batches' notes:** only SH-8's 2.6 and 2.9, where the digest's rule 38 sends for `root`, `settings-modal` and `settings`, and a search of SH-8 to SH-16's notes for routes that answered 'no page'. The earlier lines I read, by search, are:
  - SH-2's and SH-3's navigation Settings (SH-E-46f4ba19, SH-E-cea2035f);
  - SH-12's 'Domain Payment Authentication' (SH-E-b434894e);
  - SH-15's 'Create store' (SH-E-a2f5d930);
  - SH-17's store transfer (SH-E-01cb1d60, SH-E-c735816d);
  - SH-8's catch-all redirect under Agentic (SH-E-ee658cf8).
- **Twins:** I looked up the batch's routes once, by their ids' parts and paths:
  - in the concern map's router statements: SH-S-5263 to 5265, 5267, 5269 to 5275, 7123 to 7129, 1604, 1608 and 5208;
  - in the earlier router placements.

  None of the 101 routes has an earlier line. `earlier` found only lines that cite `settings-modal`, `catch-all` or `root` as a word in another route's reading.
- **The structure's source,** for the 20 routes with no section, whose items hold computed paths only:
  - their `source.jsonl` lines (1344 to 1364);
  - the router bundle that `meta.json` names (`raw/runs/20260929T234254Z-admin-bundles/fetch.warc.gz@1171`), for their children and the path builders it defines: `createRouter`, `Ss`, `Ls`, `bs`, `ys`, `Zn` and `Gn`, `storeTransferIndex` ('accept/:token') and `downloadOrganizationResource` ('/download-organization-resource/:token').

  I traced nothing into other chunks.
- **Run steps:**
  - ts15uk-ug's sweep (`raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/`), steps 508 to 543;
  - capture-advanced's `20261004T092454Z-sweep-instances`, steps 63 and 65 (`derived/step-text-from-html/`);
  - the Sidekick journey's steps 1 and 62;
  - the shipping labels journey's step 15.

## 2. The lines, by section

- **ShippingLabels:**
  - 'Create shipping label', the purchase from an order and the purchase's payment step are CM-SHP-002 `core`;
  - the payment step also takes CM-PLN-005 `core`, as SH-12's domain payment authentication did;
  - 'File shipping claim' is CM-SHP-022 `core`, a reading (section 4);
  - the catch-all at `*` is `out`.
- **Sidekick:** its index, `code` and 'Sidekick' (`playground`) are CM-AIA-002 `core`.
  - `code`'s intent, open shopify/Artifact, is in no Intents API page (`derived/intents.tsv`).
  - Every held visit to the playground answered “There's no page at this address”. It is placed by its words, as SH-10 and SH-15 placed such routes.
- **Taxes, Automated filing** (`taxes/filing`): every route is CM-TAX-006 `core` but these:
  - the region's index, a redirect, is `shows`;
  - the catch-all is `out`.

  The gate `taxFilingEnabled` is on `tax-filing:tax-region`, an ancestor, so the coordinator's script names it. ts15uk-ug's sweep answered “There's no page at this address” at every page under `taxes/filing/US` (steps 509 to 518).
- **Taxes, settings** (`settings/taxes`):
  - **'Taxes and duties'** is CM-TAX-001 `core`, with its anchors 'Regional tax settings' and 'Global tax settings'. Its anchor 'Duties and import taxes' is CM-TAX-008 `core`, and its anchor 'Apps' is CM-TAX-004 `extension-point`.
  - **The country containers and pages** (US, EU, GB, CA, `:countryCode`) are CM-TAX-001 `core`.
  - **The registration modals,** with 'Tax liability insights' (US, CA) and the EU's cross-border registration, are CM-TAX-003 `core`.
  - **The Managed Markets modals** (GB's VAT collection, CA's tax collection) are CM-TAX-003 `core` and CM-MKS-003 `core`.
  - **The tax services:**
    - the four 'Switch tax service' pages, 'Upgrade tax service in the European Union' and the EU activation are CM-TAX-002 `core`;
    - 'Tax service' is CM-TAX-002 `core`, with CM-TAX-004 `extension-point` from the page a run opened, 'Apps', 'Connect your preferred sales tax service to Shopify.';
    - `europe-launch`, a redirect to the Taxes page with Shopify Tax's Europe promotion, is `shows` on CM-TAX-001 and CM-TAX-002.
  - **The tax partner:**
    - 'Avalara Tax Compliance' is CM-TAX-004 `extension-point` alone, Avalara its filler (the digest's rule 14);
    - its redirect is `shows`;
    - 'Set up tax provider' is `shows` under beta a142026c, false in both held stores.
  - **Duties:** the index and `duties/*` are CM-TAX-008 `core`, and the old `management/*` address is `shows`.
- **TestIntent:** its three test pages are `out` (rule 37's test page). Their intents are in no Intents API page.
- **Trust:** `identity-verification` is CM-TRU-002 `core`. Its intent, open shopify/IdentityVerification, is in no Intents API page.
- **No section:**
  - **`settings-modal` and `settings`** are CM-ACC-006 `core`, as containers, after searching the cells for the admin's Settings as a place (the digest's rule 38). SH-2 and SH-3 placed the navigation's Settings there, whose address is the route `settings`. Salla's and Zid's settings roots are on the same capability (SA-E-0bfa5b40, ZD-E-595271fa).
  - **`root`** is `out`: a container over the whole admin (the ruling after SA-21).
  - **`shopless-root`** is `out`: the router's root where the session has no store or organization, over several capabilities' pages (R16.4).
  - **The account's store list and the store picker** are CM-ACC-001 `core`, as its cell reads 'Your store' on the account's pages (SH-S-2520). The store list's fallback, a redirect to it, is `shows`.
  - **The store transfer and its acceptance** are CM-ACC-001 `core`.
  - **The organization's store creation and its resource download** are CM-ACC-003 `core`.
  - **The authentication challenge's callback** is CM-TRU-001 `core`.
  - **The two Trust challenges** are CM-TRU-002 `core`.
  - **`banking-root`** is CM-PAY-023 `core`.
  - **`catch-all` and `store-transfer:fallback`** are `out`.

## 3. Rules I followed that the digest doesn't state (for the coordinator)

- **R18.1: A catch-all at `*` is placed by its loader.**
  - One whose only content redirects to a named page is `shows` on that page's capability, as SH-8 placed Agentic's catch-all (SH-E-ee658cf8): `store-list:fallback`, to the store list.
  - One that throws a 404, or redirects to the router's root, which is no capability's page, is `out`: `catch-all`, `store-transfer:fallback`.
- **R18.2: A route at a splat with a page's own component isn't rule 37's catch-all.**
  - It is its page's, `core`: `tax-settings:duties` (component Duties) at `duties/*`.
  - Where it loads its sibling's component, rule 7 gives it that page's capability: `store-picker:fallback` loads the store list, as the picker's index does.
- **R18.3: A country's or a state's own route names the place in `reading` and `terms`, not in `scope`.**
  - Examples are Taxes' `US`, `EU`, `GB` and `CA`, and Automated filing's `US-FL`, `US-NJ` and `US-LA`.
  - Only a route's gates are its scope (rule 22). The concern map gave no scope to `tax-filing:tax-region`, at path `US` (SH-S-5270), nor to the EU's routes (SH-S-7124, SH-S-7125).
  - The brief's rule 2 places "a thing the platform offers for a country" with that country as its scope. If the coordinator reads a country's tax settings so, the Taxes lines under US, EU, GB and CA, and the three states' filing lines, take it.
- **R18.4: The router's routes with no section are read from the router's own code.** Their items hold computed paths only. The source is the `source.jsonl` line and the bundle record `meta.json` names.
  - `root` is the whole admin, `out`.
  - `shopless-root` holds the store picker and the store list's routes, `out` (R16.4).
  - `banking-root` is the router's only route in banking mode (`createRouter`'s `bankingMode`).
- **R18.5: A Taxes page that a run shows listing third parties' tax apps to install takes CM-TAX-004 `extension-point` beside its own line.** This is the digest's rule 7 with M-7. Its anchor 'Apps' takes the same line.
- **R18.6: A modal that adds or edits a tax collection under Managed Markets** takes CM-TAX-003, as its sibling add-registration modal does, and CM-MKS-003, the admin's own service. Both are `core`.
- **R18.7: A label purchase's 'Complete payment authentication' takes CM-PLN-005 beside CM-SHP-002.** This follows SH-12's domain payment authentication (SH-E-b434894e), since labels are paid through the account with the platform (CM-SHP-002's 'Shipping Fees added to the next Shopify invoice').
- **R18.8: An `eligibilityMatch` beta that only brings other modules leaves the route `core`, the beta in `reading`** (rule 26). The cases are the US tax pages' beta 4d063e20 and the partner page's and Tax service's redirect under beta a142026c.

## 4. Entries I couldn't tell, and what would settle each

- **SH-E-b0a26e4f, 'File shipping claim'** (`shipping_labels/:shippingLabelId/carrier_claim/new`, FileCarrierClaim). This is the batch's one `CHANGES` line: CM-SHP-022, which held nothing on Shopify, becomes held, `core`.
  - **Why it's there:** the capability is the merchant's complaints about the carriers of the platform's labels, raised through the platform. Its note says "the complaint is the merchant's, about a carrier, and the carrier answers it first". A claim filed with a label's carrier fits it.
  - **The other reading:** CM-SHP-003, shipping insurance, if the claim is against the label's insurance.
  - **What would settle it:** the page, on a store with a bought label (no run opened it: needs an instance), or a held statement on claims. The concern map holds none: a search of Shopify's statements for 'claim' found only VAT and Merchant of Record lines.
- **SH-E-1538d489, CM-PLN-005's line** (R18.7). The page would settle it, as would the label's payment method on a store's bill.
- **SH-E-7fd99bdc, the anchor 'Apps',** on CM-TAX-004 `extension-point`. No Taxes and duties page a run opened showed an Apps section. The Tax service page's 'Apps' list is the reading. A store with a tax app installed would settle it.
- **The 'Switch tax service' pages:**
  - They are on CM-TAX-002, as the concern map places switching the tax product (SH-S-5275).
  - The pages a run opened offer Shopify Tax and Manual Tax. Manual Tax, merchant-entered rates, is CM-TAX-001's.
  - If the coordinator reads the choice as the store's tax settings, CM-TAX-001 is the other place.
- **SH-E-207ee5f0 and SH-E-a62d758c, `eu-activation`:** turning on Shopify Tax in the EU, a reading of the path, the module EuActivation and its child 'Upgrade tax service in the European Union'.
  - ts15uk-ug, where Shopify Tax was active in the EU, was sent to `settings/taxes/EU`.
  - A store without Shopify Tax in the EU would show the page.
- **The seven Managed Markets modals** (SH-E-9cd139e4, SH-E-d05e30a6, SH-E-794be84f, SH-E-b69c8fd3, SH-E-0db930cc, SH-E-ae3ccaf8, SH-E-a3c84ae8):
  - 'VAT collection' and 'tax collection' are read as registrations, a reading.
  - ts15uk-ug answered “There's no page at this address”.
  - A store with Managed Markets in the UK or Canada would settle it.
- **SH-E-7e5eb9d5 and SH-E-17d6240a, the organization's resource download:**
  - They are on CM-ACC-003, a reading of the id's words.
  - What the resource is isn't stated: an export, perhaps, which would be CM-MIG-001's.
  - The link a download email carries, or the chunk `shopless-routes-OrganizationRequestedAction`, would settle it.
- **SH-E-f27f7b60 and SH-E-4b09fb1d, the Trust challenges:**
  - They are on CM-TRU-002, by the word Trust, the admin section the cell holds (SH-S-1608).
  - A challenge at sign-in would be CM-TRU-001's.
  - A run that meets one would settle it.
- **SH-E-d6127299, the authentication challenge's callback:** on CM-TRU-001, a reading of its id and module.
- **SH-E-7b42da8c and SH-E-7d98ace2, the store transfer:**
  - They are on CM-ACC-001 alone, by their words.
  - SH-17's anchor 'Store transfer' and its modal also take CM-ACC-003, from their pages.
  - The module here, `shopless-routes-OrganizationRequestedAction`, names an organization's requested action.
  - The coordinator may align the two.
- **The store list and the store picker** (SH-E-4357a887, SH-E-08dac4b1, SH-E-ddd0e36c, SH-E-4fc5d872):
  - They are on CM-ACC-001, whose note and reading hold the account's store list.
  - CM-ACC-003, several stores under one owner, is the other place.
- **SH-E-97aa3cfb, `banking-root`:**
  - It is on CM-PAY-023.
  - Its component is BankingChatApp, and what its chat is isn't stated: an assistant would add CM-AIA-002.
  - A session in banking mode would settle it.
- **SH-E-39a1431f, `settings-modal`:**
  - It is on CM-ACC-006, as the frame whose component is the admin's Settings.
  - Read as a pathless wrapper over several capabilities' routes, the Settings and the notification templates' editors, it would be `out` by R16.4.
- **SH-E-1acdc371, 'Sidekick' at `sidekick/playground`:** no held store showed the page. It is placed by its words.

## 5. What sources state that no entry holds (second-stage leads, M-12)

- **Automated filing's fee:** 'A flat fee of $75 is charged for each tax return. The fee will be waived if the tax return is manually skipped by the 8th of each calendar month.' (`raw/runs/20261006T225457Z-sweep-trial-my-store-8/steps/508.text.txt`, line 47). This is a quality for CM-TAX-006.
- **Shopify Tax's fees by region, for CM-TAX-002** (steps 521, 525, 530 and 534, line 63 of each):
  - United States: '0.35%transaction fees after your first $100,000 in global sales';
  - EU and UK: '0.25%transaction fees after your first $100,000 in global sales';
  - Canada: '0.25%transaction fees when you reach $100,000 in global sales each calendar year'.
- **Duties at checkout:** 'Prevent surprise fees for international customers at delivery • 0.5% transaction fee' (step 519, line 135). This is a quality for CM-TAX-008.
- **The tax service each region uses:** Manual Tax, Basic Tax or Shopify Tax, by region on the Taxes and duties page (step 519, from line 72: Yemen Manual Tax, Australia Basic Tax, Canada Shopify Tax and the rest). This is a lead for CM-TAX-001 and CM-TAX-002. Basic Tax is in CM-TAX-003's evidence (SH-S-0533).
- **The global tax settings** (step 519, lines 145 to 150): 'Charge VAT on digital goods', and including tax in prices 'in markets with dynamic tax inclusion'. These are leads for CM-TAX-001.
- **Shopify Tax's own list of what it does** (step 524, line 72 on): 'Access to automated sales tax filing and remittance; additional fees apply', exemptions, nexus tracking. These are leads for CM-TAX-003, CM-TAX-005 and CM-TAX-006.
- **The EU page** (step 525, lines 70 and 71): 'Applies VAT on orders up to €150', for IOSS. This is a lead for CM-TAX-003.
- **The Tax service page's second app** (step 543, line 70): 'Vertex Tax & Compliance', a 'Paid app'. This is a lead for CM-TAX-004's providers.
- **Avalara's page** (`derived/step-text-from-html/20261004T092454Z-sweep-instances/065.html.txt`, line 123): 'Built on the Shopify Tax Platform', and Shopify's tax settings as 'backup tax collection'. This is a lead for CM-TAX-004.
- **The Europe launch:** 'Shopify Tax is now active in the European Union and United Kingdom' (step 542, line 60). This is a lead for CM-TAX-002.
- **Sidekick's app generation:** 'Enjoy a temporary boost to your app generation limits.' (`raw/runs/20261007T030938Z-journey-sidekick/steps/062.text.txt`, line 50), with the app Sidekick built there. This is a lead for CM-AIA-002.

## 6. Problems with the brief or the scripts

- **The routes with no section:** their text holds no path, since the extractor keeps only literal paths. Their terms are their ids. Their addresses are in the router's code, which I read at the bundle record `meta.json` names, a source of the structure.
- **`held_entries.py batches`:** it takes no `--platform` and printed nothing.
- **The checker's container notes:** its 31 `NOTE`s are containers (the digest's rule 8). Each is placed as a container, or is a page with its own modal child (a jurisdiction's return, a liability insights page, a country's index). Its notes on a path that 'begins other entries' paths' (`delete`, `add`, `managed-markets/add`) are siblings' relative paths, set aside by rule 8.
- **SH-17:** it ran beside this batch on OrganizationSettings and Settings. The two batches share no route.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 101 of 101 entries, no problem. `method/held_router_gates.py SH-18 --apply` named the ancestors' gates in 66 lines of 57 routes. With this batch the admin router is placed whole (SH-8 to SH-18).
- **The one `CHANGES` stands:** 'File shipping claim' makes CM-SHP-022 held, `core`. The changelog places the same claims there (its digest's rule 41).
- **The rules R18.1 to R18.8 stand** and join the digest's section 6. R18.3 holds: a country in a route's path is the page's subject, not a gate on the store, so it goes in `reading` and `terms`; a route's scope is its gates (rule 22).
- **The open readings stay as placed.** The store transfer's line differs from SH-17's twin anchor, which also takes CM-ACC-003. It is noted for Shopify's amendment.
- **Cost:** 29.2 million tokens over 134 requests, about 289,000 an entry. The context reached about 364,000 tokens.
