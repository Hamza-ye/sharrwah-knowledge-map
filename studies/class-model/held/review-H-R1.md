# Review of the held pass's dry run, part R1: BC-1, lines 2 to 37

**What this is.** Part R1 of the review that `studies/class-model/briefs/H-review.md` (at `2316f3ab`) sets: BC-1's lines 2 to 37, the structures channel-catalog (lines 2 to 27, entries 1 to 19) and contracting-entities (lines 28 to 37, entries 20 to 24). Its rows are in `review-H-R1.tsv`, one per verdict, 64 rows for 36 lines.

**What was read, pinned:**
- BC-1's placements and notes at `ff50bbee`;
- H-held.md and `held/selection.tsv` at `dc1e6414`;
- the model at `13205959`, through `class_slice.py` and `land_points.py cell` (unchanged since in the files read);
- other-product-class at `0d79b794f`.

**The sources, as cited below:**
- **ARIA:** the catalog's source, `other-product-class@0d79b794f:bigcommerce/raw/runs/20261029T023811Z-channels-en/steps/002.frame-0.aria.yaml`. Its sha256 matches `meta.json`.
- **TERMS:** the contracting entities' page, which their `meta.json` names under `source`: `https://www.commerce.com/terms/`, held in `bigcommerce/raw/runs/20261029T024622Z-legal-pricing-docs/fetch.warc.gz`. The record is `fetch.cdx` line 2, offset 1160, `urn:uuid:e7a61d91-2f1a-4a1a-ab8e-f71353f3b9ad`. A second capture, at offset 132484, reads the same. It was read with a WARC reader of my own (scratchpad), not with the repository's script.
- `source.html` beside `items.jsonl` is only a segment of TERMS: the grid's header and first five rows. Its sha256 matches `meta.json`'s `sha256_of_segment`.

Every claim below is a reading unless it quotes a source or the model, which are facts at the commits above.

## Counts of verdicts

| Verdict | Rows | Lines |
| --- | --- | --- |
| stands | 14 | 10, 12, 13, 22 to 27, and 28, 30, 32, 34, 36 |
| wrong supports: own-service | 16 | 2 to 9, 14 to 21 |
| wrong filler | 16 | 2 to 9, 14 to 21 |
| can't tell | 7 | 2 and 14 (CM-AIA-005); 29, 31, 33, 35, 37 (CM-APP-011) |
| wrong reading | 5 | 29, 31, 33, 35, 37 |
| missing line: new:Professional Services shows | 5 | 29, 31, 33, 35, 37 |
| missing scope: paid plan | 1 | 11 |
| **all** | **64** | 36 lines; 22 lines have at least one miss |

## The misses, by cause and effect

| Cause | Effect | Rows | Lines | What |
| --- | --- | --- | --- | --- |
| brief | kind | 10 | 2, 3, 6, 7, 8, 14, 15, 18, 19, 20 | Feedonomics read as a third party: `extension-point` on CM-CHN-004, which then gains `extension-point` it shouldn't (rule 4) |
| brief | count | 6 | 4, 5, 9, 16, 17, 21 | The same, on CM-MKT-010, whose cell should gain `own-service` (rule 4) |
| brief | filler | 8 | 2 to 9 | Feedonomics as a filler, though it is a company of the group (rules 4 and 5) |
| care | filler | 8 | 14 to 21 | Feedonomics as a filler of entries whose text doesn't name it (rule 5) |
| brief | capability | 5 | 29, 31, 33, 35, 37 | "Extensions" joined to CM-APP-011 on the word. The source's definition makes the maker a third party (rule 2, and a method ruling) |
| brief | capability | 5 | 29, 31, 33, 35, 37 | "Certain Professional Services", stated and left unplaced (rule 2) |
| brief | column | 5 | 29, 31, 33, 35, 37 | The reading leaves out the source's definition of Extension. The structure's `source.*` and its `meta.json` source are two files (rule 1) |
| brief | column | 1 | 11 | The reading rests on the step's "Create more storefronts with paid plan", but the scope stays empty (rules 1 and 5) |
| evidence | count | 2 | 2, 14 | Google's "AI-powered experiences": possibly CM-AIA-005's |

