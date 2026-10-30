# Held pass, BigCommerce, batch BC-CX: notes

**What this batch is:** the 40 entries of BigCommerce's control panel Settings list (`settings-list`, other-product-class@0d79b794f), placed under `briefs/H-held.md` at 657cd861, at effort xhigh, as a calibration of the brief. Read only the brief and what it names; the earlier batch's placements and the review files were not read.

**The source:** each entry is read with its source step, `bigcommerce/raw/runs/20261029T012951Z-store-settings-en/steps/002.frame-0.aria.yaml` (other-product-class@0d79b794f), cited in the readings as `002.frame-0.aria.yaml:<line>`, and the run steps that opened the sections (steps 3, 4, 41 to 45, 62, cited as `20261029T012951Z-store-settings-en/steps/<NNN>.text.txt`). Each line's address is the source's own, never the item's (handoff H-009).

**Counts:** 40 entries, 77 lines: 75 on capabilities, 2 new, none out.

## How I read the entries' groups (a rule to check)

The brief's rule 2: every thing the entry names takes a line, including "the parent's thing where the entry's own words name it (its section is the parent's term)". A settings-list entry's text names its group (`group: Orders`). A reading: the group is the section's parent in the platform's own grouping, so where the group's title is a capability's own term, and that capability's cell doesn't decline it, each entry under it takes a `core` line there:
- **General:** CM-ACC-006 (Shopify General, Salla General / عام); each of the seven sections is also a tab of the store's settings page `/admin/index.php?ToDo=viewSettings` (002.frame-0.aria.yaml:51 to 82). Lines 14, 18, 21, 23, 25, 27, 31.
- **Orders:** CM-ORD-001, line 38 (three entries).
- **Products:** CM-CAT-001, line 42 (three entries).
- **Domain:** CM-SFR-008, lines 49, 51, 53 (Domain name is itself CM-SFR-008's, line 47).
- **API and MCP:** "API" names CM-API-001 only as the model's parent of the API accounts' capabilities (CM-API-002, CM-API-003, CM-API-013), lines 73 and 77. The Storefront API's entries (CM-SFR-012, under CM-SFR-011) and MCP (CM-AIA-005) take none.
- **Not given a line:**
  - **Setup:** CM-ONB-004's cell reads Settings > Setup > Shipping, Tax and Currencies as hits that are not a setup wizard.
  - **Marketing:** CM-MKT-005's cell reads the control panel's Marketing section as "named only as the home of Promotions"; a line would make it gain core.
  - **Advanced:** names no capability.

The same rule gives the parent's line where the section's own words name a model parent: line 37 (Order notifications, CM-NTF-001), line 51 (Email & DNS records, CM-SFR-008), line 62 (Export templates, CM-MIG-001). If the coordinator reads the rule otherwise, the group lines are the 14 listed above (lines 14, 18, 21, 23, 25, 27, 31, 38, 42, 49, 51, 53, 73, 77), and none of them changes a cell.

## The lines that change the model (`CHANGES`)

Each was read again against its sources. All are `core`, and each makes a cell that held nothing held:
- **CM-SFR-009** (DNS records), line 50: Email & DNS records, 'Manage your domain, subdomain, and email records', at /admin/tools/domains. Plainly its thing.
- **CM-MIG-003** (Export templates) and **CM-MIG-001** (import and export), lines 61 and 62: Export templates, 'Orders, customers and products export settings'. Same name as Salla's Export templates; the parent's objects are named exactly.
- **CM-LOY-006** (Gifting), line 43: Gift wrapping, 'Name your gift wrapping option, set a price, etc.'. The capability holds Shopify's Gift wrap and message apps.
- **CM-EVO-001** (Feature settings), line 67: Early access, 'Try new tools, beta functionality, and upcoming features'. The cell searched for early access, beta and labs and found nothing.
- **CM-TRU-001** (sign-in security for the admin), line 29: Security & Privacy, 'Security & privacy settings for storefront and control panel'. The control panel's security is the admin's. A reading, since what the tab sets isn't held. **To settle:** the tab's content (`/admin/index.php?ToDo=viewSettings#SecuritySettingsTab`); no run opened it.
- **CM-DVT-001** (developer tools and documentation), line 69: Storefront API Playground, 'API queries examples and additional information', on the platform's own host gql-playground.bigcommerce.com. A reading: a tool and examples for building against the API.
- **CM-CHK-009** (fields at checkout), line 59: Account sign up form, 'List of form fields for signup, addresses on checkout etc.'. The cell found BigCommerce's form fields but "no held statement ties those form fields to orders or checkout"; this entry ties them. **To settle:** whether the merchant adds fields of its own (the page `/admin/index.php?ToDo=viewFormFields`, not opened by any run).
- **CM-CNT-006** (Custom URLs), line 24: URL structure, 'Product, category and web pages URL settings'. A join on role: the merchant setting the URLs of the store's pages and products, which the cell looked for. No platform defines a custom URL. **Alternative:** `new:URL structure`, a section of its own. **To settle:** the tab's content, or a definition of Salla's Custom URLs.
- **CM-CNT-001** (Files), line 65: File access (WebDAV), an application for uploading files to the store's server. A join on role, the store's own uploaded files. **Alternative:** `new:File access (WebDAV)`. **To settle:** whether WebDAV's files are the store's file library; the cell keeps files added to digital products via WebDav (BC-S-0023) apart.

No line makes a cell gain a support it lacks without also making it held. Line 55 (Data solutions, CM-ANL-007) is `core`, not `extension-point`: the entry names only kinds of outside platforms and no provider, so the brief's "a catalog card that names no one ... is core by what it shows" is followed. This differs from Accounting (line 54, `extension-point`), which the brief names ("a section for accounting software") and whose address is under apps (`/admin/apps/accounting`).

## New things

| New thing | Entry | Place of its own | Proposed domain, area, parent | Names | Terms searched |
| --- | --- | --- | --- | --- | --- |
| **Social sharing** | BC-E-ba87a83d (line 22), core | Yes: the settings list's section Share, Settings > General > Share, with an anchor of its own (`/admin/index.php?ToDo=viewSettings#SocialSettingsTab`, 002.frame-0.aria.yaml:61) | E, SFR (or D, MKT), no parent | English only: "Share", "Social sharing settings" | social sharing; share; sharing; social media; social; share buttons |
| **Throttler** | BC-E-e2655528 (line 34), shows | None: a setting named inside the Miscellaneous tab | G (or A, TRU), parent unknown | English only: "throttler" | throttle; throttler; throttling; rate limit; rate limiting; bot protection; spam; brute force; login attempts; captcha |

Notes on the two:
- **Social sharing:**
  - its entry names product pages and blog posts as where sharing shows, given in the reading, not as lines;
  - its leads (CM-CNT-004, CM-CAT-001, CM-CNT-003) were read, and none holds sharing;
  - CM-ACC-006's Salla term store_setting_edit_social_media_account is the store's own social accounts, another thing;
  - so is the webhook topic store/channel/{channel_id}/socialMediaLinks/updated (BC-I-0289), which no cell cites.
- **Throttler:**
  - nothing held defines it, and its leads (CM-ACC-006, CM-ORD-001, CM-ACC-001) hold no throttling;
  - candidates are CM-API-005 (API rate limits) and CM-TRU-004 (bot protection at checkout);
  - **to settle:** the Miscellaneous tab's content (`#MiscellaneousSettingsTab`), not opened by any run.

## Entries I couldn't tell, besides the CHANGES above

- **Localization's 'regional settings'** (line 4) are placed on CM-ACC-006. Its page shows them as Default country, Physical dimensions and Date and timezone (steps/004.text.txt lines 7 to 27), and CM-ACC-006's cell reads the store's global settings, timezone among them (BC-S-0262).
  - No capability holds the store's country or units as such.
  - The Website tab also lists 'Physical dimension settings' (line 14).
  - **Alternatives:** a new capability for the store's regional formats, or CM-MKS-001, whose BigCommerce cell reads per-region storefronts with their own language and currency (S-02's statements).
  - **To settle:** the coordinator's decision whether the store's formats are general settings.
