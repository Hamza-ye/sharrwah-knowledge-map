# SH-42: notes (Shopify `merchant-changelog`, 130 posts, 22 March 2023 back to 13 July 2022)

Effort `high`. I read the brief, the guides it names (observed-sh at `e38dc17e3`: `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, the register's and selection's rows for this structure), the evidence map, B-extent's "Cells and evidence" and "Conventions from the dry run", the rules digest (`held/rules/merchant-changelog.md`) and the rulings' last section. Of the earlier batches' notes I read only `notes-SH-41.md`, its section "The new things" and its open entries (lines 70 to 90 and 140 to 146), for Staff sales attribution's support. Besides `earlier`, I grepped the earlier batches' placements for the kinds of post no `earlier` key reached (POS discounts and navigation, Shop Promise, Shopify Payments by country, HS codes, receipts, Search & Discovery, Sign in with Shop, alerts, Staff sales attribution, Saved views, Admin search), and kept to their lines; each reading names the line it follows.

All 130 entries are placed: 127 on capabilities alone, 2 with a new thing beside capabilities, 1 on new things alone; none is `out`. 208 lines: `core` 151, `own-service` 35, `extension-point` 10, `core;extension-point` 4, `shows` 8.

## The new things

All three are earlier batches' new things, and keep their names (the digest's section 4). `caps --terms "staff attribution; sales attribution; saved view; admin search; index filter"` finds only CM-MKT-008 (crediting orders to marketing), the homonym SH-41 found. No Arabic name is held: the admin in Arabic isn't captured (`docs/GAPS.md`).

- **`new:Staff sales attribution`** (SH-E-fe992e2d, SH-E-d48459db; both `shows`, as SH-41 kept it): POS's views of the staff credited with a sale on completed orders and returns, and the attribution search bar and renamed actions. Each also takes CM-POS-001 `core`, as the digest's section 4 has it. No place of its own in the posts: it is a set of views and actions inside POS. Proposed, a reading: domain E, area POS, parent CM-POS-001. Leads: CM-MKT-008 (homonym), CM-RET-003 (the return item view is a POS screen, where the attribution is shown, not a return feature), CM-MKT-014 (affiliates' commissions, not staff's), CM-PLN-001, CM-POS-004, CM-PTN-004, CM-PTN-008, CM-ORD-003, CM-ONB-003; none is it.
- **`new:Saved views`** (SH-E-9c2e557d, `shows`, as SH-41 placed it): the index pages' filters 'merchants can use to create custom saved views'. No place of its own: a view inside a list page. Decided with Zid's and Salla's admin search (ruling SH-37). Leads: CM-SFR-013 (the storefront's search, not the admin's), CM-CAT-003, CM-CNT-003, CM-AIA-003, CM-ORD-003; none is it.
- **`new:Admin search`** (SH-E-9c2e557d, `shows`, as the changelog's earlier lines place it): 'launching search using the F key or clicking the magnifying glass' on the index pages. No place of its own in this post. Same leads.

## Rules I followed that the digest doesn't state (for the coordinator)

- **C42.1** A post that makes Shopify Payments available in a country is CM-PAY-002 `core`, the country its scope. Each local method it says merchants there can accept (Multibanco, Sofort, iDEAL, Bancontact) takes a CM-PAY-017 `core` line, the method its filler, the same scope, as SH-E-0ecae440's line holds local methods. The features it lists after 'Use features like' (payouts, chargebacks, Apple Pay, Google Pay, 133 currencies) are examples and take no line (rule 6). Sofort's post names the merchants' country and the buyers' countries, joined with ` and ` (rule 27): SH-E-e11d6f42.
- **C42.2** "Shopify Payments for POS now available in X, along with the WisePad 3 card reader" takes CM-PAY-021 `core`, CM-POS-002 `own-service` (rule 18) and CM-POS-001 `core`, each scoped to the country: SH-E-5584b4f7, SH-E-13701f6b.
- **C42.3** A post on one API field, object, connection or webhook topic is `core` on the capability of the object's own feature (ProductInput CM-CAT-001, Order CM-ORD-001, locations/activate CM-INV-005, Audit events CM-TRU-003). Where the field's own name names another capability's thing, that one takes a line too, as a reading (redirectNewHandle on CM-CNT-009). It is `extension-point` where its words say apps do the work (heldBy, 'This will allow apps more granular control over which fulfillment orders they release', CM-SHP-009; the Inventory States API, 'It allows 3rd party apps to modify inventory values', CM-INV-001).
- **C42.4** A notice of an API version's support dates is CM-API-006 `core`; the breaking changes it names as 'a few' of 'the full list' take no line (SH-E-d7c568a4).
- **C42.5** The admin's own address (admin.shopify.com) is its frame, as its loading is (rule 36), so it takes no line; what the post says embedded apps must do for it takes CM-APP-007 `extension-point` (SH-E-f118f0bc).
- **C42.6** A first-party app's launch post that names the app's features ('Customize search, filtering, and product recommendations') takes CM-APP-011 `own-service` for the release (rule 15) and an `own-service` line on each feature it names (SH-E-f6503018, SH-E-57cf12d4, SH-E-aba82227, SH-E-514b3d6c).
- **C42.7** Analytics a first-party app provides about its own feature (Search & Discovery's search results, Inbox's conversation metrics) take CM-ANL-001 `own-service` beside the feature's own capability, since the app provides them (rule 14): SH-E-6b9b5867, SH-E-ad0c07b1.
- **C42.8** A country's subdivisions added to shipping zones, for addresses at checkout (Kuwait's governorates), take CM-SHP-001 and CM-MKS-009 (rule 38), and CM-CUS-008 with CM-CHK-001 (rule 42), all `core` and scoped to the country (SH-E-131dfa61).
- **C42.9** User provisioning from identity providers through the platform's SCIM: the platform's roles are `core`, the providers that now assign them `extension-point` with the providers named as fillers (OneLogin, Okta), on CM-STF-002; 'our SCIM implementation' is `core` on CM-TRU-001, whose terms hold SCIM (SH-E-13eb8f17).
- **C42.10** Where a capability's note names a homonym, its note governs over the word: a draft order's invoice email is CM-ORD-005, not CM-ORD-008 (whose note says so) (SH-E-f543d41f).

## Entries I couldn't tell, and what would settle each

- **SH-E-e1362572, Balance with QuickBooks (CM-PAY-028 `core`, a CHANGES line):** I placed it by the post, Shopify's surface named with QuickBooks as the filler (rule 20). Before deciding, I opened the post's learn-more page, which the digest's rule 7 says isn't read. It doesn't change the placement, but the coordinator may want it. The help center holds it at `structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/finance/shopify-balance/taxes/quickbooks.md` (record `<urn:uuid:55acd322-4595-4bdd-86c5-78cd64aaa4aa>`, run `20261016T213535Z-help-en-ar-html-md`). Its lines 7 to 14 say the connection is made from QuickBooks Online's side: 'From your QuickBooks Online admin, go to **Bookkeeping** > **Bank transactions**', 'Search for <kbd>Shopify</kbd>', 'Enter your Shopify credentials and login'. Read that way, the third party does the sync through the platform's account connection, which would be `extension-point`. The coordinator decides whether that page, an entry of the help center, governs.
- **SH-E-13eb8f17, SCIM role provisioning (CM-STF-002 `core;extension-point`, a CHANGES line):** the identity providers could be read as fillers of a `core` line, or as the merchant's own tools, which take no filler (rule 51). What would settle it: whether the coordinator counts an identity provider using the platform's SCIM as a third party working through a provider interface (B-extent's `extension-point`).
- **SH-E-cefe4a5b, SMS order confirmation in 13 countries:** CM-NTF-001 `core` in those countries. The partners that 'deliver custom SMS notifications' are CM-NTF-004 `extension-point` (a CHANGES line), as the way named in place of the platform's own (rules 31, 32). The countries where Shopify stopped are not named, so no `shows` line can take them as its scope.
- **SH-E-f118f0bc, admin.shopify.com:** C42.5. If the coordinator reads the whole post as the admin's frame, it is `out`, and the CM-APP-007 line goes.
- **SH-E-aba82227, Translate & Adapt's launch:** content adapted for buyers in different markets is placed on CM-MKS-001 `own-service` (a CHANGES line), beside CM-MKS-008 `own-service` for its translations. If the coordinator holds market adaptation inside CM-MKS-008 (its note includes translating content), the CM-MKS-001 line goes.
- **SH-E-48bca7af, redirectNewHandle:** the CM-CNT-009 line rests on the field's name alone. The field's page (shopify.dev ProductInput 2023-01) isn't held (`held_index.py`).
- **SH-E-fc0411a0, Buy Again:** CM-ORD-014 becomes held (a CHANGES line). Its CM-B2B-001 line rests on the title 'Drive repeat orders for B2B' and 'your wholesale customers'. The post also says the feature is on for any store using new customer accounts.
- **SH-E-49db0469, YouTube Shopping:** earlier batches differ on the Google & YouTube app. SH-E-0bbdd469 makes the product sync `extension-point`, YouTube the filler; SH-E-90b81d95 makes publishing `core`, the venue the filler. I kept each: CM-CHN-004 `extension-point` and CM-CHN-001 `core`, YouTube the filler of both. The coordinator aligns them.
- **SH-E-51e7df71, Google Analytics 4:** CM-ANL-007 becomes held (a CHANGES line), as SH-54 placed the Edition's same feature (SH-E-6bff85f5).
- **SH-E-36918e68, Shop Promise in early access:** all three lines are `shows` (rule 29). The digest's rule 17 (`core;own-service`) is for the release, SH-E-682a2a87.
- **SH-E-bb247293, AVIF images:** no capability holds the storefront's delivery of its assets, as SH-41's notes found for asset URLs, so I placed it on CM-SFR-001.
- **SH-E-c5387d0e, Audit events topic:** the CM-API-008 line names Google Cloud Pub/Sub and AWS Eventbridge as fillers, the services the post requires for delivery. If the coordinator reads them as named with no role (rule 51), the line keeps no filler.

## The checker's other lines, read again

- The `core` notes on products named with the platform's brand are all its own admin, POS, Payments, Balance, Markets, Tax, Shipping, Editions or Analytics (rules 8, 9, 40; the corrections), and each names no maker.
- The `own-service` notes are each on an app or product the digest's table lists: Shop, Search & Discovery, ShopifyQL Notebooks (SH-E-3f85908b is in this batch: 'we’ve prepared a summary notebook in ShopifyQL Notebooks'), Shopify Collabs, Shopify Audiences, Shopify Flow, Translate & Adapt, Shopify Email, Shopify Inbox, and the POS hardware.
- The first-lead notes (CM-MKS-009 on SH-E-2e0ca367, CM-PAY-031 on SH-E-76c8fa5c, CM-B2B-005 on SH-E-bfe24178, CM-APP-010 on SH-E-49db0469) are leads by a common word. I read each name: none is the entry's thing.

## Items and sources

Each entry's text agreed with its post as `show` printed it; I found no item that disagrees with its source. Three posts hold straight double quotes inside a passage I cite (SH-E-6fed6fe6's default rate names, SH-E-c6c1aedc's 'total sales', SH-E-92a0d0be's setting name). I named those passages unquoted (the digest's rule 4).

## For the second stage

- The Balance QuickBooks help page above, for CM-PAY-028's and CM-PAY-023's cells.
- SH-E-cefe4a5b's notifications settings link (`shopify.com/admin/settings/notifications`) and its billing address link (`settings/general`) open places that the cells already cite. No run step was read for them.

## Problems with the brief or the script

None with the script. The digest's rule 7 says a learn-more link isn't read, and I read one (above). It is named here so that the coordinator can drop it.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 130 of 130 entries, no problem.
- **Two lines corrected,** both decided against the sources:
  - **Balance with QuickBooks (line 3):** `extension-point`, not `core`. The held help page has QuickBooks Online make the connection from its own admin, through the merchant's Shopify sign-in and a list of their Balance accounts (lines 7 to 14). The cell already holds `extension-point`, so it doesn't change.
  - **YouTube through the Google app (line 205):** `extension-point`. Six lines of the Editions and of SH-39 read the same channel as 'a sales channel through an app', and the app's maker isn't held. SH-35's line on the same app is aligned too: `core;extension-point`, its Publishing section the admin's own.

  The digest's table is corrected to match.
- **The other `CHANGES` stand,** each on the digest's table or rules. Among them:
  - Translate & Adapt's content by market is CM-MKS-001 `own-service`, since the app provides per-market versions of the content (the ruling after SH-57), and adapting content isn't CM-MKS-008's translation.
  - SCIM's providers are `extension-point` (C42.9).
  - SMS partners in place of Shopify's own SMS are CM-NTF-004 `extension-point`.
- **The rules C42.1 to C42.10 stand** and join the digest's section 6.
- **The new things** keep their names. Staff sales attribution's support is decided with the thing.
- **Cost:** 19.8 million tokens over 84 requests, about 152,000 an entry, against SH-41's 189,000 before the digest. The context reached about 429,000 tokens.
