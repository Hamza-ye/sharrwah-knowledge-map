# Held pass, BigCommerce, batch BC-CH: notes

**What the batch is:** the 40 sections of the control panel's Settings list (structure `bigcommerce/settings-list`). I read them from `other-product-class@0d79b794f`, whose source step is `bigcommerce/raw/runs/20261029T012951Z-store-settings-en/steps/002.frame-0.aria.yaml`. Every "source line N" in a reading is a line of that step. I read this brief (`H-held.md` at 657cd861, unchanged at HEAD), the evidence map, the repository's and BigCommerce's README and GAPS, the structure's REGISTER row and `meta.json`, the selection rows, B-extent's "Cells and evidence" and "Conventions from the dry run", and the model through `class_slice.py` and `land_points.py`. I did not read BC-1's files or any review file. Effort: high.

**How I read it:** each section is a settings item with its own title, so it is a place of its own (B-extent, "What a place of its own is"). Every section is placed on the capability its title and description name, and each further thing the description names takes its own line. All of this is a reading, as each line says.

## The new things

| New thing | Entry | Supports | Place of its own | Proposed domain, area, parent | Searched |
| --- | --- | --- | --- | --- | --- |
| `new:Social sharing` | BC-E-ba87a83d (Share: "Social sharing settings on product pages and blog posts") | core | Yes: the settings section Share (`viewSettings#SocialSettingsTab`, source line 61), in the group General | E, CNT or SFR. No parent is stated. Its leads CM-CNT-004 (blog), CM-CAT-001 (products) and CM-CNT-003 (pages) are where sharing shows, not the thing itself, so they are named in the reading only | caps: social sharing; share buttons; social media; social links; sharing; share. BigCommerce statements: social sharing; share. Only homonyms came up: Salla's social media accounts in CM-ACC-006, and "share" in the sense of a quota or a PCI scope |
| `new:URL structure` | BC-E-9087905a (URL structure: "Product, category and web pages URL settings") | core | Yes: the settings section URL structure (`viewSettings#URLStructure`, source line 66) | E, CNT. Proposed beside CM-CNT-006 (Custom URLs) and CM-CNT-009 (URL redirects), with no parent stated | caps: URL; URLs; custom URL; slug; handle; permalink; url structure. BigCommerce statements: URL structure; URL settings; URLs (one hit only, cart redirect URLs) |
| `new:Throttler` | BC-E-e2655528 (Miscellaneous: "... order settings, throttler") | shows | None: one word inside the tab Miscellaneous, which is a field or setting within a page | Unknown: nothing held says what it throttles | caps: throttler; throttle; throttling. BigCommerce statements: throttler; throttle (0 hits) |

All three are named in English, BigCommerce's only language.

**URL structure against CM-CNT-006:** I would have joined it to CM-CNT-006, Custom URLs. But that capability's cells say no platform defines a custom URL, so its readings don't show the thing, and BigCommerce's section is about the URL pattern of products, categories and pages. Either of two would settle it: the URL structure tab's page (not held: no run opened `viewSettings`), or a definition of Salla's Custom URLs. If the coordinator joins them, CM-CNT-006's BigCommerce cell becomes held.

## Entries I couldn't tell, and what would settle each

