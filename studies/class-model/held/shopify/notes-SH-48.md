# SH-48: Shopify’s `editions`, Fall 2026, from Payments to Fulfillment (96 entries)

The batch reads `shopify/editions` at observed-sh `e38dc17e3`, `structures/shopify/editions/www.shopify.com_editions_fall2026/items.jsonl`: the rendered page's sections Payments, Operations, Shop, Marketing and Fulfillment, whole (96 entries, from the heading Payments to the last Fulfillment card; SH-49 starts at Developer). Its source is the archive record `raw/runs/20261030T162210Z-shopify-editions/fetch.warc.gz@1760606` (`source.html`). It follows SH-47's rules R47.1 to R47.6, as the coordinator's check after SH-47 narrowed R47.1, the Editions digest (`held/rules/editions-page-data.md`, its section 6 included) and the rulings in `review-H-rulings.md`'s last section.

96 entries, 160 lines:
- 90 entries on capabilities only;
- 2 entries `new` only (Admin search, Fees for products and collections);
- 4 entries `out`: the section headings Payments, Operations, Marketing and Fulfillment.

The heading Shop is a container on CM-CHN-002 (R48.2).

## Rules added (R48.n), for the coordinator to check

- **R48.1, a stack card and the text cards after it.** The rendered page lays a run of features out as one `article` with `data-card-variant="stack"` (media, a paragraph, sometimes notes and stats), then `article`s with `data-card-variant="text"` (one sentence each). The extractor keeps no variant, and the page marks no group (`source.html`; the rmx-data holds the components' props only). Each article is its own card, read by its own words (R47.2).
  - A stack card's release marker covers the features its own words name. The case is 'Features rolling out soon.' in Shopify Protect's card (SH-E-a26ff54f).
  - A text card takes that marker only where its only link opens the stack card's product and its words name no other product (the digest's rules 34 and 53). The case is SH-E-d7e84c6d, the custom fraud rules, whose only link is the Shopify Protect app and which the stack card names: 'set custom fraud rules with the' Shopify Protect 'app. Features rolling out soon.'
  - A text card that links a help page, or names another product, is read by its own words, with its own marker where it has one:
    - SH-E-f19a1a89, SH-E-72c67e8e, SH-E-53842bcf, SH-E-38acf118 and SH-E-ee196bb2, which link help pages;
    - SH-E-dbd247f1, which names Shopify Payments;
    - SH-E-59260ede, with its own 'Coming soon.'