- **Shipping's 'shipping services'** (line 11) are placed on CM-SHP-015 (carriers).
  - Its page names zones, carriers and rules (steps/062.text.txt line 10), real-time quotes (line 7, CM-SHP-004), ShipperHQ (line 27, CM-SHP-023) and ShipStation's labels (lines 34 to 38, CM-SHP-002, which holds nothing).
  - Which of them the words mean isn't stated.
- **Miscellaneous' 'Email settings'** (line 32) are placed on CM-NTF-001, the store's transactional email settings. CM-NTF-004 (message delivery and its providers, which holds nothing) is the other reading. **To settle:** the tab's content.
- **'order settings'** (line 33) are placed on CM-ORD-001; CM-ORD-010 (order receiving settings, holds nothing) is possible. **To settle:** the tab's content.
- **Store profile** (line 2): 'Basic information about your business' isn't read as CM-ACC-004 (business entity, holds nothing). Its page holds name, address, address type, email and phone, but no entity (steps/003.text.txt lines 4 to 16). The checker's note on line 55 names CM-ACC-004 only by "business intelligence".
- **MCP** (line 78) is placed on CM-AIA-005 alone, the place its cell cites (BC-S-0343).
  - The checker's note offers CM-AIA-004, whose cell reads BigCommerce's MCP as the buyer's agent's, not the merchant's own assistant's.
  - 'endpoints for AI agents' doesn't say whose agents.
  - **To settle:** the MCP page (`/manage/microapps/ai-labs-ui/mcp-settings`).
