# SH-97: Shopify's `pos-settings` (last 7), `return-reasons` (9), `settings-panel` (23) and `shop-request-details` (first 41) (notes)

**The batch:** platform `shopify`, batch `SH-97`, effort `high`, 80 entries in 77 lines, at observed-sh `e38dc17e3`.
- `pos-settings`: the Screen lock page's last items (`structures/shopify/pos-settings/fake-demo-sharrwah/items.jsonl`, lines 646 to 652; run `20261005T021253Z-android-pos-walk`, step 34).
- `return-reasons`: the Return reason select of the admin's Return and exchange form, for order #1001's item The Complete Snowboard on capture-plus (`structures/shopify/return-reasons/capture-plus@the-complete-snowboard/`, lines 2 to 10; run `20261005T130823Z-journey-order-return-label`, step 7).
- `settings-panel`: the Settings panel of demo-fake-dev-store, its organization menu (nav1) and its store menu (nav2) (run `20260930T103225Z-sweep-dev`, step 363).
- `shop-request-details`: fields of the admin's `RequestDetails` answer about the shop, each standing for every store whose answers state the same value. SH-98 holds the rest of this structure.

**Count by placement:** 72 entries on a capability, 1 `new`, 7 `out`.

**What I read:** the brief; the evidence map; B-extent's "Cells and evidence" and "Conventions from the dry run"; the rulings, their last section; observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv` rows 6, 74, 81 and 131, and `index/ledger-summary.tsv`. No `index/ledger/` file enumerates these four structures. I also read `selection.tsv`'s rows 50 to 53; each structure's `meta.json`, items and source; `notes-SH-96.md`; `amendment-notes.md`; H25 in `notes-SH-33.md`; and the router digest (`held/rules/admin-router.md`).

## `pos-settings`: SH-96's lines, kept

I took SH-96's rule 8, as its coordinator's check kept it.
- '5 minutes' and '10 minutes' (radio button and label, grouped) take CM-POS-001 `core`, with `lock after inactivity: 5 minutes` and `10 minutes` as their quality.
- 'Lock screen after sale' (`LockSale`, off on this device) and its label take CM-POS-001 `core`.
- Its description takes its own line (rule 10).

`earlier` found no line on these keys. The checker notes CM-ORD-003 as the first lead of lines 4 and 5. It matched only 'completed': the setting locks the POS screen once a sale's order is completed, and it names no order status.

## `return-reasons`: the list's line, as H25

The concern map read this list whole (SH-S-2860, 'from line 1 (one option per line; first option quoted)'). Its cell's line for the list is CM-RET-003 `core`, from `SH-I-2096`, 'value list Return reasons (10 options)'. So each of the nine reasons after Too long takes that line:
- CM-RET-003 `core`;
- the label as its term, the value (`gid://shopify/ReturnReasonDefinition/<n>`) in `reading`;
- no filler and no scope, as H25 placed the adjustment reasons. The list is one product's on one store, as captured, and the source states no condition for it.

Too short, Color and Flex come before the reasons that begin with Changed my mind. I read them as this product's own reasons, as the changelog's suggested return reasons specific to the product returned (SH-E-cd206824) describe them. This is a reading; the list itself doesn't say so. As `amendment-notes.md` has it, these lines repeat the model's own reading of the list.

## `settings-panel`: the rules I set (S97.1 to S97.5), for the coordinator to check and SH-98 to keep