By effect:
- **count:** 8 rows;
- **kind:** 10;
- **filler:** 16;
- **capability:** 10;
- **column:** 6.

By cause:
- **brief:** 40;
- **care:** 8;
- **evidence:** 2;
- **tool:** 0.

By structure:
- **channel-catalog:** 35 misses on 17 of its 26 lines;
- **contracting-entities:** 15 misses on its 5 CM-APP-011 lines. Its 5 CM-ACC-002 lines stand.

## The cases

### BC-1's channel cards (lines 2 to 27): who does the work

A reading, from each card (ARIA) and its source step only, with the terms (TERMS) for whether a named company is of the platform's group.

| Lines | Card | Who the card and its step show doing the work | `supports` | Fillers |
| --- | --- | --- | --- | --- |
| 2 to 9 | Featured: Google, Meta, Microsoft Ads, Pinterest, TikTok Ads | Feedonomics, by its region "Featured channels by Feedonomics" (ARIA:27-28). TERMS makes it a company of the group | `own-service` (not `extension-point`) | the channel: Google, Meta, Microsoft, Pinterest, TikTok. Feedonomics is none |
| 10 | BigCommerce | the platform: "Our powerful built-in storefront platform" (ARIA:70) | `core` | none |
| 11 | BigCommerce, as an added storefront | the platform, on a paid plan: "Create more storefronts with paid plan" (ARIA:62) | `core`, scope paid plan | none |
| 12 | Catalyst | the platform: "Our fully composable ..." (ARIA:76) | `core` | none |
| 13 | DEITY | DEITY, with its "Falcon PWA Storefront and BigCommerce" (ARIA:82) and no "Our" | `extension-point` | DEITY |
| 14 to 21 | Ads and social: the same five | No one, in the entries' text. Feedonomics, through the step's tie: the same name, description and Learn more `Feedonomics-for-<channel>` as the featured card | `own-service` with the tie; `core` without it; `extension-point` on neither | the channel only |
| 22 | Buy Buttons | no one named. The slug `Buy-Buttons-app` is an address | `core`, maker gap | none |
| 23 | PayPal Zettle POS | PayPal Zettle: "PayPal Zettle's all-in-one POS solution". Its Learn more is Zettle's own guide to connecting with BigCommerce (ARIA:131-132) | `extension-point` | PayPal Zettle |
| 24 to 26 | Amazon, Walmart, eBay | no one named for the connection; the marketplace is the venue | `core`, maker gap | Amazon, Walmart, eBay |
| 27 | impact.com | impact.com. Its Learn more is the App Marketplace's page `www.bigcommerce.com/apps/impact-partnership-cloud/` (ARIA:159-160) | `extension-point` | impact.com |

**"Who builds these connections isn't stated"** (notes, item 4: Buy Buttons, Amazon, Walmart, eBay, on lines 22 and 24 to 26). It holds, as a fact of the step: no card and no word of the step names a maker.
- The Learn more targets are addresses: `sell.amazon.com/?ld=rpussoa-bigcommerce`, and BigCommerce's articles `Setting-Up-Walmart`, `eBay-App` and `Buy-Buttons-app` (ARIA:139-152, 123-124).
- B-extent's own-service clause settles the value: "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap". What they show is the platform's own Channel Manager offering the channel: `core`, as CM-CHN-003's cell already reads.
- What would settle the maker is a statement naming it. The articles `eBay-App` and `Buy-Buttons-app` may hold one; this part didn't search for them beyond the step.
- A lead, not read: TERMS defines the Feedonomics Platform as also "aggregating order data, bridging order management and fulfillment". But no marketplace card names Feedonomics, so CM-CHN-003's gap stays.