None of BigCommerce's older settings pages (`/admin/index.php?ToDo=…`) was opened by any run (`index/runs.tsv`; no `actions.jsonl` holds `ToDo=`). So each of these rests on the section's title and description alone:
- **BC-E-8e28f7e3, Security & Privacy, on CM-TRU-001 (core): a CHANGES line.** I read "security settings for … control panel" as the admin's sign-in security. What the tab sets isn't held. Its page, `viewSettings#SecuritySettingsTab`, would settle it. If it is not sign-in security, the line belongs on no capability yet.
- **BC-E-0c012476, Account sign up form, on CM-CHK-009 (core): a CHANGES line.** I read the form fields for "addresses on checkout", listed in the merchant's settings, as fields the buyer fills in at checkout. Whether the merchant adds fields of its own isn't held. The page `viewFormFields` would settle it. The other reading is CM-CUS-008, customer addresses, whose note keeps the order's address out of it.
- **BC-E-8dec1b9a, File access (WebDAV), on CM-CNT-001 (core): a CHANGES line.** I read "uploading files to store's server" as the store's files. A BigCommerce statement also says "Files can only be added to digital products via control panel or WebDav" (BC-C-001/boundary/BC-S-0023), which ties WebDAV to digital products' files. The page `viewFileAccess` would settle it.
- **BC-E-e2655528, Miscellaneous, "Email settings", on CM-NTF-001.** The other choice is CM-NTF-004 (message delivery, which holds nothing). The tab's page would settle it.
- **BC-E-d3e6a1ba, Tax, "recommended services", on CM-TAX-004 (extension-point).** The entry names no provider. I read the services set against "Your own tax rules" as the platform's list of tax services to connect, the brief's own example of an extension point. The tax-services structure names the providers. The checker's lead CM-PTN-005 (partner services) is not the thing: these are tax services.
- **BC-E-4deb44c1, Shipping, "shipping services", on CM-SHP-015.** I read them as carriers, from the page's own line "Manage your shipping zones, carriers and rules …" (`steps/062.text.txt`, line 10).
- **BC-E-0f0cc77a, Localization, "regional settings", on CM-ACC-006, not new.** The page sets Default country, Physical dimensions, and Date and timezone (`steps/004.text.txt`, lines 8, 19, 24). CM-ACC-006's cells already hold a store's timezone (BigCommerce, BC-S-0262) and its country (Zid). So under the brief's rule, a place whose thing a capability holds is that capability's evidence. The coordinator may still prefer a new "Regional settings" capability, whose place of its own would be the section Localization, shared with languages (CM-MKS-008).
- **The General group (entries 9 to 15) on CM-ACC-006.** Every section of the group opens one page, the store settings page `/admin/index.php?ToDo=viewSettings`, each at its own tab anchor. The group's name is CM-ACC-006's term (Shopify's General). So each section takes a CM-ACC-006 line beside the lines for its own things. No other group gets a line for its parent.

**Leads I didn't take,** from the checker's notes:
- line 45: CM-MKT-007 (email). "Email records" are DNS records (CM-SFR-009), not email marketing.
- line 48: CM-ACC-004 (business). "Business intelligence platforms" is not the business entity.
- entry 1: CM-ACC-004 (business). The Store profile page holds contact information, a display name, an address with address type "Home office", and an email (`steps/003.text.txt`), not the entity the store operates as.

**Scope:** every line's scope is empty. The list was seen on one trial store (`w5pamplexj`), but no entry or source states a plan, a country or a listing condition for any section.

## A structure whose items and sources disagree

`settings-list`'s `items.jsonl` disagrees with its source step `002.frame-0.aria.yaml`:
- **Addresses** (known, handoff H-009). Each item carries the next section's address. Item 40 (MCP) has none, and the first section's own address, `/manage/microapps/store-profile-ui` (source line 8), is in no item. Each reading cites the section's own address from the source.
- **The badge "new"** on Search (source line 73) and MCP (source line 227) is in neither item, so the rendering leaves it out too. I put it in those lines' readings, as the brief says for a listed badge.
- **No `source.*` file** sits beside `items.jsonl`. The source is the run step that `meta.json` names under `held_as`.
- **The eight groups** (Setup, General, Orders, Products, Marketing, Domain, Advanced, API and MCP) are containers that the structure holds only as labels on the sections, so none is an entry. Read as containers, they would go:
  - General on CM-ACC-006;
  - Orders on CM-ORD-001;
  - Products on CM-CAT-001;
  - Marketing on CM-MKT-001, since its one section is Promotions and coupons;
  - Domain on CM-SFR-008;
  - API and MCP on CM-API-001, with CM-AIA-005 for MCP;
  - Setup and Advanced name no capability, so as containers each would be `new:<title>`, `core`, its children as listed in the source.

## What run steps state that no entry holds (for the second stage)

All in `bigcommerce/raw/runs/20261029T012951Z-store-settings-en/`:
- `steps/003.text.txt`, line 13, Store profile: "All emails to customers will be sent from this address." This is the store's sender address, a lead for CM-NTF-004 (holds nothing; "from address" was searched) or CM-NTF-001.
- `steps/003.text.txt`, line 1: "Store country and language are now managed within Localization settings."
- `steps/004.text.txt`, line 9, Localization, under Default country: "Determines available payment options." This ties the store's country to its payment methods (CM-PAY-001, CM-ONB-001).
- `steps/004.text.txt`, line 21: "Physical dimension format presented to shoppers. Length and weight entered for a product will be autoconverted into this format."
- `steps/062.text.txt`, lines 34 to 37, Shipping: the section Shipping labels, "Native label printing powered by ShipStation. Manage orders, create and print shipping labels from within BigCommerce.", with Install ShipStation. This is a lead for CM-SHP-002, shipping labels, which holds nothing on BigCommerce. The maker statement is ShipStation's, not BigCommerce's.
- `steps/062.text.txt`, lines 26 to 29, Shipping: "Advanced shipping rules", ShipperHQ, which "integrates with over 50 parcel and LTL freight providers", with Install ShipperHQ. A lead for CM-SHP-023 and CM-SHP-004.
- `steps/062.text.txt`, lines 20 to 25, Shipping: "Shipping address form display", which controls the countries shown at checkout.
- MCP's address, `/manage/microapps/ai-labs-ui/mcp-settings` (source line 224), sits under the route of Early access, `/manage/microapps/ai-labs-ui` (source line 196). Only the addresses show this.

## Problems with the brief or the script

- The brief says to read "the `source.*` file beside `items.jsonl`". `settings-list` has none (see above).
- The checker flags a quote from the model's own statements (BC-S-…) as "found nowhere held". I removed the quotation marks from the two I had used instead of citing them as quotes.
- The checker's NOTEs on lines 21, 23 and 31 (new things whose entries have leads) are answered above: the leads are where the thing shows, or they are already placed on the entry's other lines.
