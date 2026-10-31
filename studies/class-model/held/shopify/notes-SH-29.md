# SH-29: Shopify `flow-connectors`, entries 131 to 196, and `flow-workflow-limits`

**The batch:** 67 entries.
- **`flow-connectors`, 66:** the last 66 of the structure's 196 entries, the connector Shopify's actions `actionTasks/34` (Submit fulfillment request) to `actionTasks/99` (Get market data), in `structures/shopify/flow-connectors/capture-plus@installed/items.jsonl`, line 3 (observed-sh at `e38dc17e3`; run `20261007T033925Z-journey-flow`, `getInstalledConnectors`). SH-28 placed the first 130.
  - 39 are prefixed `shopify::admin::`;
  - 26 are prefixed `shopify::flow::`: the 24 Get data actions `shopify::flow::fetch::*`, Look up customer in segment and Get analytics data;
  - 1 is prefixed `shopify::iris::`, Send Shopify alert for errors.
- **`flow-workflow-limits`, 1:** the whole answer `getWorkflowLimits` on capture-plus (`structures/shopify/flow-workflow-limits/capture-plus/source.json`, same run).

**Count:** 67 entries, all `capability`; no `new`, no `out`. 68 lines:
- CM-AUT-001 `own-service`: 67, one for each entry;
- CM-SHP-020 `shows`: 1 (entry 53 of the batch, `actionTasks/86`, Get inventory item data, SH-E-3530b073).

**What I read:**
- the brief, the evidence map, and observed-sh's guides: `README.md`, `docs/READING.md` (its Structures and Limits sections), `docs/GAPS.md` and `structures/README.md`. None of them names Flow;
- `structures/REGISTER.tsv`, rows 105 (`shopify/flow-connectors`) and 106 (`shopify/flow-workflow-limits`). No `index/ledger/` file enumerates either structure: each is one answer of Flow's API;
- `selection.tsv`, rows 28 (`flow-connectors`: placement `where`, reason S-1) and 29 (`flow-workflow-limits`: placement `decides`, 'Flow's workflow limits, as its API states them');
- `show --meta`, both structures' `meta.json` and `source.json`, and `items.jsonl` line 3's `actionTasks/34` to `/99` with each task's fields;
- B-extent's "Cells and evidence" and "Conventions from the dry run", and the rulings' last section;
- SH-28's notes and placements;
- the earlier lines that `earlier` printed: SH-34:137, SH-34:198, SH-35:58, SH-35:68, SH-35:166, SH-36:68, SH-37:83, SH-37:222, SH-38:39, SH-39:68, SH-40:163, SH-41:13 and SH-60:95. I also read the earlier lines on Shopify alerts, found by grep, such as SH-2's Alerts Feed (SH-E-41c00fd6) and the post SH-E-4b64cb21;
- the cells of each task's record, with `held_entries.py cells`;
- CM-LOY-007's Shopify row in `merged/cells.tsv`, for SH-I-2027;
- one run step, `steps/042.frame-0.text.txt`, for the statement REGISTER row 106 names (M-12, below).

## How I kept SH-28's rules

- **R28.1.** Every task is CM-AUT-001 `own-service`, with the task's `label` as its term. Held posts name Shopify as Flow's maker (SH-E-0678ff26, SH-E-aca9896c). That gives the ruling after SH-55 and the router digest's rule 17.
  - **Scope:** empty on every task but Get analytics data (R28.6, below). No other task states a plan, a store condition or a release state: `restricted` is `false` and `badgeType` is null on the other 65.
  - **Quality:** none on the 66 tasks. No description of mine states a limit. The posts' 'return a list of up to 100 resources' (SH-35:58, SH-35:68, SH-37:222) are the posts' words, not these entries'.
- **R28.2, as the check amends it.** What a task sets or reads takes no line. For each task, I looked up the record's capability with `cells` (every lookup is in that task's `reading`). Every one holds something on Shopify:
  - CM-SHP-009, CM-SHP-011, CM-CAT-001, CM-CAT-002, CM-CAT-003 and CM-CAT-007;
  - CM-CHN-001 and CM-CNT-002 to CM-CNT-004;
  - CM-CNT-009, the URL redirects;
  - CM-ORD-001, CM-ORD-002, CM-ORD-005 and CM-ORD-006;
  - CM-INV-001 and CM-INV-005, CM-LOY-002 and CM-POS-003;
  - CM-CUS-001, CM-CUS-002 and CM-B2B-002, CM-B2B-003;
  - CM-SEL-001, CM-SHP-009 again for fulfillment orders, CM-MKT-001 and CM-CHK-007;
  - CM-ANL-001 and CM-ANL-006, CM-PAY-008, CM-PAY-022 and CM-NTF-001, CM-NTF-002;
  - CM-API-001 and CM-MKS-001.

  So R28.2's `shows` line applies to none of the records themselves. The one `shows` line is on a field of a record (CM-SHP-020, below).

  The Admin API and ShopifyQL are means, and take no line (rule 14 of the changelog digest, as R28.2 cites it).
