# Review of the held pass's dry run, part R3: BC-1, lines 97 to 176

**What this is.** Part R3 of the review (`studies/class-model/briefs/H-review.md` at `2316f3ab`). It covers lines 97 to 176 of `held/bigcommerce/placements-BC-1.tsv` at `ff50bbee`, which are BC-1's entries 82 to 147:
- plan-comparison, lines 97 to 123;
- settings-list, lines 124 to 168;
- tax-services, lines 169 to 176.

The rows are in `review-H-R3.tsv`: 84 rows on 80 lines.

**What was read, and at which commit:**
- H-held.md and `held/selection.tsv` at `dc1e6414`.
- The model at `13205959`. The merged files are unchanged since then; `class_slice.py` changed only in how it reads held items.
- other-product-class at `0d79b794f` (`opc` below), through its README, then `bigcommerce/README.md`, `GAPS.md`, `structures/REGISTER.tsv` and `index/`.
- Each structure's `meta.json`, its `source.*` or `held_as`/`answer` file, and the run steps that the notes and readings cite.
- The leads as `show --candidates` prints them at `0018e2bc`.

BigCommerce's entries and selection rows are the same at `ff50bbee` and at HEAD.

**How to read the rows:**
- Every `why` is a reading unless it says it is a fact. A fact is cited at its file and line in `opc`, or by the model's key.
- **Two rows on one line.** Where a line's own placement stands but the entry also holds another capability's thing, the line has a `stands` row and a `missing line` row: lines 112, 125, 141 and 148.
- **`in_leads`.** On a `missing line` or `wrong capability` row, it is for the capability the verdict names. On a `can't tell` row, it is for the line's own capability.
- **`effect: column`** also covers two cases where no cell's placement changes:
  - line 132: one evidence row's `supports` changes, and its cell keeps `core` and `extension-point`;
  - line 112: a cell turns from none-held to held, placed not-stated.

  Each row's `why` says so.

## Counts

| Structure | Lines | Rows | stands | Not `stands` |
| --- | --- | --- | --- | --- |
| plan-comparison | 97 to 123 (27) | 28 | 24 | missing filler 1, missing line 1, wrong quality 2 |
| settings-list | 124 to 168 (45) | 48 | 39 | can't tell 3, wrong supports 1, missing line 2, wrong capability 2, should not be new 1 |
| tax-services | 169 to 176 (8) | 8 | 8 | none |
| **All** | **80** | **84** | **71** | **13** |

**The 13 by cause and effect:**

| Cause | count | capability | filler | column | All |
| --- | --- | --- | --- | --- | --- |
| care | 2 (157, 168) | 1 (161) | 1 (99) | 3 (112, 141, 148) | 7 |
| brief | | | | 3 (113, 119, 132) | 3 |
| evidence | 2 (140, 153) | | | 1 (125) | 3 |
| tool | | | | | 0 |

No row has `kind`.