- **S97.1:** a link of the Settings panel is a settings item with its own title, a place of its own (B-extent). It is `core` on the capability its title names.
  - It takes the line the model gives its twin in `admin-settings-nav` (SH-S-1481 to SH-S-1503, ibx5bt-xy's items, which the anchor parts placed), and the line the router's batches give the route it opens.
  - It has no scope: the panel is one store's, and states no condition.
  - Each line names its twin on this store in `admin-settings-nav` (SH-E-d263a68e and the others, in SH-20, which hasn't run yet). The coordinator aligns SH-20 with these lines.
- **S97.2: every thing a title names takes a line** (rule 2).
  - 'Taxes and duties' also takes CM-TAX-008, duties. That cell's note keeps Shopify's duties under the Taxes and duties settings. SH-18's line on the route took CM-TAX-001 alone.
  - A title that is one capability's own name takes that capability's one line: Shipping and delivery, Metafields and metaobjects, Customer accounts, Customer events.
- **S97.3: the anchors and sub-routes of a linked page take no line on the link,** since the link names none of them. They are placed by their own route entries (the ruling after SA-41: things a page holds in passing).
  - The cases: Organization's Business Entities (CM-ACC-004); Customer accounts' Sign in with Shop (own-service) and Multipass (CM-CUS-011); Notifications' Webhooks (CM-API-009); Payments' providers.
  - I read the ruling after SA-19 ('A second line follows the page') as being for a page whose own title names two things, as 'Taxes and duties' does.
- **S97.4: the nesting.** Users is a container, `core` on its own page's capability (CM-STF-001): Roles and Security nest under it (`parent: 1`). Roles and Security aren't kinds of users, so they take no CM-STF-001 line (M-6 refined). The two menus' own labels have no entry: 'Organization settings menu' and 'Shop settings menu' are aria-labels in `source.html`.
- **S97.5: the store's icon.** The store header's button 'Update internal icon' sits over the store's avatar, with an edit icon, beside its name and domain. It is the store's own icon setting, CM-ACC-006 `core`, as SH-41 placed the changelog's custom store icon uploaded from the Settings page (SH-E-2006da63).

**Homonyms the leads raised:**
- CM-PTN-002's Organization is the Partner Dashboard's.
- CM-APP-003's Billing is its API group.
- CM-APP-002's 'Shipping and delivery' is an App Store category.
- SH-11's CM-SFR-011 line at settings/general is a Hydrogen storefront's General.
- CM-TRU-005 leaves the privacy settings to its child CM-TRU-006, by its own reading.

## `shop-request-details`: the rules I set (S97.6 to S97.16)

- **S97.6: what an entry is.** One field of `data.shop.plan`, `resourceLimits`, `entitlements` or `features`, with one value. It stands for every store whose answers state that value: its labels. Each store's plan is what the same answers' `plan` states, set by set (`sets.jsonl`). I printed each key's values by store, set and plan with a script of my own; the readings name the plans.
- **S97.7: scope.** The scope is the stores of the entry's labels, `;`-separated, as the model scopes a store feature (SH-S-5292, 'its stores as scope'). Their plans go in `reading`.
- **S97.8: support by value.** This follows the coordinator's message for this batch, the brief's rule for a store's flag stated by its value, and the router digest's rule 29.
  - A flag or entitlement whose value is true, or a value that grants it (`FULL`, `enabled: true`, a plan's name), supports `core` on its feature's capability.
  - `false`, or `null`, on the stores held supports `shows`.
  - The value goes in `reading`, never in quality. A rate the platform sets for the store, `transactionRate`, is the one exception: it is a quality, of the fee kind `qualities.tsv` records.
- **S97.9: terms.** The key, as Zid's feature flags take theirs. For a plan's name or displayName, the value too: it is the platform's name for the plan (`unlimited`, 'Advanced App Development').
- **S97.10: the plan section is the store's plan,** CM-PLN-001's, placed as the platform's offer, as the brief places a subscription's add-on.
  - Its name is the platform's handle: `unlimited`, displayed Advanced; `professional`, Grow; `shopify_plus`, Plus; `affiliate`, the Custom plan. These are readings, from the same answers' displayNames.
  - `trial` and `trialPeriod` are the store's trial on its plan, as SH-1 placed the trial stores' Trial indicator (SH-E-21c1d264). The dates are the store's own and go in `reading`.
  - `shopifyPlus` `true` is `core`; `false` is `shows`.
- **S97.11: development stores.** `partnerDevelopment: true` states the store a partner's development store, the platform's own kind of store: CM-DVT-004 `core`. `false` is `shows`.
  - A plan named '… App Development' takes a second line on CM-DVT-004, a reading: 'App Development' names the store's use.
  - The entitlement `appDevelopment.cliAppDev` holds on exactly the stores on those plans. It takes CM-DVT-002, the CLI, and CM-DVT-004.
  - 'App Development' here isn't CM-APP-009's App development, the admin's custom apps: a homonym.
- **S97.12: out.**
  - `__typename`, the GraphQL type name of an object (ShopPlan, ShopResourceLimits, EntitlementsType, ShopFeatures), is the answer's own schema marker, the software's bookkeeping.
  - A section's row with key and value `null` is the build's mark for a section the answer doesn't hold. It states nothing.
- **S97.13: a flag of the store's own selling that turns** (`sellsSubscriptions`, `multiCurrencyGatewayEnabled`: `false` in each development store's first set, `true` later) is read as a flag, `core` where true, with the turn in `reading`. `multiCurrencyGatewayEnabled` names the gateway too, so it takes CM-PAY-001 beside CM-MKS-006 (rule 2).
- **S97.14: an entitlement over a capability that third parties do through the platform takes that capability's support** (the ruling after SA-44: the thing a tool does sets the support). So `checkoutExtensibility` takes CM-CHK-004 `extension-point`.
- **S97.15: a flag no capability holds is `new:<name>`, `shows`,** with no place of its own (the brief's rule 2).
- **S97.16: `upsell.shopifyApp` names the Shopify app,** the mobile app for managing the store (CM-SRF-001), read by the Help Center's section 'Using the Shopify app for iPhone and Android' (`help-center/help.shopify.com@en-ar/outline.md`, line 898). It is `core`, as the admin's own client (the router digest's first-party table keeps POS so). CM-MKT-021's upsell is offers to buyers: a homonym.

## The new thing

**`new:Review modal`.**
- **Entry:** SH-E-f5d1ecb7, `entitlements.ignoreReviewModalCooldown: true` on the seven development stores, `shows`. It is `false` on the trial and Advanced stores (the concern map's SH-I-2521, unplaced).
- **A place of its own:** none. It is one entitlement, and no held statement here says what the modal asks or who shows it.
- **Proposed:** domain F, area APP, parent CM-APP-002, a reading. The alternative, if the modal is Shopify's own request for the merchant's review, is domain A.
- **Names:** English only, the key. The admin isn't held in Arabic (`docs/GAPS.md`).
- **Searched:** `caps --terms` for review modal, app review, app reviews, review, reviews, rating and ratings. The nearest are CM-APP-002 (the platform's review of the apps it lists, another sense) and CM-SUP-001 and CM-SUP-002 (buyers' reviews).

## The checker's lines

- **CHANGES: CM-DVT-004@shopify gains `core`,** by lines 47, 50, 55, 68 and 77. I read each again against the answers:
  - **Line 50** (SH-E-f166680a, `partnerDevelopment: true` on seven stores) is the decisive one. It is the platform's own API field for its own kind of store. The concern map reads RequestDetails' true values as `core` the same way (`rbacEnabled` on CM-STF-002, `hasOrgSettings` on CM-ACC-003), and the model's own derived scopes already call these stores 'development store'.
  - **Lines 47, 68 and 77** ('Advanced', 'Shopify Plus' and 'Grow App Development') and **line 55** (`appDevelopment.cliAppDev`) are readings, marked as such. If the coordinator drops them, line 50 still gives the cell `core`.
  - The cell's reading said no place, plan line or definition of a development store is held. That stays true: these are API values, not a place of its own.
- **NOTE line 67:** core on a product named with the platform's brand. 'Shopify Plus App Development' is a plan of the platform, not a separate product: CM-PLN-001 `core`, as the Plus tier is.
- **NOTE lines 4 and 5** (CM-ORD-003) **and line 23** (CM-PAY-032): the leads matched only words ('completed'; 'link', 'payment'). The readings say so.
- **NOTE line 16:** Users is a container (S97.4).
- **NEW:** Review modal, 1 line.

## Entries I couldn't tell, and what would settle each

1. **Taxes and duties' CM-TAX-008 line** (SH-E-8b7017d3), against SH-18's CM-TAX-001 alone on the same route. Neither changes a cell. Settled by whether the coordinator reads CM-TAX-001's own name, 'Shopify Taxes and duties', as covering the duties the title names.
2. **The linked pages' anchors** (S97.3). If a link takes every line of the page it opens (the ruling after SA-19, read widely), these lines are added:
   - Organization takes CM-ACC-004 `core`;
   - Customer accounts takes CM-CUS-011 `core`, and `own-service` on CM-CUS-010 for Sign in with Shop.

   No cell changes either way.
3. **`checkoutExtensibility` FULL** (SH-E-8b622b73): CM-CHK-004 `extension-point`, or CM-CHK-003 `core`, whose plan row Checkout customization reads Limited on Basic, Grow and Advanced and Full on Plus, the same values. Placed on CM-CHK-004, the key's own words ('Shopify Checkout Extensibility' is its term). If the coordinator reads the entitlement as the platform's own and gives it `core` there, CM-CHK-004's cell gains `core`.
4. **`partialOrderPayments`** (SH-E-e11d7abc): CM-PAY-020, where the help page on collecting and recording partial payments stands (SH-E-92a8c895). The other reading is CM-PAY-008, where the changelog's partial payments and deposits stand (SH-E-86c0c5a9). Both are `core`; the coordinator aligns them.
5. **The review modal** (the new thing): settled by a held statement saying what the modal is. It is a lead for the second stage.
6. **`upsell.shopifyApp`**: the admin's upsell of the Shopify app, or an upsell shown in it. Either way the thing it names is the Shopify app, CM-SRF-001.
7. **The four `__typename` entries:** `out`. The alternative is CM-PLN-001 `core` for ShopPlan, the public Admin API object's name, which changes nothing.
8. **The trial lines' term 'trial'.** The brief has "A store's state (suspended, trial) is its scope, never a term". Here the trial is the entry's own thing, as it was for SH-1's 'Trial' indicator, so I kept it as the term and put the stores in `scope`.
9. **`sellsSubscriptions` and `multiCurrencyGatewayEnabled`** turn true between a store's answers. They may reflect the store's own data, such as an app installed or a gateway set up, which the answers don't state. If the coordinator reads them as a condition on the store's own data, their lines become `shows`. No cell changes either way.
10. **The duties rate as a quality** (S97.8). If a store's value is never a quality, the two rates move to `reading`.

## Structures whose items and sources disagree

- **`settings-panel`:** each menu's source holds a header that the items leave out. The extractor reads `<a>` and `<button>`, not `s-internal-link`.
  - nav1: the organization's name 'My Store' (an `h3`) and its link '2 stores' (`s-internal-link` to settings/organization-details#stores).
  - nav2: the store's name 'demo fake dev store' and its domain link 'demo-fake-dev-store.myshopify.com' (`s-internal-link` to settings/domains).

  Both are one organization's or store's own data, so no cell loses a thing.
- **`shop-request-details`:** the sets of seven items have rows with key and value `null` for plan, resourceLimits and entitlements. Their answers hold no such keys (as capture-advanced's set 2, `raw/runs/20261002T003931Z-sweep-capture-advanced/answers/admin.shopify.com/RequestDetails/25a659e974aae7e8bf544df2a653f0d0be2c3a6733ed194ada8eed9c43d67205.json`). The source governs: the rows state nothing (S97.12).
- **`show`** prints a structure's labels cut with '…' even at `--width 4000`. I read this structure's labels in `entries.tsv`.

## What the sources state that no entry holds (for the second stage)

- **The return form** (`raw/runs/20261005T130823Z-journey-order-return-label/steps/007.text.txt`, lines 47 to 60):
  - 'Exchange items', with 'Items to be sent to the customer. Items will not be reserved until you process the return.';
  - 'Return shipping options': 'Upload a return label', 'Use return label URL instead', 'Tracking number', 'Shipping carrier' and 'No shipping required'.

  These are leads for CM-RET-003's exchanges and return shipments.
- **The answers' `data.shop` beyond the four sections** (the same answer file as above): `lastActivePriceLookupKey: unlimited_app_development` names the development store's price key, a lead for CM-DVT-004 and CM-PLN-001. The same answers hold `billingAddress.countryCodeV2: YE`, `unifiedAdminEnabled` and `shopifyEmployeeSession`.
- **The trial's length:** every held trial store's `trialPeriod` spans three days (2jiwxs-gr, ctcbwa-r1, fake-demo-sharrwah, ibx5bt-xy, ts15uk-ug, zyd38b-ze). This is a reading of the dates, and a lead for CM-PLN-001's trial terms beside the pricing pages' trial.
- **The duties rates:** the answers' `transactionRate` is 0.0085 on the three Plus stores and 0.015 on the others. The pricing pages' quality reads 0.85% with Shopify Payments and 1.5% without (SH-E-5ca29a8c). Which condition the answers' rates follow, plan or payments, isn't stated.

## Problems with this brief or the script

- **`earlier` doesn't find a twin in another structure.** The settings-panel links are the twins of `admin-settings-nav`'s items on the same store (same title and address). I found them by grepping `entries.tsv`. Matching a link's `href` against a nav item's `url` would print them.
- **The checker's brand note (line 67)** reads a plan named for Shopify Plus as a product. A plan name could be exempted.
- **No rule of the brief read differently from B-extent.md here.**

## The coordinator's check

Measured: 22.0 million tokens over 103 requests, about 275,000 an entry. The checker prints no problem.
- **Kept:** S97.1 to S97.16, which SH-98 keeps for the rest of `shop-request-details`, and the one `CHANGES` line, CM-DVT-004 `core`, which line 50 settles alone. The rule-4 `NOTE` on line 67 names a plan of the platform, so `core` stands.
- **Taxes and duties:** the link's second line, CM-TAX-008, stands by S97.2. SH-18's route keeps CM-TAX-001 alone, since its own sub-route `settings/taxes/duties` carries CM-TAX-008 (SH-18:81).
- **`checkoutExtensibility`:** CM-CHK-004 `extension-point` stands; CM-CHK-004's definition names Checkout Extensibility, apps' blocks in the checkout.
- **`partialOrderPayments` and the review modal:** kept as placed, and both go to `amendment-notes.md`: partial payments stand on two capabilities across batches, and no held statement says what the review modal asks (a search of observed-sh found none).
- **SH-20's `admin-settings-nav`:** its entries on demo-fake-dev-store are this batch's twins. SH-20 was running when this batch reported, and was told to take these lines.
