# SH-31: Shopify's Help Center notes, the second 80 (high)

**What the batch is.** 80 entries of `help-notes` (observed-sh at `e38dc17e3`, `structures/shopify/help-notes/help.shopify.com@en-md/items.jsonl`): the asides of the English `.md` pages whose class is `note note-plan`, `note note-staff-permissions` or `note note-beta`, as `selection.tsv` reads them, from the draft orders page (`fulfillment/managing-orders/create-orders/create-draft`) to the abandoned checkouts page (`promoting-marketing/create-marketing/abandoned-checkouts`). SH-30 placed the 80 before them; I kept to its rules H1 to H13 and its coordinator's check, and to the ruling after SH-30.

Each item holds the aside's heading, text and `html`. Its source is the page's record in the run `20260930T003703Z-help-en-md`. I read the page where the note's own words left its feature, its scope or its maker open: 25 pages, each cited in the line that rests on it as `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz@<offset>`.

**Count.** 88 lines over 80 entries:
- 77 entries on capabilities, 1 `new` (SH-E-24e89d53, Planet), 2 `out` (SH-E-ed5a8135, SH-E-2742525b: the admin's refreshed design, H6);
- supports: `core` 54, `shows` 26, `own-service` 5, `extension-point` 2, and 1 `out` line.

## The rules I added (H14 to H20, for SH-32 and SH-33)

**H14. A note under a 'Plan requirement' heading that names no plan takes no scope.** The heading is the aside's class, not a condition. The note is placed by what its words state:
- the Shop app's notifications that merchants can't turn off (SH-E-a5c1a0b1);
- the files a store keeps above a lower plan's storage limit (SH-E-f79de107).

**H15. A note's linked words can give its scope where its own page gives none.**
- 'Some additional tax fields are in early access' links to the international considerations page's section Additional tax fields in checkout.
- That section's table, 'Countries and regions with additional tax fields that are in early access', names 14 countries (@2963614). They are the scope of the note on that page (SH-E-f9025a10) and of its twins on the China pages (SH-E-7a3dd6f4, SH-E-a8d0c489).
- This extends H3's 'the page's own country line', by H1's reading of the item's `html` links.

**H16. A staff permission note takes its feature's support, including a release state its page states.** The Markets permission note on the shipping options page (SH-E-13126680) is `shows`: the same page's early access note (SH-E-890f8e61) states the feature available only to certain stores (H2, H7).

**H17. 'Only the store owner can …' is a gate on the user, like a staff permission (H7).** The line is the feature's, with the owner (or the Administrator role) named in `reading`, and no CM-ACC-001 line:
- activating Shopify Payments (SH-E-69ce97e1);
- Shopify Payments' verification requests (SH-E-6d1a7544);
- a POS device's first login (SH-E-d91345c6);
- Shopify Network Intelligence (SH-E-00f7256d).

**H18. A first-party app named as a caveat's condition takes its own feature's line, under the caveat's plans (H9).**
- The case: 'even if you use the Translate & Adapt app for market-specific wording' (SH-E-c47c3072).
- The line is on CM-MKS-008, scope `Basic;Grow`.
- It is `own-service`, by the app's held maker statement, “we've added automatic translation updates to Translate & Adapt” (SH-E-04551fad; the ruling after SH-55).

**H19. Shopify Scripts on a page that states no end goes on its replacement, with no scope** (SH-E-65e0c901).
- The international discounts page still says 'Shopify Scripts is available only on the Shopify Plus plan.'
- The held posts state Scripts' end on June 30, 2026, with Shopify Functions its replacement (SH-E-677df824).
- So the line goes on CM-APP-005, as H8 and `earlier` place Scripts' other notes. Plus was the retired feature's plan, so the line takes no scope.

**H20. A page whose plans differ from a post's keeps its own words, each in its line.** The theme overrides page keeps 'Shopify B2B is available only to stores on the Shopify Plus plan' (SH-E-d300c8ae), while SH-E-86c0c5a9's post of April 2026 states native B2B features on Basic, Grow and Advanced too. This is SH-30's open question 4, for Scripts' dates, read the same way.

## The new thing

**Planet** (`new:Planet`, `own-service`, scope `Plus`; SH-E-24e89d53, 'The Planet checkout extension'):
- It is SH-50's new thing (SH-E-bc581483) and SH-55's (SH-E-31dd37c9), named the same way.
- **Maker:** 'Planet app from Shopify' (SH-E-31dd37c9) and “we're releasing the Planet app” (SH-E-41c88730), by `makers`.
- **What it does:** the extension 'lets your customers add $0.50 USD to their checkout to make their shipment carbon neutral and fund high-impact carbon removal projects' (@2468292). It needs Planet installed and an active Planet subscription.
- **Place of its own:** none held. Its App Store listing isn't one by B-extent, and the help page is a guide.
- **Proposed domain and parent:** as SH-50 proposed. In English only, since this batch reads no Arabic.
- **Searched:** 'Planet; carbon; sustainab; carbon-neutral' found no capability (`caps --terms`).
- **The checker's leads:**
  - CM-APP-011 is the platform's own apps. SH-50 and SH-55 placed a line there where the card itself named Shopify the maker. This note doesn't, so it has no CM-APP-011 line.
  - CM-CHK-004 is apps' blocks in checkout. By the ruling after SH-57, Planet's checkout extension is Planet's own thing: carbon-neutral shipping offered at checkout. So it has no CM-CHK-004 line (couldn't tell, 4).
  - CM-PLN-001 and CM-PLN-002 matched only by name, on the plan's words: no lead.

