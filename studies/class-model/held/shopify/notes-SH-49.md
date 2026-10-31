# SH-49: Shopify's `editions`, Fall 2026, entries 1 to 63 (Developer)

The batch reads `shopify/editions` at observed-sh `e38dc17e3`, `structures/shopify/editions/www.shopify.com_editions_fall2026/items.jsonl`: the page's last section, Developer, from its heading (h2, `id="developer-title"`) to its last card and 'Back to navigation'. Its source is `source.html`, the archive record `raw/runs/20261030T162210Z-shopify-editions/fetch.warc.gz` of www.shopify.com/editions/fall2026. Its rules are SH-47's (R47.1 as narrowed at the coordinator's check, R47.2 to R47.6), the Editions digest (`held/rules/editions-page-data.md`, with its section 6) and the last section of `review-H-rulings.md`.

**What I read.** The brief, SH-47's notes, the digest whole, the rulings' last section, SH-65's notes for E125 to E132, observed-sh's README, `docs/READING.md`, the head of `docs/GAPS.md`, `structures/README.md`, the register's and selection's rows for `editions`, and B-extent's "Cells and evidence" and "Conventions from the dry run". For earlier lines: `earlier` (it found nothing on Fall 2026's own keys), then greps of the placements for each chunk's distinctive words, which found the changelog's lines (SH-34, SH-36), Spring '26 (SH-65, SH-66, and SH-67, which was running beside me and isn't checked yet), Winter '26 (SH-62, SH-64) and SH-47 and SH-48 on this page.

**The section's shape.** Unlike the sections SH-47 and SH-48 read, Developer has sub-headings: h2 Developer, then five `section`s, each with an h3 (Agentic experiences, Platform primitives, Tooling, Secure ecosystem, Storefronts) over `article` cards whose title is an h4. Most cards are one h4 sentence with inline links (R47.2).

## Count

- 63 entries in 114 lines: 107 on capabilities, 1 `new`, 6 `out`.
- By entry: 56 on capabilities only; SH-E-b079d474 `new` plus two capabilities; 6 `out` (the heading Developer and its five sub-headings).
- Supports: `core` 58, `extension-point` 19, `shows` 14, `core;extension-point` 9, `own-service;extension-point` 6, `own-service` 2.

## Rules added for the Developer section (R49.n), for the coordinator to check

