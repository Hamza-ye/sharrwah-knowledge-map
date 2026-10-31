# Inspection of the held pass's rewritten brief (30 October 2026)

**What this is:** the inspection, before the other 68 batches run, of `studies/class-model/briefs/H-held.md` at `657cd861`, rewritten after the dry run (BC-1, ZD-1), its review (`held/review-H.md`) and the coordinator's rulings (`held/review-H-rulings.md`). `PLAN.md`, section 3: "Before a brief runs, a separate agent reads it for anything that presupposes the answer" (Fagan 1976). The inspector wrote none of the files read and changed none but this one.
- **Read:**
  - the brief, against its previous version (`dc1e6414`, which the dry run followed) and that version's inspection (`inspection-H.md`);
  - `B-extent.md`, "Cells and evidence" and "Conventions from the dry run";
  - the review's sections 4 to 7, and the rulings;
  - the checker (`method/held_entries.py`: `cmd_check`, `show --candidates`), and `method/held_amend.py` with `class_slice.py`'s `held_items`, which carry placements into the model;
  - `held/batches.tsv`, `held/selection.tsv`, and the entries of the kinds the dry run didn't hold, with their sources.
- **Pinned:**
  - every line number is at `657cd861`, the head when this ran. `B-extent.md` is unchanged since `04aefe93`;
  - the evidence was read at observed-sh `19a5f6435`, observed-sa `b0bd0b16` and other-product-class `0d79b79`, through their guides first, and the WooCommerce release at `/home/user/woocommerce-release/11.2.1/woocommerce` (cited `woocommerce-11.2.1:<path>`).
- **Tests that write** ran on a copy of `studies/class-model/` in the session's scratchpad, with `CLASS_MODEL_DIR` set. BC-1's and ZD-1's placement files were removed from the copy. The inspector didn't read them, nor the calibration's batches (BC-CH, BC-CX, ZD-CH, ZD-CX).

Severity, as in `inspection-H.md`:
- **must fix:** an agent following the brief would write wrong placements, or the entries lose evidence;
- **should fix:** the output would be less consistent, harder to check, or more expensive than it needs to be;
- **note:** for the record.

Every claim below that isn't a quoted text, a count or a command's output is a reading, the inspector's, whether or not its sentence says so again. No claim rests on an assumption.

**In short:** 8 must fix, 15 should fix, 12 notes.
- **Two rules of the brief undo others:**
  - "How to work" limits the lookups that rule 2 requires, and drops the one FX-3 added. These are the lookups whose absence made the dry run's care misses (MF-1);
  - "B-extent.md governs" lets an agent overturn the rulings the rewrite applies, since none is marked as one (MF-2).
- **Kinds the dry run didn't hold, which the brief decides wrongly or leaves open:**
  - flags in four more forms, and the early-access case the join left open (MF-3);
  - WooCommerce's own "Built by WooCommerce" maker statement, which the field rule discards (MF-4);
  - access scopes and webhook topics, against B-extent's API convention (MF-6);
  - a marked feature's `supports`, M-8, and the venue as filler, all left out (MF-7).
- **What the scope rule needs, but the entries or the brief's sources don't give:**
  - WooCommerce's countries and Zid's plans, lost in the nested renderings (MF-5);
  - Salla's plan marks, held only in its page's HTML (MF-8).

---

## Must fix

**MF-1. "How to work" limits the lookups rule 2 requires, and drops FX-3's.**
- *Found:*
  - **Rule 2 asks for three lookups before a line:**
    - line 48: "Before you place a section, a route or a setting, search the model for its own place ... and its address";
    - line 49: "Read the placed capability's note";
    - line 50: "Every thing the entry names takes a line, on its own capability".
  - **Line 105 allows a lookup only** "where the entry's thing is unclear from its text and sources, or where its placement would change a cell: a cell that holds nothing, a new thing, or a `supports` the cell doesn't hold yet. The leads print each cell's state. Where the entry's words plainly name a lead's thing and that cell already holds the same placement, place it from its text."
  - **The two read two ways on the misses the review found effort couldn't avoid at `high`** (`review-H.md`, section 7, kind 2's misses):
    - "a capability, or `new`, where a cell already holds the place or the thing: BC-1 157, 161, 168";
    - "a second capability the words name, left without its line", on 16 lines;
    - by line 105, an entry whose words plainly name a lead with the same placement is placed from its text. Its place isn't searched, its second thing isn't looked up, and its capability's note isn't read. The Extensions homonym (M-2) was of this kind: "Extension" plainly named CM-APP-011, whose cell held `own-service`.
  - **FX-3's instruction for this isn't in the brief:** "Before you write one line, read the entry's leads and the cells of the capabilities its words name: where a cell's reading cites the same page, place or term, the entry is that capability's too" (`review-H.md`, line 336). `grep -c "cells of the capabilities its words name"` on the brief gives 0.
  - **Line 105's list leaves out `scope`, `filler` and `quality`.** Rules 1 and 5 (lines 37, 39 and 78) need the source read for them: a table's heading, a plan card, a country's line, a listing condition. All 28 missing-scope rows of the dry run were the brief's, and fillers are among its important details (`review-H.md`, sections 1 and 3).
  - **"The leads print each cell's state" holds only for the leads, three at most** (`held_entries.py`, line 678, `most_common(3)`). Over the 14,580 entries of the 68 batches:
    - 3,297 have no lead;
    - on SA-4, SA-6 and SA-7, the first lead is CM-ACC-001 "by merchant" on 130 of 151, 123 of 153 and 132 of 156 entries;
    - on ZD-5 and ZD-6, it is CM-ACC-008 "by available in" on 193 of 390 and 173 of 243 (SF-10).

    So a second thing's cell is mostly not printed. Line 105's condition, that the placement "would change a cell", can't be known without the lookup it forbids.
- *Fix:*
  - **Append to line 50:**
    > Before you write an entry's lines, find the capability of each thing its words name: from its leads, or with `class_slice.py caps --terms` for a thing no lead names. Read each one's cell where the leads don't print it. Where a cell's reading cites the same page, place or term, the entry is that capability's too.
  - **Replace line 105 with:**
    > - **Look things up for every thing an entry names.** Rule 2's lookups always run:
    >   - the search for a section's, a route's or a setting's own place, where its own identifier (a route id, a path, a key) gave no lead;
    >   - the capability's note, before you place on it;
    >   - the capability and the cell of every thing the entry's words name.
    >
    >   Rule 1's reading always runs where the entry's text leaves a column open: the heading, plan card, country line or listing condition that gives its `scope`, `filler` or `quality`.
    >
    >   Skip a lookup only where all of these hold:
    >   - a lead names the entry's thing by the entry's own identifier;
    >   - its cell already holds the same placement;
    >   - its note names no homonym;
    >   - the entry's text states its scope, filler and quality.
    >
    >   About a quarter of the entries have no lead. A lead whose `by` is only a field's name, or a word every entry of the structure holds, is no lead.