**The notes' problem with catalog cards.** The notes report: "The supports rules don't cover a catalog card in the platform's own admin that names a third party as the venue or the provider". B-extent settles most of it by who a card names as doing the work:
- no one, or the venue only: `core` by what it shows, with the maker gap;
- a named third party: `extension-point`;
- a company of the group: `own-service`.

The venue is the filler. What B-extent doesn't settle is whether the platform's own catalog of channels is "something the platform provides" for `extension-point`. Its list names an app-store or marketplace category, an extension target, a provider interface and an API. A method ruling, M2 below.

### The entries that name a company (lines 2 to 9, 14 to 21, 28 to 37)

Judged by each entry's own words and its own sources only.

**The contracting entities (lines 28 to 37).**
- Each row names a "Commerce Entity" as the provider of "Ecommerce Platform, Extensions, and certain Professional Services".
- Their source makes each entity the platform's company: "“Commerce” means the Commerce entity with which you are entering into this Agreement ... “Commerce” means the entity identified in the following table:" (TERMS). The grid follows that clause in the page's order: the streamed block that ends with the clause stands just before the grid, and "Eligibility" just after it.
- The source also says what the services are:
  - the Ecommerce Platform is "the subscription to Commerce’s ecommerce software-as-a-service platform": the platform itself, not a separate product;
  - an Extension is "a service developed by a third party but implemented and provided by Commerce that is identified in the Order Form as an Extension and further described in the corresponding Program Document".
- So each row names a company of the group as the **provider, not the maker**, of a separate service, Extensions, and as the provider of "certain Professional Services".
- `own-service` holds as a value, since B-extent says "maker or provider". Whether CM-APP-011 is the capability is the method ruling M1. Professional Services takes a `new` line.

**The Feedonomics cards (lines 2 to 9 and 14 to 21).**
- By their own words and their step, they name Feedonomics as the provider of the featured channels: the region "Featured channels by Feedonomics", and for lines 14 to 21 only through the step's tie.
- They never say Feedonomics is of Commerce's group. Nor do they say it is a third party: the readings' "a third party as far as the entry says" is an assumption.
- The batch's other source, TERMS, says it is of the group:
  - "This Master Services Agreement (...) is between Commerce.com US, Inc. and any of Commerce’s affiliates, subsidiaries, including, but not limited to Feedonomics Holdings, LLC, successors, or parent companies (“Commerce”)";
  - "“Affiliate” means any entity that directly or indirectly controls, is controlled by, or is under common control with the subject entity";
  - the Contracting Entity table names "Feedonomics Holdings, LLC, a Delaware corporation in the United States" for the "Feedonomics Platform", "If purchasing and/or contracting solely with Feedonomics";
  - the platform defines that product as one that "optimizes product catalogs to syndicate listings across hundreds of online channels (data feed management)";
  - commerce.com's navigation links "BigCommerce", "Feedonomics" and "Makeswift", each labelled "external link to ... product and brand site".
- B-extent's maker evidence is "a statement naming the company". I read the card, which names the provider, and the terms, which name it of the group, together as supporting `own-service`. CM-CHN-004's cell already builds its `own-service` that way from BC-S-0366.
- If the coordinator rules that the group statement must be in the entry or its own source, the cards take:
  - `shows` (lines 2 to 9, the named provider's status unknown);
  - `core` (lines 14 to 21, no provider named);
  - in both cases with the gap noted, never `extension-point`.

  That is M3 below.

**Other names:**
- "BigCommerce" in "Showcase your BigCommerce products" (lines 5 and 17) and in DEITY's card is the platform's brand, not a maker.
- No held statement names DEITY, PayPal Zettle or impact.com as of the group. TERMS lists six entities and three brands, none of them these.

## Readings that rest on a file beyond the item and its source

None of my part's 36 lines does:
- lines 11 and 14 to 21 cite ARIA, which is the structure's own source (`meta.json`'s `held_as`);
- lines 23 and 28 to 37 cite the model's cells, which H-held.md names.