**Where they fall** (for R6's thirds; BC-1 has 175 placement lines, 2 to 176):
- lines 99, 112 and 113 are in the second third;
- lines 119, 125, 132, 140, 141, 148, 153, 157, 161 and 168 are in the last.

A reading: the misses gather in settings-list, whose one-line descriptions need the most judgement. That structure is also where the batch ends, so its position and its kind of entry can't be told apart in this part alone.

**The four `count` rows,** each a cell's `core` resting on one held line:
- lines 157 and 168 give `core` to the wrong cell;
- lines 140 and 153 give it on words that don't settle the capability's thing.

## The cases

### BC-1's plan lines (lines 97 to 123)

**The rule, by B-extent.** Each row of the plan table is a plan line, and B-extent's `core` is "a plan line that includes it", with the plans checked as its scope.

**The cells agree on every line.** Every cell the batch placed a row on reads the same kind of line in the same way:
- CM-SFR-001: BC-S-0221;
- CM-CHK-001: BC-S-0095;
- CM-PAY-012: BC-S-0162;
- CM-MKT-002, CM-MKT-001 and CM-LOY-002: BC-S-0063;
- CM-SHP-004: BC-S-0377;
- CM-SFR-010: BC-S-0423;
- CM-MKT-022: BC-S-0090;
- CM-CUS-002: BC-S-0209;
- CM-SUP-001: BC-I-0415;
- CM-B2B-003: BC-S-0049;
- CM-SFR-013: BC-S-0068;
- CM-SHP-023: BC-I-0410;
- CM-INV-005: BC-S-0038;
- CM-PLN-001: BC-S-0185;
- CM-PLN-003: BC-S-0152 and BC-S-0153;
- CM-CHN-007: BC-S-0228;
- CM-CHN-003: BC-S-0369;
- CM-POS-001: BC-S-0372.

**The one exception the cells make.** A plan line that names other companies' solutions as what the store connects to is `extension-point` (POS, BC-S-0372). Line 105 follows it, and stands.

**What the plan lines get wrong or leave out:**
- **Tooltips naming a second thing.** Where a row's tooltip names another capability's thing, the batch gives it a line: lines 97 to 100, 103 to 105, 120 and 121. It doesn't for entry 90's "or even a loyalty program" (line 112). That case reads two ways: method ruling M3.
- **Marks.** A check mark and "Available" are the same mark of inclusion. The batch reads every check mark as scope only, but writes "Available" as a quality too (lines 113 and 119).
- **Fillers.** The batch names as fillers:
  - the carriers (line 109), as CM-SHP-004's cell does;
  - the marketplaces (line 104);
  - the channels' venues (line 103).

  It leaves the wallets out (line 99), which CM-PAY-012's cell makes fillers from the same kind of line.
- **What the row leaves unsaid, the run says.** The surcharge rate (line 116) is the platform's fee. This is a fact: the Core checkout states "Payment method platform fee: This plan includes a 2% platform fee on order GMV processed through non-preferred payment methods" (`opc:bigcommerce/raw/runs/20261029T015915Z-plan-upgrade-en/steps/012.text.txt:26`, also in `index/runs.tsv`'s note for the run).

### BC-1's settings sections (lines 124 to 168)

**The rule, by B-extent.** Each section the Settings list names, with its own title and address, is an admin section ("What a place of its own is"). It is `core` where its words name the platform's own feature. Where a capability already holds its thing, it is that capability's evidence, not `new`.

**Every section's own address checks out.** This is a fact, for all 40 sections. Each item carries the next section's address, item 40 carries none, and the source holds each section's own (`opc:bigcommerce/raw/runs/20261029T012951Z-store-settings-en/steps/002.frame-0.aria.yaml`, lines 7 to 227). Every address in the batch's readings is the section's own.

**What the review found:**
- **The platform's own place for third parties' services.**
  - The Tax section's "recommended services" (line 132) are services its page installs as apps. By B-extent's clause "the platform itself does it for the merchant", that is `extension-point`, as CM-TAX-004's cell reads Settings > Setup > Tax > TaxProviderName (BC-S-0389).
  - Accounting (line 153) isn't settled by the entry: method ruling M1.