- **R28.3.**
  - The 26 `shopify::flow::` actions are Flow's own, and the data they read takes no line (SH-35, line 58).
  - Send Shopify alert for errors I read by its words (below).
  - No task of mine has an app's id or a connector of its own.
- **R28.4.**
  - A task's `path` (Actions, Misc on all 66) and `categories` give no line. These include Shopify payments (Charge vaulted payment for B2B order), Shopify markets (Get market data), Retail, Store properties, Analytics, Online store, Metafields and Inventory.
  - The frame goes in no column.
- **R28.5.** `customConfigurationPageUrl` is null on all 66.
- **Earlier lines:** each task an earlier post announced takes that post's line, CM-AUT-001 `own-service`, and its reading names the line. There is one exception, SH-34:198 (below).

## Entries I decided against a rule's letter, or couldn't tell

1. **Get analytics data (SH-E-30b38dce, `actionTasks/89`, `shopify::flow::execute_shopifyql`, `badgeType: LIMITED_RELEASE`): `own-service`, not `core`.**
   - R28.6, as the check settles it, says that a task listed on the held store with this badge 'is offered on that store, so it is `core`', with the badge its quality. I kept what it settles: the task is offered, not `shows`; capture-plus, the store it is listed on, is its scope, as a beta enabled in a held store makes a route's scope; and the badge is its quality, `badgeType: LIMITED_RELEASE`. These are the source's own words. The check's 'limited release' isn't a string the source holds.
   - I read the check's `core` as the support an offered task takes. For a task of the platform's own admin, that is `core` (D1). For Flow's own task, it is R28.1's `own-service`, which the same check keeps for every other task. B-extent's `own-service` covers a separate product the platform's company makes, which is what Flow is (the ruling after SH-55).
   - If the coordinator meant `core` literally, the line's `supports` is the one word to change. The cell's supports don't change either way: CM-AUT-001@shopify holds `core` already, and the other 66 lines give it `own-service`.
   - **SH-34:198,** the changelog post announcing this action (SH-E-ae37b2d7, May 09, 2026), is still CM-AUT-001 `core`, on 'Flow's maker is not stated (as this cell reads it)'. The ruling after SH-55 aligned 38 Flow lines to `own-service`, among them SH-34:137, which carries the coordinator's check's words. SH-34:198 doesn't, and looks missed. It is for the coordinator to align.
2. **Get inventory item data (SH-E-3530b073, `actionTasks/86`): a second line, CM-SHP-020 `shows`, on 'customs information'.**
   - The description: 'Get data about your inventory items, which provide the stock keeping unit (SKU), whether quantities are tracked, shipping requirements, and customs information for the product variant'.
   - CM-SHP-020 (International shipping readiness and customs data) holds one Shopify row, `shows`: the help-centre section International shipping. Its reading says 'No Shopify statement held names an HS code, a customs code or customs data for a product or shipment', and it searched 'customs information' among others. This description names customs information kept for a product variant, on the platform's own record.
   - The check's amendment of R28.2 adds a `shows` line where the record's capability 'holds nothing'. CM-SHP-020 holds one row, so its letter isn't met. I added the line by the amendment's reason: the cell's reading is contradicted, as CM-ORD-011's and CM-ORD-013's were.
   - Against it is the ruling after SA-41: things named only in a list take no line. The description lists what an inventory item provides.
   - **What would settle it:** the coordinator's reading of whether a field a task's record keeps, which a cell's reading says isn't held, takes R28.2's `shows` line. If not, the line is the one to drop, and the description stays a lead for CM-SHP-020's second stage.
   - **The list's other fields take no line:**
     - the SKU, kept on variants and inventory items (CM-CAT-002, CM-INV-001);
     - whether quantities are tracked (CM-INV-001);
     - shipping requirements (CM-SHP-001).

     Their cells all hold.