My own verdicts on lines 2 to 9 and 14 to 21 do rest on another structure's source (TERMS). H-held.md doesn't allow that for those entries: its rule 1, and its Rules' "only from what the entry and its source state". That is fix F1.

## What the batch never placed

### channel-catalog (source ARIA)

| What the source states that no entry holds | Place | Would it change a cell? | Left out by |
| --- | --- | --- | --- |
| The Channel Manager's own place: link "Channels" to `/manage/microapps/channel-manager`, heading "Add new channel" | ARIA:1-4 | CM-CHN-001's BigCommerce cell gains its first admin place, as core evidence. Already core: column | the build (cards only) |
| The category link "Featured channels" to `#featured-channels-by-feedonomics` | ARIA:10-11 | no. It ties the category to Feedonomics, which lines 14 to 21 rest on | the build |
| The Storefronts block: "Create more storefronts with paid plan"; "Optimize your operations and enable multi-geo selling with Multi-storefront capabilities. Manage multiple storefronts in one place by upgrading to one of our paid plans."; "Upgrade plan" | ARIA:61-67 | Column on two cells. CM-CHN-007 takes the paid plans as scope (line 11). CM-MKS-001's BigCommerce cell is core on S-02's statements only and gains held evidence for "multi-geo selling" | the build: `meta.json`'s `items` note records it, as no item |
| Each card's Learn more, 19 links | ARIA:32-33 ... 159-160 | No count. They carry the maker evidence above: Zettle's guide, impact.com's App Marketplace page, `Feedonomics-for-<channel>` | the build. The notes name this |
| "View more storefront platforms", to `developer.bigcommerce.com/tools-resources#headless-integrations` | ARIA:86-87 | CM-SFR-011 at most: other storefront platforms, none named. Column | the build. The notes name this |
| The store the catalog is shown to: `meta.json`'s `source.store`, "trial store w5pamplexj, default country Oman, currency OMR". The REGISTER notes "the list follows the store's country and currency" | `meta.json`; `structures/REGISTER.tsv` | Filler. Every channel line's scope is empty, so its fillers get no market: Google, Meta, Microsoft, Pinterest, TikTok, DEITY, PayPal Zettle, Amazon, Walmart, eBay, impact.com | the build: the entries' label is `.`. H-held rule 5 takes scope from the entry's words only |

### contracting-entities (sources `source.html` and TERMS)

| What the source states that no entry holds | Place | Would it change a cell? | Left out by |
| --- | --- | --- | --- |
| Two more rows of the same grid: "If purchasing and/or contracting solely with Feedonomics", Worldwide, Feedonomics Holdings, LLC, New York, Feedonomics Platform; and Worldwide, Makeswift, Inc., New York, Makeswift visual editor / builder | TERMS. The segment ends at the very byte where the Feedonomics cell begins | No. The concern map holds them: BC-S-0366 in CM-CHN-004 and BC-S-0285 in CM-SFR-006, both `own-service`; BC-I-0547 and BC-I-0548 in CM-ACC-002 | the build: `meta.json` counts 5 rows "per country of residence", as REGISTER describes it. The notes don't name this disagreement |
| The preamble's "any of Commerce’s affiliates, subsidiaries, including, but not limited to Feedonomics Holdings, LLC" | TERMS (S:1) | Yes, count. CM-MKT-010's BigCommerce cell gains `own-service`: it withholds it because "no statement says it is BigCommerce's group company: a gap". CM-CHN-004's gap closes (column). It settles lines 2 to 9 and 14 to 21 | the build (the grid only), and the concern map, whose BC-S-0425 stops at "any of Commerce’s affiliates" |
| The Contracting Entity clause in full: a previous agreement's entity governs, and otherwise "the entity identified in the following table" | TERMS (S:1, just before the grid) | Column. CM-SFR-006's "no statement held says so in those words" for Makeswift, Inc.: the clause makes each entity of the table a Commerce entity. BC-S-0427 holds only its first sentence | the build |
| The definitions: Extension in full; Ecommerce Platform; Feedonomics Platform's second sentence (syndicating listings; order data, order management and fulfillment); Services; Third-Party Product(s); Affiliate | TERMS (S:1) | Capability: CM-APP-011's join on "Extensions" (M1); its cell reads "No statement ... says what they are". Column: CM-CHN-004 | the build. BC-S-0464 holds only the Extension definition's last sentence |
| commerce.com's brand links, "external link to feedonomics product and brand site" and the same for BigCommerce and Makeswift, and the footer's "Products" | TERMS (navigation, footer) | Column: more maker evidence for CM-CHN-004, CM-MKT-010 and CM-SFR-006. A reading that site chrome is a statement | the build |