## CHANGES, each read again against its source

**CM-MKS-008 gains `own-service`** (line 44, SH-E-c47c3072):
- **What the line is:** Translate & Adapt's 'market-specific wording for the same language', which can't make homepage banners, announcement bars and block content differ between markets on Basic or Grow.
- **Earlier lines:** SH-36's lines 104 and 136 already give Translate & Adapt `own-service` on CM-MKS-008, on the posts “we've added automatic translation updates to Translate & Adapt”. The ruling after SH-55 aligned the app's lines.
- **Why it shows as a change:** the checker compares with the concern map's cell, not with the earlier batches.
- Kept.

My first draft also had a CHANGES on CM-SHP-007, which would have gained `extension-point` from the pickup service (SH-E-c930b8af). Read again, the page's link opens shopify.dev's local pickup delivery option generators. CM-SHP-019's cell holds that target, `local_pickup_delivery_option_generator`, so I moved the line there, `extension-point` on Plus. That cell already holds `extension-point`, so CM-SHP-007 doesn't change.

## The other NOTEs

**`core` on a product named with the platform's brand** (lines 5, 33, 39, 55, 65, 74, 79, 80, 81, 89). Each is the platform's own feature, not a separate product:
- Shopify POS and its POS Pro subscription: the platform's own sales channel, which the plans include (the ruling after SH-55).
- Shopify Scripts and Shopify Functions: the platform's own API (SH-30's NOTE on lines 12 and 63).
- The Shopify Help Center's Support Inbox: Shopify's own support.
- Shopify Payments, activated in the admin.
- Shopify Network Intelligence, a setting of the admin.
- Shopify B2B, the admin's B2B features.
- The Shopify Combined Listings app (line 81). It has no maker statement held (`makers` finds none), so it is `core` by what it shows, as CM-CAT-008's cell reads it and SH-38:159 placed it (the ruling after SH-36).

**`own-service`** (5 lines):
- the Shop app's notifications (line 13) and the store's posts in Shop (line 57): Shop does its things as `own-service` (the ruling after SH-34);
- Planet (line 19), Shopify Inbox (line 25; the ruling after SH-2) and Translate & Adapt (line 44).

**Line 13's first lead, CM-ORD-003 (order statuses), holds nothing** (SH-E-a5c1a0b1). The note names Shop's notifications 'for tracking updates and order statuses'. CM-ORD-003 is 'the stages an order is set to, which the merchant can customize'. The note shows neither the stages nor their customization, so it takes no line there. It is the homonym SH-30's H13 names, in another form.

No container, footnote mark or app's embedded page is in the batch, and no quote was found missing.

## Entries I couldn't tell, and what would settle each

1. **Scripts on the international discounts page** (SH-E-65e0c901, H19).
   - I put it on CM-APP-005 with no scope, as `earlier` places Scripts' lines.
   - The alternative is a line for the section's own use, currency-based discounts: CM-MKT-001, or CM-MKS-006.
   - Settled by: the coordinator's reading of a stale page against the posts that state the end.
