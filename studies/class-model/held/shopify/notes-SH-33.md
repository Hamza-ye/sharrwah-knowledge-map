# SH-33: Shopify's Help Center notes, the last 60, and the inventory adjustment reasons (high)

**What the batch is.** 66 entries of two structures (observed-sh at `e38dc17e3`):
- 60 of `help-notes` (`structures/shopify/help-notes/help.shopify.com@en-md/items.jsonl`, lines 3320 to 3968): the asides of the English `.md` pages whose class is `note note-plan` (37), `note note-staff-permissions` (3) or `note note-beta` (20), as `selection.tsv` reads them, from the POS offline checkout page (`sell-in-person/shopify-pos/selling-offline/offline-checkout`) to the Partners help's page on managing roles (`partners/manage-account/manage-users/roles/manage-roles`). I kept to SH-30's rules H1 to H13, SH-31's H14 to H20 (H18 as narrowed) and SH-32's H21 to H23, with their coordinator's checks, and to `review-H-rulings.md`'s last section.
- 6 of `inventory-adjustment-reasons` (`structures/shopify/inventory-adjustment-reasons/capture-plus@adjust-available/items.jsonl`, lines 2 to 7): the options of the reason picker of the admin's adjust-available form, read with its `source.html` and the run `20261005T124111Z-journey-product-subroutes` (steps 14, 17 and 19, an inventory item's page on capture-plus). No batch had placed this structure.

Each help note's source is its page's record in the run `20260930T003703Z-help-en-md`. I read the page where the note's own words left its feature, its scope or its maker open: 11 pages, cited in the lines that rest on them as `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz@<offset>`. Where only a sibling aside of the same page was needed (whether a page has a plan note, H21), I read the structure's own items of that page.