TERMS links the Professional Services program document (`/terms/professional-services-program-document/`). The run doesn't hold it: its `urls.txt` lists 20 addresses, none of them that one.

## The notes' claims for my structures

| Claim (`notes-BC-1.md` at `ff50bbee`) | Verdict | Why |
| --- | --- | --- |
| channel-catalog is entries 1 to 19, contracting-entities 20 to 24 | stands | `entries.tsv` locates them at `items.jsonl` lines 1 to 19 and 1 to 5. The entries' text matches the items |
| Couldn't tell 3: the Feedonomics cards are `extension-point`, "Not `own-service`: no entry names Feedonomics as a company of Commerce's group" | wrong in its outcome | True of the channel entries. But the batch's own contracting-entities source names Feedonomics Holdings, LLC among Commerce's affiliates and subsidiaries (TERMS): `own-service`. Its "stricter reading ... would make 9 to 13 `core`" is right for that reading |
| Couldn't tell 4: Amazon, Walmart, eBay and Buy Buttons `core`, the maker unstated "as CM-CHN-003's cell already says"; Buy Buttons on CM-CHN-001 | stands | The cell says so ("No statement held says whether BigCommerce, Feedonomics or an app builds the marketplace connections"). CM-CHK-008 and CM-PAY-032 were tested and fail. The slug rule applies to `eBay-App` too |
| Couldn't tell 5: PayPal Zettle, DEITY and impact.com `extension-point`; impact.com the first on CM-MKT-013, which was none-held | stands | Each names a party's own solution. Zettle's and impact.com's links are the third party's guide and the App Marketplace page. CM-MKT-013's BigCommerce cell is none-held (searched: affiliate; influencer; creator) |
| Couldn't tell 6: CM-ACC-002 `shows` | stands | As the cell reads BC-S-0425 to BC-S-0433 |
| Couldn't tell 6: CM-APP-011 `own-service`; "The terms' definition would settle it" | the definition is held, and unsettles the line | TERMS: "a service developed by a third party but implemented and provided by Commerce": provider, not maker. Can't tell, M1 |
| Couldn't tell 6: "certain Professional Services" left unplaced; "No capability is the platform company's own professional services" | the search stands; the omission doesn't | My search agrees: CM-PTN-005 is partners' services, and CM-ONB-003 is support and learning. By H-held rule 2 the thing then takes `new:Professional Services` with `shows` (no place of its own) |
| Differences: CM-MKT-013 none-held, gains a placement (19) | stands | `land_points.py cell CM-MKT-013 bigcommerce`: none-held |
| Differences: "CM-ACC-002 stays `shows`" | stands | The cell is `not-stated`, and the held lines are `shows` |
| Items against source, channel-catalog: the items leave out the Learn more links, the "Create more storefronts with paid plan" block with "Upgrade plan", and "View more storefront platforms" | stands, incomplete | All three are at ARIA:32-160, 61-67 and 86-87. It also leaves out the banner, "Channels" and "Add new channel" (ARIA:1-4), and the store the catalog is shown to |
| Items against source, contracting-entities: not listed | missed | TERMS's grid has two more rows (Feedonomics, Makeswift), and the definitions the rows' words need |
| Problems: "The supports rules don't cover a catalog card ..." | partly settled | B-extent settles it by who is named doing the work. Whether the catalog is "something the platform provides" is M2 |
| Problems: `show --candidates` drops a word's first letter | fixed | Fixed at `ff50bbee` ("whole words only"). The current leads for entries 1 to 24 show none of those fragments |
| New things | none in my part | — |

