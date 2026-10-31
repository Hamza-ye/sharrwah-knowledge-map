# SH-63: notes

Batch SH-63: 84 entries of Shopify's `editions-page-data` (observed-sh at `e38dc17e3`, `structures/shopify/editions-page-data/loaderData/items.jsonl`). They are Summer 2025's developer collection Extensions (`developerCollections[4]`, line 9, entries 1 to 10), then Winter 2026 (line 10) from its first section, Sidekick, through Marketing's `text-list-4` (entries 11 to 84). Winter 2026's ChatGPT XXL card (Shopify Product Network, SH-E-7cdac625) opens SH-64.

What I read:
- the brief (`briefs/H-held.md`);
- the digest, `held/rules/editions-page-data.md`, whole, its section 6 included;
- the last section of `held/review-H-rulings.md`;
- observed-sh's `README.md`, `structures/README.md` and `docs/READING.md`, with `docs/GAPS.md` and `structures/REGISTER.tsv` read by their Editions rows;
- the selection rows for `editions` and `editions-page-data`;
- B-extent's "Cells and evidence" and "Conventions from the dry run";
- the evidence map's Shopify start;
- SH-62's last lines, the batch before mine.

Earlier batches' notes, only where the digest sent me:
- `notes-SH-60.md`, E80 (lists introduced by 'including' or ending 'and more') and E83 (a title naming the API it extends);
- `notes-SH-61.md`, E90 (a separate tool at its own site).

Precedent lines, read with `earlier`, `makers` and `grep` on the placements: SH-1, SH-14, SH-30, SH-34 to SH-37, SH-56, SH-57, SH-60 to SH-62, SH-95.

Counts:
- entries: 83 on capabilities, 1 new, none out;
- lines: 135, of which 94 `core`, 17 `own-service`, 12 `extension-point`, 7 `shows`, 4 `core;extension-point` and 1 `outside`.

## The new thing

- **`new:Tinker by Shopify`**, `own-service`, one entry: SH-E-5d225f0e, Winter 2026 > Online > Tinker.
  - The card: 'Tinker app', 'Introducing Tinker', 'An app where entrepreneurs can play with the latest AI tools in a single place.', with Get app to www.tinker.com.
  - The name: SH-95 named it so from its Google Play listing (SH-E-e95ada94, `new:Tinker by Shopify`, `own-service`). That listing names Shopify Inc. as the developer, the maker statement (the ruling after SH-2), and I kept the name.
  - No place of its own: a separate app with its own site, not an admin route, section, API group, plan line or app category.
  - Proposed: domain F (AIA), parent CM-AIA-001 or none. CM-AIA-001 is the platform's AI in the merchant's admin, and Tinker isn't in the admin (the digest's rule 50).
  - Its name in English, the Editions' only language: 'Tinker app', 'Introducing Tinker', 'Tinker by Shopify'.
  - Terms searched: Tinker, playground, AI apps, AI tool, experiment with AI, AI tools, entrepreneurs. Only CM-AIA-001 (by 'AI tool') and CM-SFR-012 (by 'playground', a homonym) came up.
  - The checker's leads for it (CM-OPS-004 by 'tools', CM-SHP-004 and CM-TAX-004 by 'app, place') are none of them its thing.

## Rules I followed that the digest doesn't hold (for the coordinator, from E105)

