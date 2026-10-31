# SH-58: notes

**The batch:** Shopify, `editions-page-data`, 96 entries of the Summer 2024 Edition (`www.shopify.com/editions/summer2024`). They run from the collection World's best checkout (collection 6, `formattedCollections[6]`) through AI for commerce, Connect with customers, Ship & fulfill, Centralize operations and Developer: Storefronts, to Developer: Extensions & APIs up to its Shopify Planet API card (`SH-E-2b35bff7`). SH-59 takes the rest of that collection. The evidence is observed-sh at `e38dc17e3`. Effort: high.

**What I read:** the brief and the structure's rules digest (`held/rules/editions-page-data.md`). I read the last section of `review-H-rulings.md` twice, since it changed during the run. The new ruling after SH-30 ('A help page's plan requirement is its feature's condition, not a plan line') bears on entry 2 and agrees with its line. I also read:
- the guides named in the brief;
- SH-53's E23, for Commerce Components;
- SH-57's E58, for Sidekick and Inbox;
- SH-57's lines for the Top 10 twins.

Every collection of my part has an empty `descriptionHtml`, so each card is read with its collection's title alone (`items.jsonl` line 7, `formattedCollections[6]` to `[12]`).

**Count:** 147 lines for 96 entries:
- 93 entries are `capability` alone;
- 1 entry is `capability` and `new` (entry 5);
- 1 entry is `new` alone (entry 96);
- 1 entry is `out` (entry 56).

## The new things