- **Early access's address is ai-labs-ui** (002.frame-0.aria.yaml:197), the parent of MCP's address. Whether its tools are AI ones (CM-AIA-001) isn't stated by the entry.

## The checker's other notes, answered

- **Line 12** (Tax): first lead CM-PTN-005 (partners' services) by "services". The 'recommended services' are automatic tax services, CM-TAX-004's (line 13), not partners' services.
- **Line 50** (Email & DNS records): first lead CM-NTF-004 or CM-MKT-007 by "email". The 'email records' are DNS records of the store's domain (CM-SFR-009), not the delivery of the store's messages or campaigns.
- **Lines 21, 31:** the new things' leads were read (above).

## Where the items and their source differ

- **The addresses:** each item's `address` is the next section's (handoff H-009). Every reading cites the source's own.
- **The badge new:** the source marks two sections with it, which the items leave out:
  - Search (`text: new`, 002.frame-0.aria.yaml:73);
  - MCP (002.frame-0.aria.yaml:227).

  Each is offered to the store, and its badge is in the line's reading (lines 26, 78).
- **Addresses outside the store's control panel:** Domain name and SSL certificates are at the account's `manage.bigcommerce.com/account/stores/1003524922/...` (lines 134, 149), and Account-level API accounts at `https://accounts.bigcommerce.com/tokens` (line 220). The Storefront API Playground is at `gql-playground.bigcommerce.com` with the store's hostname and a `storefront_token` (line 205), cited like any evidence.

## What the run steps state that no entry holds (for the second stage)

All are in `bigcommerce/raw/runs/20261029T012951Z-store-settings-en/steps/`:
- **`062.text.txt` lines 34 to 38:** the Shipping page's section Shipping labels, with "ShipStation: Native label printing powered by ShipStation. Manage orders, create and print shipping labels from within BigCommerce." and Install. This bears on CM-SHP-002 (labels bought through the platform), which holds nothing. The page names ShipStation as the label service.
- **`062.text.txt`, more of the Shipping page:**
  - line 7: "print shipping labels and get real time shipping quotes";
  - line 27: ShipperHQ's advanced shipping rules (CM-SHP-023);
  - lines 20 to 25: the shipping address form display.
- **`042.text.txt`, the Currencies page:**
  - line 4, "Default Currency": where the store's default currency is set, which CM-MKS-005's cell says isn't held;
  - line 10, "set a fixed conversion rate to your default currency or set individual prices through Price Lists (only on supported plans)": CM-MKS-007, with a plan condition;
  - line 11, a payment provider per currency, "(Stripe, PayPal by Braintree and more)".
- **`004.text.txt` lines 8 and 9:** "Default country", "Determines available payment options.": the store's country, which no capability holds as such (CM-ONB-001 is the country given at sign-up).
- **`004.text.txt` line 21:** the physical dimension format "presented to shoppers", with autoconversion.
- **`003.text.txt`:**
  - line 13: "All emails to customers will be sent from this address.", the store's sender address (CM-NTF-001 or CM-NTF-004);
  - line 1: country and language moved to Localization.
- **`041.text.txt`, the Payments page:**
  - line 6: "Online payment methods are disabled for this store. Please switch to a paid plan to activate online payments.", a plan condition on online payments (CM-PAY-001);
  - line 8: "Offline payment methods" (CM-PAY-016);
  - lines 10 and 11: test card payments.
- **`043.text.txt`, the Tax page:**
  - lines 9 to 11: Basic Tax;
  - lines 21 and 22: the fallback tax, "A flat rate of 10% tax applies when your automatic tax service is unreachable." (a quality for CM-TAX-004);
  - lines 23 and 24: tax inclusive pricing.
- **`045.text.txt` line 19:** "CCH® SureTax®", a tax service the store is offered. Its other services' names are not in the step's text.

## Problems with the brief or the script

- **The brief's parenthetical "(its section is the parent's term)"** fits a field named `section`. In `settings-list` that field is the item's own title and the parent is `group`, so I read `group` as the section (above). The brief could say which field a structure's parent is in.
- **The checker's first lead isn't stable between runs.** Line 50's first lead was CM-NTF-004 in one run and CM-MKT-007 in the next. Line 78's was CM-AIA-005 in `show` and CM-AIA-004 in a `check`. Its candidates seem to tie and come out in set order, so a `NOTE` about the first lead can come and go.
- **B-extent.md and the brief read alike on everything this batch needed.**