- **E105. Sidekick doing a task on a platform feature.**
  - The card takes CM-AIA-002 `core`, the admin's own AI assistant. With no limit stated in Winter 2026, it is `core` even where an earlier source had the feature in early access or rolling out (the digest's rule 4: each edition by its own words).
  - The feature Sidekick builds, edits or acts on takes its own line, as SH-30, SH-35 and SH-36 placed the same tasks from the changelog:
    - custom apps: CM-APP-009 `core`;
    - segments: CM-CUS-002 `core`;
    - theme edits and blocks: CM-SFR-002 `core`;
    - reports in the ShopifyQL query editor: CM-ANL-001 `core`, as SH-36;
    - Shopify Balance: CM-PAY-023 `core`;
    - B2B companies: CM-B2B-002 and CM-B2B-001 `core`;
    - Flow's workflows: CM-AUT-001 `own-service`;
    - Messaging's email editor: CM-MKT-007 `own-service`;
    - the Shopify mobile app it runs in: CM-SRF-001 `core`.
  - An image it makes takes CM-CAT-007 only where the card names a product ('a highly polished product shot', SH-E-dd6965bd), as SH-61 kept it off for 'Generate visuals' (SH-E-ca07f06e).
  - Two kinds of thing take no line:
    - the admin's areas it answers about, which are the admin's frame (rule 49);
    - a card's example prompts (`customData`: 'Reorder products', 'Team tasks App' and others), which are examples (rule 51).
- **E106. A Sidekick card with only its title** ('Sidekick video', SH-E-b3d10dd8, an xxl video card) is CM-AIA-002 `core` by its title (rule 38). The group's description is a claim.
- **E107. Extension APIs for developers.**
  - The API's own thing goes on the extension's capability, `extension-point`:
    - customer account UI extensions: CM-CUS-014;
    - checkout UI extensions: CM-CHK-004;
    - POS UI extensions: CM-POS-004;
    - payment extensions: CM-PAY-011 (E63).
  - Debugging the extensions on a device is CM-DVT-001 `core` (rule 17).
  - The POS Print API is CM-POS-004 `extension-point`, with CM-ORD-009 `shows`. CM-ORD-009's note sends the printing apps do through an extension to the extension's capability, and its cell holds `admin_print` so.
- **E108. Payments at the POS, in more countries or by more methods.**
  - In-person payments and Tap to Pay: CM-PAY-021 `core`, the countries the scope (SH-E-1fa0501d).
  - A card network: the filler, as EFTPOS was (SH-E-8c127661).
  - Local methods paid by QR code in store: CM-PAY-017 `core`, the methods the fillers (SH-E-f44a40b4).
  - A stablecoin: CM-PAY-018 `core` (SH-E-54492956).
  - 'in store' adds CM-POS-001 `core` (E68).
- **E109. The POS Hub is `own-service`** on its maker statement, 'The Shopify POS Hub is now generally available on the Hardware Store, and we’ll start shipping units to all merchants who pre-ordered.' (SH-E-04dd57d3, SH-35's line). The POS group's following cards are read with its lead card (rule 38). Barcode scanners 'newly integrated' with the POS, whose makers aren't named, are CM-POS-002 `shows`, the makers a gap (the ruling after SH-43).
- **E110. A refund screen's exhaustive list of where the money goes** gives each item a line (E80): original payment on CM-RET-002, gift card on CM-LOY-002, store credit on CM-LOY-001, all `core`.
- **E111. A third party's app doing the store's local delivery** (Uber Direct) is CM-SHP-006 `extension-point`, where the cell holds the App Store category Delivery and pickup apps, not CM-SHP-008, the store's own delivery. Its live tracking is CM-SHP-017 `extension-point`, the third party the filler of both.
- **E112. AI in an admin settings flow that isn't Sidekick** (domain name suggestions at `settings/domains/buy`) takes CM-AIA-001 `core` beside the flow's capability. A language limit ('English only.') is a quality.
- **E113. A third party's AI builder** that spins up a Shopify store and storefront (Lovable), with no platform interface named, is CM-SFR-011 `outside`, the builder its filler (the check after SH-60).
- **E114. Shopify Messaging's planner** ('Calendar view for messaging') is CM-MKT-019 `own-service`: a marketing calendar the app itself provides (rule 16).

## Entries I couldn't tell, and what would settle each

- **SH-E-b4a83097, 'Attribute removal via UI extensions'**, line 6: CM-CHK-009 `extension-point`.
  - My reading is that a cart attribute is a custom field of the order. CM-CHK-009's Shopify cell holds nothing, so this line alone makes it held (CHANGES).
  - What would settle it: a held statement that says what a cart attribute is. The card says only 'an attribute attached to the cart and checkout'.
  - Failing that, the line could go, leaving the card on CM-CHK-004 alone.
- **SH-E-9e78ba59, 'Localize extensions for customer accounts'**, line 4: CM-B2B-001 `extension-point`.
  - My reading is that 'company-specific logic' names business buyers' companies, as SH-60's card on the same accounts names B2B customers (SH-E-d6d3c7df).
  - What would settle it: the localization API's own statement of what 'company' is. Its page, shopify.dev's customer-account-ui-extensions/unstableapis/localization, is outside the entry's sources and wasn't read.
- **SH-E-ded2866e, 'Calendar view for messaging'**, line 131: CM-MKT-019 `own-service` (CHANGES: the Shopify cell becomes held).
  - What would settle it: whether the class's marketing calendar (Salla's, whose content no statement defines) is the same thing as Messaging's planner.
