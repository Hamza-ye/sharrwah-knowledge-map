# SH-28: Shopify `flow-connectors`, entries 1 to 130

**The batch:** the first 130 of the structure's 196 entries, the tasks Shopify Flow's API listed as the installed connectors on capture-plus (`structures/shopify/flow-connectors/capture-plus@installed/items.jsonl`, observed-sh at `e38dc17e3`; run `20261007T033925Z-journey-flow`, `getInstalledConnectors`):
- entry 1: the connector Shop's one trigger;
- entries 2 to 14: the connector Flow's 2 triggers, 1 condition, 8 actions, 1 for each loop and 1 wait step;
- entries 15 to 96: the connector Shopify's 82 triggers;
- entries 97 to 130: the first 34 of its 100 actions (to `actionTasks/33`, Mark order as paid). SH-29 has the other 66 and `flow-workflow-limits`.

**Count:** 130 entries, all `capability`; no `new`, no `out`. 132 lines:
- CM-AUT-001 `own-service`: 130, one for each entry;
- CM-SUP-001 `own-service`: 1 (entry 1, Shop Review Published);
- CM-NTF-002 `own-service`: 1 (entry 9, Send internal email).

**What I read:**
- the brief, the evidence map and observed-sh's guides (`README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`);
- `structures/REGISTER.tsv`, row 105 (`shopify/flow-connectors`). No `index/ledger/` denominator lists this structure: it is one answer of Flow's API, not a sitemap, route or mutation;
- `selection.tsv`, row 28 (rule `nested:triggerTasks,conditionTasks,actionTasks,forEachTasks,waitTasks`, placement `where`, reason S-1) and `inspection-H.md`'s S-1, which that reason names;
- `show --meta`, and both labels' `meta.json`, `items.jsonl` and `source.json`;
- B-extent's "Cells and evidence" and "Conventions from the dry run", and the rulings;
- the digests' parts my message names:
  - the router digest's rule 17 and its section 3 table;
  - the Editions digest's section 3 table, rule 16, E73 and E81;
  - the changelog digest's C43.10 and rule 14;
- the earlier lines `earlier` printed, with the SH-34, SH-35, SH-36, SH-38 to SH-41, SH-44, SH-57 and SH-60 lines they lead to. SA-23's webhook events (`placements-SA-23.tsv`, its notes' rules 3 to 5) I read only to compare.

I read no help page. The tasks' `documentationUrl` links to Flow's reference pages, which the brief's rule 1 doesn't list among the files that may clarify an entry.

## The rules for `flow-connectors` (R28.1 to R28.6), for the coordinator to check and SH-29 to keep

**R28.1. A task's place.** Each task of the connectors Flow and Shopify is CM-AUT-001's thing: a trigger, a condition, an action, a for each loop or a wait step. CM-AUT-001 is the automations the merchant builds from triggers and actions.
- **Support:** `own-service`. Held posts name Shopify as Flow's maker: “Today we’re introducing test runs in Shopify Flow” (SH-E-0678ff26) and “We’ve added a new trigger to Shopify Flow for when subscription contracts are created” (SH-E-aca9896c). That gives the ruling after SH-55, the router digest's rule 17, and Flow's rows in both digests' tables.
- **Terms:** the task's `label`.
- **Scope:** empty. The answer is capture-plus's installed connectors. No task states a plan, a store condition or a release state: `restricted` is `false` and `badgeType` is null on all 130. The store is named in these notes, as the earlier Shopify batches name it in `reading` and never in `scope`.
- **Quality:** a limit the description states. The only one is Workflow error occurred, 'limited to a single occurrence per workflow version within 30 days' (entry 3).
- **Earlier lines:** where an earlier line placed the same task, I kept it, and the reading names that line. Most of these are changelog posts announcing it; SH-35, SH-37, SH-56 and SH-62 placed Flow's own actions. All of them are CM-AUT-001 `own-service`.

**R28.2. A task's record takes no line.** A task starts from, reads or sets one of the platform's records or events: an order, a fulfillment order, a return, a customer, a company, a tag, a note, a payment. That record takes no line, whoever makes it: the merchant, a customer, a store admin, a fulfillment service or a 3PL, or an app. Flow doesn't provide the record; it is what the step works on. This is the practice the earlier batches set for this very case:
- the Editions digest's rule 16, and its E81 (SH-60, lines 97 and 101): 'Metaobject triggers in Flow' and 'Return automation in Flow' give CM-CNT-002 and CM-RET-003 no line, 'the returns are what they act on, not a thing Flow provides';
- the changelog digest's rule 14;
- SH-34's rule 7, as SH-35 (line 58), SH-36 (line 141), SH-41 (lines 3 and 13) and SH-44 (lines 79, 114 and 141) read Flow's tasks. SH-36 (line 141) gives no line even where the post says the records are made “by you or third-party apps”.

