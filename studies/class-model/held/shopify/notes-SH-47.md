# SH-47: Shopify's `editions`, Fall 2026, entries 1 to 80

The batch reads `shopify/editions` at observed-sh `e38dc17e3`, `structures/shopify/editions/www.shopify.com_editions_fall2026/items.jsonl`: the rendered page's text blocks in document order, from the page's opening through the sections Agentic, Sidekick, Online and Merchandising into Retail (its first 20 cards; SH-48 goes on from there). Its source is the archive record `raw/runs/20261030T162210Z-shopify-editions/fetch.warc.gz@1760606` (`source.html`). No earlier batch placed this structure. Its rules are the Editions page data's (`held/rules/editions-page-data.md`, with its section 6, E59 to E124) and the rulings in `review-H-rulings.md`'s last section.

80 entries, 129 lines: 76 entries on capabilities only, 3 with a `new` line beside their capabilities, 1 `out`.

## Rules added for the rendered form (R47.n), for the coordinator to check and SH-48 and SH-49 to keep

- **R47.1, section headings.** An `h2` entry (Agentic, Sidekick, Online, Merchandising, Retail) is the page's section, a heading of the platform's public site. The page-data digest has no rule for it, since its sections were never entries (its rule 37). Where its title names a capability (Agentic: CM-AIA-005, whose cell holds the admin's Agentic section; Sidekick: CM-AIA-002; Retail: one of CM-POS-001's own terms) or one part of the platform (Online: the online store, CM-SFR-001), it is a container on that capability, `core` (M-13; the ruling after SA-2 and SA-5; the ruling after SA-28's 'a title that names a capability or one part of the platform'). A title that names only a grouping over several capabilities (Merchandising) is `out`, each card placed on its own (the ruling after SA-28). The opening's list of sections (Agentic 01 to Developer 11) is the page's table of contents: no line, each section placed at its own heading.
- **R47.2, a rendered card.** A card is an `article` (`data-component-name="product"`, its `id` a handle). Its `h3` is the title and its `p` the description, as a page-data card's (the batch message). Many cards have no paragraph: their `h3` holds the whole sentence with its links, read whole as title and description.
  - An inline link carries a hidden tooltip (`role="tooltip" hidden`: 'Learn more', 'Read help doc', 'Get app', 'Try it', 'Read dev docs', 'Read article'), which the rendering joins to the link's text (`shop.mdLearn more`). It is the link's CTA, read by its address (the digest's rule 53). A quote or a term stops at the link (the digest's rule 5).
  - A `div` after the CTA is the media's alt text, read with the card, with no line of its own (the digest's rule 1).
  - 'Notes' with `[n]` marks are the card's footnotes, part of the entry (the brief's rule 1). A note that links another card (`#<handle>`) names that card's thing, placed at its own entry, unless it states a feature that card doesn't hold: 'In-store digital receipts get sent to' Shop (SH-E-498f0818) takes its own line, since the linked Shop card (`#new-shop-com-with-detailed-tracking`) names no receipt (`items.jsonl`, `grep receipt`).
  - A `figcaption` stat, and the page opening's three stats, are claims (the digest's rules 21 and 55): the opening's stand alone and take `shows` on their topics; a card's stat takes no line.
  - 'Copy prompt' (a copy-to-clipboard button) and 'Back to navigation' are UI strings.