- **SH-E-bca897c1, 'Vibe code with Lovable'**, line 72: CM-SFR-011 `outside` (CHANGES).
  - That Lovable builds a custom storefront on the platform's data is a reading. The card says 'Spin up a Shopify store using Lovable'.
  - What would settle it: Lovable's page (lovable.dev/shopify), outside the sources.
- **SH-E-5b90f327, 'Sell on WordPress'**: CM-CHN-001 `shows`, WordPress the filler.
  - 'The Shopify plugin' has no maker statement held (`makers`: none), so the plugin is `shows`, the maker a gap.
  - The products and collections it adds are records (E96).
  - The cart and checkout it adds take no line of their own: I read them as the channel's parts. If the coordinator reads them as the platform's own cart and checkout on another site, CM-CHK-002 and CM-CHK-001 would take `shows` lines.
- **SH-E-a8545cb4, 'POS Hub-compatible scanners'**: CM-POS-002 `shows`.
  - I first wrote `core`, for the platform's own integration of the scanners. I changed it to `shows`, since the scanners' makers aren't named (the ruling after SH-43).
  - If the coordinator reads 'newly integrated' as the platform's own POS support for the hardware, it is `core`, which would be CM-POS-002's first `core`.
- **SH-E-00f21563, 'Transfers POS extension'**: CM-INV-006 and CM-POS-001 `core`, scope 'POS Pro'.
  - The extension's maker isn't named (`makers`: none).
  - I read it as the POS's own access to the admin's own transfers, under the add-on's plan statement. If it is read as an app with no maker, the CM-INV-006 line would be `shows`.
- **SH-E-eb93704f, 'Sidekick for app discovery'**: CM-APP-002 `core;extension-point`, as SH-62 placed app recommendations (E86, matched), and CM-APP-001 `core` for installing.
  - The card doesn't say the apps are third parties'. The `extension-point` rests on the App Store's cell.
- **SH-E-dd6965bd, 'Sidekick edits images on mobile'**: besides CM-AIA-002 and CM-SRF-001, it takes CM-CNT-001 `core` for the mobile app's 'file editor' (a place its news names) and CM-CAT-007 `core` for 'product shot'. Either could be read as named in passing.
- **SH-E-5e7f4c68, 'Sidekick generates blocks for all themes'**: I gave the Shopify Theme Store no line, reading it as named in passing for where the themes come from (E68). Read as what the news now covers, it would take CM-SFR-003 `core`.

## The checker's other notes

- **Line 21** ('Sidekick video', SH-E-b3d10dd8) is flagged as a container. The card shares its title with its xxl group ('Sidekick video', `hideXxlTitle: true`). That group holds only this card and has no entry of its own. The entry is the card, not the group.
- **Lines 105, 118 and 125**: their first leads hold nothing on Shopify, and none is the entry's thing:
  - CM-MKS-009, by 'countries', is market data;
  - CM-ORD-003, by 'processing', is order statuses, a homonym;
  - CM-API-013, by 'all, one, rather', is no lead.