The connector Shopify's 'GraphQL-based Shopify Admin API' takes no line either: it is the means, and rule 14 excludes 'a means such as an API it uses'.

E81's second bullet ('A platform feature the app automates takes `core`') is for a statement whose own subject is the platform's feature, such as the card 'Automate new account setup' (SH-60, line 17). A task in Flow's catalog is Flow's own step, as 'Return automation in Flow' was, and that card's return actions are this batch's entries 112 to 114.

The leads this rule leaves are listed below, with the cells they would change.

**R28.3. Who provides a task, and when its thing takes a second line.** The connector (`within`) and the id's prefix say who provides a task:
- **Connector Flow, prefix `shopify::flow::`:** Flow's own logic ('Logic tasks within Shopify Flow'). It is `own-service`.
- **Connector Shopify, prefix `shopify::admin::`:** Flow's own triggers and actions over the store's records ('Integrate your Shopify store with Flow using the GraphQL-based Shopify Admin API.'). It is `own-service`. In SH-29's part, the same connector also holds:
  - 26 actions prefixed `shopify::flow::`: the 24 Get data actions `shopify::flow::fetch::*`, Look up customer in segment and Get analytics data. They are Flow's own, and the data they read takes no line (SH-35, line 58).
  - one action prefixed `shopify::iris::`, `send_shopify_alert_for_errors` ('Send Shopify alert for errors'), whose prefix names another service. SH-29 reads it by its own words.
- **An installed app's connector:** the app's tasks through Flow. Shop is the case here: its task carries the app's own id (`8a9252b0-7760-44c7-8204-1f39534ccd07`, with no `shopify::` prefix), and the connector has an `installUrl` on apps.shopify.com and a `configUrl` at the store's `admin/apps/shop-72`.
  - On CM-AUT-001, an app's task takes the app maker's support:
    - Shopify's own app takes `own-service`. Shop does its things as `own-service` (the ruling after SH-34).
    - A third party's app takes `extension-point`, with the app as filler. There is none in SH-28.
    - An app with no maker statement held takes `shows` (the ruling after SH-43).
  - **A second line:** where the task's provider itself provides the thing the task starts from or does, that thing takes its capability's line with the provider's support (the Editions digest's rule 16: 'only where the app provides that thing'). In SH-28:
    - entry 1: Shop's reviews are the Shop app's own product reviews, which CM-SUP-001's note names (SH-S-7476). That gives CM-SUP-001 `own-service`.
    - entry 9: Flow's Send internal email: “Send an email notification to your staff”, which Flow sends itself. That gives CM-NTF-002 `own-service`. SH-35 (line 152) kept the same action on CM-AUT-001 alone. That post was about the action's From field, not about what the action is.
  - No other Flow logic task names a thing another capability holds: I searched 'HTTP request; external service; JavaScript; custom code; run log; scheduled; schedule; internal email; staff email', and nothing came back but other capabilities' schedules.
- **The connector's `publisher` field** names Shopify on all three connectors. I don't use it as a maker statement: whether Flow shows it to merchants isn't held, and the ruling after WC-4 asks for a field merchants are shown. It is a lead below.

**R28.4. Groups and frame.**
- **Groups give no line.** A task's `path` (Triggers or Actions, with Order, Customer, Product or Misc) and its `categories` say where Flow lists the task, not what it is (rule 3; M-6 as refined). The categories are Orders, Products and collections, Shipping and fulfillment, Discounts and marketing, Customers, B2B, Inventory, Metaobjects, and the like.
  - So 'Discounts and marketing' doesn't make entries 33, 34, 35, 94 or 95 a marketing automation. The Editions digest's E73 (CM-MKT-006) is for automations whose own words call them marketing automations powered by Flow.
- **Frame goes in no column.** These are the ports ('Then', 'Otherwise', 'Input'), `returnType` (`void` on all 196), `iconUrl`, `version`, `lastUpdated`, `restricted`, `connectorInfo` and `dynamicDescriptionTemplate`.
- **What is `out`:** an entry that is only a task's frame, such as a port with no statement of its own. None of SH-28's is: every task has a label and a description of its own, and no two of the 196 share a label.

