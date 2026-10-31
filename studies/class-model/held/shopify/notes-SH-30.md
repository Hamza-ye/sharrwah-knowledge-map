# SH-30: Shopify's Help Center notes, the first 80 (high)

**What the batch is.** 80 entries of `help-notes` (observed-sh at `e38dc17e3`, `structures/shopify/help-notes/help.shopify.com@en-md/items.jsonl`, lines 5 to 716): the asides of the English `.md` pages whose class is `note note-plan` (plan requirement), `note note-staff-permissions` or `note note-beta` (early access), as `selection.tsv` reads them. Pages from `ai-powered-tools` to `fulfillment/…/dhl-eu`, in the structure's order. No batch had placed this structure: the rules below are the ones SH-31 to SH-33 should keep, for the coordinator to check.

Each item holds the aside's heading, text and `html`. Its source is the page's record in the run `20260930T003703Z-help-en-md` (`held_index.py <page>` gives the offset; `warc_text.py` prints it). I read a page where the note's own words left its feature, its scope or its maker open: nine pages, each cited in the line that rests on it.

**Count.** 79 lines over 80 entries:
- 74 entries on capabilities, 6 `out` (the admin's refreshed design, SH-E-84996116, SH-E-869f0c61, SH-E-225c62a1, SH-E-ff3cf28a, SH-E-9f6e707c, SH-E-73cb87ad), no `new`;
- supports: `core` 40, `own-service` 26, `shows` 8, `extension-point` 3, and 2 `out` lines.

## The rules my lines follow (H1 to H13, for SH-31 to SH-33)

**H1. A note's thing** is the feature its own words name ('Media generation with Sidekick', 'a delivery method customization using Checkout Blocks'). Where its words leave the feature open ('this feature', 'Some apps'), the page's own words around the note decide: its title, the section the aside stands in and the paragraph after it (brief, rule 1). A note's page address alone makes no line. The item's `html` holds the links the text drops: read them where the note names its feature by a link ('feature test drive' opens `organization-settings/test-drive`).

**H2. Its support is its feature's,** as the model and the earlier batches give that feature:
- Shopify's own admin feature: `core` (Sidekick, catalogs, the theme editor, bot protection, identity providers, segments, discounts);
- a first-party app's feature: `own-service` where a held statement names Shopify the app's maker. Checkout Blocks is the case: 'we’re upgrading the Checkout Blocks app' (SH-E-a2643162; the ruling after SH-35).

A note's plan requirement is the feature's condition, not a plan line: it makes the plans the line's scope and leaves the support the feature's. A plan line (a plan table's row, a plan's own list) stays `core`, as the ruling after SH-55 has it. This is a reading, and 26 lines on 23 entries rest on it (the first item under "couldn't tell").

**H3. Scope.**
- A list of plans goes as the plans' labels, as the pricing batches write them: `Basic;Grow;Advanced;Plus`, `Grow;Advanced;Plus`, `Advanced;Plus`, `Plus` for 'the Shopify Plus plan', `Plus;Enterprise` for 'Shopify Plus and Enterprise', `Enterprise` for “Shopify's Enterprise offering”.
- An open range goes in the note's own words: `Basic plan or higher`, `Basic Shopify plan or higher`. It is quoted where it holds 'and': `'Advanced plan and higher'` (the ruling after SH-38).
- 'all plans' takes no scope, its words in `reading`, as SH-38's SH-E-58939e82 keeps them.
- A country list the note states for its feature is its scope (SH-E-1cf32bfc's 15 countries). Where the note names only a region ('in Europe', 'certain origin countries and regions'), the page's own country line is the scope, cited in `reading` (SH-E-4a6e5110).
- The `reading` takes:
  - a condition on the store's own setup or data: 'have customer accounts set up', 'with a connected identity provider', 'who use Shopify Capital', 'If you previously added companies', “If you've activated the … feature test drive”;
  - a condition on the device: 'in a desktop browser'.

**H4. One feature under two conditions** takes a line for each, on its capability, each with its own scope (the rulings after SH-34 and SH-69). Examples:
- catalogs: 'up to 3 active catalogs' on Basic, Grow and Advanced, unlimited and assigned to company locations on Plus;
- Checkout Blocks: its content blocks on the Basic plan or higher, 'All other features' on Plus.

A second feature the note names under its own plans takes its own line ('Theme editor customizations by market … Advanced plan and higher', beside the catalogs).

**H5. Release markers.**
- A `note-beta` saying early access, or 'available only to certain merchants' or stores: `shows`, its words in `reading` (the brief's rule on release states).
- A feature test drive, enabled by the merchant before its release: `core`, with its plans as scope and its release date in `reading` (the ruling after SH-34).
- The test drive itself takes CM-EVO-001's line where the note makes it the feature's way of being offered: 'available only as a feature test drive', SH-E-0e1c25b9. It takes none where the note only names it as the condition of a caveat (SH-E-a279d2be, SH-E-98f2f52d, SH-E-290a45a9).

**H6. The admin's own look is `out`,** whatever the heading: 'A refreshed design for the Shopify admin is rolling out gradually', which 'changes only the appearance and layout of the Shopify admin' (SH-34's E1; the ruling after SH-37). These notes stand under 'Early access' on Sidekick's pages: where Sidekick's icon stands is that layout.

**H7. A staff permission note** is its feature's line, on the capability of what the permission gates, the permission named in `reading`. The permission's own line is the permission tree's (SH-E-323d6b61: Form 1099-MISC on CM-TAX-009; View tax documents is SH-E-11b87110's).

**H8. A note that retires a feature and names its replacement** supports the replacement (SH-34's rule 9). Shopify Scripts' end, with 'transition to Shopify Functions', is `core` on CM-APP-005, as SH-E-677df824's line. The retired feature's plan (Scripts on Plus) is not the replacement's scope: no scope.

**H9. A caveat about one feature's effect on another** takes a line for each, both with the note's scope, the affected thing by what its words show. Ship and pickup in one order on:
- checkout customizations, which the merchant should 'Confirm … render correctly': `shows` on CM-CHK-004;
- discount apps that 'might give you options': `extension-point` on CM-MKT-004;
- B2B pickup locations: the same capability, CM-SHP-007.

**H10. What a note names in passing takes no line:**
- where a feature is assigned or used: the catalogs' B2B markets and company locations, kept out of `terms` too;
- 'Learn more about …' links;
- the page's own subject named as context: a Balance rewards page for a 1099-MISC note.

**H11. Checkout Blocks' features go on the capability of what each does** (the ruling after SH-57), as SH-34 to SH-41 placed them, all `own-service`:
- its blocks and its branding editor: CM-CHK-003;
- its custom field block: CM-CHK-009, and CM-CHK-003 as a block;
- its custom discounts: CM-MKT-004;
- its delivery method customizations: CM-SHP-013;
- its payment method customizations: CM-PAY-019;
- its address blocker: CM-CHK-005.

The pages say what each is: 'powered by Shopify Functions' for the customizations (@452303).

**H12. Third parties' apps that a note says do a thing in the checkout** are `extension-point` on CM-CHK-004, with the note's plans: 'an app that customizes the information, shipping, and payment pages of checkout'.

**H13. Leads that are no leads here:**
- CM-ORD-003 (by 'order status'): the 'Order status page' is the buyer's page after checkout, its note's homonym;
- CM-OPS-004 ('status'), CM-SHP-023 ('line, plan'), CM-PTN-010, CM-APP-012 and CM-API-013 (common words);
- CM-MKS-009 for a note's country list, whose thing is the feature offered in those countries.

`earlier` prints only the headings as keys (problems, 1).

## The new things

None. The searches for things no lead named, before placing them:
- 'Scripts; Script Editor': only CM-SFR-004's script tags, a homonym. Scripts is placed on its replacement (H8).
- 'ship and pickup; mixed delivery; split shipment': none, so CM-SHP-007, as SH-E-5e991683's line.
- 'contextual; customer type': none, so CM-SFR-002, as SH-E-d02463ae's line.
- 'address collection; address field; additional address': none, so CM-CUS-008, as SH-E-861b8676's line.
- 'custom discount; order discount; shipping discount': CM-MKT-004.
- 'payment customization; delivery customization; address blocker; address validation': CM-PAY-019, CM-SHP-013 and CM-CHK-005.
- 'saved payment; vault': CM-PAY-022.
- 'Shopify Balance; Capital; financing': CM-PAY-023 and CM-PAY-026.
- 'sales staff; sales rep': CM-B2B-006.
- 'deposit': CM-PAY-008, as SH-E-86c0c5a9's line.
- 'media generation; image generation; generate apps; Sidekick; Pulse; screen sharing': CM-AIA-002, CM-CAT-007 and CM-APP-009.

## CHANGES, each read again against its source

The checker compares each line with the concern map's cell, not with the lines of earlier batches. Three of the seven CHANGES are already in SH-34 to SH-41's lines.

**CM-CHK-003 gains `own-service`** (lines 32 to 44). The lines are Checkout Blocks':
- its dynamic and static content blocks, its custom field, line item content, line item edit and shipping & payments icons blocks;
- its branding editor;
- 'All other features of Checkout Blocks', on Plus.

SH-35 (SH-E-a2643162) and SH-38 (SH-E-58939e82) gave the same, by the ruling after SH-35. Kept.

**CM-CHK-005 gains `own-service`** (line 54). The address blocker, which, as its page says, 'allows you to block unsupported address formats and types with specific field validation' (@474765). SH-34, SH-35, SH-37 and SH-41 gave Checkout Blocks' checkout rules the same. Kept, with its sunset (couldn't tell, 3).

**CM-CHK-009 holds nothing and becomes held, `own-service`** (line 36): the custom field block, read against its page (@394676):
- 'You can collect additional customer information with the' Custom field block;
- 'Custom fields can be optional or required';
- its input types run from text and dropdowns to checkboxes and a date picker;
- what the buyer enters is saved to the order as a metafield, an attribute or the order note;
- its templates are Agree to terms, Birthday and Gift message.

That is the capability's thing, fields the merchant adds for the buyer to fill in when ordering. Checkout Blocks itself provides the field (the ruling after SH-57), and its maker is Shopify (H2). Kept.
- The cell's reading had found only 'Editing the checkout form options' (SH-I-2107), the built-in form's options. The page says Checkout Blocks doesn't add fields into the existing checkout forms; its block stands above or below them.
- The metafields Q1's U-005 ruled apart are only where the field's answer is saved.
- CM-CHK-003 also takes the block's line (H11).

**CM-MKT-004 gains `own-service`** (lines 45, 46, 47 and 55): custom discounts, custom order discounts and custom shipping discounts using Checkout Blocks. The section's page (@438067):
- 'Checkout Blocks extends the default Shopify discount types to offer custom shipping and order discounts.';
- they apply as discount codes or as automatic discounts;
- 'all custom discounts from Checkout Blocks are automatically removed from your store' when the app is uninstalled.

I read them as the app's own discount logic, which is CM-MKT-004's thing, 'apps' custom discount logic run by the platform'. The app is Shopify's, so `own-service`. Kept, with an alternative (couldn't tell, 2).

**CM-PAY-019 gains `own-service`** (lines 49, 52, 53 and 57): the payment method customizations. The section's page: 'You can use Checkout Blocks, powered by Shopify Functions, to reorder, rename, and conditionally hide delivery and payment options in checkout.' (@452303). SH-38's SH-E-d41524a3 gave the same. Kept.

**CM-SHP-013 gains `own-service`** (lines 48, 50, 51 and 56): the delivery method customizations. The same page, and the delivery page's 'Checkout Blocks lets you customize delivery methods in checkout in the following ways': hide, rename, reorder (@459010). That is a delivery customization function, written by Shopify's own app (the rulings after SH-35 and SH-57). No earlier line placed them; my grep of the placements found none. Kept.

## The other NOTEs

- **Lines 12 and 63** are `core` on a product named with the platform's brand. Shopify Functions is the platform's own API, not a separate product: CM-APP-005's cell gives it its own reference group, and Shopify invokes the functions itself. So `core` by B-extent's rule for the platform's own API. Shopify Scripts, the retired feature, is in `terms` and `reading`.
- **The 26 `own-service` NOTEs** are each Checkout Blocks (H2, H11).
- No quote was found missing, and no container or footnote mark is in the batch.

## Entries I couldn't tell, and what would settle each

1. **A first-party app's feature under a plan requirement** (H2; the 26 lines of entries 24 to 46, SH-E-df3866ca to SH-E-f695a1f3).
   - My reading: the note states the feature's condition, so the line keeps the app's support, `own-service`.
   - If the coordinator reads a Help Center plan requirement as a plan line, these 26 lines are `core`. CM-CHK-009 still becomes held, as `core`.
   - Settled by: the coordinator's reading of 'plan line' in the ruling after SH-55, against a help page's 'Plan requirement' aside.
2. **Checkout Blocks' custom discounts, CM-MKT-004 or CM-MKT-001.** The page names no function for its discounts, as it does for the customizations (@452303).
   - If they are read as discounts of Shopify's own kinds, codes and automatic ones that the app extends, the four lines go to CM-MKT-001 as `own-service`.
   - Settled by: a held statement that Checkout Blocks' discounts run as discount functions, or the coordinator's reading of CM-MKT-004 as the extension type alone.
3. **The address blocker** (SH-E-9f128374).
   - SH-E-9aa1c2ef's post states it deprecated, to sunset on August 31, 2026, replaced by address format validation (CM-CHK-005).
   - This page, captured on 30 September 2026, still documents it under a plan requirement. I placed it as the page states it, with the sunset in `reading`.
   - If the later post governs, the line is `shows`, a retired feature whose replacement is already on CM-CHK-005.
4. **Shopify Scripts' end** (SH-E-c1f71c64 against SH-E-b15a9334 and the nine after it). The pages differ:
   - the B2B quantity pricing page: 'reached end of life on August 28, 2025';
   - the Script Editor's pages: 'As of June 30, 2026, Shopify Scripts has been deprecated';
   - the changelog (SH-E-677df824): editing ends April 15, 2026, and execution June 30, 2026.

   Each line keeps its page's words. Settled by: whether the August 2025 date is Scripts' end for B2B quantity pricing alone (not stated).
5. **Media generation** (SH-E-ab2e31b1).
   - The note says 'with Sidekick', so CM-AIA-002. The page is 'Media generation in the file editor', for 'professional product images', so CM-CAT-007.
   - SH-35 put the file editor's AI image editing on CM-AIA-001 (SH-E-dd6647f3): a CM-AIA-001 line is the alternative to the Sidekick line.
   - Settled by: the coordinator's reading of a note that names Sidekick on a page about the file editor.
6. **Additional address fields** (SH-E-1cf32bfc).
   - On CM-CUS-008, as SH-34 placed the released ones (SH-E-861b8676, the page's five countries).
   - CM-CHK-003 is the alternative: the page is a checkout setting, Address collection preferences.
   - Settled by: SH-34's open question 5, whether the checkout's address form is CM-CUS-008's.
7. **Sales staff** (SH-E-766f4856).
   - On CM-B2B-006. The page calls them 'sales representatives', and says they 'place orders and view account information for their assigned customers' (@332426). That answers the cell's gap, 'No statement says what an assigned staff member does … or calls it a sales rep', for the coordinator's amendment.
   - The note's limit on staff accounts states no number: its CM-STF-001 quality is the words alone.
8. **Ship and pickup in one order** (SH-E-a279d2be, SH-E-98f2f52d, SH-E-0e1c25b9, SH-E-290a45a9).
   - On CM-SHP-007, as SH-34's SH-E-5e991683.
   - CM-SHP-006's reading cites the help-centre section 'Ship and pickup in one order in Shopify Checkout' (SH-I-2114) as `shows`. The coordinator may prefer CM-SHP-006, the parent of pickup and local delivery.
9. **'Some apps are available only to certain stores on the Shopify Plus plan'** (SH-E-c8a87df9).
   - Read with the page's app availability as the apps that customize the checkout's information, shipping and payment pages: CM-CHK-004.
   - The same section puts the apps for customer accounts on the Basic plan or higher, so I placed none on CM-CUS-014.
   - 'certain stores' may mean a release narrower than Plus. Settled by: the page's table, its 'App type' rows, which I didn't read row by row.

## Items and sources

- The items agree with the pages read: each item's `text` is its aside's text, and its `html` the aside as the page holds it.
- The text sets a space between a link's words and the punctuation after them ('Shopify Functions .', 'organization , and then'). A quote that runs past a link keeps that space; mine stop before it.
- `held_index.py` names three records for each page: the en-md run's, and two in `20261016T213535Z-help-en-ar-html-md`. The structure was read from the first, and my readings cite it.

## For the second stage: stated on the notes' pages, held by no entry

All in `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz`, at the record and the line of `warc_text.py`'s print:
- **@46654, line 19:** 'For a limited time, media generation in the file editor is available on all Shopify plans at no additional cost.' A price for CM-AIA-001 and CM-CAT-007, beside the note's plans.
- **@394676, for CM-CHK-009:** the custom field block's templates (lines 11 to 15), 'Checkout Blocks doesn't support' adding fields into the existing checkout forms (line 24), and its input types (line 47 on).
- **@361133, for CM-CUS-008 or CM-CHK-003:**
  - address autocompletion (line 45) and shipping address validation at checkout (line 96);
  - line 145: the released countries' extra address fields are required, and 'You can't change which additional fields are included'.
- **@509877, lines 14 to 71:** the checkout apps' availability by plan, a table of app types against 'Basic Shopify plan or higher' and 'Shopify Plus', for CM-CHK-004 and CM-CUS-014.
- **@1894029, line 18:** 'DHL Express Europe rates aren't displayed at checkout.', for CM-SHP-002.
- **@452303, line 9:** Checkout Blocks' customizations are deactivated and removed when the app is uninstalled, for CM-SHP-013 and CM-PAY-019.
- **@407625, line 19:** the line item edit block's selling plan selector, which 'isn't compatible with' Recharge: a lead for CM-SEL-001.
- **@474765, line 7:** Checkout Blocks' translations settings: a lead for CM-MKS-008.
- **@332426, lines 14 to 16:** sales managers and sales representatives, and the managers' control over which representatives work with which company locations, for CM-B2B-006.

## Problems with the brief or the scripts

1. **`earlier` finds no key of a note's feature.** For this structure its keys are only the notes' headings: 'Plan requirement', 'Early access' and 'Staff permissions'. Other batches cite those for other things (SH-13:13 on CM-MKT-006, SH-8:5 on CM-STF-002), so it printed no lead.
   - I grepped the placements for each feature's own name instead: Checkout Blocks, Scripts, ship and pickup, catalogs, identity provider, deposits, DHL Express, Capital flex, saved payment methods, Sidekick's features.
   - A key from the note's page address, or from the words before 'is available', would make `earlier` reach them for SH-31 to SH-33.
2. **The checker's CHANGES compare with the concern map's cell,** so a support an earlier batch already gave a cell shows as a change again (CM-CHK-003, CM-CHK-005, CM-PAY-019).
3. **The rulings file changed twice during the batch.** Neither change moves a line here:
   - the ruling after SH-41 makes a separate product of the platform's, such as Shopify Credit and its lending, `own-service`; the Capital flex lines are `shows`, in early access;
   - its corrections keep Shopify Balance the admin's own money account, `core`, and put AI for merchants outside the admin on the place's capability. My Balance line is `shows`, in early access, and my AI lines are on Sidekick and the admin's file editor.

## Where B-extent and the brief differ

None found in this batch.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem.
- **H2 is ruled as read:** a help page's plan requirement is the feature's condition, not a plan line (the ruling after SH-30). The 26 Checkout Blocks lines stay `own-service`, the plans their scope. The rules H1 to H13 stand for SH-31 to SH-33.
- **The `CHANGES` stand:**
  - CM-CHK-003, CM-CHK-005 and CM-PAY-019 gain `own-service` from Checkout Blocks. SH-34 to SH-41 had already given those supports.
  - CM-CHK-009 becomes held, `own-service`: Checkout Blocks' custom field block, which collects buyers' answers at checkout.
  - CM-MKT-004 gains `own-service`: the app's own custom discounts, 'apps' custom discount logic run by the platform'. The app makes them itself (the ruling after SH-57).
  - CM-SHP-013 gains `own-service`: the app's delivery method customizations, 'powered by Shopify Functions'.
- **The open choices stay as placed:**
  - Media generation on CM-AIA-002, by the note's 'with Sidekick', and on CM-CAT-007, by its page;
  - the additional address fields on CM-CUS-008, and ship and pickup in one order on CM-SHP-007, as SH-34 placed both;
  - the address blocker as its page of 30 September states it, its sunset in the reading;
  - 'certain stores on the Shopify Plus plan' on CM-CHK-004;
  - each page's own date for Scripts' end.
- **For Shopify's amendment:** the sales staff page calls them 'sales representatives', which fills the gap CM-B2B-006's cell states.
- **For SH-31,** from SH-79's search: the help note 'MB WAY is in early access, and isn't available to all eligible merchants' (SH-E-413b6623) is `shows` on CM-PAY-017, with MB WAY as its filler (H5). The plan rows' MB WAY rates stay `core`.
- **`earlier` now keys a help note's feature:** its words before 'is available', with the heading dropped. The headings themselves ('Plan requirement', 'Early access', 'Staff permissions') are no longer keys, since other things cite them. For SH-31 it finds eight leads, among them Shopify Inbox, Shopify Scripts, Feature test drives and Shopify B2B.
- **Cost:** 18.1 million tokens over 84 requests, about 226,000 an entry. The context reached about 362,000 tokens.