- **The brand notes**, each settled by a rule of the digest:
  - lines 17, 55, 58 and 59: POS (rule 9), Shopify Balance (rule 25), Agentic Storefronts (the ruling after SH-2);
  - line 27: CM-APP-007 for an `apps/<handle>` link (rule 40);
  - line 25: I narrowed its terms to Sidekick's own words.

## What the sources state that no entry holds (for the second stage)

Winter 2026's page data, `structures/shopify/editions-page-data/loaderData/items.jsonl`, line 10, under `loaderData` > `routes/($locale).editions.winter2026`:
- **`topSkills`**: the page's Sidekick prompts, each with a command and an admin address: 'editions', 'seo-optimization', 'monthly-snapshot' and others. An example is 'Take my top-selling product and optimize it for SEO.', at `admin.shopify.com/sidekick?sk_s=seo-optimization…`. They are prompts, a lead for CM-AIA-002's second stage, not features.
- **`globalContent`**:
  - the 'Get notified' modal, with 'This feature will be available soon. Sign up to get notified.';
  - the label 'Try it with Sidekick' that cards' CTAs use.

  No card of my batch has a `signUpModal`.
- **`hero.subtitle`**: 'A new world of commerce. 150+ product updates.'
- **The collections' descriptions** I read the cards with:
  - Sidekick: “The AI-powered Shopify expert who's just as obsessed with your business as you are.”;
  - Agentic: 'Sell directly in AI chats with built-in tools that syndicate your products to every AI platform.';
  - Online: 'Validate store changes with A/B testing and an AI tool that simulates shopping behavior.';
  - Retail: 'New in-store hardware that provides unwavering reliability.';
  - Marketing: 'Grow your sales with a first-of-its-kind product network.'

  The Marketing description names the product network that SH-64's first card holds.

Winter 2026's page holds no 'rolling out', 'early access', 'coming soon' or 'beta' (searched in line 10), so no summary limits its cards (E69 doesn't apply).

## Structures whose items and sources disagree

None found. The item's `descriptionHtml` was read as rendered by `show`. Quotes keep within one text node where a link splits the text (rule 5).

## Problems with the brief or the scripts

- `held_entries.py batches` takes no `--platform`. It wasn't needed.
- The checker computes CHANGES against the model, not against earlier batches' held lines. Several of mine repeat those lines' support and change nothing once those lines are amended in:
  - Flow, Messaging, Bundles and Subscriptions `own-service`;
  - CM-MKT-003 `core` (rule 47);
  - receipts on CM-ORD-008 (rule 44);
  - Shop's sign-in `own-service`.
- The container note on a card that shares its group's title (line 21) seems a false positive.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 84 of 84 entries, no problem.
- **The `CHANGES` stand.** Flow, Messaging, Bundles, Subscriptions and Shop's sign-in are `own-service` by the digest's table. The automatic discounts, the receipts and the tax field validation follow rules 47 and 44, and E67.
- **The four resting on the batch's readings stay as placed,** each marked in its line:
  - the cart attribute as CM-CHK-009's custom field;
  - 'company-specific logic' as B2B;
  - Messaging's planner as CM-MKT-019;
  - Lovable `outside` on CM-SFR-011, since no platform interface is named (B-extent).
- **The reversed line stands:** the POS Hub's compatible scanners are `shows`, since their makers aren't named. The POS Hub itself is `own-service` (E109).
- **The new thing** keeps SH-95's name, Tinker by Shopify, `own-service` on its listing's developer, with no place of its own.
- **The rules E105 to E114 stand** and join the digest's section 6.
- **Cost:** 17.5 million tokens over 83 requests, about 208,000 an entry. The context reached about 380,000 tokens.