**R28.5. A page another app supplies for a step.** `customConfigurationPageUrl` is null on all 196 tasks. So no task takes the router digest's rule 17 line (`extension-point` on CM-AUT-001, with CM-APP-006 `core`).

**R28.6. For SH-29.** One task has `badgeType: LIMITED_RELEASE`: `shopify::flow::execute_shopifyql`, Get analytics data, `actionTasks/89`. The source doesn't define the value. SH-29 weighs:
- the brief's rule that a release 'available only to some merchants or stores' is `shows`;
- against D1: a listed badge with no limit stated is `core`, the badge in `reading`.

The task is listed on capture-plus.

## `CHANGES` lines, and what I decided

1. **CM-AUT-001@shopify gains `own-service`,** on all 130 entries. The merged cell is `core;extension-point`, and its reading says no statement names Flow's maker. The held batches have since placed Flow's own features `own-service` (38 lines aligned after SH-55; the router digest's rule 17). Kept.
2. **CM-SUP-001@shopify gains `own-service`** (line 3, entry 1, Shop Review Published). The merged cell is `extension-point`, with the Shop app's product reviews as `shows` on SH-S-7476's 'Shop isn't responsible for the content, accuracy, or reliability of the reviews that you receive'. That statement says who answers for the reviews' content. This entry shows the Shop app publishing reviews, a feature of Shopify's own consumer app (the ruling after SH-34; the Editions digest's rule 16). Kept, for the coordinator to weigh against the cell's reading of SH-S-7476.
3. **CM-NTF-002@shopify gains `own-service`** (line 12, entry 9, Send internal email). The merged cell is `core;extension-point`. Kept, as R28.3 reads it. The coordinator may prefer SH-35's precedent, CM-AUT-001 alone; if so, line 12 is the one to drop.

## The first leads that hold nothing, and why no line names them

- **Line 6** (entry 4, Condition): CM-API-010, conditional webhooks, by 'conditions'. A workflow's branch isn't a webhook's condition (as SH-34 found).
- **Lines 32 and 102** (entry 29, Fulfillment order holds released; entry 99, Hold fulfillment order) and **line 34** (entry 31, by 'failed'): CM-ORD-003, order statuses. That capability is the order's own statuses, not a fulfillment order's hold or a fulfillment service's failure.
- **Line 33** (entry 30): CM-OPS-004, by 'status'. That capability is a store's system status.
- **Line 126** (entry 123): CM-DVT-006, by a field's name ('name: then, update'). No lead.
- **Lines 127 and 128** (entries 124 and 125, Update order note and Update draft order note): CM-ORD-013, notes on an order. This is a real lead, and a cell that holds nothing on Shopify. By R28.2, the note is the data the action sets, so it takes no line. See the leads below.

## Leads: the records the tasks act on (R28.2), for the coordinator and the second stage

Each task's record, as I read it. None takes a line under R28.2. These are the lines the coordinator would write if it ruled otherwise:
- for a trigger, by E81's first bullet, none either way;
- for an action, `core` by E81's second bullet, or `shows`.