## Where the model's cells differ from the held evidence (found on the way)

- **CM-CHN-004, CM-MKT-010 and CM-SFR-006** each read that no held statement says Feedonomics Holdings or Makeswift is of BigCommerce's group. TERMS's preamble says so of Feedonomics Holdings, LLC, and its Contracting Entity clause makes Makeswift, Inc. a Commerce entity. For CM-MKT-010 this changes the count (`own-service`).
- **CM-APP-011's BigCommerce cell:** "No statement shows Extensions in a category of their own in the App Marketplace, or says what they are". TERMS says what they are: services developed by third parties. The cell's own `own-service`, from BC-S-0428 and BC-S-0432, rests on the same homonym (M1).
- **CM-CHN-004's note:** "no held statement puts listings or feeds under sales channels on either platform". The note speaks of the anchor platforms. BigCommerce's Channel Manager puts its five feed channels under "Add new channel" (ARIA:1-58), a grouping for the note (B-extent, `parent`).
- **CM-CHN-007's note:** "no statement of BC-C-039 ties a storefront to a place". The Storefronts block reads "enable multi-geo selling with Multi-storefront capabilities" (ARIA:64).
- **CM-ACC-002's reading:** the Feedonomics and Makeswift rows "are inventory entries no statement covers (BC-I-0547, BC-I-0548)". BC-S-0366 and BC-S-0285 are statements of the same rows, cited in CM-CHN-004 and CM-SFR-006.

## Fixes to H-held.md, and the method rulings

Each fix is in words the coordinator can paste, with whether it stays within B-extent.md and the checker test that would catch the miss.

- **F1, rule 4, `own-service`** (lines 2 to 9, 14 to 21). Replace the bullet with:

  > `own-service`: where the entry names the platform's company, or a company that a held statement names as of its group, as the maker or provider of a separate product, app, extension or service. The statement naming the group may be in the entry, in another source of your batch (a terms page's parties or contracting entities), or the cell's own maker evidence: cite it in `reading`. A named company that no held statement places in or out of the group is not a third party for that reason: place the line by what the entry shows, and note the missing maker statement as a gap. A brand in a product's name, a field's value such as `type: salla`, and a capture's label never name a maker.

  - **B-extent:** within it. Its own-service clause covers it, and so does "Maker evidence is a statement naming the company".
  - **Checker test:** a NOTE for each line whose `filler`, or whose `extension-point` or `outside`, names a company that the platform's CM-ACC-002 cell lists in its terms. For BigCommerce those are Feedonomics Holdings, LLC and Makeswift, Inc. It would catch all 16 lines.
- **F2, rule 5, `filler`** (lines 14 to 21). Replace the bullet with:

  > `filler`: a third party or a law the entry's own words name as doing it or setting its terms. A party known only from the source (a link, a sibling card) goes in `reading`, never in `filler`, and a company of the platform's group is never a filler.

  - **B-extent:** within it.
  - **Checker test:** each filler's name, before any parenthesis and without a leading "the law of", is in the text of each of its entries, as the terms test checks terms. It would catch all 8 lines.
- **F3, rule 1, the source** (lines 29 to 37). Add:

  > A structure's source is the file its `meta.json` names under `source` (`held_as`, or `url` with `held_in`, or `answer`). Where the `source.*` file beside `items.jsonl` is a segment of that page, read the page around it where the segment's words need it (a definition, the clause it sits under), compare its rows with the page's, and say so in your notes.

  - **B-extent:** within it.
  - **Checker test:** none in `check`. A build-side test would compare a segment's last row with the page's grid.