- **R48.2, a section all of whose cards are Shop's.** Each of the Shop section's ten cards names Shop: its app, its website, its account. So the heading takes CM-CHN-002, as Sidekick's takes CM-AIA-002 (R47.1, narrowed). Its support is `own-service`, since Shop's things are (the digest's rule 11). Sidekick's heading line is `core`.
- **R48.3, a card in the Shop section.** Shop's own feature goes on its own capability, `own-service` (E102), with CM-CHN-002 `own-service` beside it where the card names the app, the website or the Shop account (E120):
  - the universal checkout and cart, CM-CHK-001 and CM-CHK-002;
  - order tracking, CM-SHP-017;
  - personalized recommendations and ranking, CM-MKT-023;
  - the agent, CM-AIA-005;
  - discount codes, CM-MKT-002;
  - synced carts, CM-CHK-010.

  Search across Shop's products is CM-CHN-002's alone, since CM-SFR-013 is the store's own storefront search (SH-E-09389545, SH-E-abe60090).
- **R48.4, a Shopify Shipping carrier newly offered in a country.** It takes CM-SHP-002 `core`, the carrier its filler and the country its scope, and CM-SHP-015 `shows`. This is the digest's rule 42, in force.
  - The cases are DHL Express (SH-E-73af70bb), DHL eCommerce (SH-E-95fbe447), UPS (SH-E-928f05bc) and Canada Post (SH-E-0ddce72f).
  - SH-34 (SH-E-2ae24465) and SH-36 (SH-E-d4730476) wrote CM-SHP-015 `core` on the same posts. The coordinator aligns one way or the other.
- **R48.5, a release marker on one item of a list.** In 'Microsoft Advertising, Snapchat, and soon X Ads' (SH-E-4af8f62d), X Ads is a thing of the same capability under its own condition. It takes its own CM-MKT-010 line, `shows`, X Ads its filler, beside the line for the channels offered now (the digest's rule 52; the ruling after SH-34).
- **R48.6, a feature an earlier batch read in early access.** Where this edition's card states no limit, it takes its own words' support, `core`, and the early access goes in `reading` (R47.5: each line's support by the card's own words). The cases, with the help pages SH-31 and SH-32 read as of 30 September:
  - Managed Markets' flat shipping rates (SH-E-6df24b66);
  - MB WAY (SH-E-f50a908d);
  - the new payouts view (SH-E-4874557f);
  - app events in analytics (SH-E-07ad4d2b).

## New things

- **Admin search** (`new:Admin search`, SH-36's name; the digest's section 4): SH-E-637c4915 ('Search sections, pages, and installed apps from one faster surface in the admin.'), `shows`, as every earlier line on it writes it. It is decided with Zid's and Salla's admin search (the ruling after SH-37). The leads CM-APP-001, CM-API-007 and CM-DVT-001 are leads by words ('installed apps', 'one', 'doc'), not its thing.
- **Fees for products and collections** (`new:Fees for products and collections`): SH-E-2b5f225a.
  - What it is: 'Set up' fees for products and collections per market 'and collect them automatically at checkout with full financial reporting built in. Early access.' Its help link is help.shopify.com's `taxes/additional-fees`, not held under either address.
  - Support: `shows`, by the early access (rule 32), and with no place of its own.
  - Place of its own: none held. The card's handle `additional-fees-configured-in-checkout-settings` names a settings place, but a handle states nothing (the digest's rule 1).
  - Proposed: domain C, area TAX or CHK, parent CM-TAX-001, since the help page sits under taxes; CM-CHK-001 is the alternative, since the fees are collected at checkout. A reading.
  - Name: in English only; the Editions are in English. The help address's word is 'additional fees'.
  - Terms searched with `caps --terms`: additional fees; fees; surcharge; cart fee; add_fee; service fee; additional charge; extra charges; extra fee; product fee; regulatory fee; recycling fee; handling fee; fees per market.
  - Leads read and set aside:
    - CM-PAY-007 is the payment service's processing fees, which the platform charges the merchant;
    - CM-CAT-003 is the collections the fees apply to;
    - CM-MKS-001 is the markets, the fees' condition;
    - CM-EVO-001 is a lead only by 'early access';
    - CM-STF-005 is a lead by words only.
  - SH-35's California battery fee (SH-E-d63b361f) is on CM-TAX-002, as a fee Shopify Tax calculates. That makes it the nearest held thing, and CM-TAX-001 or CM-TAX-002 could take this instead.

## Entries I couldn't tell, and what would settle each

1. **The Shopify Protect cards (SH-E-a26ff54f, SH-E-d7e84c6d, SH-E-dbd247f1, SH-E-ee196bb2).** The page calls Shopify Protect 'the Shopify Protect app', at apps.shopify.com/shopify-protect, which isn't held.
   - The maker: 'We’ve just released Shopify Protect, Shop Pay’s free and built-in fraud protection' (SH-E-2ee1a831, 2022) and the warranty issuer Shopify Inc. (CM-PAY-010's `own-service` row) name Shopify as its maker. Under rule 32 this changes nothing while the app's features are 'rolling out soon'. When they are offered, its own features would be `own-service`, its admin route `core`.
   - R48.1 makes the custom fraud rules (SH-E-d7e84c6d) `shows`. Read by its own words alone, the card would be CM-ORD-006 `own-service`.
   - SH-E-dbd247f1 (custom reports) links the Protect blog post, and SH-E-ee196bb2 (AI-generated responses for every chargeback) restates the stack card's 'win more disputes with AI'. Both are `core` by their own words.
     - The help page as held on 16 October states AI-generated insights only for product not received disputes: 'AI-generated insights are included in the evidence submitted to help support your case.' (`raw/runs/20261016T213535Z-help-en-ar-html-md/fetch-00000.warc.gz@49382285`, line 91).
     - The blog post `introducing-shopify-protect`, the App Store listing, or the help pages captured after 30 October would settle it.
2. **SH-E-d1df7358, payment approval by machine learning.** It is placed on CM-PAY-020, by its help link payment-authorization, and on CM-PAY-002, Shopify Payments as the one that does it. One of the two may be enough.
3. **SH-E-0b94c2f6, the high-value goods review.** It is placed on CM-PAY-003, the service's checks. CM-PAY-006, account holds, which its help address names, is the alternative.
4. **SH-E-ab85d4c9, 'Your store’s status on Shopify'.** It is placed on CM-ONB-002, the store's standing. CM-TRU-009 is the alternative. The help page `compliance/seller-health` isn't held, and it would settle the question. CM-OPS-004 (WooCommerce's system status report) is a homonym and was set aside.
5. **SH-E-bc359ba3, barcode scanning from any admin page.** It is placed on CM-CAT-002, the variants' barcodes. Read as finding records anywhere in the admin, it would be the admin search (`new:Admin search`).
6. **SH-E-daa046f5, HSA and FSA funds in Shop Pay.**
   - It is placed on CM-PAY-001 (a way buyers pay) and CM-PAY-014 (Shop Pay), both `shows` by 'Coming soon', with Truemed as the filler.
   - No capability holds health-account funds (searched: HSA; FSA; health savings).
   - Once offered, Truemed's work, eligibility, documentation and compliance, would be `outside`.
7. **SH-E-bfe7ba2e, the universal checkout on Shop.** CM-CHK-001 and CM-CHK-002 `own-service`, by E102. Read as Shop's own and no part of the store's checkout, only CM-CHN-002 would stand.
8. **SH-E-df2dd8bc, Shop Promise's badge in Shopify Catalog.** CM-AIA-005 `core`, as SH-47 places Shopify Catalog (SH-E-53bdd82f). It could instead be named in passing (the digest's rule 51).
9. **SH-E-dc028e5a, the agent in Shop's 'order help, and support'.** No capability of the model holds the platform's own help to shoppers, so only CM-AIA-005, CM-MKT-023 and CM-CHN-002 take lines.
10. **SH-E-632e67c8, Shop Campaigns' metrics in ShopifyQL.**
    - CM-MKT-012 is `own-service`, as SH-63 and SH-66 place the programme. SH-34's line on the same post (SH-E-9f019906) is `core`.
    - CM-ANL-006 is `core`, since this card names no app. SH-34's line is `extension-point`, for the post's analytics apps.
11. **SH-E-dd57fae0, shipping in markets.** CM-SHP-001, with CM-MKS-001 (a market's own setting) and CM-B2B-001 ('company location', rule 46). The two lines beside it could be read as the setting's conditions only.
12. **SH-47's open question on SH-E-498f0818's note** (in-store receipts sent to Shop). The Shop section's shop.com card (SH-E-05e8e112) names order tracking (CM-SHP-017 `own-service`) and no receipt, so it doesn't settle the question.
13. **SH-E-ac751d5d, return and cancellation requests by market in the checkout editor.** CM-RET-003 and CM-ORD-004 (E140), with CM-CHK-003 as the place where the setting is. SH-34 placed the per-market rules (SH-E-5e20deab) on CM-RET-003 alone.

## Leads looked at and set aside

- CM-ORD-003 (order statuses) for SH-E-f19a1a89 and SH-E-72c67e8e: a lead by 'completed' and common words.
- CM-SHP-021 (packaging materials ordered from carriers, Salla's) for SH-E-c24fc738: the store's own package defaults are CM-SHP-001's, as SH-36 placed them.
- CM-MKS-009 (countries reference data) for SH-E-936c4060: the markets named after 'like' are examples, not a reference list.
- CM-PTN-010 for SH-E-49553d41: a lead by 'powered by'.
- CM-SFR-013 for Shop's search (R48.3).
- CM-ACC-009 ('coming soon'): a lead by the release words, on the cards of Payments and Operations.
- CM-EVO-001 ('early access'): the same.

## Structures whose items and sources disagree

- `items.jsonl` keeps no `data-card-variant`, so the stack card and the text cards after it can't be told apart in the entries (R48.1). The source states them (`source.html`, each `article`'s attribute).
- The tooltip joins SH-47 noted ('Shop PayLearn more', 'Shopify ProtectGet app') hold here too. Each quote stops at its link.

## What the sources state that no entry holds (for the second stage)

**The help page Chargebacks in the admin** (`raw/runs/20261016T213535Z-help-en-ar-html-md/fetch-00000.warc.gz@49382285`):
- line 74, 'Get help understanding a dispute with Sidekick': Sidekick guidance on a dispute's reason code, a lead for CM-AIA-002;
- line 37, the issuer claims and responses: Shopify's summaries of the bank's documents;
- lines 89 and 109: evidence submitted automatically on the due date;
- line 153: the opt-out of the AI-generated insights;
- line 178: the due date, '7 to 21 days';
- lines 100 to 103, the evidence files' limits: 'fewer than 50 pages', each file not over '2 MB', combined not over '4 MB'.

These are leads for CM-PAY-009's qualities.

## Problems with the brief or the scripts

- The checker's `CHANGES` compares with the merged model as it stands, so CM-AIA-004 and CM-CHK-010 read as becoming held although SH-47's unamended lines already hold them.
- `earlier` found almost nothing, since Fall 2026's keys are new. Its 'Read help doc' label prints the same unrelated SH-57 lines for every card that has one. Searching the placements for the cards' distinctive words found the changelog's and the Editions' lines (R47.5).
- No conflict with B-extent.md was found. R48.4 follows the digest's rule 42 against two changelog batches' lines, which the coordinator aligns.

## The coordinator's check

Measured: 21.5 million tokens over 95 requests, about 224,000 an entry. The checker prints no problem.
- **Kept:** every `CHANGES` line, R48.1 to R48.6 and the two new things. The Editions digest's section 6 takes the rules, beside R47's.
- **R48.4, decided:** rule 42 holds. The changelog's eight CM-SHP-015 `core` lines for carriers of the platform's own labels are aligned to `shows`, their carriers left as the CM-SHP-002 lines' fillers: SH-34:59, SH-35:113, SH-35:124, SH-36:128, SH-36:196, SH-36:200, SH-38:52 and SH-46:51 (the changelog digest's C47). The merchant's own carrier accounts stay `core` (SH-34:77, SH-35:142, SH-36:201, SH-46:113).
- **The rule-4 `NOTE` on line 124:** Shopify Catalog is a part of the platform, so `core` stands (the ruling after SH-45: a possessive on a part of the platform names its own feature).
- **The new things** and the open cases go to `amendment-notes.md`.