**MF-2. "B-extent.md governs" lets an agent undo the rulings the rewrite applies.**
- *Found:*
  - **Line 29:** "Where this brief and B-extent.md read differently, B-extent.md governs: say so in your notes."
  - **The rulings are readings "where B-extent.md doesn't settle a case"** (`review-H-rulings.md`, line 3). Three of them read differently from B-extent's general clauses, which an agent can set against them:
    - M-4 (line 66: a list the platform calls its integrations is `core`) against B-extent's `extension-point`, "a provider interface" (line 116);
    - M-10 (line 72: a page at an app's address, with no maker or gate stated, is `shows`) against B-extent's `core`, "its own admin section, setting, route" (line 114);
    - S7 as the brief widens it (line 74: "A partner's or an app's permission or access is `shows`") against B-extent's S7, which is only "A permission listed for staff and for partners" (line 142), and against its API convention (line 140; MF-6).
  - **No rule of the brief is marked as a ruling,** and the reading list (lines 17 to 29) doesn't name `review-H-rulings.md`.
  - **The join used the review brief's same clause to settle D1 for B-extent's reading** ("the review brief makes B-extent govern", `review-H.md`, section 4, D1). An agent on the other batches can do the same against a ruling.
- *Fix:*
  - **Replace line 29's last sentence with:**
    > The rules marked (M-n) or (ruling) are the coordinator's, on cases B-extent.md leaves open (`held/review-H-rulings.md`), each listed for the founder's veto: follow them. Where any other rule of this brief reads differently from B-extent.md, B-extent.md governs: say so in your notes.
  - **Mark each ruling where it stands:**
    - (M-12) at line 40;
    - (M-6) at line 50;
    - (M-13) at line 62;
    - (M-4) at line 66;
    - (M-1) at line 67;
    - (M-3, M-7) at line 69;
    - (M-10; M-3) at line 72;
    - (M-9) at line 73;
    - (ruling: S7 widened, `inspection-H.md`, B-1) at line 74;
    - (M-11) at line 78;
    - (M-5) at line 94;
    - and the rulings MF-3, MF-4 and MF-6 add.

**MF-3. The flag rule covers two forms. The other batches hold four more, and the case the join left open.**
- *Found:*
  - **Line 75:** "A flag stated as not released (`released: false`, `is_experimental: true`) is `shows`. A page the platform lists with a badge (`new`, `beta`) is offered to the store: `core`, with the badge in `reading`."
  - **The forms the other batches hold:**

    | Form | Where | Entries | Example | What line 75 says |
    | --- | --- | --- | --- | --- |
    | `released` with `enabled` | Salla `dashboard-features` (SA-8) | 241 | 23 entries are `enabled: true; released: false`; 6 are `enabled: false; released: true` | `released` decides; `enabled` isn't named |
    | `is_experimental` with `enabled_by_default` | WooCommerce `release-features` (WC-2) | 25 | 12 experimental; 6 not experimental and off by default | the same |
    | a store's flag stated only by its value | Zid `store-feature-flags` (ZD-4) | 73: 58 `false`, 15 `true` | ZD-E-36d3e78f "key: is_reverse_order_enabled; value: false"; ZD-E-5360f48c "key: is_mazeed_pilot; value: false" | nothing: neither "released" nor a badge |
    | a limited early release, in a help page's note | Shopify `help-notes`, class `note note-beta` (SH-15 to SH-17) | 69 | SH-E-8de52e75 "Early access Sidekick Pulse is in early access and is available only to certain merchants."; SH-E-2f5b7ba4 "Shopify Capital flex accounts are in early access, and are available only to certain Shopify merchants in the United States who use Shopify Capital." | the release-marker clause (line 76) is for titles only; the badge clause gives `core` |
    | a preview | Shopify `dev-store-feature-previews` (SH-14) | 6 | its source step, `raw/runs/20261007T010009Z-journey-partner-dashboard/steps/065.text.txt`, line 21: "Preview changes to Shopify and APIs before they're generally available" | nothing |
    | a route gated by a beta | Shopify `admin-router` (SH-4 to SH-10) | 37 | SH-E-b16b7f2a `eligibilityMatch: [eligibility: {betas: [29ece4dc]}]` | the gate is the `scope` (line 78), but is it released? |

  - **For the routes gated by a beta:**
    - the evidence map (line 84): "Shopify's beta flags are held under hashed names, so nothing can be placed from them";
    - `structures/shopify/admin-betas/<store>/items.jsonl` gives each hash's `enabled` value per held store. 29ece4dc is `{"position": 29, "name": "29ece4dc", "enabled": false}` in both stores;
    - the brief names neither.
  - **The join left the early-access case open:** "A method ruling would remain only for a badged page the platform states can't be used. The dry run holds none." (`review-H.md`, line 232). Section 6 (line 532): "Flags: none held ... The flag clause is untested".
  - **A reading: line 75 as written splits agents two ways on each case:**
    - "in early access ... available only to certain merchants" read as a badge (`core`) or as not released (`shows`);
    - Zid's `value: false` read as off for that store (`shows`) or as a released flag (`core`).

    Either choice decides whether a cell gains `core`.
- *Fix:* replace line 75 with this ruling, for the founder's veto:
  > - **Flags, badges and release states (ruling):**
  >   - a flag the source states isn't released (`released: false`, `is_experimental: true`) is `shows`, whatever its value for the store;
  >   - a released flag (`released: true`, `is_experimental: false`) supports `core`, with its plans as its `scope`, or the store's label where it names no plan. Its value for that store (`enabled`, `enabled_by_default`) goes in `reading`;
  >   - a store's flag stated only by its value (Zid's `feature_flags`, `key: …; value: true|false`):
  >     - `true` supports `core`, the store as its `scope`;
  >     - `false` supports `shows`, with the value in `reading`;
  >     - a name that says pilot, preview or test (`is_mazeed_pilot`) supports `shows` while its value is `false`;
  >   - what the platform states is in early access, a preview or a beta, available only to some merchants or stores, supports `shows`, its words in `reading`:
  >     - Shopify's help notes: "is in early access, and is available only to certain merchants";
  >     - a dev store's feature previews: "before they're generally available";
  >   - a route gated only by Shopify's hashed `betas`: read `structures/shopify/admin-betas/<store>/items.jsonl`. A beta `enabled: true` in a held store makes the route `core`, that store its `scope`. `false` in every held store makes it `shows`;
  >   - a page or route the platform lists with a badge (`new`, `beta`), with no such limit stated, is `core`, the badge in `reading` (D1);
  >   - a flag named for a third party is the capability's evidence, never a slot filler.

**MF-4. "A field's value never names a maker" discards WooCommerce's own maker statement.**
- *Found:*
  - **Line 67:** "A brand in a product's name, a field's value such as `type: salla` or `type: platform`, and a capture's label never name a maker".
  - **WC-1's `core-profiler-free-extensions` entries carry `is_built_by_wc`:** `true` on 15 entries, `false` on 9.
    - `true`: WooPayments, WooCommerce Shipping, WooCommerce Tax, Google for WooCommerce, Pinterest for WooCommerce, Snapchat Ads, Reddit Ads, ShipStation and MailPoet (WC-E-c5b3bb15, WC-E-b840b778, WC-E-8bc33809 and others);
    - `false`: Jetpack, Klaviyo, Mailchimp, PayPal Payments for WooCommerce, "Meta Ads & Pixel by Kliken" and "Print on Demand with Printful" (WC-E-5954b83f, WC-E-2d8663f2, WC-E-d1b71f8e and others).
  - **The field is WooCommerce's statement, not the capture's:**
    - the release declares it: `woocommerce-11.2.1:src/Internal/Admin/RemoteFreeExtensions/DefaultFreeExtensions.php`, line 123, `'is_built_by_wc'  => true,` for Google for WooCommerce, and line 149, `'is_built_by_wc' => false,` for Facebook for WooCommerce;
    - its admin shows it to the merchant as a pill reading "Built by WooCommerce": `woocommerce-11.2.1:assets/client/admin/chunks/3799.js`, line 1, `isBuiltByWC:r` … `r&&(0,k.jsx)(x.Pill,{children:(0,a.__)("Built by WooCommerce","woocommerce")})`.
  - **B-extent's `own-service` asks only that "the statement names the platform's company ... as the maker or provider"** (line 115), and says nothing of fields. Line 67's blanket rule came from `inspection-H.md`'s S-7, about Salla's `type: salla`, whose meaning no source states.
  - **A reading:**
    - the rule decides against a statement whose meaning the platform's own code states;
    - it would make WooPayments, WooCommerce Shipping and Google for WooCommerce `core` or `extension-point` by what they show, with a "missing maker" gap the evidence fills.

    The brand NOTE (line 865) misses WooPayments and MailPoet, whose names have no space after the brand.