3. **Send Shopify alert for errors (SH-E-6f4fc71d, `shopify::iris::send_shopify_alert_for_errors`): CM-AUT-001 alone.**
   - 'Send Shopify alert when workflow error occurs'. The alert is the admin's own Shopify alerts, which the earlier batches place on CM-NTF-002 `core` (SH-E-41c00fd6, SH-E-4b64cb21, SH-E-7184be60). It is a thing the action sets that Flow doesn't provide (R28.2), and CM-NTF-002's cell holds `core;extension-point`.
   - **The alternative:** the check gave Send internal email CM-NTF-002 `own-service`, since Flow sends that email itself. If the coordinator reads Flow's error alert as a notice Flow itself provides to staff, this entry takes the same line. The cell wouldn't change: it holds `own-service` already from SH-28.
   - **What would settle it:** Flow's reference page `actions/send-shopify-alert-for-errors` (the task's `documentationUrl`), which this brief doesn't let me read.
4. **Send payment reminder (SH-E-66ede047): CM-AUT-001 alone.**
   - 'Send an email to the buyer reminding them of their payment', in the connector Shopify, through the Admin API. As a reading, the email is the store's own payment reminder, a notification (CM-NTF-001, `core;extension-point`) under payment terms (CM-PAY-008, `core`). It is not an email Flow sends itself.
   - Shopify's notification template Payment reminder (SH-I-2027) is cited by no cell. CM-LOY-007's Shopify reading lists it as 'found and not cited'. It is a lead for CM-NTF-001 or CM-PAY-008 at the second stage.
5. **Create order risk assessment (SH-E-c4b60c48): CM-AUT-001 alone.**
   - 'Show your own fraud analysis on the order page'. The risk assessment it sets on the order is CM-ORD-006's (`core;extension-point`), and 'your own fraud analysis' is what the merchant brings.
   - R28.2 gives it no line. If the coordinator wanted the merchant's own analysis recorded, it would be `shows` on CM-ORD-006, which changes nothing.
6. **Get cash tracking session data (SH-E-a5ee7a9f): no scope.**
   - 'Get data about your cash tracking sessions from POS Pro' says where the sessions come from. It isn't a condition the platform sets for listing the task.
   - SH-37:222 kept no scope for its post's words on POS Pro (SH-E-3535373d). By the ruling after SH-70, 'POS Pro' would be the scope of a feature that comes with POS Pro. That fits cash tracking itself (CM-POS-003), which this entry gives no line.
7. **Charge vaulted payment for B2B order (SH-E-445b6048):**
   - its category Shopify payments is a group (R28.4). Whether the task needs Shopify Payments isn't stated;
   - it is the only one of my 66 tasks with no `documentationUrl` (null in the source). Across all 196 tasks, the only others are Shop Review Published and Flow's Get workflow run data.

## The workflow limits (SH-E-c7a5b710)

- **Its line:** CM-AUT-001 `own-service`, term `workflowLimits`. The limits are its quality, in the source's words: `maxWorkflowSteps: 500;maxWaitSteps: 40;maxWaitDurationSeconds: 7862400;maxWorkflowNoteCharacterLength: 2000;maxTotalWorkflowVariablesBytes: 50000`.
- **The wait:** 7862400 seconds is 91 days, by arithmetic. This is a reading, written only in `reading`.
- **Scope:** empty. The answer is capture-plus's and states no plan, and the limits may differ by plan; whether they do isn't held. The store is named in `reading`, as R28.1 names it.

## `CHANGES` lines, and what I decided

1. **CM-AUT-001@shopify gains `own-service`,** by lines 2 to 69, all but 55: every CM-AUT-001 line. The merged cell is `core;extension-point`, and SH-28's 130 lines make the same change. Kept, per R28.1 and the ruling after SH-55.