| Entries | What the task acts on | Capability (a reading) | Its Shopify cell now |
| --- | --- | --- | --- |
| 15, 126, 127 | orders, archiving | CM-ORD-001 | core;extension-point |
| 53, 128 | cancellation (128 also 'voids authorization', CM-PAY-020) | CM-ORD-004 | core |
| 54 | deletion | CM-ORD-012 | core |
| 56, 130 | paid state (130 also CM-PAY-016's 'Mark as paid') | CM-ORD-015 | core |
| 57 | a new risk level | CM-ORD-006 | core;extension-point |
| 67, 68 | draft orders | CM-ORD-005 | core |
| 110, 111 | invoice emails | CM-ORD-008 | extension-point |
| 117 to 120 | order and draft order tags | CM-ORD-011 | **holds nothing** |
| 124, 125 | order and draft order notes | CM-ORD-013 | **holds nothing** |
| 58 | refunds | CM-RET-002 | core |
| 59 to 65, 112 to 114 | returns | CM-RET-003 | core;extension-point |
| 66 | 'a chargeback or inquiry dispute' | CM-PAY-009 | core;outside |
| 76, 77, 129 | tender and order transactions, capture | CM-PAY-020 | core;outside |
| 90 to 92 | customer payment methods | CM-PAY-022 | core |
| 93, 106 | payment schedules, payment terms | CM-PAY-008 | core |
| 16, 73, 81 | products, product status | CM-CAT-001 | core |
| 74, 75 | variants | CM-CAT-002 | core;extension-point |
| 48, 49 | collections | CM-CAT-003 | core |
| 121, 122 | product tags | CM-CAT-006 | core |
| 82 to 89 | selling plan groups, subscription contracts and billing attempts | CM-SEL-001 | core;extension-point |
| 69, 70, 78 to 80 | inventory items and levels | CM-INV-001 | core |
| 71, 72 | inventory transfers | CM-INV-006 | core |
| 17 to 19, 24, 26, 27, 31 | fulfillment requests to 'a fulfillment service' (18: 'or a 3PL') | CM-SHP-011 | core;extension-point |
| 21 to 23, 28 to 30, 32, 50 to 52, 55, 97, 99, 101 | fulfillment orders, holds, fulfillments | CM-SHP-009 | core;extension-point |
| 20 | local delivery | CM-SHP-008 | core |
| 25 | pickup | CM-SHP-007 | core |
| 98 | shipping labels | CM-SHP-002 | core;outside |
| 36, 37, 42, 43, 115, 116, 123 | customers, their tags and note | CM-CUS-001 | core |
| 38, 39 | customer accounts | CM-CUS-010 | core;extension-point |
| 40, 41 | segments | CM-CUS-002 | core;extension-point |
| 33 | email marketing subscription | CM-CUS-007 | core |
| 34 | abandoned checkouts | CM-CHK-007 | core |
| 35 | a visit with a product viewed and no purchase | CM-MKT-022 (or CM-MKT-009) | core;extension-point |
| 94 | automatic discounts | CM-MKT-003 | holds nothing, but SH-60's line 147 already makes it `core` |
| 95 | discount codes | CM-MKT-002 | core |
| 96 | metaobject entries, 'including some apps like Shopify Forms and other third-party apps' | CM-CNT-002 | core;extension-point |
| 44 to 47, 100, 104, 105, 107 to 109 | companies, locations, contacts and their settings | CM-B2B-002 | core |
| 102, 103 | catalogs | CM-B2B-003 | core |

**What would change the model:**
- **CM-ORD-011, order tags.** Its note sends “Shopify's automations that tag orders, if any” to CM-AUT-001, which these lines do. But its reading, 'No Shopify statement held shows tags on orders', is contradicted by entries 117 to 120. The admin's own order page would be the better statement, for the second stage.
- **CM-ORD-013, notes on an order.** Its reading is 'No Shopify statement held shows notes or comments on an order'; entries 124 and 125 show them. The admin's order page would be the better statement, as above.
- **CM-ORD-008, order invoices.** Entries 110 and 111 ('Send an invoice email for an order') would add the admin's own invoice email to a cell that holds only the App Store category. Whether Shopify's invoice email is CM-ORD-008's invoice or CM-PAY-032's payment link (CM-PAY-032's note: “Shopify's draft orders' invoices (SH-S-7225, CM-ORD-008) aren't stated to carry a link to pay (U-018, apart)”) would be settled by Flow's reference page `actions/send-order-invoice`, which this brief doesn't let me read.

**Statements in the descriptions beyond the event,** kept in each line's reading:
- 52 defines a fulfillment order, 'an assignment of line items to a fulfillment location', ready 'if there is inventory available to fulfill the order' and (after a run of spaces in the source) 'a risk assessment has been performed on the order';
- 76 defines a tender transaction, 'after money passes between merchant and customer';
- 107: 'Addresses entered at checkout won't be saved to company location.';
- 108: 'Orders without shipping addresses will be submitted as draft orders.';
- 40: 'It is not started for existing segment members.'

## Entries I couldn't tell, and what would settle each

- **Entry 1's CM-SUP-001 `own-service`:** settled by the coordinator's reading of the ruling after SH-34 for the Shop app's reviews, against the cell's `shows` on SH-S-7476.
- **Entry 9's CM-NTF-002 `own-service`:** settled by whether a workflow's email to staff is a staff notification in CM-NTF-002's sense. SH-35's line 152 kept the same action on CM-AUT-001 alone.
- **Entry 96:** 'some apps like Shopify Forms and other third-party apps' sets Shopify Forms beside third-party apps. It names no company, so it is no maker statement (B-extent; the ruling after SH-43). It is a lead for Shopify Forms' maker gap (the Editions digest's table: none held).
- **Entry 35:** if its visit is ever placed, it is CM-MKT-022 (buyers who left without completing the order) or CM-MKT-009 (the customer events behind it). The words name neither recovery nor an event.