No new thing is named here. Two lines take new things that earlier batches named, under their names:
- **Commerce Components by Shopify** (SH-51's), entry 5 (`SH-E-7ee1751d`), `shows`, scope 'Commerce Components'. The Shop Pay Component is one of the components (M-6 refined), as SH-53's E23 placed `SH-E-6970c2c4`. Its place of its own, domain, parent and terms are SH-51's.
- **Planet** (SH-50's), entry 96 (`SH-E-2b35bff7`), `own-service;extension-point`. Apps integrate with it (the card: 'Turn your app into a vehicle…'), and 'our carbon-neutral shipping program' names Shopify as its maker, as SH-E-bc581483 does. Its other attributes are SH-50's.

The Editions are in English only, so no Arabic name is held. Terms searched for the lines whose capability no lead named:
- pickup point; pickup points;
- address field(s); address form; prefilled address; one-time-use address;
- tax ID; VAT number; tax number; registry; gift registry;
- subscription(s); checkout kit; checkout sheet; embedded checkout;
- image editing; media editing; edit images; AI image; image generation; background removal;
- discount code(s); iDEAL;
- sales channel(s); social commerce; Checkout Kit; mobile checkout; TikTok;
- taxonomy; product category; attributes; marketing automation(s); consent; cookie; customer privacy; attribution;
- form(s); form submissions; lead capture;
- payment extension; payments app(s); alternative payment; offsite; private label; overselling; inventory availability.

## Rules I followed that the digest doesn't state (E59 on)

- **E59. Top 10 repeats.** `earlier` printed no twins for Summer '24's Top 10 repeats, since their handles differ (`shopify-magic` and `shopify-magic-top-10`). I matched them by their words to the Top 10 entries SH-57 placed, and took those entries' lines (the digest's rule 3):
  - 1 ↔ SH-E-afa20a5c;
  - 18 ↔ SH-E-f244d8db;
  - 39 ↔ SH-E-25c1bf86;
  - 52 ↔ SH-E-5e6457fa;
  - 62 ↔ SH-E-d56bbb21;
  - 65 ↔ SH-E-ab2b0c32, whose title differs ('Flex sections' against 'Theme style settings'). The capability and support are the twin's, and the title is the term.
- **E60. A component's feature on another capability.** The Shop Pay Component's 'buy online and pick up in store' (entry 5) is local pickup, which the component itself offers. So it takes CM-SHP-007 `own-service`, scoped 'Commerce Components', beside E23's CM-PAY-014 `own-service` and the new thing's `shows`. This is E23 with the ruling after SH-57.
- **E61. Developer and merchant twins in one edition.** The merchant collection and the Developer collection describe some features twice, in other words. I gave each pair the same capabilities, and its own words decide each line's support and scope:
  - 6 ↔ 79 (PCI DSS v4);
  - 7 ↔ 75 (pickup points);
  - 8 ↔ 85 (address autocomplete);
  - 9 ↔ 77 (address fields);
  - 10 ↔ 78 (prefilled and predefined addresses);
  - 11 ↔ 76 (tax ID);
  - 13 ↔ 91 (discount codes on drafts);
  - 30 ↔ 94 (pixel consent);
  - 37 ↔ 95 (pixel events, the same words);
  - 3 ↔ 73 (apps on the thank-you and order status pages);
  - 50 ↔ 88 (exchange APIs).
- **E62. A buyer's tax ID collected at checkout.** Entries 11 and 76 collect it for shipping ('regional shipping requirements'). They take CM-TAX-005 `core`, as SH-E-e4278b2b placed Mexico's RFC, and '14 additional countries' is a quality.
- **E63. Payment extensions.** They are CM-PAY-011 `extension-point`, as its cell reads Payments extensions (81, 82, 83). Third-party gift cards accepted through them are CM-LOY-002 `extension-point`. A store's own branded card ('private label credit cards') stays on the CM-PAY-011 line.
- **E64. A partners' protocol for the platform's checkout.** Checkout Sheet Protocol (entry 17) is CM-CHK-001 `extension-point`, and 'Partners like TikTok' makes TikTok its filler (the digest's rule 54).
- **E65. A kind of store named as the condition is the scope** (the digest's rule 27). The cases:
  - 'Shops upgraded to Checkout Extensibility' (79);
  - 'Approved brands' (45);
  - 'eligible US stores' (46);
  - 'Eligible stores' (20).
- **E66. Staff permissions as the card's own thing.** Entry 33 ('Permissions for customer data') takes CM-STF-002 `core` (rule 5). The records the permissions gate take CM-CUS-001 `core` (the ruling after ZD-7).
- **E67. An API's field that names another capability's thing takes that capability's line,** by the field's name, as a reading. Entry 91's `acceptAutomaticDiscounts` is CM-MKT-003 `core` (the digest's rule 47). That cell holds nothing on Shopify now, so the line changes it (CHANGES below).
- **E68. Places named in a card's own news take their line, not those named in passing.**
  - 'now on mobile' (23) takes CM-SRF-001 `core`, as SH-E-04b7375e's line does.
  - 'Custom discounts now work on POS' (89) takes CM-POS-001 `core`.
  - 'on mobile and across the admin', named in passing in 18's overview, takes none, as SH-57's twin line has it.

## Entries I couldn't tell, and what would settle each

1. **Entry 5, CM-SHP-007 `own-service`.** Is the Shop Pay Component's pickup choice the component's own thing, like Stocky's transfers, or Shop Pay's own thing, like Collective's rates (the ruling after SH-57)? If the latter, the line goes and the words stay in CM-PAY-014's. A ruling on components of Commerce Components would settle it.
2. **Entry 83, CM-INV-001 `core`.** 'Inventory confirmation' by payment partners. I placed the partners' work on CM-PAY-011 `extension-point`, and the stock they check on CM-INV-001 `core`. I first wrote that line `extension-point`, then read the stock as the platform's own. Whether a line on inventory belongs here at all is the question.
3. **Entries 11 and 76, CM-TAX-005.** The tax ID serves shipping, not the VAT exemption that CM-TAX-005's name holds. I followed SH-E-e4278b2b's precedent. CM-CUS-008, the checkout's address form, is the other reading. A ruling on buyers' tax identifiers would settle both.
4. **Entry 19, Sidekick: 'Thousands of stores can now use Sidekick'.** I read it as 'live on thousands of Shopify stores' (the digest's rule 36), so `shows`. Its 'Get started' link to the set-up help page could support `core`.
5. **Entry 10, prefilled addresses.** I wrote one line, CM-CUS-008 `shows`. The card names checkout extensions as the means, and a CM-CHK-004 `shows` line would also fit.
6. **Entry 6, PCI DSS v4.** No line for 'upgrading to Checkout Extensibility' (CM-CHK-004), which the card names as the means.
7. **Entry 93, SellingPlan metafields.** Three lines: CM-SEL-001, CM-CNT-002 and CM-PAY-019, all `core`. Hiding gateways is done in practice by a payment customization function, but the card names none, so CM-PAY-019 isn't `extension-point`.
8. **Entry 28, Unified ad insights.** I placed it on CM-MKT-008, the report titled Attribution at `marketing/reports/channels` (SH-E-b8faa2bb). SH-E-84ceca21 placed 'channel performance reports' on CM-ANL-002. Google and TikTok are its fillers, the channels whose campaign data it syncs.
9. **Entry 17, Checkout Sheet Protocol.** CM-CHK-001, or CM-CHN-001, whose sales channel apps connect the store to outside surfaces.
10. **Entries 45 and 47, Marketplace Connect.** Rule 13 gives different supports for one app in one collection:
    - 45 links `admin.shopify.com/apps/shopify-marketplace-connect`, so it is `shows` with CM-APP-007 `core`;
    - 47 links only `apps.shopify.com/marketplace-connect`, so it is `core`, the maker a gap.

    I kept to the rule. The coordinator may want one support for the app.
11. **Entry 96, Planet and CM-APP-011.** The card calls the program 'our', not the app, so it takes no CM-APP-011 line (the digest's rule 14). Its productType is 'Planet App'.

## Makers

- **The Pixel Helper (entry 38).** The digest lists it under 'none held'. `makers` finds SH-E-0a66f16d: 'We've added error messages to the Shopify Pixel Helper…' (SH-39). I kept CM-MKT-009 `core`, as SH-39 and the digest have it, for another reason. The help page shows it as the admin's own test, opened from Settings > Customer events > Test: 'The Shopify Pixel Helper lets you test your custom pixel on your online store to view the events being received in real-time, alongside the data for those events.' (`raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz@7624721`). So it is a built-in tool, and a 'we've added' post about it makes it no separate product, as one about Shopify Payments doesn't (the digest's rule 25). The digest's 'none held' could read 'not a separate product'.
- **Shopify Forms (entry 35).** `makers` finds only 'refer to our help docs' (SH-E-ee2ee993), which names no maker (the digest's rule 10). So the app takes `shows` and CM-APP-007 `core` (rule 13).
- **Shopify Subscriptions: a maker statement no entry holds.** The help page entry 12 links calls it 'the free first-party Shopify Subscriptions app' (the page above, `fetch.warc.gz@7054363`, line 4 as `warc_text.py` prints it). Entry 12 places the platform's own checkout behaviour, not the app's, so no line rests on this.

## What a source states that no entry holds (for the second stage)

Both pages are in `raw/runs/20260930T003703Z-help-en-md/fetch.warc.gz`; line numbers are as `warc_text.py` prints them.
- **CM-MKT-009, the Pixel Helper's limits** (`@7624721`):
  - line 49: 'You can test only 1 custom pixel at a time using the Shopify Pixel Helper.';
  - line 53: “The Shopify Pixel Helper isn't compatible with” headless commerce stores 'or stores in private mode.'
- **CM-SEL-001, a selling limit** (`@7054363`), line 10: 'Subscription-only products without a one-time purchase option can be sold only on the Online store sales channel.'

## Problems with the brief or the script

- **`earlier` and the Top 10 repeats.** It printed no twins for them, since they have other handles (E59). It also lists a label's lines only where a reading cites the label, so SH-57's three lines on 'Ship to & from store' showed as one. I read SH-57's placements for each twin.
- **`&` in a filler.** The checker reads the raw HTML text, where a name holding '&' is written `&amp;` ('Zoorix Bundle Kit &amp; Cross Sell'). So such a name can't be a filler in its own words. I wrote 'Zoorix', the part of the name before the '&'.
- **The digest's 'none held' for the Pixel Helper** differs from what `makers` finds (above).

## The checker's NOTE lines, read again

- **`core` on a product named with Shopify's brand.** Each is `core` by what the entry shows:
  - lines 26 and 32, Shopify Magic: the admin's own AI, as the CM-AIA cells hold it;
  - line 62, the Pixel Helper: a built-in test (Makers, above);
  - line 65, Shopify POS: the platform's own client (the digest's rule 9);
  - lines 83 and 84, Shopify Shipping: the digest's rule 7.
- **The new things' leads.**
  - Line 7: Commerce Components' entry already takes CM-PAY-014 and CM-SHP-007, its two real leads. CM-ACC-002, CM-PAY-015 and CM-ONB-003 are leads by common words only.
  - Line 148: Planet's leads are CM-API-001 (by 'API' in the title), CM-APP-011 (case 11), CM-PTN-001 and CM-APP-010 (by name). The API is Planet's own, for apps, not the platform's developer API, so the line stays on the new thing.
- **Each `own-service` line** rests on the maker statement its reading cites (the digest's table and rule 11).

## CHANGES, as the checker printed them, with what I decided

- **CM-AUT-001 gains `own-service`** (Flow: entries 29, 44, 58 to 61, 71). Kept: Flow's maker statement SH-E-0678ff26 and the ruling after SH-55, which aligned 38 lines. The model isn't amended yet.
- **CM-CHK-001 gains `extension-point`** (17, Checkout Sheet Protocol). Kept: partners present the platform's checkout through its protocol (E64; case 9).
- **CM-CHK-003 gains `own-service`** (2, Checkout Blocks). Kept: the ruling after SH-35 and the new ruling after SH-30.
- **CM-CHN-002 gains `extension-point`** (32, 84, Shop Minis). Kept: the digest's rule 11.
- **CM-CUS-009 gains `extension-point`** (8, 85). Kept: providers replace the platform's autocomplete through its extensibility, as SH-E-6242fae0 and SH-E-c6b4dbc1 have it.
- **CM-MKT-003 gains `core` and becomes held** (91, `acceptAutomaticDiscounts`). Kept: a reading of the field's name (E67; the digest's rule 47).
- **CM-MKT-007 gains `own-service`** (34, Shopify Email). Kept: the digest's table.
- **CM-MKT-011 gains `own-service`** (24, 25, Shopify Audiences). Kept: SH-E-234dcbd7, 'a new app from Shopify'.
- **CM-SHP-007 gains `own-service`** (5, the Shop Pay Component's pickup). Kept, as E60, but open (case 1).
- **CM-SHP-018 gains `own-service`** (46, Shop Promise). Kept: the digest's rule 11.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 96 of 96 entries, no problem.
- **The `CHANGES` stand.** Each rests on the digest's table or rules:
  - Flow, Checkout Blocks, Shopify Email, Shopify Audiences and Shop Promise `own-service`;
  - third parties' Shop Minis and address autocomplete `extension-point`;
  - the draft order field `acceptAutomaticDiscounts` on CM-MKT-003, a reading of the field's name (E67).
- **The rules E59 to E68 stand** and go into the digest's section 6:
  - Top 10 repeats take their twins' lines;
  - a component's own feature takes its capability (E60, with the ruling after SH-57);
  - developer and merchant twins share capabilities;
  - a buyer's tax ID at checkout is CM-TAX-005;
  - payment extensions are CM-PAY-011;
  - a partners' protocol for the checkout is CM-CHK-001 `extension-point`;
  - a kind of store named as the condition is the scope;
  - a card's own staff permissions are CM-STF-002;
  - an API field names its thing's capability;
  - places named in a card's own news take their line.
- **The Pixel Helper:** a held post names its maker (SH-E-0a66f16d), but its help page opens it from the admin's Customer events. So it is a built-in tool, `core`, not a separate product. The digests say so now.
- **Open, as placed:** Marketplace Connect's two supports by its two links (rule 13). The app has no maker statement held, so it is `core` by what its cards show, and the admin's page for it is CM-APP-007. Entry 45's `shows` rests on its card's own words.
- **Cost:** 23.4 million tokens over 102 requests, about 244,000 an entry, against SH-57's 329,000 before the digest. The context reached about 416,000 tokens.