- *Fix:* replace, in line 67, "A brand in a product's name, a field's value such as `type: salla` or `type: platform`, and a capture's label never name a maker" with:
  > A brand in a product's name, a field's value whose meaning the source doesn't state (Salla's `type: salla`, `type: platform`), and a capture's label never name a maker. A field that the platform's own code shows as a maker statement does, as a reading (ruling): WooCommerce's `is_built_by_wc: true`, which its admin shows as "Built by WooCommerce" (`woocommerce-11.2.1:assets/client/admin/chunks/3799.js`; `src/Internal/Admin/RemoteFreeExtensions/DefaultFreeExtensions.php`, line 123), names WooCommerce as the maker: `own-service`, citing both in `reading`. `is_built_by_wc: false` names no maker.

**MF-5. WooCommerce's lists by country, and Zid's plan advantages, lose their country and their plan.**
- *Found:*
  - **How the build carries an ancestor:** `flatten` (line 135) carries an ancestor into `within` only through `name_of` (line 124), which reads `name`, `title`, `label`, `key`, `slug`, `handle`, `id`, `path` and `url`. Items that render the same are one entry, at the first one's locator.
  - **WooCommerce `payments-providers` (WC-2):**
    - each line of `items.jsonl` is one location, its `location` key: AE, EG, GB, JP, OM, SA, US, YE;
    - its flattened providers, offline methods and suggestions carry no location;
    - 9 of its 31 entries stand for elements of several locations. `id: woocommerce_payments` is listed in all 8. `id: _wc_pes_paypal_full_stack` is listed in AE, EG, GB, JP, OM and US, not in SA or YE;
    - their locator is line 1, which is AE (WC-E-a65499e0: "line 1 pointer /providers/0").
  - **WooCommerce `core-profiler-free-extensions` (WC-1):** each line is one `store_country` (US:CA, GB, AE, SA, OM, YE, EG). 25 of its 29 entries stand for elements of several countries.
  - **Zid `plans-offered` (ZD-4):**
    - a package names itself in `display_name`, a variant in `duration_code`, and no entry carries `within` (0 of 55);
    - so an advantage such as ZD-E-5892caa9 ("Connect your store with external systems (via API)") doesn't say its package;
    - 16 of the 55 entries stand for elements of 35 different packages or variants.
  - **What this loses:**
    - line 59 says: "A thing the platform offers for a country or location, such as a payment provider, a free extension or a tax service, is placed on its capability, with that country as its scope";
    - the entry doesn't state the country, and its locator names one;
    - a reading: which providers WooCommerce lists for Saudi Arabia and Yemen, and which plan includes each of Zid's advantages, reach the model under one country or one plan, or under none.
- *Fix:*
  - **In the build** (`method/held_entries.py`, `name_of`, line 124): read also `display_name`, `duration_code`, `location` and `store_country`, so that `within` carries the package, the variant and the country. Then rebuild WooCommerce and Zid, and cut WC-1, WC-2 and ZD-4 again. No placement names their entries yet, and ZD-1's structures don't use `nested:`.
  - **Until then, add to the brief's known cases (line 41):**
    > - WooCommerce's `payments-providers` and `core-profiler-free-extensions`: each line of `items.jsonl` is one country (`location`, `store_country`), and the rendering leaves it out. An entry stands for the same element in every country that lists it, at the first one's line. Find its `id` or `key` in every line, and write each country that lists it as its `scope`. A country that leaves it out goes in `reading`.
    > - Zid's `plans-offered`: an advantage's package (`display_name`) and variant (`duration_code`) are its ancestors on its pointer, and the rendering leaves them out. An advantage several packages share is one entry. Find it in each package, and write each package as its `scope`.

**MF-6. B-extent's API convention isn't restated, and the S7 bullet reads against it for access scopes.**
- *Found:*
  - **B-extent (line 140):** "The platform's own API (its folder, object, scope, webhook topic, or a mutation's requirement) for its own feature is `core`, a guide addressed to app developers included. It is `extension-point` where the API's statements say apps or partners do the work."
  - **The brief restates it only in part:**
    - its `core` keeps "its own API for its own feature" (line 66);
    - its `extension-point` reads "an API whose statements say apps or partners use it" (line 68), where B-extent's reads "use it to do the work" (line 116);
    - it never says that a scope, a webhook topic or a guide to app developers is `core`.
  - **Line 74:** "A partner's or an app's permission or access is `shows` (the dry run's S7)".
  - **SH-12 holds 200 entries of `dev-dashboard-scopes`,** the Dev Dashboard's scope picker: scope groups ("Analytics", "Cash Tracking", "Audit Events") and each one's API ("Admin API; parent: 39"). Its selection row is `boundary`, with no S7 note.
  - **The model places the same scopes `core` on their feature:** CM-POS-003's Shopify cell cites `SH-C-087/boundary/SH-S-5940` as "own access scope read_cash_tracking", `core` (`land_points.py cell CM-POS-003 shopify`).
  - **`inspection-H.md`'s B-1 fix had the sentence** "An API's own access scope is `core` for its own feature (C1)" (line 351). The coordinator took B-1, but the sentence isn't in the brief, at `dc1e6414` or now (`grep -c "access scope"`: 0).
  - **The other batches of B-extent's API kinds:**
    - webhook events: SA-12 (`dashboard-webhook-events`, 63; `docs-event-lists`, 169) and WC-3 (`release-webhook-topics`, 16);
    - REST controllers: WC-2 (52);
    - the docs' API groups: SA-13.

    A docs page for app developers says that apps subscribe to the webhooks: `extension-point` by line 68, `core` by B-extent.
- *Fix:*
  - **After line 68, add:**
    > - **The platform's own API** (its folder, object, access scope, webhook topic, REST controller, or a mutation's requirement) for its own feature is `core`, on that feature's capability, a guide addressed to app developers included. It is `extension-point` only where the API's statements say apps or partners do the work (B-extent, "Conventions from the dry run"). A scope or scope group of the API's own list (Shopify's `dev-dashboard-scopes`) is `core`, as the model places the same scopes (CM-POS-003: "own access scope read_cash_tracking").
  - **In line 68,** replace "or an API whose statements say apps or partners use it" with "or an API whose statements say apps or partners use it to do the work".
  - **In line 74,** replace "A partner's or an app's permission or access is `shows`" with "What a partner or an app asks of a merchant or of the platform (a collaborator request, a Partner API permission set, an app's install consent) is `shows`".