## A structure whose items and sources disagree

None in substance: `items.jsonl` holds `data.connectors` of `source.json` in order, with `position` added.

The rendering (`show`) leaves some things out: the Shop task's id `8a9252b0-7760-44c7-8204-1f39534ccd07`, every task's `iconUrl` and `version`, and the null fields. The source governs: entry 1's lines cite the id at `items.jsonl`, line 1.

## What the source states that no entry holds (M-12), for the second stage

- **The connectors themselves,** in `capture-plus@installed/items.jsonl`, lines 1 to 3. They are no entry, since the structure's rule nests only their tasks. The concern map cites their names (SH-S-2461 to SH-S-2463, at `b46731d0`). Their own fields:
  - **Shop** ('Reach millions of high-intent shoppers on Shop'): `publisher` 'Shopify', with `externalUrl` `https://apps.shopify.com/532861601aa89a5e70f5d56d075e82ac/partner`; `installUrl` on apps.shopify.com; `configUrl` `https://capture-plus.myshopify.com/admin/apps/shop-72`;
  - **Flow** ('Logic tasks within Shopify Flow'): `publisher` 'Shopify', with `externalUrl` `https://www.shopify.com`;
  - **Shopify:** `publisher` 'Shopify'; its 15 `taskCategories`, Orders to Shopify markets (line 3).

  If Flow's editor shows `publisher` to merchants, it is a maker statement for each connector (the ruling after WC-4). That isn't held either way.
- **`capture-plus@first-party`** (`getFirstPartyConnectors`): five connections with no tasks, so no entries: Google Sheets for Shopify Flow, Asana, Trello, Slack and OpenAI, each with its description. The concern map cites them (SH-S-2464 to SH-S-2468), and CM-AUT-001's cell holds three as `shows` (SH-I-1700, SH-I-1703, SH-I-1704). The operation's name, first-party, is the API's and is shown to no merchant, so it names no maker. It is a lead for those connections' maker.
- **Flow's reference pages** that each task's `documentationUrl` links to, 'the Help Center reference pages state the triggers and actions in prose (83 and 109 pages)' (REGISTER, row 105). They are for the second stage, which may settle CM-ORD-008 against CM-PAY-032 (entries 110 and 111) and entry 35's place.

## Problems with this brief or the scripts

- **Rule 2 (M-6) reads differently from the digests' practice for a first-party app's tasks.** Rule 2 gives a line to every thing a description names. The Editions digest's rule 16 and E81, the changelog digest's rule 14, and SH-34's rule 7 as later batches read it, give none to the platform's thing an app's feature acts on. I followed the digests, which are the coordinator's rulings on this very case. B-extent doesn't settle it. Each line names R28.2.
- **`earlier` reports a port's name as a key.** 'name input' is the input port's name, and it matches 51 unrelated earlier lines on entries 4 to 14 (SH-101's and others). A port's name is no key.
- **The checker's first-lead NOTE fires on words any task can hold** ('status', 'on hold', 'failed'). It is harmless.
- **`show` drops the Shop task's id.** It is cited from the source instead.

## The coordinator's check

Measured: 15.9 million tokens over 79 requests, about 122,000 an entry. The checker prints no problem.
- **Kept:** R28.1 and R28.3 to R28.6, every line on CM-AUT-001 `own-service`, CM-SUP-001 `own-service` (the Shop app provides its own reviews, the Editions digest's rule 16) and CM-NTF-002 `own-service` (Flow sends the staff email itself, rule 16). SH-35's post on the same action now takes CM-NTF-002 `own-service` as well, a line added at the end of `placements-SH-35.tsv`.
- **R28.2, amended:** the record a task acts on takes no `own-service` line, since Flow doesn't provide it (rule 16; the changelog digest's rule 14). Where the record's capability holds nothing on Shopify, the task takes a `shows` line on it, since it shows the platform has the record (B-extent's `shows`; the brief's rule 2). So three lines are added: order tags on CM-ORD-011 (Add order tags, Remove order tags) and the order note on CM-ORD-013 (Update order note). A draft order's tags and note stay with the draft order. The other leads the checker names (CM-ORD-003, CM-OPS-004, CM-API-010, CM-DVT-006) are words only. CM-ORD-008's invoices stay a lead.
- **R28.6, for SH-29:** a task listed on the held store with `badgeType: LIMITED_RELEASE` is offered on that store, so it is `core`, 'limited release' its quality; a release the held stores lack is `shows`.