**Count.** 66 lines over 66 entries:
- 49 entries on capabilities, 17 `out` (the admin's refreshed design, H6), no `new`;
- supports: `core` 52, `own-service` 4, `shows` 3, `extension-point` 1, and 6 `out` lines (grouped).

## The rules I added (H24 to H27, for the coordinator to check)

**H24. A POS Pro plan note on a page of the users and roles pages is read as H23 reads one on a POS page:** its feature's line and a CM-POS-001 line, both `POS Pro`. The feature is the POS's staff or roles, used in the POS app; the CM-POS-001 line takes the note's words 'Shopify POS Pro subscription'.
- The cases: SH-E-3d0e19e9 and SH-E-7b510f39 (managing and adding POS staff, CM-STF-001), SH-E-867973b2, SH-E-31aff3c5 and SH-E-19e19c59 (POS roles and the predefined POS roles, CM-STF-002).
- SH-E-8943e34e is on a POS page (Managing staff in the Shopify POS app), so H23 itself.
- The alternative is the feature's line alone, with no CM-POS-001 line, since these pages are the admin's users pages, not the POS's.

**H25. An option of the admin's adjust-available form is a kind of the form's thing (M-6), the store's stock quantities: CM-INV-001 `core`, its label the term.**
- **The form's capability:** `earlier` found no line on the structure's keys. The placements give the form's own words to CM-INV-001: 'inventory adjustment reasons' (SH-E-3c6ba4d2, January 26, 2022: “We’ve added inventory adjustment reasons to allow you to assign, and better track changes to your inventory”; SH-E-55d73be2), and the adjust popover's Set To and Adjust By (SH-E-48519b5e). The cells of CM-INV-001 to CM-INV-004 and CM-INV-008 to CM-INV-010, read in one call, hold no other place for it: CM-INV-002, the inventory history, is where SH-E-3c6ba4d2 says the changes are viewed ('the inventory history page'), not the form.
- **Each line:** CM-INV-001 `core`, no scope (the form's options as captured on capture-plus, a capture's label, not a condition the platform states), the label as the term, the value (`cycle_count_available`, `received`, `restock`, `damaged`, `shrinkage`, `promotion`) in `reading`, as `method/held_tracking_carriers.py` keeps a carrier's identifier in its reading (SH-102).
- **No filler** (see "Where B-extent and the brief differ"): a reason names no third party and no law, so it isn't a slot filler by B-extent's definition. The carriers took their label as the filler because each carrier is a third party.
- **No line on what a reason names:** counts (CM-INV-003), returns (CM-RET-003), promotions (CM-MKT-001, CM-MKT-003) and the unavailable state Damaged (SH-E-58752638, another list of the same cell) take none, by the ruling after SA-41, as SH-102's carriers take none on CM-SHP-015. CM-RET-003 and CM-MKT-001/003 were the checker's leads, by 'return' and 'promotion' only.

**H26. A note that its page repeats is one entry, read in each section it stands in** (as the brief has it for a line Salla's plans page repeats). SH-E-3d0e19e9 is the POS Pro note of the page Inviting users, which the page sets twice (`items.jsonl` lines 3904 and 3906, positions 1 and 3): in its section on user permission requirements, over who can manage POS staff, and in its section Add POS app-only users. Its lines name both (@11110934).

**H27. A partner organization named as an alternative condition takes its own line on CM-PTN-002, under its own condition** (the ruling after SH-69). Three notes make roles at the organization's level (the Organization role category; custom organization-level roles) available on Plus or to a partner organization: SH-E-68aa6f5c, SH-E-2fe85378, SH-E-7001d6da.
- The Plus store's or organization's roles stay on CM-STF-002, `core`, scope `Plus` (with SH-E-68aa6f5c's 'multi-store organizations not on the Shopify Plus plan').
- A partner organization's roles are those it gives its own users, the partner's employees: CM-PTN-002 `core`, scope `Partner organization`. That cell is 'the partner's account or organization, with … its employees', and its reading found 'a partner's employees' nowhere for Shopify.
- SH-E-7001d6da's page is the Partners help's, its section 'Create a role for your Partner organization' (@11374916).
- The alternative is CM-STF-002 alone, the partner organization added to its scope (couldn't tell, 2).

## The new things

None. The searches for things no lead or earlier line named, before placing them (`caps --terms`, and greps of the placements):
- 'secure sign-in; two-step; 2-step; authentication; passkey; login': CM-TRU-001, as for SAML, SCIM, domain verification and the organization's security settings.
- 'deactivate; close store; store status; pause and build; closing': CM-ONB-002 for deactivation (as SH-E-d436cf76's cancel route); CM-ONB-002's and CM-OPS-004's store status are homonyms of the organization's Store status (CM-ACC-003).
- In the placements: offline checkout and payments, activity log, storage limit and paid storage, rollouts ('might not be available', 'rolling out'), Send HTTP request, workflow templates, Shopify Flow's supports and qualities, tax exemptions and product categories in tax, business entities, expansion stores and store grouping, SCIM, Store status, deactivation, POS roles, organization roles, user groups, POS-only staff, and the adjust-available form ('adjustment reason', 'Adjust by', 'Manage inventory').

## CHANGES, each read again against its source

**CM-AUT-001 gains `own-service`** (lines 12, 13, 15 and 17: SH-E-8f852473's Flow and its Send HTTP Request action, SH-E-631f41f4's B2B workflow templates, SH-E-35a0cc4d's 'This action').
- Each note is on Shopify Flow's own pages: 'Shopify Flow is a free app available on the Basic, Grow, Advanced, and Plus plans'.
- Flow's maker statement is held: 'Today we’re introducing test runs in Shopify Flow' (SH-E-0678ff26; `rules/merchant-changelog.md`, section 3). The ruling after SH-55 aligned 38 Flow lines to `own-service`; 75 earlier lines that name Shopify Flow are `own-service` on CM-AUT-001.
- The plans are each line's scope (the ruling after SH-30). The checker compares with the concern map's cell, which has no `own-service`. Kept.

SH-E-8f852473's third line, 'tasks created by custom partner apps' on Plus, is `extension-point`, which the cell already holds.

## The other NOTEs

- **`core` on a product named with the platform's brand** (lines 5, 6, 36, 45, 47, 49, 59). Each is a CM-POS-001 line whose term is 'Shopify POS Pro subscription' or 'activity log for Shopify POS'. POS is the platform's own sales channel, which the plans include, and stays `core` (the ruling after SH-55), as in SH-31 and SH-32.
- **`own-service` on CM-AUT-001** (4 lines): Shopify Flow, by its held maker statement (above).
- No container, footnote mark or app's embedded page is in the batch, and the checker found no quote missing.

## Entries I couldn't tell, and what would settle each

1. **SCIM** (SH-E-3225088d, SH-E-923486df, SH-E-6fd31228).
   - On CM-TRU-001 alone: its note holds 'for Shopify organizations MFA management, SAML and SCIM', and SH-E-13eb8f17 placed 'our SCIM implementation' there.
   - SH-E-3225088d says SCIM is set up 'to create and manage users', on the page Inviting users, and SH-E-6fd31228 names it 'SCIM user management'. A CM-STF-001 line on each is the alternative: users provisioned from an identity provider are staff accounts.
   - Settled by: the coordinator's reading of CM-TRU-001's note against CM-STF-001's thing.
2. **Roles in a partner organization** (H27; SH-E-68aa6f5c, SH-E-2fe85378, SH-E-7001d6da). On CM-PTN-002 under its own condition, beside CM-STF-002 on Plus. If a partner organization's users are read as staff like a store's, the three CM-PTN-002 lines go, and CM-STF-002 takes the partner organization in its scope. CM-PTN-002 then stays without its employees.
3. **Store status** (SH-E-15b71a61). On CM-ACC-003: the status of each store in the organization's Stores list, 'either active or pending Shopify Plus contract addition' (@11061877). CM-PLN-002, the Plus contract, is the alternative, since the status is the store's place in that contract.
4. **B2B companies in Flow's workflows** (SH-E-631f41f4's second line). On CM-B2B-002, `core`, `Plus`, the page's own words kept (H20). If the coordinator reads the companies as named in passing, where the workflows use them (H10), the line goes and the entry keeps its Flow line.
5. **Deactivating a Plus store** (SH-E-f0bb74b8). On CM-ONB-002, the store's closure, with Shopify Plus Support as the way, named in passing. A CM-ONB-003 line for Shopify Plus Support is the alternative, here and on the five expansion stores notes (SH-E-6a4796a6, SH-E-4657f7da, SH-E-b33c6183, SH-E-e5e5e9f3), where Plus Support assists with 'complex store management tasks'.
6. **Sidekick recommendations** (SH-E-0387bfbe). `shows`, 'rolling out gradually, so they might not be available in your store yet', read as a release to only some stores (H5), as SH-E-ad73c84d's 'might not be available to your store'. If a gradual rollout is read as offered to every store, the line is `core`, as CM-AIA-002 already holds.
7. **Tax calculation by product categories** (SH-E-1c669df9). On CM-TAX-002, `shows`, scope United States, from the note's 'sales to customers in the United States'. The tax overrides and the product categories are named in passing.
8. **A store's default business entity** (SH-E-1226f169). On CM-ACC-004, the entity the store operates as, changed through Shopify Support where the store 'uses multiple entity payment accounts' (a condition on its setup, H3). CM-ACC-005, selling with several entities, is the alternative, since the note is about stores that do.
9. **The adjustment reasons' filler** (H25). Placed with none, against the message's 'its label the filler'. If the coordinator wants the labels as fillers, a script can copy each line's term into its `filler`; nothing else in the lines changes.

## Items and sources

- **`inventory-adjustment-reasons` holds 7 items, and 6 have entries.** The first item, `{"position": 0, … "label": "Correction", "value": "correction"}` (`items.jsonl`, line 1), has no entry in `held/shopify/entries.tsv`, and no other batch holds it. `source.html` and step 19's text (`steps/019.text.txt`, line 48) state it as the first reason. It would take the same line as the others: CM-INV-001 `core`, term Correction (H25). A problem with the build (problems, 2).
- **`help-notes`:** the items agree with the pages read. Each item's `text` is its aside's text, and its `html` is the aside as the page holds it. As SH-30 to SH-32 found, the text sets a space between a link's words and the punctuation after them ('Shopify POS Pro subscription .', 'Store manager , Cashier'); my quotes stop before that space.
- SH-E-3d0e19e9 stands for two asides of one page (H26).

## For the second stage: stated on the notes' pages or held items, held by no entry

In `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz`, at the record and the line of `warc_text.py`'s print, unless another file is named:
- **@9359479, lines 14 and 15, for CM-POS-001 and CM-TRU-003:** 'Events are kept in the activity log for Shopify POS for 1 year.', a retention quality; the log can't be exported from the admin. Lines 24 to 37: the events captured and not captured.
- **@9420994, for CM-CNT-001's qualities** (the same tables SH-31 listed at @6972882):
  - line 581 on: the storage limits for each plan;
  - lines 627 to 651: the paid storage increases, '$100 USD/month per 1 TB' and '$1,000 USD/month per 10 TB', by plan.
- **`help-notes` items 3369 and 3370 (class `note`, not selected), for CM-CNT-001:** Plus and Enterprise stores contact Shopify Support for increased video and 3D model upload limits.
- **`help-notes` item 3318 (class `note`), for CM-POS-001:** 'Offline checkout isn't available for retail locations in France.', a country where the feature is stated unavailable.
- **`help-notes` item 3426 (class `sidekick`), for CM-AIA-002:** Sidekick recommendations, 'including Sidekick Pulse insights', shown as cards in the Home feed.
- **@9355812, line 24, for CM-STF-001 and CM-STF-002:** 'You can create an unlimited number of POS app-only staff', added by the owner or by a POS role with the Manage Point of Sale staff permission.
- **`help-notes` item 3905 (class `note`), for CM-STF-001's plan line:** a store on the Basic or Starter plans can't add users.
- **@11061877, lines 23 to 70, for CM-ACC-003:** the store statuses' and store types' tables of the organization's Stores list.
- **@11067602, for CM-ONB-002 and CM-PLN-002:**
  - line 39: deactivation requires signing in and completing any required two-step authentication challenge;
  - line 41: Shopify's no-refund policy for subscription plans, section 5.10 of its Terms of Service;
  - line 50: a deactivated store's myshopify.com address can't be used again;
  - line 59: invoices after deactivation.
- **@11210750, lines 6 to 12, for CM-TRU-001:** domain verification proves ownership of the users' email domains and opens SAML, SCIM and two-step resets.
- **Run `20261005T124111Z-journey-product-subroutes`, for CM-INV-001** (the register: 'the action types and unavailable categories are in the steps ARIA and text only'):
  - `steps/017.text.txt`, lines 44 to 46: the adjust form's action types, Set to and Adjust by;
  - `steps/014.text.txt`, lines 37 to 45: the unavailable inventory's categories, Damaged, Quality control, Safety stock and Other;
  - `steps/019.text.txt`, line 48: Correction, the reason with no entry.

## Problems with the brief or the scripts

1. **`earlier` found a lead for 2 of the 66 entries** (SH-E-f8cb3d66 and SH-E-b367d2e1, by the label 'Groups').
   - The other notes key on a phrase no line cites, or on the whole sentence ('This feature is available only…').
   - The adjustment reasons key on their labels, which no line cites, though SH-E-3c6ba4d2 and SH-E-55d73be2 place 'inventory adjustment reasons'. A key from the structure's container ('Select adjustment reason') or its register row would reach them.
   - I grepped the placements for each feature's own words instead (the new things, above).
2. **The build left out the first item of `inventory-adjustment-reasons`** (Correction), as "Items and sources" says. The coordinator may add its entry and its line.
3. **`held_tracking_carriers.py --help` runs the script:** it printed '203 carriers take CM-SHP-017's line; 20 other entries stay for an agent (SH-101)' instead of a usage. `git status` showed no file it changed. The brief says each script's `--help` says what it prints; this one has none.
4. **The checker's CHANGES compare with the concern map's cell,** so Flow's `own-service`, which 75 earlier lines give, shows as a change again (as SH-30 and SH-31 found for other cells).

## Where B-extent and the brief differ

- **The adjustment reasons' filler.** The message for this batch says to give each reason the form's line, 'its label the filler, as `method/held_tracking_carriers.py` did for the return form's carriers'. B-extent defines a slot filler as 'a third party or a law that a statement names as doing the capability, or as setting its terms', and the brief's rule 5 says the same. A carrier is a third party; a reason ('Damaged', 'Theft or loss') is neither. So I followed B-extent: the label is the term and the filler is empty (H25; couldn't tell, 9).
- Otherwise none found in this batch.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 66 of 66 entries, no problem. With this batch the help notes are placed whole (SH-30 to SH-33).
- **The one `CHANGES` stands:** CM-AUT-001 `own-service`, on Flow's own pages, as Flow's other 75 lines are.
- **H25 stands as the batch wrote it:** the adjustment reasons take CM-INV-001 `core` with no filler. A filler is a third party or a law (the changelog digest's rule 51), and a reason such as 'Damaged' is neither. The carriers took their names as fillers because each is a third party, so the coordinator's prompt was wrong to ask for a filler here.
- **The missing 'Correction' isn't a build fault of the kind the batch supposed.** The concern map cites the whole list (SH-S-2861, 'from line 1 (one option per line; first option quoted)'), and the build reads that citation as line 1 alone.
  - So 'Correction' was read, and so were the other six. They repeat a list the model read, on the line its cell gives it.
  - The same holds for the tracking carriers (SH-102) and the return reasons (SH-97). The build's reading of 'from line N' and of 'lines A-B' citations is recorded in `shopify/amendment-notes.md`, for the amendment and the next rebuild.
- **The rules H24 to H27 stand.**
- **The open readings stay as placed:** SCIM on CM-TRU-001, the organization's store status on CM-ACC-003, Flow's B2B companies on CM-B2B-002, Sidekick's recommendations `shows`.
- **Cost:** 17.0 million tokens over 84 requests, about 258,000 an entry. The context reached about 310,000 tokens.