**MF-7. A marked feature's `supports`, M-8, and the venue as filler are left out.**
- *Found:*
  - **The rulings:**
    - D4 (line 20): "a provider's feature mark (Recurring Payments ✔) is a statement of the marked feature's capability: a line there, `shows` unless the row says who does it, the provider its filler";
    - M-8 (line 13): "A third party's own feature through the platform's interface (Avalara's return filing) is `extension-point` on the capability whose thing it is (CM-TAX-006), beside the provider's line";
    - M-3 (line 8): "The venue is the filler."
  - **The brief:**
    - the marked feature takes a line "with its own `supports`" (lines 50 and 81), and the brief never says which;
    - M-8 isn't there (`grep -c "beside the provider"`: 0);
    - line 72 keeps "names no one, or only the venue, is `core`" but not that the venue is the filler, and line 80's filler is only "a third party or a law the entry's own words name as doing it".
  - **The other batches hold these:**
    - Salla's `shipping-carriers` (SA-32): 25 carriers, each with `supports_salla_awb`, `supports_ratings` and its `shipping_types`;
    - WooCommerce's suggestions (WC-2): "Accept 60+ local payment methods including Apple Pay and Google Pay";
    - venues in WooCommerce's free extensions (WC-1): Google for WooCommerce, Pinterest for WooCommerce, Snapchat Ads, Reddit Ads.

    Supports and fillers are among the review's important details (section 3).
- *Fix:*
  - **In line 50, after "(a ✔ under Recurring Payments)", add:**
    > The marked feature's line is `shows` unless the row says who does it, with the provider as its `filler` (D4). A third party's own feature that the platform's listing names is `extension-point` on that feature's capability, beside the provider's line (M-8): Avalara's return filing, or a WooCommerce suggestion's "Accept 60+ local payment methods".
  - **In line 72, after "with the missing maker noted as a gap", add:** "The venue it names is its `filler` (M-3): a marketplace or an ad platform, such as Google in "Google for WooCommerce"."
  - **In line 80, after "doing it or setting its terms", add:** "A catalog card's venue is its filler (M-3)."

**MF-8. Salla's published plans: the entries hold no plan marks, and the brief gives no route to the page that holds them.**
- *Found:*
  - **The structure:** `com-plans` (SA-2, 319 entries) is read by the `text:` rule, one entry per line of `text.txt`, "the page's text nodes in document order, one per line" (its `meta.json`). Its `source` is an archive record: `warc` `raw/runs/20261008T133928Z-com-plans/fetch.warc.gz`, `uri` `https://salla.com/en-sa/plans`, and a `record_id`. It has no `held_as`, no `answer` and no `source.*` file.
  - **The page's "Key features" rows hold each plan's mark in the HTML only.** `python3 -I method/warc_text.py /home/user/observed-sa raw/runs/20261008T133928Z-com-plans/fetch.warc.gz@555939` (the offset `held_index.py` gives for the address) prints the page. Its rows:

    | Row | Marks |
    | --- | --- |
    | "Unlimited products", "Unlimited orders", "Lower shipping costs with Salla Shipping Labels" | three `data-framer-name="Included (Check)"` |
    | "All product types supported", "Online & flexible payments", "Salla Ads", "Sell on Mahally" | one `"Not Included (Cross)"`, then two checks |
    | "Built-in SEO", "Built-in VAT support with ZATCA integration" | two crosses, then one check |

    The desktop layout holds 19 checks and 8 crosses in all. `text.txt` holds the labels alone, at en-sa lines 101 to 109 and 211 to 219.
  - **A `text:` entry stands for every line holding the same text.** 143 of en-sa's lines repeat: "Unlimited products" is at lines 101 and 211, and its entry SA-E-ecf3dba6 is located at en-ae line 93.
  - **Rule 1's sources (line 36) are `held_as`, `answer` and `source.*`;** none of them is this record. Line 105 allows no lookup for a scope.
  - **A reading:**
    - an agent writes "Built-in SEO" with no plan, where the page includes it on one plan only: the third column, Pro, by the cards' order Basic, Plus, Pro;
    - `inspection-H.md`'s E-5, where BigCommerce's plan rows would have been read on the wrong plans, was a must fix for the same reason.

    `com-specialplan` (SA-3), from the same extractor, has 6 checks and no cross on en-sa.
- *Fix:* add to the brief's known cases (line 41):
  > - Salla's `com-plans` holds the plans page's text nodes only. Its "Key features" rows mark each plan in the page's HTML, not in `text.txt`: `data-framer-name="Included (Check)"` or `"Not Included (Cross)"`, one per plan, in the cards' order. The page is the archive record its `meta.json` names: `python3 -I method/held_index.py <uri>` gives its offset, and `python3 -I method/warc_text.py /home/user/observed-sa <warc>@<offset>` prints it. Write the plans each row is included in as its `scope`. A line the page repeats is one entry: grep `text.txt` for each place it stands.

---

## Should fix