No other line changes a cell. Line 55 (CM-SHP-020 `shows`) adds a row to a cell that stays `not-stated`.

## The leads that are words only

The leads below hold nothing on Shopify. The checker printed no first-lead NOTE.
- CM-DVT-006, by 'then, update' (the output port 'Then' and the label's 'Update');
- CM-CHK-009, by 'add, order';
- CM-LOY-008, by 'get, order' or 'customer, get';
- CM-MKT-017, by 'about, product';
- CM-TRU-021, by 'company, data';
- CM-INV-004, by 'product, quantity, stock'. Get inventory item data's tracked quantities aren't a low-stock alert;
- CM-SHP-022, by 'about, shipping';
- CM-ANL-007, by 'analytic, data';
- CM-LOY-007, by 'reminder' (reorder reminders, not a payment reminder);
- CM-PAY-032, by 'order, send' and 'buyer, order, payment'. No description of mine names a link to pay;
- CM-OPS-004, by 'status' (a store's system status, not a product's).

Leads by a homonym, whose cells hold, are named in their lines' readings:
- CM-ACC-004 by 'company': a business entity, not a B2B company;
- CM-APP-003 and CM-PLN-004 by 'billing': an app's and a plan's billing, not a subscription's billing attempts;
- CM-PAY-023 by 'balance': 'the balance for a scheduled payment' is what is owed, not Shopify Balance;
- CM-RET-003 by 'return': 'return the results'.

## A structure whose items and sources disagree

None in substance.
- **`flow-connectors`:** the rendering leaves out each task's `iconUrl`, `version` and null fields, as SH-28 found. Charge vaulted payment for B2B order's null `documentationUrl` is read from the source.
- **`flow-workflow-limits`:** it has no `items.jsonl`. Its one entry renders `data.workflowLimits` of `source.json` whole, leaving out `__typename` ('WorkflowLimits').

## What the sources state that no entry holds (M-12), for the second stage

- **Recent runs:** `raw/runs/20261007T033925Z-journey-flow/steps/042.frame-0.text.txt`, line 2: 'Workflow runs are deleted 14 days after completion'. This is a limit Flow states on its own run history, a quality of CM-AUT-001. REGISTER row 106's next/reason names it in the capture's words.
- **Flow's reference pages** that each task's `documentationUrl` links to (REGISTER row 105: 'the Help Center reference pages state the triggers and actions in prose'). For my part they would settle three things:
  - Send Shopify alert for errors' recipient and channel (entry 3 above);
  - Send payment reminder's email (entry 4);
  - whether Charge vaulted payment for B2B order needs Shopify Payments (entry 7).

## Problems with this brief or the scripts

- **`earlier` still reports the input port's name 'name input' as a key,** with 52 unrelated `out` lines on every entry, as SH-28 found. I filtered those lines out. The remaining keys, the tasks' labels, matched the posts that announced them.
- **The checker's `own-service` NOTE fires on all 67 lines.** This is expected, since every line is a Flow task or limit.
- **R28.6's `core` and R28.1's `own-service` read differently for one task** (entry 1 above). The brief says B-extent governs where a rule reads differently from it, and B-extent's `own-service` is Flow's support, so I followed it.

## The coordinator's check

Measured: 10.4 million tokens over 64 requests, about 155,000 an entry. The checker prints no problem.
- **Kept:** every line on CM-AUT-001 `own-service`, the workflow limits as their quality, and decisions 4 and 5 (Send Shopify alert for errors and Send payment reminder on CM-AUT-001 alone, their notifications held elsewhere).
- **Decision 1, Get analytics data:** `own-service` stands. R28.6's `core` meant the support an offered task takes, which for Flow's own task is R28.1's `own-service`; SH-28's check is worded so.
- **Decision 2, SH-34:198:** aligned to `own-service`. It rested on 'Flow's maker is not stated', which the maker statements held since (SH-E-0678ff26, SH-E-aca9896c) answer, as SH-34:137 was aligned after SH-55.
- **Decision 3, the CM-SHP-020 line:** dropped. R28.2 as amended gives a record a `shows` line only where its capability holds nothing on Shopify, and CM-SHP-020 holds the platform's customs documents (SH-34, SH-48).
- `flow-connectors` and `flow-workflow-limits` are placed whole.