- **R47.3, an outside AI assistant linked to the store.** A card naming an outside AI assistant that works on the store through the platform's connector or plugin, as its help link shows (help.shopify.com's `ai-powered-tools/connecting-ai-tools/`: the Shopify connector for Grok, for Gemini, for Muse, for Claude, the plugins for ChatGPT and Microsoft Copilot), is CM-AIA-004 `core`, the assistant its filler. A third party's own product built on the connector (xAI's Grok Bot, 'AI teammates') adds `extension-point`. A card that names the assistant at work on the store with no connector named and no held link (Product sourcing in agents) is `shows`.
- **R47.4, Shop Pay in buyers' agents.** Shop Pay in a buyer's AI agent is Shop Pay apart from the platform's checkout: CM-PAY-014 `own-service` (the digest's rule 11), the agents its venues as fillers. Buyers buying through those agents is CM-AIA-005 `extension-point`, and `core;extension-point` where the card links the platform's Agentic Storefronts. A note offering the tools for adding Shop Pay to any agent adds `extension-point` on CM-PAY-014. The Shop skill, which 'we used to create', is Shop's own (`own-service`) and runs in third parties' agents (`extension-point`).
- **R47.5, a feature the changelog already placed.** Fall 2026 repeats many changelog posts of September and October 2026 and a few earlier lines (SH-34, SH-35, SH-36, SH-32, SH-63, SH-66). A card takes the earlier line's capabilities and terms, each line's support and scope by the card's own words (the digest's rule 4; E61). A plan the post or a help page states, which the card doesn't, isn't the card's scope: POS Pro on local delivery, stock counts and recent carts, the Plus test drive on variants. The reading names it.
- **R47.6, the linked help pages.** A card's linked page was read only where the card's own words left its capability or support open: the Shopify connector for Grok, selling digital products from an AI tool, the CLI's `store create preview`, digital downloads, and Sidekick's generate-content (whose held copy of 16 October has no print-on-demand section). Each quote from them cites its record.

## New things

- **Store preview** (`new:Store preview`): SH-E-de899665 ('Store preview in agents': “Start building a store with” Shopify CLI “before signing up, and keep what you create when you’re ready to sell.”) and SH-E-2730895b ('Create a store or connect one to' Grok). A store built before signing up and kept, or claimed, at sign-up. The CLI's page states 'Creates a new Shopify store, with no need for an existing account.' (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@20958778`). The Grok connector's help page says the connector 'can help you start a store' and that a preview is a store once claimed (`raw/runs/20261016T213535Z-help-en-ar-html-md/fetch-00000.warc.gz@682980`). Both help pages read point to a help page, Setting up a store created with an AI tool or vibe code partner, not read.
  - Place of its own: none of B-extent's kinds is held. Its CLI command is CM-DVT-002's, and it has no admin route, plan line or API group in these sources.
  - Support written: `core`, by the digest's rule 22 (a new thing's support is what the platform does with it), since the platform creates the store. The brief's rule for a new thing with no place of its own is `shows`. The coordinator decides between them.
  - Proposed domain ONB, area the merchant's start, parent CM-ONB-004 (store setup) or CM-ACC-001 (the merchant's account), a reading. Name in English only: the Editions are in English.
  - Not CM-DVT-004: development stores are given to developers to test apps and themes. Not CM-DVT-005: ready stores are prepared by partners. Not CM-DVT-006: staging environments.
  - Terms searched with `caps --terms`: store preview; storefront preview; preview store; sign up; signup; create a store; store creation; claim; free trial; vibe code; onboarding; setup guide; new store; store setup; account creation; trial store. Placements searched: storefront preview, vibe code, claim a store, before signing up, store create.