**SF-1. Rule 1's sources name the forms that 7 of the 145 selected structures use.**
- *Found:*
  - Line 36 names "the file its structure's `meta.json` names under `source` (`held_as` or `answer`)" and "the `source.*` file beside `items.jsonl`".
  - By the 145 `yes` rows' `meta.json` files:
    - 7 name `held_as` or `answer`;
    - 76 name a run's step (`run_id` with `step` or `steps`, or `html_file`), and 11 a run without a step;
    - 29 name an archive record (`warc` with `record_id` and `uri`): among them Shopify's `admin-router` and `help-notes`, Salla's `com-plans` and Zid's `dashboard-route-manifest`;
    - 1 names `held_in`;
    - 6 name their source in yet other forms: `warc_records`, `warcs`, `bodies`, `run_files`, `runs` (among them Salla's `settings-center`, ten batches);
    - 13 have no `meta.json` at all, the structures built by a rule (`json:`, `rows:`, `release:`, `changes:`);
    - Salla's two app-route manifests have an empty `source`.
  - 32 have neither a `held_as` or `answer` source nor a `source.*` file. FX-1 also named "`url` with `held_in`".
  - The checker's quote search reads only `held_as` and `answer` (line 746). So a quote from an archive page, such as a help page around its note, is printed as "found nowhere held".
- *Fix:* replace the second clause of line 36 with:
  > whatever its structure's `meta.json` names under `source`:
  > - a held file (`held_as`, `file`, `html_file`, `held_in`);
  > - an answer (`answer`);
  > - a run's step (`run_id` with `step` or `steps`: `raw/runs/<run_id>/steps/<NNN>.*`, with its `.text.txt`);
  > - an archive record (`warc`, `record_id`, `uri`): `held_index.py <uri>` gives its offset, and `warc_text.py <repository> <warc>@<offset>` prints it.
  >
  > Also the `source.*` file beside `items.jsonl`, and, for a structure built by a rule, the files its rule names in `selection.tsv`.

**SF-2. Line 39 lets `terms` and `filler` come from the sources, where rule 5 and the checker don't.**
- *Found:*
  - Line 39: "Its `scope`, `terms`, `filler` and `quality` still come from the entry and its sources."
  - Rule 5 contradicts it:
    - line 79: terms are "each found in the entry's text";
    - line 80: "A party known only from a source (a link, a sibling card) goes in `reading`, never in `filler`".
  - The checker follows rule 5. On the scratch copy, a WC-1 line with a term and a filler taken from beyond the entry gave:
    - `PROBLEM placements-WC-1.tsv line 265: term 'payment gateway' is not in the text of each of its entries`;
    - `PROBLEM ... filler 'Stripe' is not named in the text of each of its entries: a party known only from a source goes in reading`.
  - FX-1 and FX-15 read the same two ways (`review-H.md`, lines 321 and 432).
- *Fix:* replace that sentence of line 39 with:
  > What such a file states clarifies the entry. The entry's `terms` and `filler` still come from its own text (rule 5, which the checker tests), and its `scope` and `quality` from its text and its structure's sources.

**SF-3. `quality` reads "a limit or value", and a store's own value has no column.**
- *Found:*
  - **Line 81:** "a limit or value the entry states, as `<what>: <value in its words>`: a maximum, a rate, a fee, a duration, a certification, an uptime, a data location".
  - **The sources it departs from:**
    - B-extent (line 125): "a limit, a certification, an uptime or a data location a platform states";
    - FX-16 (`review-H.md`, line 435): the same, "by plan where the entry gives one". The brief drops "by plan".
  - **The fees, rates and durations it adds are the model's practice:** `merged/qualities.tsv` holds "transaction fees per plan", "checkout rate limit", "days logs are kept, by default". But "value" also takes in a store's own value of a setting. On the scratch copy, `approved directories mode: enabled` (a WooCommerce option's value) passed as a quality, while `autodetect done: yes` was refused as a mark.
  - **`inspection-H.md`'s B-5 fix had "Its value for that store goes in `reading`, if anywhere"** (line 410), which line 59 doesn't hold. It matters for WooCommerce's `options` (237 entries), Shopify's `shop-request-details` (49), Zid's flags (73) and Salla's `enabled` (241).
- *Fix:*
  - **Replace the first clause of line 81 with:**
    > `quality`: a limit, a certification, an uptime or a data location the entry states, or a value of the kind the model's `qualities.tsv` records (a maximum, a rate, a fee, a price, a duration), as `<what>: <value in its words>`, by plan where the entry gives one. A store's own value of a setting or a flag (an option's value, `enabled: true`, `value: false`) is never a quality: it goes in `reading`.
  - **Add to line 59:** "Its value for that store goes in `reading`."
  - **Say in the notes' list** that the brief departs from B-extent's list as the model does.

**SF-4. "A run of entries of one kind ... routes under one section is decided once."**
- *Found:*
  - Line 106 gives "routes under one section" as a run decided "from its first entries".
  - In Shopify's `admin-router` (1,046 entries, SH-4 to SH-10), the 30 sections of ten routes or more lead to a median of 4 distinct first leads: "Orders" 50 routes and 16, "Payments" 52 and 14, "OrganizationSettings" 85 and 11.
  - Rule 3 places each sub-page on its own capability's thing.
  - The dry run's whole-table choices are the precedent: one term and one misquote went down 44 and 22 rows (`review-H.md`, section 2).
- *Fix:* in line 106, replace "(a list of carriers, gateways, permissions or routes under one section)" with:
  > (a list of carriers, gateways or permissions). Routes and settings are placed one by one, since a section's routes are many capabilities' (rule 3)

**SF-5. The brief says a batch holds about 150 entries; `batches.tsv` wasn't cut again.**
- *Found:*
  - Line 102: "Your batch holds about 150 entries. Your context should stay under about 200,000 tokens."
  - The 68 batches to run hold 20 to 390 entries: 30 hold more than 200, and 16 more than 300 (ZD-5 390, SA-15 381, SA-8 378, SH-3 373). The commit's message says "batches of about 150"; `batches.tsv` changed at `657cd861` only in two rows' counts.
  - The dry run's contexts reached 257,452 and 297,153 tokens at 148 and 153 entries. The review: "Keep kind 2's batches within the dry run's size" (`review-H.md`, line 574).
  - A reading: on a 390-entry batch, the brief's cap can be kept only by skipping lookups (MF-1).
- *Fix:*
  1. Remove the files and rows of the 68 batches.
  2. Cut them again with `python3 -I method/held_entries.py batches --size 150`. Its rule makes batches of about 75 to 195 entries, ending where a structure or section ends.
  3. Set each new batch's effort by its kind of entry (`review-H.md`, section 7).

**SF-6. Reading every `meta.json` at the start costs up to about 900 kB a batch.**
- *Found:*
  - Line 23 says "and the rest of a structure's `meta.json`", and line 103 "Read once, at the start: ... your structures' `meta.json`".
  - SH-15, SH-16 and SH-17 each name `help-notes`, whose two `meta.json` files are 453 kB each: about 900 kB of archive records. SA-13's `meta.json` files come to 209 kB.
  - The previous version said "Read the rest of a `meta.json` only where an entry needs it" (`dc1e6414`, line 21, after `inspection-H.md`'s B-9).
- *Fix:*
  - **Line 23:** "`show --meta` prints each structure's descriptive keys. Read any other key of a `meta.json` only where an entry needs it, by that key."
  - **Line 103:** "your structures' descriptive keys (`show --meta`)".

**SF-7. A route's gate on the user, and the Partners portal's permissions, have no rule.**
- *Found:*
  - **Shopify's `admin-router` gates its entries by:**
    - the store: `features` (71 entries), `entitlements` (31), `betas` (37), `organizationFlags` (12), `organizationFeatures` (9), `regions` (1);
    - the client: `clients` (21);
    - the user: `permissions` (181), `organizationPermissions` (51).

    Line 78 makes a condition the platform sets for a store the entry's `scope`, and says nothing of a gate on the user.
  - **Salla's `permission-gates` (SA-15) has 218 rows of `surface: portal`,** the Partners portal's own users' permissions, e.g. SA-E-6cab53d2 "Services Orders (route services-orders-admin); permissions: manage-services". Line 74 doesn't say whether that is "a partner's ... permission" (`shows`) or a staff permission (`core`). Its selection row carries no S7 note.
- *Fix:*
  - **Add to line 78:**
    > A route's gate on the store (`features`, `entitlements`, `betas`, `organizationFeatures`, `organizationFlags`, `regions`, a plan) is its `scope`, in the source's identifiers. A gate on the user (a staff permission: Shopify's `permissions` and `organizationPermissions`, Zid's page permission) is named in `reading`. It takes a line on CM-STF-002 only where the entry names the permission as its own thing.
  - **The coordinator rules on the Partners portal's own users' permissions** and states the ruling at line 74.

**SF-8. 1,475 entries give their group only as a position.**
- *Found:*
  - Where a structure records nesting by position, the rendering keeps `parent: 39` or `within: 15`, and drops `position` (`SKIP`, line 56). So the number points to an item the agent can't see without opening `items.jsonl`.
  - 1,475 such entries carry no other group name:
    - Shopify: `mobile-app-settings-index` 350, `mobile-app-navigation` 188, `pos-settings` 135, `dev-dashboard-scopes` 101, `pos-app-navigation` 94, `tinker-tools` 88, `dev-nav` 70, `admin-main-nav` 44;
    - Salla: `portal-menu-definitions` 131, `dashboard-main-navigation` 126.
  - Rule 3's containers and rule 2's "parent's thing" need the group. `inspection-H.md`'s E-4 fix was "rendering `parent` as the parent's label or id".
  - Example: in `dev-dashboard-scopes`, "Admin API" with `parent: 39` sits under position 39, "Cash Tracking".
- *Fix:*
  - **In the build:** render a numeric `parent` or `within` as the `name_of` of the item at that `position`, in the same file.
  - **Until then, add to the known cases:**
    > A `parent` or `within` that is a number is the `position` of the item the entry sits under, in the same `items.jsonl`. Read that item: its title is the entry's group, as a table's heading is a row's.

**SF-9. The repositories' derived tables mix the platform's words with the capture's.**
- *Found:*
  - Salla's `plan-gates` (SA-16, 284) and `permission-gates` (SA-15, 330) are rows of `derived/*.tsv`: "What a plan, a permission or a store's state allows, in Salla's words, beside what each store's pages showed" (observed-sa `docs/READING.md`, line 122).
  - Their columns mix the two:
    - Salla's words: "merchant: Available on Plus, Pro, and Special / Upgrade to Plus …", and `edu_allowedPlans: plus, team, special`;
    - the capture's observations: "demo: (not swept)", "held: in /me's permissions: manage-services yes", "public_demo_or_shown: not in the rendered side menu".
  - Shopify's `admin-router-changes` (SH-10, 81) is the repository's diff of two router versions.
  - The brief says nothing of derived tables. `inspection-H.md`'s S-9 had "where a placement rests on one, cite the bytes it names".
- *Fix:* add to the known cases:
  > A row of a repository's derived table (Salla's `plan-gates` and `permission-gates`, Shopify's `admin-router-changes`) joins bytes the repository holds. The columns that quote the platform (`merchant`, `edu_allowedPlans`, `permissions`, `eligibility before` and `after`) are the entry's text. The repository's own columns (`demo`, `held`, `demo_or_admin`, `public_demo_or_shown`) are its observations: never the platform's terms, a scope or a quote. Where a placement rests on a row, cite the step or file it was built from.

**SF-10. Leads come from field names and app prefixes, which also blinds the checker's first-lead NOTE.**
- *Found:*
  - `candidates` matches every platform's cell terms against the whole rendering, field names included (line 670). Only identifiers get a frequency filter (line 650).
  - Measured over the 68 batches:
    - "merchant", from Salla's micro-frontends `ui-merchant-*`, leads with CM-ACC-001 first on 130 of SA-4's 151 entries, 123 of SA-6's 153 and 132 of SA-7's 156;
    - "available in", from Zid's `available_in` field, leads with CM-ACC-008 first on 193 of ZD-5's 390 and 173 of ZD-6's 243;
    - in Shopify's Flow tasks (SH-14, 196 entries), "categories" leads with CM-ANL-002 on 160 entries and "connector" with CM-API-002 on 123. Workflow automation (CM-AUT-001) is a lead on only 15;
    - "data", from the field name `data-node-id`, leads with CM-MKS-009, whose Shopify cell holds nothing, first on 11 entries, 6 of them among the 18 collaborator permissions. So the checker's NOTE prompts a line on it.
  - Where such a lead is first, the NOTE for "a first lead whose cell holds nothing" can't fire for the real one.
- *Fix:*
  - **In `candidate_index` and `candidates`:**
    - match terms against the rendering's values, not its keys;
    - drop a term that more than a fiftieth of the platform's entries hold, as `common` does for identifiers.
  - **Add to the brief's line 15:** "A lead whose `by` is only a field's name, or a word every entry of your structure holds, is no lead."

**SF-11. The brief says the checker notes "each container"; it notes only Zid's.**
- *Found:*
  - Line 128 lists "each container" among the NOTEs.
  - The test (lines 893 to 905) reads only `pageKey`, which only Zid's `dashboard-page-index` carries, and that structure is ZD-1's alone.
  - The other batches' containers nest by `parent`, `within` or `parentId`: Shopify's `admin-main-nav` and `admin-permission-tree`, Salla's `dashboard-main-navigation` and `dashboard-nav`, Zid's route manifest.
- *Fix:*
  - **Extend the test:** a NOTE for an entry whose own id, path or position is another entry's `parent`, `within` or `parentId` in its structure.
  - **Or, in line 128,** write "each container of Zid's page index (`pageKey`)".

**SF-12. Smaller clauses of the rulings and fixes are left out.**
- *Found* (`grep -c` on the brief: "computed" 0, "grouping" 0, "conditional title" 0, "CM-ACC-002" 0):
  - **M-11, a computed listing condition:** "A computed one with no name of its own is named by the module it comes from (`use-is-ngo-store`), marked as a reading" (`review-H-rulings.md`, line 22). The same goes for FX-14's parent route state (`$lang.suspended.$storeId`) and its "Where your reading rests on the source's words for a plan, a country or a store (a region's "with paid plan"), put them in `scope`" (`review-H.md`, line 421).
  - **M-13:** "A section whose title names only a grouping is placed the same way" (line 26).
  - **M-14:** "A conditional title is a statement of its own ...: the platform states the page under each condition, and the condition is its scope" (line 24).
  - **FX-9:**
    - "A named company that no held statement places in or out of the group is not a third party for that reason" (`review-H.md`, line 387);
    - the join's test notes say a batch names a group company that the checker's `GROUP` list (line 717) lacks, so that the coordinator adds it.

    The brief doesn't say where the group's companies are held: CM-ACC-002's cells, from which `GROUP` is drawn.
- *Fix:*
  - **Append to line 78:** "A condition with no name of its own is named by the module it comes from, or by what it is computed from, as a reading (M-11)."
  - **Append to line 62:** "A section whose title names only a grouping is placed the same way (M-13). A title the source gives under a condition is a statement of its own, with that condition as its `scope` (M-14)."
  - **Append to line 67:**
    > The companies the model holds as the platform's group are in its CM-ACC-002 cell (`land_points.py cell CM-ACC-002 <platform>`), and the checker's `GROUP` list holds them. A company a held statement places in the group, which that cell lacks, goes in your notes. A named company that no held statement places in or out of the group is not a third party for that reason: place the line by what the entry shows.

**SF-13. The `out` list and line 59 miss the store's bookkeeping, an account's features and a store's subscriptions.**
- *Found:*
  - **The out list (lines 55 to 57)** names UI strings, one store's or account's data, and market data. The other batches also hold:
    - the software's bookkeeping: about 31 of WooCommerce's 237 `options` by their names, such as `wc_blocks_db_schema_version: 260`, `wc_variation_gallery_migration_completed_at`, `wcpay_styles_cache_version`;
    - a scaffold: Salla's `app: ui-merchant-%7Bapp-name%7D` routes (5);
    - Android layout nodes: N-4.
  - **Line 59 covers "for a store" only.** Salla's `portal-private-settings` (SA-21, 68 entries) is "the features on for a partner account".
  - **Salla's `merchant-subscriptions` (SA-14, 15)** holds one store's subscriptions to add-ons: dates, invoices, status.
- *Fix:*
  - **Add to the out list:**
    > - the software's own bookkeeping: a schema or database version, a migration's done-marker, a cache, a stored state, an install or activation time;
    > - a template or scaffold the code holds for no place (a `{app-name}` placeholder).
  - **In line 59,** "for a store" → "for a store or an account".
  - **Add:** "A store's subscription records are its data. The add-on they name (`type: addon`) is the platform's offer: place it on its capability, with the store as its `scope`."

**SF-14. Two selection reasons presuppose what the entries should decide.**
- *Found:* the brief sends the agent to the selection's reasons (line 24).
  - **`tracking-carriers`:** "the carriers Shopify offers for tracking: a list of what it connects through an interface of its own". The structure is a return form's select options ("type: option; label: 99 Minutos; value: gid://shopify/TrackingCarrier/99minutos"), and no entry states an interface. The model reads the list as `core`, "the platform's value list Tracking carriers (204 options)" (CM-SHP-017, `SH-I-2095`).
  - **`core-profiler-free-extensions`:** "the free features the set-up offers". Its entries are plugins to install, nine of them stated `is_built_by_wc: false`.
- *Fix:* reword the two reasons:
  > `tracking-carriers`: the carriers the return form's tracking field lists
  >
  > `core-profiler-free-extensions`: the free extensions the set-up offers to install, by country, bundle and plugin

**SF-15. `class_slice.py` takes an entry's scope from any placement file, the calibration's included, and one per entry.**
- *Found:*
  - `held_items` reads every `placements-*.tsv` (line 185) and keeps the first non-empty `scope` per entry (line 188).
  - `held_amend.py` skips the batches `batches.tsv` doesn't list, "a calibration's batches" (line 53). `held_items` doesn't.
  - So where BC-1's or ZD-1's line has no scope and a calibration line has one, the calibration's reaches the model. Files are read in name order, BC-1 before BC-CH.
  - The brief gives each line its own `scope` (lines 50 and 78), but the model keeps one per entry, whichever line comes first.
- *Fix:*
  - In `held_items`, skip a placement file whose batch `batches.tsv` doesn't list.
  - Key the scope by entry and capability, or tell agents (line 50) that an entry's lines share its first line's scope.

---

## Notes

**N-1.** Line 74 says S7 covers "Salla's partner access requests. Their selection rows carry this note". No batch holds them: `portal-stores-access-requests-permissions` and `portal-app-scopes` are read already (`registers`: cited 15 of 15 and 24 of 24; the concern map has 210 citations of the first, quoting its nested permissions).

**N-2. The quote NOTE's reach:**
- `run_text` reads Zid's, BigCommerce's and WooCommerce's answers, but not Shopify's or Salla's, and no locale or archive page (lines 759 to 766);
- it compares folded text, not exact text;
- it ignores quotes under 8 characters, and stops a quote at an apostrophe (line 725).

Line 83 asks for a quote "copied exactly ... from ... the file it cites", which the test doesn't check.

**N-3.** The checker prints at most 120 NOTEs (line 925). The per-entry NOTEs are printed last: a first lead holding nothing, an embedded page, a container. On the fixtures, SH-21 gave 36 NOTEs and SH-17 54, so the cap wasn't reached, but a 390-entry batch could reach it.

**N-4.** SH-19's `mobile-app-settings-index` has 60 of 352 entries that render only Android layout (`class: android.widget.LinearLayout`, `parent`, `id`).
- They pass because `says_something` (line 120) counts the item's numeric `index`, which `render` leaves out at the top level (line 103). An example is the item of SH-E-73ca10a5: `{"step": 51, "index": 1, "parent": 0, "class": "android.widget.FrameLayout", "text": null, ...}`.
- Make `says_something` skip the keys `render` skips. Such entries are `out` meanwhile.

**N-5.** "Every thing the entry names" (line 50) should say "names as its own". A route's `metadata.nextRoutes` and `redirect` name other places. Of Shopify's 43 router entries with `nextRoutes`, 13 have a lead that only the `nextRoutes` give.

**N-6.** The join's proposed tests the checker lacks, which the brief doesn't claim either:
- FX-4: the entry's place cited by another cell;
- FX-6: a homonym in the capability's note;
- FX-8: every `extension-point` line;
- FX-10: `shows` on a `core` cell's term;
- FX-14: an empty scope under a condition;
- FX-15: an empty filler for a party the cell holds;
- FX-17: one term on different capabilities.

So the safety net is narrower than the join proposed.

**N-7.** Line 67 quotes B-extent: "place the cell by what its statements show". A held line places one entry: "place the line by what the entry shows" (FX-8's words).

**N-8.** Line 107 tells an agent whose structure began in the batch before to read that batch's placements. Where two batches of one structure run at once (SH-4 to SH-10; SA-23 to SA-32), the earlier hasn't written them. Say: "If it hasn't run, say so in your notes; the coordinator aligns the two."

**N-9.** The selection's `placement` column (`where`, `decides`, `boundary`, `responsible`) is the concern map's kind of statement (B-extent, "What the concern map holds", lines 18 to 23). The brief sends agents to it (line 24) without saying so, and its own output has a `placement` column with other values.

**N-10.** `payments-providers`' rule drops `supports` (`selection.tsv`). That is the providers' feature marks, `["products", "refunds", "tokenization", "add_payment_method"]` on 8 provider elements (one provider, in each of the 8 locations), which rule 2 would place. Their cells (CM-PAY-022, CM-RET-002) already hold statements, so no count moves, a reading.

**N-11.** A changelog post or FAQ that names a third party doing something reads `shows` by line 76 ("`shows` where it names only ... a third party") and `outside` by line 73 ("a third party named as doing it"). No dry-run line took either.

**N-12. What the rewrite applies, as the join and the rulings say:**
- FX-2, footnotes (line 37);
- FX-5, a new thing against its parent's cells (line 51);
- FX-7, containers (line 62);
- FX-11 with D1, the badge (line 75);
- FX-17, a store's state never a term (line 79);
- M-1, M-4, M-5, M-6, M-9 and M-12;
- the checker's mark test, which strips plans in parentheses (FX-16's test).

The founder's rules stand:
- every claim is one of the three kinds;
- the founder's words are never evidence;
- the repositories are read-only;
- effort is never below `high`.

---

## The review's fixes and the rulings, one by one

| Fix or ruling | At `657cd861` | Brief's lines | Finding |
| --- | --- | --- | --- |
| FX-1, what else may be read | in part: the forms of a source, and terms and filler "from its sources" | 36, 39, 40 | SF-1, SF-2 |
| FX-2, footnotes | applied | 37 | — |
| FX-3, every thing named | in part: "read the entry's leads and the cells of the capabilities its words name" is out, and line 105 runs against it | 50, 53 | MF-1 |
| FX-4, a place another cell cites | applied; line 105 runs against it | 48 | MF-1 |
| FX-5, new against its parent's cells | applied | 51 | — |
| FX-6, homonyms | applied; line 105 runs against it | 38, 49 | MF-1 |
| FX-7, containers | applied; the checker notes only Zid's | 62 | SF-11 |
| FX-8, B-extent's clauses | applied, with B-extent's "cell" wording | 66 to 68 | N-7, MF-6 |
| FX-9, the group outside the entry | in part | 67 | SF-12 |
| FX-10, a table's rows in an article | in part: its integrations clause only, as M-4 | 37, 66 | MF-2 |
| FX-11, flags and badges | applied, for two forms | 75 | MF-3 |
| FX-12, an app's page with no maker or gate | applied, wider than M-10's "the platform's navigation lists under its brand" | 72 | MF-2 |
| FX-13, a catalog of services | in part: the venue as filler is out | 69, 72 | MF-7 |
| FX-14, `scope` | in part: computed conditions, parent routes, a region's words | 78 | SF-12 |
| FX-15, `filler` | applied, except a party the cell holds as a filler | 80 | SF-2 |
| FX-16, `quality` | stated otherwise: "or value", and "by plan" dropped | 81 | SF-3 |
| FX-17, `terms` | applied for a store's state | 79 | — |
| FX-18, `reading` | applied, except "A reading that says what a cell holds quotes the cell" | 83 | N-2 |
| M-1, maker evidence anywhere held | applied | 67 | SF-12 |
| M-2, BigCommerce's Extensions | BC-1's only | — | — |
| M-3 and M-7, the platform's list of third parties' things | applied, except "The venue is the filler" | 69, 72 | MF-7 |
| M-4, integrations are `core` | applied, unmarked | 66 | MF-2 |
| M-5, a role from other platforms | applied | 94 | — |
| M-6, a thing named counts in each | applied | 50 | — |
| M-8, a third party's own feature | left out | — | MF-7 |
| M-9, a tooltip's "you can build" | applied | 73 | — |
| M-10, an app's page | applied, wider, unmarked | 72 | MF-2 |
| M-11, a listing condition | in part: the computed condition | 78 | SF-12 |
| M-12, what a step states | applied | 40 | — |
| M-13, containers | in part: the grouping title | 62 | SF-12 |
| M-14, a conditional title | left out | — | SF-12 |
| D1, a badge | applied; the limited release it left open isn't | 75 | MF-3 |
| D4, a mark is never a quality | in part: the marked feature's `supports` is out | 50, 81 | MF-7 |
| Section 7, effort | applied | 31 | — |
| Section 7, size | stated, not applied to `batches.tsv` | 102 | SF-5 |

---

## The kinds the dry run didn't hold, and what an agent on them is unsure of

These are the kinds `review-H.md`'s section 6 lists, read entry by entry from `show --candidates` and their sources.

| Kind | Batches, entries | What the brief tells the agent | What it leaves the agent unsure of |
| --- | --- | --- | --- |
| Flags and release states | ZD-4 73; SA-8 241; WC-2 25; SH-14 6; SH-15 to SH-17 69 beta notes; SH-4 to SH-10 37 beta gates | `released` and `is_experimental`; a badge is `core` | a store's value; early access; previews; hashed betas (MF-3) |
| Staff permissions | SH-2, SH-3 469; SA-12 15; ZD-4 216; WC-2 17 | the staff permission is `core` | whether each takes a CM-STF-002 line beside its feature's; clear enough, a reading |
| A partner's or an app's access | SH-11 29; SH-12 18; SH-20 2 | `shows` (S7, and the selection's note) | clear |
| An API's own scopes, webhooks, controllers | SH-12 200; SA-12 232; WC-2 52; WC-3 16; SA-13 | "its own API for its own feature" | access scopes read as an app's access; docs read as apps using the API (MF-6) |
| The Partners portal's own permissions | SA-15 218 | nothing | S7 or staff (SF-7) |
| A route's gates | SH-4 to SH-10: gates of 232 entries on the user, 161 on the store and 21 on the client (one entry can hold several) | a store condition is the `scope` | a gate on the user or the client (SF-7) |
| Plan lines as text or answers | SA-2 319; SA-3 242; SH-21 361; SH-22 321; ZD-4 55; ZD-5, ZD-6 633; SA-16 284 | a plan's mark is the line's `scope` | marks held only in HTML (MF-8); Zid's packages lost (MF-5); a per-plan value's form (SF-3) |
| Lists by country | WC-1 29; WC-2 31 | the country is the `scope` | the country is lost (MF-5) |
| Plugins and apps one by one | WC-1; SA-1 30 apps; SA-33 26 themes | the platform's list of third parties' things is `extension-point` | "Built by WooCommerce" (MF-4); an app's price as a quality (SF-3) |
| Carriers | SH-26 203; SA-32 25 | the list rule (M-3, M-4) | a bare select list (SF-14); `type: salla` against `type: app`; the carriers' feature marks (MF-7) |
| A store's settings and records | WC-1 237; SH-24 49; SA-14 15; SA-21 68 | a setting the platform lists for a store is the platform's | the value's column (SF-3); bookkeeping, accounts, subscriptions (SF-13) |
| Derived tables | SA-15 330; SA-16 284; SH-10 81 | nothing | the capture's columns against the platform's (SF-9) |
| Route manifests beyond ZD-1 | SH-4 to SH-10 1,046; SA-4 to SA-8 706; SA-17 to SA-19 615; ZD-2 to ZD-4 | rule 3, and Zid's modules | "decided once" per section (SF-4); noise leads (SF-10); scaffolds (SF-13) |
| Mobile and POS apps | SH-18, SH-19, SH-23 | nothing specific | groups given as positions (SF-8); layout nodes (N-4) |
| Help notes and changelogs | SH-15 to SH-17 300 notes; SH-17 305 posts; SA-1 20 | the help-page clause, for titles | plan and staff notes clear enough, a reading; beta notes (MF-3); a third party named (N-11) |
| `out` and `outside` lines | every batch | the out list; `outside` | bookkeeping and scaffolds (SF-13); `outside` against `shows` (N-11) |

---

## What I ran

All commands ran from `/home/user/sharrwah-knowledge-map`, with `python3 -I`. Scripts were kept in the session's scratchpad, not in the repository.
1. **The two briefs:** `git show 657cd861:` and `dc1e6414:studies/class-model/briefs/H-held.md`, `git diff --stat dc1e6414 657cd861`, and `grep -c` on the brief for each clause of the fixes and rulings.
2. **The entries:**
   - `held_entries.py show --platform P --batch B --candidates` and `--meta` on SH-4, SH-12, SA-4, ZD-2, ZD-4 and ZD-5;
   - by importing `held_entries`, the first entries and leads of 40 structures of the kinds above.
3. **By script, over the 68 batches:**
   - each batch's entries with no lead, and its most common first lead;
   - the renderings of `nested:` structures that merge elements of different top-level lines or parents;
   - each selected structure's `source` form in its `meta.json`, and whether it has a `source.*` file;
   - each batch's `meta.json` sizes;
   - the entries with a numeric `parent` or `within`;
   - the admin router's gates, its sections' distinct first leads, and the leads that only `nextRoutes` give.
4. **The evidence:**
   - Shopify: `dev-dashboard-scopes`' items; `dev-store-feature-previews`' step `065.text.txt`; `admin-betas`;
   - Salla: `com-plans`' `text.txt` and its archive record, through `held_index.py` and `warc_text.py`, counting the plan marks; the same for `com-specialplan`; `permission-gates.tsv`'s header and `docs/READING.md`, line 122; the concern map's citations of `portal-stores-access-requests-permissions`;
   - WooCommerce: the release's `DefaultFreeExtensions.php`, `ContextPluginsRuleProcessor.php` and `assets/client/admin/chunks/3799.js`; `payments-providers`' and `core-profiler-free-extensions`' items.
5. **The model:** `land_points.py cell` for CM-SHP-017 and CM-POS-003; `class_slice.py caps --terms` for tracking, Flow and saved payment methods; `merged/qualities.tsv`'s kinds; `merged/cells.tsv` for CM-ACC-002, CM-MKS-009, CM-PAY-022 and CM-RET-002.
6. **The checker on fixtures,** on the scratch copy:
   - SH-21 and SH-17, each entry placed on its last lead;
   - WC-1 likewise, with three lines of a term, a filler and two option values that the brief and the checker read differently.

## What I didn't check

- I placed no entry beyond the fixtures, and judged no placement but the examples cited.
- I read no line of BC-1's or ZD-1's placements or notes, nor of the calibration's batches.
- I checked items against their sources for about eight structures (those in "What I ran", item 4), not all 145.
- I didn't run `held_amend.py`, which needs placements, nor measure what the fixes cost.
- I read Arabic entries only where they are cited above.
- Whether `is_built_by_wc: true` names WooCommerce as the maker is the reading MF-4 proposes, not a fact. The release states the field and shows it as "Built by WooCommerce", and the coordinator rules.