- **A cell already citing the same place.** CM-AIA-005's cell already cites Settings > API and MCP > MCP (BC-S-0343). That decides line 168.
- **A description naming a second capability's thing.** The batch splits several sections:
  - Website (lines 133 and 134);
  - Tax (131 and 132);
  - Store logs (159 and 160);
  - Account sign up form (156 and 157).

  It doesn't split three more, which the review rows name:
  - "regional settings" (line 125, can't tell);
  - "order settings" (line 141, CM-ORD-001's own term);
  - "coupon limits" (line 148, CM-MKT-002's).
- **Sections whose words alone turn a cell `core`.** Besides lines 153 and 168, six lines do it:
  - line 140, CM-TRU-001;
  - line 157, CM-CHK-009;
  - line 146, CM-LOY-006;
  - line 151, CM-SFR-009;
  - line 158, CM-MIG-003;
  - line 163, CM-EVO-001.

  The last four stand: their words are the capability's name or its thing. The first two rest on words that don't name the capability's own thing:
  - line 140's "security settings for ... control panel" names no sign-in;
  - line 157's "form fields for ... addresses on checkout" names no field the merchant adds.
- **The new things.**
  - Display, Share and URL structure stand.
  - File access (WebDAV) is CM-CNT-001's (line 161). That capability's note is "The store's library of uploaded files", and its Shopify cell holds the uploads (fileCreate, SH-S-6202).

### The tax services' `extension-point` (lines 169 to 176), by B-extent's definition

**The facts:**
- Every provider but Basic Tax carries an `app_id` (`opc:bigcommerce/structures/tax-services/items.jsonl:1,3-7`, equal to `source.json`'s `data`, itself the answer file byte for byte).
- The Tax page recommends Avalara, with an Install link to `/manage/app/32120` (`…/steps/043.aria.yaml:8-14`).
- Every other service is listed with Install at `/manage/app/<its app_id>` (`…/steps/045.aria.yaml:17-40`).
- The platform's own statement calls tax providers "third-party tax providers" (BC-S-0396, in CM-TAX-004's cell).

**Reading: `extension-point` stands.** The entries show third parties doing the tax calculation through something the platform provides: its list of tax services, which installs each as an app. That is B-extent's `extension-point`. The alternatives fail:
- **`type: platform`.** H-held rule 4 says a field's value never names a maker, and the item doesn't define this one. It doesn't show the platform calculating, so it gives neither `core` nor `own-service`.
- **Basic Tax** has no `app_id` (null in the source; the rendering drops it). It is the store's own tax rules, `core` on CM-TAX-001 (line 171).
- **Avalara's filing** on CM-TAX-006 (line 170) is method ruling M2.

**What the batch could have relied on less.** Steps 43 and 45 are beyond the item and its source (H-held rule 1). The item alone gives the same reading less firmly: an `app_id`, a named product, and "Sales tax compliance for BigCommerce".

**The four default countries.** The register's "the same for four default countries" is a fact. Every call of `/internalapi/v1/tax/providers`, at steps 43, 45, 46, 51, 56 and 61, received one body (`…/answers.jsonl`, the row for that path). So the agent's "I didn't read the other answers" loses nothing.

The entries carry no label of the store's default country (`labels` is `.`). H-held rule 2's scope for "a tax service ... offered for a country" therefore isn't available to an agent. The lines use `supported_countries`, which is in the entry's words (rule 5). Fix F8.

### The differences the notes find with the model's cells

**CM-CHN-007's storefronts (line 101): the difference holds; its explanation fails.**
- The facts:
  - the table states 4, 5, 8 and 15 storefronts, at $30, $50, $100 and $100 (`opc:bigcommerce/structures/plan-comparison/items.jsonl:2-3`);
  - BC-S-0228 states "Add storefront $30/mo (max. 3) Add storefront $50/mo (max. 5) Add storefront $100/mo (max. 8) Contact Sales".
- They differ on Core (4 against 3) and on Performance (15 at $100, against Contact Sales). They agree on Growth (5) and Scale (8).
- So the notes' "one counts the first storefront and the other doesn't" fails: it would make every plan differ by one.
- A reading: these are two surfaces read at different times. BC-S-0228 is the concern map's, finished on 12 October (H-held.md). This one is the control panel's, on 29 October. Neither states a change.
- B-extent's practice settles what to do: keep each as stated, each with its source, as CM-INV-005's cell does ("the qualities keep each as stated").

**CM-INV-005's limit (line 120): holds.** These are facts:
- Performance is "Up to 50" here (`items.jsonl:17`) against "Custom" in BC-S-0038;
- Core to Scale agree;
- BC-S-0039's Enterprise plan is 100.

Keep both.

**CM-PAY-001's payments page (line 127): holds.** This is a fact: the Settings list holds Payments at `/manage/microapps/payments-settings-ui` (`002.frame-0.aria.yaml:22-25`). Once the line is amended, the cell's "No control panel page where the merchant activates payment methods is held" has to go.

## Method rulings: where B-extent doesn't settle a case

**M1, line 153: a platform's own settings section for connecting a kind of third-party software.**
- The section is "Connecting accounting software", at `/admin/apps/accounting`.
- B-extent's convention makes a route "named for an application, and gated only by the apps permission" the app's page. This route names a kind of app, not one, and its gating isn't held.
- CM-PAY-028's cell reads accounting connections as apps' (App Marketplace categories). CM-ANL-007's cell reads the platform's own product sending data out as `core` (BC-S-0336), and line 154 follows that reading, which fits.
- `core` or `extension-point`? The page `/admin/apps/accounting`, not held, would settle the fact. Either way, the count changes on CM-PAY-028.

**M2, line 170: a third party's own feature in its listing's description.** Avalara's "automatic return filing" is placed on CM-TAX-006 as `extension-point`, which turns that cell from none-held.
- CM-TAX-006's definition is filing "through the platform", and its parent is the platform's own tax service, CM-TAX-002.
- A third party's filing on it is the capability with another `supports`, as B-extent allows. Keeping the provider only in CM-TAX-004 is the other way.

**M3, line 112 against line 121: a plan line's tooltip naming what the merchant can build with it, against what it includes.**
- Entry 90: "building unique customer groups or even a loyalty program". Read as `shows` here.
- Entry 98: "Sell and fulfill orders ... including in-store pick up and curbside". `core`, line 121.
- B-extent's `core` is "a plan line that includes it". Whether a tooltip's "or even" includes a thing is for the coordinator. CM-LOY-004's BigCommerce cell, none-held, turns held either way, and `core` only if ruled so.

## Fixes to H-held.md, each in words to paste, with its lines and the checker test

**F1, rule 4: restore B-extent's own clauses.** Within B-extent. Lines 132 and 153.

> `core`: the platform itself does it for the merchant: its own admin place, setting, route, plan line or staff permission, its own API for its own feature, or a built-in feature it states. `extension-point`: the entry shows third parties doing it through something the platform provides: an app's page, an app store's category, an extension target or a provider interface. The platform's own admin place that lists third parties' services to install or connect, such as a list of tax services, is `extension-point`.

- **Test T2** (new): print each `core` line on a capability whose name or definition gives the work to third parties ("Third-party ...", "apps and providers"), for re-reading, as the checker already prints `own-service`.

**F2, rule 5: a plan's mark of inclusion is scope.** Within B-extent ("Qualities and slot fillers"). Lines 113 and 119. It also touches the tax lines' `document_submission supported` (169, 172 to 176): they pass rule 5 as written, so their rows stand, but under F2 they would move from the quality to the reading.

> A plan's mark of inclusion (a check mark, "Available", "Included", "Yes") gives the line its scope, never a quality. A quality is a limit, a certification, an uptime or a data location, or a value by plan of the kind the model records (a maximum, a rate, a fee, a sales limit).

- **Test T1** (new): flag a quality whose every value is a mark of inclusion.

**F3, rule 1: which files beyond the item and its source may clarify an entry.** Within B-extent; a choice of method for the coordinator.

> To clarify an entry you may read, beyond its item and source, the steps of the same run that the platform's `index/runs.tsv` names for it, including the step at which the structure's answer was first received (`meta.json` source.first_call) and the section's own page. A reading that rests on one cites it at its file and line; a reading never calls it the source.

The readings that rest on such a file:
- **line 125's "the default country and standard formats":** the Localization page, `…/20261029T012951Z-store-settings-en/steps/004.text.txt:1-29`, or the run's note in `index/runs.tsv`;
- **line 169's "the page recommends it (step 043)":** `043.aria.yaml:8-14`;
- **line 171's "'Configure your own tax classes, rates and zones' (source step 043)":** `043.text.txt:11`. The source is the answer received at step 43, not the page;
- **the notes' item 15, "the page offers each with 'Install'":** `043`, `045`.

Rule 1 names only the item and its source, so none of them is allowed as written. H-held does list `index/` among the files to read. The settings-list readings' addresses come from `002.frame-0.aria.yaml`, which is that structure's `held_as` source and is allowed. Line 116's settlement, from the checkout at step 12, is the review's, from `index/runs.tsv`'s note.

- **Test:** none mechanical. A reading citing a step that isn't its structure's `held_as` or `answer` could be printed for the coordinator.

**F4, rule 2: test every thing a description or tooltip names.** Within B-extent. Lines 112, 125, 141 and 148. The rule exists ("an entry two capabilities' at once ... two lines"); the batch applied it unevenly.

> Read each thing a section's description or a row's tooltip names, and give it its own line where a capability's thing is named, even where that cell is already `core`. A field group with no capability says so in the reading.

- **Test T7** (new): print an entry with a lead found by a term of its own text, not an identifier, whose capability none of its lines names. This catches lines 112 (CM-LOY-004, by "loyalty program") and 141 (CM-ORD-001, by "order settings"). It doesn't catch 148 (CM-MKT-002 isn't among the leads) or 125.

**F5, rule 2, `capability`: read the cells that cite the same place.** Within B-extent. Line 168.

> Before you place a section, a route or a setting, search the model for its own place (such as "Settings > API and MCP > MCP") and its address; where another capability's cell already cites that place, the entry is that capability's.

- **Test T4** (new): flag a settings or route entry whose place, as "Settings > <group> > <section>", is cited in another capability's cell (`class_slice.py search` over the cells' readings).

**F6, rule 2, `new`: bring B-extent's last sentence into the brief.** Within B-extent. Line 161.

> A place whose thing a capability already holds, as its cells' readings show, is that capability's evidence, not new: where you would name a capability as the new thing's parent, read that capability's cells first.

- **Test T6** (new): flag a `new` line whose capability, named in the notes as its parent, is among the entry's leads.

**F7, the selection and the build, for plan-comparison.** Within B-extent. No line; "What the batch never placed" below.
- The `meta:` rule (`0018e2bc`) applied to BigCommerce's `prices_above_the_table`.
- The plan page's billing toggle and GST line, which neither the items nor `meta.json` hold. That is the evidence repository's extraction, read-only here; the held pass can read step 4's text as the structure's `held_as`.

**F8, the build, for tax-services.** Within B-extent. Lines 169 to 176.
- Label each entry with the store's default countries under which the list was offered: the United States, Oman, the United Kingdom and Saudi Arabia, one answer. H-held rule 2's "offered for a country" scope can then be written.

**For the other recurring misses:**
- **Test T3** (new), for `count`: print each cell that one held line alone would turn `core`, from none-held, not-stated or `extension-point` only. `held_amend.py plan` already computes them. It catches:
  - lines 140, 153, 157 and 168;
  - and the five lines that stand: 117, 146, 151, 158 and 163.
- **Test T5** (new), for fillers: flag a line whose entry names a party that the same cell already holds as a slot filler, with `filler` empty. It catches line 99: Apple Pay and Amazon Pay, in CM-PAY-012's fillers.

## What the batch never placed

**plan-comparison.** The items match `source.html` row for row; that is a fact. The page the table was cut from, step 4 (`held_as`), and `meta.json` state more, and no entry holds any of it:

| Thing | Where (`opc:bigcommerce/raw/runs/20261029T015915Z-plan-upgrade-en/steps/004.text.txt`) | Would change | Left out by |
| --- | --- | --- | --- |
| **Prices:** Core $39 monthly or $29/mo billed annually, Growth $105/$79, Scale $399/$299, Performance by quote | 15 to 37; `meta.json` `prices_above_the_table` | CM-PLN-001's reading: "no statement gives the plans' prices, and no plan page of the control panel is held" goes. The cell stays `core`; a price-per-plan quality, as the model records GMV caps | the build (the `meta:` rule is Zid's only); the extractor kept them in `meta.json`, not in the items |
| **Billing period:** "Annual (Save 25%)" and "Monthly"; "Billed Annually" on each plan; "All prices in US Dollars. Billed annually." | 13-14; 18, 24, 30, 35; 38 (the last in `meta.json`) | **CM-PLN-002, a count:** its BigCommerce cell is none-held, searched "monthly; annual; annually; renewal; …", and would gain `core` | the extractor ("Annual (Save 25%)" is in neither items nor meta) and the build |
| **GST:** "All prices shown in US Dollars. Purchases in Australia will be assessed GST." | 65 (`004.aria.yaml:257`) | CM-PLN-007's reading: "No tax on BigCommerce's own fees or rate is named (searched: VAT; GST; …)" goes. The cell stays `core` (from S-02's statements); scope Australia; GST possibly a filler | the extractor and the selection (the table only) |
| **Performance by quote:** "Contact sales or call 1-855-884-6731 for custom pricing"; "Performance? Call 1-855-884-6731, UK: +0808-1893323 for pricing tailored to your business" | 34; 64 | CM-PLN-001, column | as prices |
| **"Current plan: Free Trial"** | 11 | none: one store's state, out by H-held; it shows a trial plan exists (CM-PLN-001) | the extractor |
| **The plans' taglines and "MOST POPULAR"** | 19, 25, 31, 36; `004.aria.yaml:44` | none (shows, or a UI string) | the extractor |

Beyond the structure, the same run's checkout steps (12 to 113) hold the platform fee disclosure and the Taxes by billing address in 15 places. No structure holds them (`structures/REGISTER.tsv` lists none). They bear on CM-PLN-003 and CM-PLN-007, both already `core`.

**settings-list.** The items and the source agree on all 40 sections, their groups, positions and descriptions; that is a fact. Two things are in no entry:
- **Each section's own address.** The selection drops it (`drop:address`), as the items carry the next section's. The extractor's pairing left it out, and the selection's rule took it away. The agents took every address from the source, so the lines lose nothing.
- **The "new" marks on Search and MCP** (`002.frame-0.aria.yaml:73`, `:227`). These are release markers, which the readings of lines 138 and 168 carry.

Neither changes a cell.

**tax-services.** The items equal the answer, so no thing the source states is missing from them; that is a fact.
- **Dropped by the rendering:** empty values, namely Basic Tax's `app_id: null`, Avalara's and Vertex's empty `supported_countries`, `connection`, `connection_target` and `unsupported_countries`. No cell change.
- **In the entries, on no line:** each provider's tax class codes (Avalara's OH010000, FR, P0000000 and SG030100; Vertex's HANDLING, SHIPPING, TAXABLE and WRAPPING). No capability holds them, and they aren't a quality by B-extent. No cell change.
- **In no entry:** the store's default country under which the list was offered (F8).

## The notes' claims for these structures

**The new things:**

| Claim | Verdict | Why |
| --- | --- | --- |
| `new:Display` (entry 110): its terms and its parent, CM-ACC-006 or CM-SFR-001 | holds | Re-searched "display; display settings; product page; category page; storefront settings; theme settings": no capability. The parent by the platform's grouping (General, CM-ACC-006) follows B-extent's `parent` convention. CM-SFR-001 fits less, as the section covers the control panel's display too |
| `new:Share` (111) | holds | The "share" hits are other words, such as a share of revenue; CM-SUP-003 is social proof |
| `new:URL structure` (112), not joined to CM-CNT-006 | holds, as a reading | CM-CNT-006's own note: "No statement defines what a custom URL is". The coordinator decides with it |
| `new:File access (WebDAV)` (133), parent CM-CNT-001 | refuted | It is CM-CNT-001's thing (line 161) |

**The notes' "couldn't tell":**

| Item | Verdict | Why |
| --- | --- | --- |
| 7, Comments (121) | stands as placed, still open | The cell's "built-in comment system" (BC-S-0072) carries it. The page would settle it |
| 8, Miscellaneous (115) | CM-ACC-006 holds; a line is missing | "order settings" is CM-ORD-001's own term (BC-S-0104), line 141 |
| 9, Security & Privacy (114) | CM-TRU-006 holds; CM-TRU-001 can't tell | Line 140, a `count` |
| 10, Website (109) | holds | No capability holds physical dimension settings |
| 11, MCP (140) | settled: CM-AIA-005 | Its cell cites Settings > API and MCP > MCP (BC-S-0343); line 168 |
| 12, Storefront API Playground (136) | holds | B-extent's own-API rule ("a guide addressed to app developers included"); CM-DVT-001 fails |
| 13, Account sign up form (130) | second line refuted | CM-CUS-008 (line 157). CM-CHK-009 stays none-held |
| 14, Accounting (127) | open | Method ruling M1, a `count` |
| 15, tax services (141 to 147) | settled: `extension-point` | Steps 43 and 45 (Install to `/manage/app/<app_id>`) and BC-S-0396. `type: platform` names no maker. Avalara's CM-TAX-006 line is M2. The four countries are one answer, a fact |
| 16, Surcharge rate (94) | settled: CM-PLN-003 | Step 12: "This plan includes a 2% platform fee on order GMV processed through non-preferred payment methods" |
| 17, Full-featured storefront (82) | holds | The wallets are fillers it leaves out (line 99) |
| 18, claims of effect, not qualities (89, 96) | holds | B-extent's quality is a limit, a certification, an uptime or a data location |

**The differences with the model's cells:**
- **CM-CHN-007, CM-INV-005 and CM-PAY-001:** as in "The cases" above. The storefronts' difference holds and its explanation fails; the other two hold.
- **None-held cells gaining a placement:**
  - CM-EVO-001 (135) holds;
  - CM-MIG-003 (131) holds;
  - CM-CHK-009 (130) is refuted, so the cell stays none-held;
  - CM-AIA-004 (140) is refuted, so the cell stays none-held;
  - CM-MKT-013 (19) is R1's.
- **What the list leaves out.** These lines also change cells, and the notes don't list them:
  - CM-LOY-006 (line 146) and CM-SFR-009 (line 151) gain `core` from none-held;
  - CM-TRU-001 (line 140) gains `core` from none-held; can't tell;
  - CM-TAX-006 (line 170) gains `extension-point` from none-held; M2;
  - CM-PAY-028 gains `core` from `extension-point` only (line 153).
- **Not-stated cells gaining `core`:** CM-ONB-003 (95) holds (line 117).

**Structures whose items and source disagree:**
- **settings-list:** holds. All 40 were verified (above).
- **plan-comparison:** holds. All 19 rows were verified against `source.html`.
  - The value cells hold 39 check marks (`glyph="ic-check"`).
  - The 10 icons in the feature cells are tooltip icons (`ic-info-outline`), not marks.

**The notes' problems that bear on these lines:**
- **The leads' first-letter bug** is fixed at `ff50bbee`. No lead of entries 82 to 147 now rests on a broken word.
- **Two other faults of the leads remain:**
  - 10 of the 19 plan entries lead to CM-PLN-001 "by performance", the plan column's name, not the entry's words. Only for entry 99 is it the right capability.
  - No tax entry has a CM-TAX lead.
- **The quality format** "<what>: <value> (<plan>), …" holds, and keeps values by plan apart.

## The leads

How often the right capability is among the entry's leads, as `show --candidates` prints them now. This counts one per line on a capability, for the capability the verdict names:

| Structure | Right capability among the leads |
| --- | --- |
| plan-comparison | 12 of 27 |
| settings-list | 24 of 41 |
| tax-services | 0 of 8 |
| **All** | **36 of 76** |

The four `new` lines are left out. Entries 106, 120 and 126 have no leads at all.