- **R49.1, sub-headings.** An h3 inside a section is that section's sub-heading, read as R47.1, as narrowed, reads a section heading. All five are `out`: each groups several capabilities' cards. Agentic experiences is the nearest case (see below).
- **R49.2, Shop's things offered for developers' own apps.** Where a card offers developers Shop's sign-in or Shop Pay for their own apps or agents, the line is `own-service;extension-point`. Shop's own thing is `own-service` (the digest's rule 11). Developers adding it is `extension-point`, as R47.4 has the tools for adding Shop Pay to any agent, and as SH-67 placed 'Access to sign-in with Shop' (SH-E-4540aede). The cases are SH-E-9b5c6aaa, SH-E-8366b941, SH-E-8aa84291, SH-E-debf4134 and SH-E-7edf9e6d.
  - Shop sign-in named only as the condition of another feature ('for shoppers who sign in with Shop') stays `own-service`, as SH-65 placed SH-E-5a3303bc. The case is SH-E-15fc3b15.
  - A unified checkout across brands is also a checkout: CM-CHK-001 `own-service`. This follows E102, and SH-48's line on Universal checkout on Shop (SH-E-bfe7ba2e), which cites this batch's card.
- **R49.3, events an app's extension responds to.** POS background extensions respond to transactions and to cash-tracking sessions (SH-E-77d4bdfc). Each event takes its capability, `core`, as the digest's rule 17 places the webhooks the platform sends apps. The extension itself is CM-POS-004 `extension-point`.
  - Alternative: `extension-point`, as SH-67 (not yet checked) placed Cash management extensions on CM-POS-003 (SH-E-7579a340). Those extensions manage the cash sessions themselves, which is why I didn't take that line here.
- **R49.4, a third party's tool that signs a merchant up.** The card on the Stripe Projects CLI (SH-E-281bce36) leaves open who creates the store. Its linked help page settles it (E129; R47.6): 'Shopify is one of those services'.
  - The store and account are CM-ACC-001 `core;extension-point`, the CLI their filler. This is the capability where the sign-up's other lines sit (SH-92, SH-93).
  - The plan the store is created with is CM-PLN-001 `core`.
  - The page's United States limit isn't the card's scope (R47.5).
- **R49.5, a retirement in a developer card.** A retirement takes the replacement's lines, as the changelog digest's rule 30 has it. The case is script tags replaced by theme app extensions (CM-SFR-004) and web pixels (CM-MKT-009). Both are apps' work: `extension-point` (E84). The retired script tags are named in `reading`.

## New things

- **Sponsored products** (`new:Sponsored products`, SH-65's name), SH-E-b079d474.
  - What the card says: 'Earn the' commission businesses set in Shop Campaigns 'plus 0.3% from Shopify, on every sale you drive using the Catalog API. Early access.' Its link is shopify.dev's agents/catalog/promoted-placement, the page SH-65's twin SH-E-e1827630 links by its section Promoted placements.
  - Support: `shows` (early access, the digest's rule 32). Its quality is Shopify's 0.3%.
  - Place of its own: none (a docs page).
  - The card ties the thing to Shop Campaigns, which SH-65's coordinator check found no statement for. So it also takes a CM-MKT-012 `shows` line: the businesses' commission set in the platform's ads programme, whose cell has its ads run on third parties' placements too. It keeps SH-65's CM-AIA-005 `shows` line (the digest's rule 4).
  - Candidates for the thing itself, for the coordinator:
    - CM-MKT-012, Shop Campaigns, the merchant's side;
    - CM-PTN-009, partner affiliates, who 'earn commissions on the orders they bring', whose Shopify cell holds nothing;
    - CM-MKT-014, affiliate marketing run by the store.
  - Searched: commission; promoted placement; paid placement; sponsored; affiliate; referral; revenue share. I read the cells of CM-MKT-012 and CM-PTN-009. The checker's other leads (CM-CAT-001, CM-EVO-001, CM-MKT-005, CM-DVT-001) are leads by name or by 'early access' only.
  - English only, as all the Editions are.

## The CHANGES lines, as decided

- **CM-PAY-014 gains `extension-point`** (lines 6, 21, 23): Shop Pay offered to developers for their own apps and agents (R47.4; R49.2). Kept.
- **CM-CUS-010 gains `own-service`** (lines 5, 15, 59, 60): Shop's sign-in, Shopify's own (rule 11), as SH-65's and SH-67's lines. Kept.
- **CM-CHK-001 gains `own-service`** (line 24): the unified checkout across brands, Shop's own (E102), as SH-48's SH-E-bfe7ba2e. Kept. I first wrote `own-service;extension-point` and took the `extension-point` back: the developers' part sits on the Shop Pay line.
- **CM-AIA-004 becomes held, `core`** (line 79): apps, themes and stores managed from the developer's own agent, through the CLI and the AI Toolkit its link opens. This follows SH-66 (SH-E-80bdfc5c) and SH-67 (SH-E-e63a0cd0). The cell also becomes held by SH-47's connectors, as decided at SH-47's check. Kept.
- **CM-DVT-004 gains `core`** (line 81): the CLI's commands for dev stores (the digest's rule 41), as SH-36 and SH-67. Kept.
- **CM-ACC-001 gains `extension-point`** (line 82): sign-up from Stripe's CLI through the platform's own service there (R49.4). Kept, resting on the help page's record.
- **CM-PTN-008 becomes held, `core`** (line 86). 'Earn from subscription revenue and online GMV for every business you bring to Shopify, on all plans, for four years' is the partner programme's earnings on the merchants a partner brings. That is the referral programme for the platform's plans that the capability names. Its quality is the four years. Kept. Its link, the partners blog's a-new-partner-earning-model, isn't read.
- **CM-SFR-011 gains `extension-point`** (lines 111, 113), both with Vercel as filler:
  - Hydrogen's 'one-click deploys to Vercel', a second line on the Hydrogen card under its own filler;
  - Vercel Shop, 'Vercel’s' template built on the Hydrogen SDK.

  Both show a third party working through the platform's framework, not Lovable's `outside` (E113), since the platform's interface is named. Kept.

## Entries I couldn't tell, and what would settle each

- **SH-E-1290ef89, the sub-heading Agentic experiences, written `out`.** 11 of its 12 cards take CM-AIA-005 lines. SH-E-8366b941 ('Add Shop Pay to any app or shopping experience') is Shop Pay's alone. If the coordinator reads all twelve as agentic experiences, the heading takes CM-AIA-005 `core`, as Sidekick kept CM-AIA-002.
- **SH-E-426b63fa, the permalinks' contents.** 'that include products, customer details, discounts, and order attribution':
  - I gave discounts (CM-MKT-001) and order attribution (CM-MKT-008) lines, as items of the card's news (E80). The products and customer details are read as the cart's and the checkout's own contents.
  - Read as a list of the link's contents (rule 51), both lines go.
- **SH-E-5d77f172, UI extension logs, placed CM-DVT-001 `core`,** beside CM-CHK-004 and CM-CUS-014 `extension-point`.
  - SH-67 (unchecked) placed Spring '26's App Events API on CM-APP-004 (SH-E-244b9ce2) by the cell's term 'App Events API'.
  - That cell's note says its App Events are the Partner API's: events on an app's lifecycle in a store. The new app events are events that apps send to Shopify. I read them as a homonym. So I placed SH-E-bf096312 on CM-ANL-001, as SH-36's changelog post (SH-E-fd61d70b), and this card on the developer's tools.
  - The coordinator's alignment of SH-67's line settles both.
- **SH-E-debf4134, the data requested through Shop sign-in.** Its link's use case is lead capture (shopify.dev's api/shop/guides/use-cases/lead-capture), which rule 11 places on CM-CUS-007. But the card's own consent is consent to share data with the app, not marketing consent. So I placed it on CM-CUS-010 alone. A line on CM-CUS-007 is the alternative.
- **SH-E-43b9038f, mock.shop's 'to build a store, then publish to Shopify.'** I placed it on CM-SFR-011 `core`, as SH-51's mock.shop. Publishing a store an agent built may be SH-47's Store preview (a store built before signing up and kept). mock.shop's page isn't held. A held page of that flow would settle it.
- **SH-E-77d4bdfc's events** (R49.3), and **SH-E-281bce36's support** (R49.4), as above.
- **SH-E-ee3a2dd1, App Store reviews checked against shop trust:** `core;extension-point`, as SH-62's trusted reviews (SH-E-f1e6b735). The ratings mark third parties' apps. Read as only the App Store's own check, it is `core`.