- **F4, rule 5, `scope`** (line 11). Add:

  > Where your reading rests on the source's words for a plan, a country or a store (a region's "with paid plan", the store a catalog is shown to), put it in `scope`, in the source's words, and name the source in `reading`.

  - **B-extent:** within it, as a reading of "a statement's scope stays its own".
  - **Checker test:** none.
- **F5, rule 2, a second thing** (lines 29 to 37). Add:

  > An entry that states a second thing no capability holds, beside the one it is placed on, takes a `new` line for that thing too.

  - **B-extent:** within it.
  - **Checker test:** none.
- **F6, rule 4, catalog cards** (lines 2 to 27). Add:

  > A card of the platform's own catalog of channels or integrations (BigCommerce's Channel Manager) takes its supports from who it names as doing the work. No one, or the venue only (a marketplace, an ad platform): `core`, with the maker gap noted. A third party: `extension-point`, the catalog being what the platform provides. A company of the platform's group (F1): `own-service`. The venue is the slot filler.

  - **B-extent:** the `extension-point` clause is the method ruling M2; the rest is within it.
  - **Checker test:** none.
- **F7, rule 2, homonyms** (lines 29 to 37). Add:

  > Before you place a term on a capability that uses the same word, read the term's definition where the entry's source holds one. A word that names another thing on another platform is a homonym (B-extent, Names): say so in `reading` and in your notes.

  - **B-extent:** within it.
  - **Checker test:** none. `check` could print each line's capability name beside its `own-service` NOTE.
- **A build fix, not H-held's.** Label each channel-catalog entry with the store it was shown to (`meta.json`'s `source.store`), since the list follows the store's country and currency (REGISTER). Rule 5 then gives the fillers a market.

**Method rulings for the coordinator** (B-extent doesn't settle them):
- **M1:** whether CM-APP-011, a capability named for its maker ("Apps made by the platform's company"), holds BigCommerce's Extensions, which a third party develops and Commerce implements and provides. If it doesn't, CM-APP-011's own BigCommerce cell loses the `own-service` it rests on BC-S-0428 and BC-S-0432.
- **M2:** whether the platform's own catalog of channels is "something the platform provides" for `extension-point`.
- **M3:** whether maker evidence held outside the entry counts for the entry's line. I read B-extent as yes, and the verdicts follow that reading. If no, see the fallback in "The entries that name a company".

## Recurring misses, and the checker

| Recurring miss | Lines | A test in `held_entries.py check` that would catch it |
| --- | --- | --- |
| A company of the platform's group read as a third party: `extension-point` and filler | 2 to 9, 14 to 21 (32 rows) | F1's test: a filler, `extension-point` or `outside` naming a company in the platform's CM-ACC-002 terms |
| A filler the entry's text doesn't name | 14 to 21 (8 rows) | F2's test: the filler's name in the entry's text, like the terms test |
| A term joined on a homonym (Extensions) | 29 to 37 (5 rows) | none |
| A second thing an entry states, left unplaced (Professional Services) | 29 to 37 (5 rows) | none |

## The leads

`show --candidates` at HEAD is the version after `99d429ad`. The right capability is among the leads for:
- **channel-catalog: 5 of 26 lines.**
  - Leads hold the right capability: lines 12 (CM-SFR-011), 23 (CM-POS-001) and 24 to 26 (CM-CHN-003).
  - The 16 Feedonomics lines lead to CM-CAT-001, CM-API-003, CM-CHN-001, CM-AIA-005 and CM-AIA-003; never to CM-CHN-004 or CM-MKT-010.
  - The storefront lines 10, 11 and 13, Buy Buttons (22) and impact.com (27) get no right lead.
  - CM-AIA-005, the subject of lines 2 and 14's "can't tell", is entries 1 and 9's first lead.
- **contracting-entities: 10 of 10.** CM-ACC-002 and CM-APP-011 are each entry's first two leads, so the leads carried the homonym too.

In the TSV, `in_leads` answers for the line's own capability. For a "can't tell" or "missing line" row it answers for the capability the row names, and `-` for a `new` one.