2. **Partial payments** (SH-E-92a8c895).
   - On CM-PAY-020: collecting and recording an order's payments, by a vaulted or new card or manually.
   - The page limits them to 'orders with payment terms', and they include deposits, so CM-PAY-008 is the alternative, where SH-30 put deposits.
3. **Activating Shopify Payments** (SH-E-69ce97e1).
   - On CM-PAY-002, the service activated.
   - CM-PAY-003, its onboarding, is the alternative: the page is the account setup page.
4. **The Planet checkout extension** (SH-E-24e89d53).
   - On `new:Planet`.
   - If the coordinator reads a first-party app's checkout extension as CM-CHK-004's thing, it takes an `own-service` line there too, which would change that cell.
5. **Posts in Shop** (SH-E-583322c8).
   - On CM-CHN-002, `own-service`.
   - No capability holds a store's posts to its followers in a shopping app. Searched: 'posts; Shop posts; posts in Shop; social; followers; content marketing'.
   - If Shop's posts have a route of their own in the admin's Shop channel, not held here, they may be a new thing.
6. **A/B pricing experiments** (SH-E-359b938a, SH-E-f38c5743, SH-E-25fb8046).
   - On CM-CAT-013, `shows`, in early access.
   - They are a feature of the Smart Pricing app, which 'uses machine learning models to generate data-driven pricing recommendations' (@6617871).
   - No held statement names the app's maker. `makers "Smart Pricing"` finds only Managed Markets' 'smart pricing, duties, and taxes automated by Shopify' (SH-E-7c46cfa6), another thing.
   - CM-AIA-001, the platform's AI tools for merchants, is the alternative for the price tips.
7. **Return policy information on Shop's product pages** (SH-E-ada278b5). Its second line is on CM-CNT-008, the return policy. The page says the information is the return window set under Settings > Policies, so CM-RET-003's return rules are the alternative.
8. **Flat shipping rates from Managed Markets** (SH-E-6f99569e, SH-E-3da7c807).
   - Placed `shows` on CM-MKS-003 and on CM-SHP-001.
   - The page ties the rate to 'the prepaid label for the order' (@2867588), a lead for CM-SHP-002.
9. **The plans in the order routing note** (SH-E-03c916c7). I gave it no scope: its early access is for 'Partners enrolled in the early access program', and Plus merchants must join the Partners program. `Plus` is the alternative scope.
10. **MB WAY's scope** (SH-E-413b6623).
    - I took `Portugal` from the page, 'MB WAY is a local payment method in Portugal' (@5158646), by the brief's rule for a thing offered for a country.
    - The coordinator's decision named the support and the filler, not a scope.
11. **The subscription disclosure's wording** (SH-E-bd98b407, SH-E-57cade3b).
    - The texts edited go on CM-SFR-002, the theme content editor, as SH-E-45489c6c's line; the disclosure itself on CM-SEL-001; the cancellation policy on CM-CNT-008.
    - The coordinator may prefer all the wording on CM-SEL-001.

## Items and sources

- The items agree with the pages read. Each item's `text` is its aside's text, and its `html` is the aside as the page holds it.
- As SH-30 found, the text sets a space between a link's words and the punctuation after them ('Shopify POS Pro .', 'in early access ,'). My quotes stop before that space.
- **The Managed Markets shipping page** (@2867588) says 'Flat shipping rates from Managed Markets are in early access, and are available only to certain merchants.' twice:
  - in its opening paragraph (line 3), which is no aside, so no entry;
  - in the aside of its section (line 20), SH-E-3da7c807.

## For the second stage: stated on the notes' pages, held by no entry

All in `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz`, at the record and the line of `warc_text.py`'s print:
- **@6972882, for CM-CNT-001's qualities:**
  - lines 163 to 212, the file storage limits by plan: Starter, Pause and Build, Retail and Basic 100 GB, Grow 300 GB, Advanced 500 GB, Plus 1 TB, Enterprise 10 TB;
  - lines 216 to 245, the paid storage increases: $100 USD/month per 1 TB on Plus, $1,000 USD/month per 10 TB on Enterprise;
  - line 256 on, the video and 3D model limits by plan.