- **Staff sales attribution** (`new:Staff sales attribution`, the digest's existing name, rule 44): SH-E-f6b9b367 ('Track every sale to the associate who made it'), `core`, beside CM-POS-001 `core`, as the correction with the changelog digest has it.

## Entries I couldn't tell, and what would settle each

- **SH-E-1ea6d195, the heading Online.** I placed it on CM-SFR-001 `core`: it names one part of the platform, the online store, the counterpart of Retail. Its cards span many capabilities: themes and Canvas, the storefront chat, Shop sign-in, rollouts, SimGym, search, languages, B2B catalogs and carts. Read as a grouping, it would be `out`, like Merchandising. The coordinator's reading of 'one part of the platform' settles it.
- **CM-AIA-004, the AI connector** (SH-E-b8b2191f, SH-E-f63ff45f, SH-E-2730895b, SH-E-6bf14186, SH-E-529f60a6, SH-E-10d335b2, SH-E-eb1266a8, SH-E-ae27c837). These lines make Shopify's cell held. The capability's name says 'through an MCP server the platform provides', but neither help page I read names MCP: the Grok connector works 'through the Shopify Admin API' where it has no dedicated action. They show the same thing as Salla's AI Connector: an outside assistant linked to the store for the merchant, approved in the admin. The capability's name, or its join, may need the coordinator's word. The connectors for Gemini, Muse and Copilot and the ChatGPT plugin rest on their help links' addresses (the digest's rule 53); their pages weren't read.
- **The agents' makers.** Grok and Grok Bot are xAI's products (the Grok help page), and Muse is 'Meta’s' (SH-E-529f60a6). No held statement names the makers of Claude Duet or Instinct. ChatGPT, Claude, Gemini and Copilot are taken as third parties' venues, as earlier lines take them (SH-34, SH-63, SH-92), a reading. A statement naming each would settle it.
- **SH-E-498f0818, its note 2** (in-store digital receipts sent to Shop): CM-ORD-008 `own-service`, the receipt delivered by Shop (the digest's rules 44 and E102). It could instead be CM-CHN-002, Shop as the buyer's order-tracking app. The Shop section's cards (SH-48 or SH-49) may settle it.
- **SH-E-07f54e8f, POS devices in the admin:** CM-POS-002 `core`, by the digest's rule 44 ('POS devices are CM-POS-002'). The devices whose status, location and app version the page shows run the POS app; CM-POS-002's note defines the device that takes the buyer's card. CM-POS-001 is the alternative. This line gives CM-POS-002 its first `core`.
- **SH-E-92c81f50, rollouts across channels.** By the digest's E68, the places its news names take their lines: headless builds (CM-SFR-011), Shopify POS (CM-POS-001), Google Shopping (CM-CHN-004, Google Shopping the venue) and the Shop app (CM-CHN-002 `own-service`). Read as a list of where a rollout may reach (the digest's rule 51), only CM-MKS-002 would stand. SH-E-22a4fbbe's list of what a rollout may include takes no line.
- **SH-E-8cfdd4da, the receipts' tax summaries:** a second CM-ORD-008 line scoped 'EU;UK;Canada', as a thing of the receipt under its own condition. A tax capability (CM-TAX-001) is the alternative.
- **SH-E-5376442f, print-on-demand by Sidekick:** CM-CAT-010 `shows`, since neither the card nor its held help page says who prints. The help page as recaptured after 16 October would settle it.
- **SH-E-f63ff45f, Product sourcing in agents:** CM-AIA-004 `shows`. Its blog link isn't held, and the card names no connector.

## Leads looked at and set aside

- Leads by name on common words (CM-LOY-008 'get, they'; CM-ORD-003 'processing'; CM-PTN-010 'powered by') name no thing of the entries.
- CM-OPS-004 (store status) and CM-OPS-002 (service status page) were set aside for SH-E-be6e25fb: the POS's connectivity status checks the internet, the Shopify service and hardware from the POS app. It is a screen of POS, as SH-34 placed it, not a status report or page.
- CM-CHK-010 (persistent cart) is the buyer's cart on their account. The POS's recent carts (SH-E-69915b45) and its cart on screen (SH-E-1c7fb0ca) are staff-side homonyms, CM-POS-001's. Shop's synced carts (SH-E-54b85104) are CM-CHK-010's.
- CM-MKT-023 for Sidekick's and SimGym's 'recommendations' (SH-E-238d1021, SH-E-97c8be79, SH-E-67d763db): these are recommendations to the merchant, not products recommended to buyers. Only the Inbox agent's recommendations to shoppers (SH-E-1221bb25) are placed there.
- CM-MIG-001 for SH-E-6bb56e86's catalog CSV export: the export and its column are the catalogs' own (the ruling after SA-25 and SA-26).
- New-thing leads: for Store preview, I read the cells of CM-DVT-002, CM-DVT-004, CM-DVT-005 and CM-AIA-005. CM-SHP-012 and CM-ACC-005 were leads by name only. Staff sales attribution's leads (CM-ACC-004, CM-PLN-001, CM-TRU-013) are by name only, and CM-POS-001 takes its line.

## What the sources state that no entry holds (for the second stage)

- **The Grok connector's help page** (`raw/runs/20261016T213535Z-help-en-ar-html-md/fetch-00000.warc.gz@682980`, its text lines 3, 4, 33 and 42 to 99):
  - standard plan pricing applies and 'there's no extra Shopify fee for using the connector';
  - the connector isn't on the App Store and is added from Grok's connectors page, with approval in the Shopify admin;
  - what the connector does depends on the data access approved and the staff account's permissions;
  - its actions table: products, collections, inventory, discount codes (percentage-off only), and orders, customers and analytics read-only. Pages, blogs, menus, metafields, markets and translations go through the Admin API.

  These are leads for CM-AIA-004's and CM-API-002's cells.
- **Selling digital products from an AI tool** (`…fetch-00000.warc.gz@465862`):
  - 'The maximum file size is 5 GB.' for a file sent from the chat;
  - links work only from the Digital Products app's supported providers;
  - automatic delivery marks the order fulfilled.

  These are leads for CM-SEL-002.
- **Digital downloads** (`…fetch-00000.warc.gz@66467613`): 'If you add a file from the product page in your Shopify admin instead of in the Digital Products app, then each file can be up to 500 MB.' A file attached from the admin's own product page is a lead for a `core` line on CM-SEL-002, whose Shopify cell holds only the App Store category.
- **The CLI's `store create preview`** (`raw/runs/20260930T003705Z-shopify-dev-md/fetch.warc.gz@20958778`): its flags `--country` and `--name`, the store's country and name.
- **The Fall 2026 page data** (`structures/shopify/editions-page-data/rmx-data/`) holds the components' props, among them, perhaps, the Shop skill's prompt behind Copy prompt. Not read.

## Problems with the brief or the scripts

- `editions`' items join each link's hidden tooltip to its text ('shop.mdLearn more', 'Shopify CollectiveLearn more'), so an entry's text isn't what the page shows. Quotes and terms must stop at each link (R47.2). The extractor could drop `role="tooltip" hidden` spans, or keep them apart.
- `earlier` found nothing for most entries, since Fall 2026's keys are new. Searching the placements for each card's distinctive words found the changelog's and Spring '26's lines (R47.5).
- The digest has no rule for a section heading as an entry (R47.1). Neither does the brief, apart from M-13 and the rulings on public-site headings.
- The checker's quote test reads a cited record only where the reading names it: 'the same record' fails, so each quote cites its record again.
- No conflict with B-extent.md was found, apart from the support of a new thing with no place of its own (the brief's `shows` against the digest's rule 22), under Store preview above.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 80 of 80 entries, no problem.
- **Two of the batch's choices decided:**
  - **Store preview is `shows`** (lines 18 and 25). The brief writes a new thing with no place of its own `shows`, and the digest's rule 22 ('a new thing's support is what the platform does with it') is for a new thing that has one. Rule 22 is restated so.
  - **A section heading over several capabilities' cards is `out`:** Agentic (CM-AIA-004's connectors and CM-AIA-005's agents), Online and Retail, as Merchandising is. The pricing page's 'Always included' is `out` the same way (P9), and the page data's collection titles are no entries at all. Sidekick, whose cards are all CM-AIA-002's, keeps its line. R47.1 is narrowed so.
- **The `CHANGES` stand:**
  - CM-AIA-004 becomes held from the platform's own connectors and plugins for outside AI assistants, `core`, with xAI's Grok Bot `extension-point`. The cell names an MCP server, which the help pages don't; its definition is noted for the amendment.
  - Shop's things (its skill, sign-in, lead capture, carts and receipts) are `own-service`, by rule 11.
  - Checkout Blocks, Collective, Translate & Adapt and Inbox are `own-service`, by the table.
  - CM-PAY-014 is `extension-point` for Shop Pay in others' agents.
  - The POS receipts and devices are `core`.
- **The rules R47.2 to R47.6 stand,** with R47.1 as narrowed, for SH-48 and SH-49, and join the digest's section 6.
- **Cost:** 19.6 million tokens over 87 requests, about 245,000 an entry. The context reached about 401,000 tokens.