## Leads looked at and set aside

- CM-CAT-005 (brands) for 'brands on or off Shopify' (SH-E-9b5c6aaa, SH-E-8aa84291): the businesses selling, not a product's brand.
- CM-API-006 (API versioning) for Polaris's versions (SH-E-fcccbcb2): the API's versions, not the UI components'.
- CM-PLN-002 (plan term) for an app's annual plan (SH-E-dbe420f0): the platform's own plan.
- CM-OPS-005 (store logs) for an app's production logs (SH-E-6bbe4483): the store's logger, not the app's.
- CM-SUP-001 (reviews) for App Store reviews (SH-E-ee3a2dd1): buyers' reviews of products.
- CM-ORD-003 ('completed') for the security card's image text, which takes no line.
- CM-MKS-001 for app prices 'localized across markets' (SH-E-5bf43c78): the markets are named in passing.
- CM-STF-005 for the Dev Dashboard's store index and the partners' details (SH-E-38557031, SH-E-a8460421): `shows`. A collaborator request is a partner's request (the ruling on the dry run's S7).
- CM-AIA-004 for SH-E-c0eaf790 (agents managing dev stores from the CLI) and SH-E-a2c9a339 (the agent fixing the app's code): no store of a merchant is worked on, and no AI Toolkit link stands on the first.

## What the sources state that no entry holds (for the second stage)

- **The Stripe Projects help page** (`raw/runs/20261016T213535Z-help-en-ar-html-md/fetch-00000.warc.gz@1087752`):
  - it is 'available in the United States only';
  - 'The Shopify Plus plan isn't available through the Stripe Projects CLI.';
  - the trial is 'currently for 4 months', and a trial store stays in private mode until a paid plan and a launch from the Online Store page;
  - plan changes can be made from the CLI, authorized against the linked Shopify account;
  - on a paid plan 'Stripe is the payment method in your Shopify billing settings';
  - the Shopify CLI's `shopify store stripe-auth` connects the store, with `--store`, `--scopes` and `--signup`;
  - staff accounts depend on the plan ('The Basic plan doesn't include staff accounts');
  - support is split between Stripe and Shopify.

  These are leads for CM-ACC-001, CM-PLN-001, CM-PLN-005 (Stripe as the billing payment method), CM-DVT-002 and CM-STF-001.
- **The section's own text that no card holds:** 'Back to navigation' (in SH-E-871738c3) and the page's footer disclaimer ('*Based on the number of Shop Pay accounts as of September 30, 2026.'). The disclaimer is the opening stat's footnote, SH-47's.

## Problems with the brief or the scripts

- As SH-47 noted, `editions`' items join each link's hidden tooltip to its text ('Read dev docs you’re building'). So quotes and terms stop at each link (R47.2).
- `earlier` finds nothing for Fall 2026's keys. The developer cards' twins were found by greps of the placements for each chunk's distinctive words (R47.5).
- SH-67, whose Spring '26 developer cards are this batch's nearest twins, was being written beside this batch, unchecked. Where I followed it, the reading names its line. Where I didn't (the App Events API), the case is above.
- No conflict with B-extent.md was found.

## The coordinator's check

Measured: 17.0 million tokens over 79 requests, about 270,000 an entry. The checker prints no problem.
- **Kept:** every `CHANGES` line and R49.1 to R49.5, which the Editions digest's section 6 takes. The rule-4 `NOTE`s (lines 52 to 104) name parts of the platform (Shopify Tax, the CLI, Shopify App Pricing, the Theme Store, the App Store), so `core` stands (the ruling after SH-45).
- **R49.3 and SH-67's cash management extensions agree:** the events the platform sends an extension are `core` on their own capability (rule 17), and apps doing the work through the platform's APIs is `extension-point` (SH-67, SH-E-7579a340). Both stand.
- **The App Events divergence:** this batch's reading holds. The cards' App Events API sends an app's own events to Shopify, not the Partner API's lifecycle events that CM-APP-004 names (SH-I-0075). SH-67's line 87 is corrected to CM-DVT-001 `core`, and CM-APP-004's wording goes to `amendment-notes.md`.
- **Agentic experiences `out`:** kept. R47.1's exception needs every card to be one capability's thing, and one of the twelve is Shop Pay's alone.