- **@2468292, line 6:** the Planet checkout extension's '$0.50 USD' added at checkout, a price for `new:Planet`.
- **@2339810, line 83, for CM-NTF-001:** 'If your store is on the Shopify Plus plan, then there is no Shopify branding in your customer notification email footers.'
- **@2963614, for CM-TAX-005:**
  - lines 98 to 121: the additional tax fields are 'activated by default for all stores', with no admin setting, deactivated through Shopify Support, shown only in the online store, and editable only by the `orderUpdate` mutation;
  - lines 128 to 175: the default countries' fields (Brazil CPF or CNPJ, China resident ID, Italy CF and PEC, Mexico RFC, South Korea PCCC).
- **@2867588, lines 23 to 29, for CM-MKS-003, CM-SHP-001 and CM-SHP-002:**
  - Managed Markets' flat rates are guaranteed with the prepaid label;
  - the cost is split between the rate at checkout and the product prices;
  - the merchant can absorb a set amount.
- **@3642300, lines 272 to 286, for CM-POS-001 and CM-PLN-002:**
  - POS subscriptions are chosen per location, monthly or yearly on Retail, Basic, Grow and Advanced, a 30-day cycle on Plus;
  - 'The first 20 POS Pro locations are included in all Shopify Plus plans'.
- **@7312257, line 28, for CM-MKT-022 and CM-B2B-001:** 'Abandoned checkouts are turned off by default for Shopify B2B', turned on by the owner through Shopify Support. It is an aside of class `note`, which `selection.tsv` doesn't select.
- **@2488605, lines 6 to 10, for CM-SHP-001:** shipping options by market roll out gradually, stores using shipping apps are upgraded later, and an opt-out window follows.
- **@2227111, lines 23 and 72, for CM-RET-003 and CM-B2B-001:**
  - return rules apply to B2B orders;
  - the return window shown on Shop's product pages comes from the Policies settings.
- **@3274294, lines 91 to 95, for CM-ONB-003:** Support Inbox shows a support ticket's status and the estimated reply time.
- **@4964341, lines 6 to 9, for CM-PAY-020 and CM-PAY-008:** partial payments by vaulted card (for B2B customers), new card, or recorded manually.
- **@2303789, lines 45 to 72, for CM-SHP-007 and CM-INV-006:** store transfers to a pickup location, with their processing time, and transfer exclusions by collection.
- **@6617871, line 3, for CM-CAT-013 or CM-AIA-001:** the Smart Pricing app's markdown and markup recommendations and its price tips for new products.

## Problems with the brief or the scripts

1. **`earlier` found leads for 8 of the 80 entries:** Shopify Inbox, Shopify Scripts, Retail markets, Theme editor customizations by customer type, Markets, Feature test drives, Shopify Combined Listings app and Shopify B2B.
   - For a note that begins 'This feature …' or 'Your store must be …', its key is the whole sentence, which no line cites.
   - A key from the page's section heading, or from the page address, would reach them.
   - I grepped the placements for the features' names instead: return rules, cancellation rules, deposits, ship and pickup, delivery dates, pickup points, POS Pro, tax ID fields, theme content editor, catalogs, Shopify B2B, Smart Pricing, Store Migration.
2. **The checker's CHANGES compare with the concern map's cell,** so a support an earlier batch already gave shows as a change again (CM-MKS-008, SH-36).
3. **The brand NOTE fires on the platform's own features** (POS, Payments, B2B, Network Intelligence, Scripts). The ruling after SH-55 already keeps them `core`.

## Where B-extent and the brief differ

None found in this batch.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem.
- **The one `CHANGES` stands:** CM-MKS-008 `own-service`, from Translate & Adapt, which SH-36 had already placed.
- **One line aligned:** the Combined Listings app's note (entry 81) is `own-service`, by the corrections with the changelog digest and the ruling after SH-30.
- **The MB WAY note** is `shows` on CM-PAY-017, as decided. Its scope is Portugal, by its page's own words.
- **The rules H14 to H20 stand for SH-32 and SH-33,** with H18 narrowed: a first-party app named in a caveat takes a line only where the caveat states what the app does. Otherwise it is named in passing (H10).
- **Planet** keeps the name SH-50 gave it, `own-service` on Plus. Its checkout extension takes no CM-CHK-004 line (open question 4, as placed).
- **Cost:** 22.0 million tokens over 101 requests, about 275,000 an entry. The context reached about 357,000 tokens.
