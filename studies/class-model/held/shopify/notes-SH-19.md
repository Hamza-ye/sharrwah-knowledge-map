# SH-19: Shopify's `admin-router-changes`, 81 entries (notes)

The batch is the repository's derived table of what changed between the two held versions of the admin's router: `derived/admin-router-changes/router-577b0ff35365..router-dd413330f40a.jsonl` in observed-sh at `e38dc17e3`, the version of 2026-09-29 (`structures/shopify/admin-router/`) against that of 2026-10-07 (`structures/shopify/admin-router-versions/router-dd413330f40a/`). Each entry is one route: 11 added, 1 removed, 69 changed (`structures/REGISTER.tsv`, row `shopify/admin-router-versions`). The rules are the router's digest (`held/rules/admin-router.md`, its section 6 included) and the rulings' last section.

## 1. Who placed what

- **The script placed 50 entries, in 58 lines** (`method/held_router_changes.py`, the coordinator's run): each change of a route the router batches placed, its rendered eligibility the same before and after, takes the route's own lines; the removed `editor:labs` takes them as `shows`. They are the file's first 58 lines, kept as the coordinator left them.
- **I placed the other 31, in 34 lines**, appended after them: 29 on capabilities, 2 `new` (`new:Finance`), none `out`.

## 2. How I placed the 31

Every entry's text holds only the route's id, the kind of change and the rendered eligibility (R19.1), so each line's `terms` is the route's id, and its reading gives what the derived table's `before` and `after` state. For a changed route, the rest of the route is read in the router's items at its id.

### 2.1 Fifteen routes the concern map read

Each takes the cell that holds its concern's statement in the model (`merged/evidence.tsv`, key `<concern>/decides/<statement>`; the cells read with `held_entries.py cells`), its support by the digest's rules (R19.3), its scope by its own gates after the change:

| Entry | Route | Statement | Line |
| --- | --- | --- | --- |
| SH-E-9c9b1e3b | `analytics:reports:promise_summary` | SH-C-145 and SH-C-125, SH-S-5033 | CM-ANL-002 and CM-SHP-018, `shows`, `beta 9ed93472 and not beta 3f9554f3` |
| SH-E-7736e5e9 | `inactive-account-billing-invoice:list` | SH-C-016, SH-S-5072 | CM-PLN-004 `core` |
| SH-E-57361a91 | `billing:list` | SH-C-016, SH-S-5087 | CM-PLN-004 `core` |
| SH-E-ff99fafa | `issued:invoice:list` | SH-C-016, SH-S-5088 | CM-PLN-004 `core` |
| SH-E-62a2db1b | `growth:integrated-campaigns` | SH-C-129, SH-S-5175 | CM-MKT-005 `core` |
| SH-E-b4697d53 | `listings:channel-mapping` | SH-C-138, SH-S-5198 | CM-CHN-004 `shows`, `beta b529fc07 and beta 715156a4` |
| SH-E-e97d50a1 | `option-definition:create` | SH-C-106, SH-S-5205 | CM-MKS-001 `core`, with CM-SHP-001 `core` (R19.3), `marketDrivenShipping` |
| SH-E-56eb37a8 | `editor` | SH-C-029, SH-S-5211 | CM-SFR-002 `shows`, `beta 4e79d5b1 and beta 2847a1c7` (R19.3) |
| SH-E-6630ce9b | `order:write-off:create` | SH-C-054, SH-S-5220 | CM-ORD-001 `shows`, `beta bfbcab91` |
| SH-E-b40d859e | `settings:organizations:details:business-details:edit` | SH-C-004, SH-S-5230 | CM-ACC-004 `core`, `CENTRAL_LEGAL_ENTITIES and centralLegalEntitiesEnabled` |
| SH-E-9320cf74 | `settings:organizations:accounts:roles:create` | SH-C-010, SH-S-5236 | CM-STF-002 `core` |
| SH-E-6572bd7e | `settings:organizations:partner-billing` | SH-C-169, SH-S-5241 | CM-PTN-004 `core`, `PARTNER and 9a01b514` (R19.3) |
| SH-E-9bf5b191 | `rollout:list` | SH-C-112, SH-S-5257 | CM-MKS-002 `core`, `rollouts.scheduledRollouts` |
| SH-E-2ce9d663 | `rollout:create` | SH-C-112, SH-S-5258 | CM-MKS-002 `core`, `rollouts.scheduledRollouts` |
| SH-E-358a9c20 | `shippingLabel:index` | SH-C-116, SH-S-5265 | CM-SHP-002 `core` |

What changed, from the derived table: an own eligibility for three (`promise_summary` gains the exclusion of beta 3f9554f3; `editor` the staff permission EDIT_THEME_CODE; `order:write-off:create` the staff permission WRITE_OFF_ORDERS and the context activities), a rebuild for eight (R19.2), and for the rest the icon `delivery` (`option-definition:create`), an intent's input and context (`business-details:edit`), a path from `:id` to `:handle` with its intent's channel handle (`listings:channel-mapping`), and the loss of a path, which makes `settings:organizations:partner-billing` a pathless wrapper whose children's paths begin with `partner-billing`. No intent of these routes has an Intents API page (`derived/intents.tsv`, its `docs` column empty), so each is named in `reading` (the digest's rule 19).

### 2.2 Two placed routes whose rendered eligibility differs

`growth:channels` (SH-E-395e7182) and `growth:campaigns-report` (SH-E-422f5e9a) take their routes' lines, SH-13's lines 15 and 16, CM-MKT-008 `core`. What the later version adds is an `eligibilityMatch`: with beta e1868734, a redirect to `/growth/attribution`, the route `growth:attribution` that it also adds. The entries' 'eligibility after' is that condition, and an `eligibilityMatch` gates nothing (the digest's rule 26). So the routes' own gate, the staff permission REPORTS alone, is the same before and after, and the lines take no scope (R19.1). The beta is false in both held stores.

`growth:channels` also has a concern-map row (SH-C-129, citing SH-S-5032), but the model holds SH-S-5032 only as `analytics:reports:eligibility`'s, on CM-ANL-002 through SH-C-145. So it is counted here, as the coordinator's message counts it, with its router line.

### 2.3 Fourteen routes no router entry holds

Eleven are added. Three (`money`, `finance:dashboard` and `route:home`) are in the held version, but no `admin-router` entry holds them (`entries.tsv`).

- **Added:**
  - `analytics:reports:payments_summary`: CM-ANL-002 `shows`, `beta 1809038c`, as its sibling 'Shop Promise summary' and SH-8's 'Finances summary' are Reports' (R19.4).
  - `growth:attribution`: CM-MKT-008 `shows`, `beta e1868734`. It is the Attribution dashboard that the two reports above redirect to under the same beta.
  - `market:managed:biggest`: CM-MKS-003 `core`, a loader-only Managed Markets route, read as SH-14's lines 13 to 17 read its siblings.
  - `markets:market:pick` and `markets:market:pick-changes`: CM-MKS-001 `shows`, `beta b807da6c`. Both are modal pickers with private intents that no Intents API page holds.
  - `order:mobile:order-cancel-shipping-label`: CM-SHP-002 and CM-SRF-001 `core`, its twin `order:mobile:cancel-shipping-label`'s two lines (SH-15's lines 58 and 59). Both are 'Void shipping label', native clients only.
  - The partner billing card routes, `settings:organizations:partner-billing:list:credit-card` and `…:card-complete-authentication`, and their second-tree twins under `organization-settings:organizations:partner-billing`: CM-PTN-004 `core`. They are the payment methods a partner organization pays Shopify's bills with, as SH-15's line 108 placed Payment methods (R15.2 for the twins).
  - `payments:settings:shopify-payments:konbini-support-settings`: CM-PAY-017 `core`. Konbini is one of 'popular Japanese payment methods' in the Summer 2024 Edition (`structures/shopify/editions/www.shopify.com_editions_summer2024/items.jsonl`, position 523), which SH-57 placed on CM-PAY-017 for Japan. The route has no gate on the store, so it takes no scope (R18.3).
- **Changed:**
  - `money`: `new:Finance` `shows`, `beta 8c7faba1 and financesOverview and US`. The later version adds regions US to its gate.
  - `finance:dashboard`: `new:Finance` `core`, `financesOverview`. Its beta d40a1c38 alternative, a "next" Finance home, is dropped.
  - `route:home`: CM-ANL-003 `core`, as SH-2's lines 23 and 75 place the navigation's Home. Only its action's module is renamed.

## 3. Rules I followed that the digest and the rulings don't state, for the coordinator to check

- **R19.1. The rendered eligibility is the `eligibilityMatch`'s, and the derived table governs.**
  - What the entries render: their 'eligibility before' and 'eligibility after' hold only the conditions of the route's `eligibilityMatch` alternatives, never its own `eligibility`. So a route whose own gate changed renders `[]` and `[]`, as `promise_summary`, `money`, `editor` and `order:write-off:create` do. An added route's own gate renders `[]` too, as `payments_summary`'s beta 1809038c does.
  - What I read instead: the derived table's `before` and `after`. The line's scope is the route's own gates on the store after the change. A condition that only the rendering shows is an `eligibilityMatch`'s, which gates nothing (the digest's rule 26). The route then keeps its line and its own scope, and the change is named in `reading`.
  - How this reads your message: I took "its scope by the eligibility after" (the two routes of 2.2) as the route's own eligibility after. That is no scope for both, not `beta e1868734`. Under that beta the two routes only redirect, so scoping their pages by it would invert the condition.
  - The script's 50: among them only `order:write-offs:reverse` (SH-E-74c74aee) has an own-eligibility change the rendering hides. It gains the staff permission WRITE_OFF_ORDERS, a gate on the user, so its scope `beta bfbcab91` stands.
- **R19.2. A rebuild is no change of the route.** Some records differ only in the file names and dependency lists inside an `eligibilityMatch`'s expressions, or in a module's renamed file (`route:home`'s `action-…js` to `Home-action-…js`). That is a reading of the two records, made after setting the hashed names aside. Such a route takes its line unchanged, and the reading names the rebuild. This covers nine of the 31: `route:home`, and eight concern-map routes, `inactive-account-billing-invoice:list`, `billing:list`, `issued:invoice:list`, `growth:integrated-campaigns`, `settings:organizations:accounts:roles:create`, `rollout:list`, `rollout:create` and `shippingLabel:index`.
- **R19.3. A concern-map route takes the concern's capability, its support by the digest.**
  - **Capability:** the route takes each cell that holds its statement and whose thing the route's own words name.
    - `promise_summary` takes both: Reports, and the Shop Promise's CM-SHP-018, whose note cites SH-S-5033.
    - `partner-billing` takes CM-PTN-004 alone. SH-S-5241's row on CM-PTN-003 stands for the partner-payouts routes of the same eligibility, which this route's words don't name.
  - **Support:** it follows the digest's rules. `editor`'s own betas 4e79d5b1 and 2847a1c7 are false in both held stores, so rule 29 gives `shows`, as the script's line for the removed `editor:labs` under the same betas has it. The concern map's row (SH-C-029/decides/SH-S-5211) reads `core`. It is for you to read again at the amendment, as the ruling after SH-8 has SH-S-5044.
  - **A second line:** a route whose title names another capability's thing, as its twin's line does, takes that line too. `option-definition:create`, 'Add shipping option', takes CM-SHP-001 beside the concern's CM-MKS-001, as SH-14's line 18 placed its twin `option-definition:update` and the script that twin's change (SH-E-53bd3e0e). Drop it if a concern-map route is to take the concern's line alone.
- **R19.4. A route that only the later version holds is placed from the derived table's `after`, which holds it whole.**
  - **How it is placed:** as the digest places a route. Its words name its capability in the digest's order (rule 2), its own gates are its scope (rule 22), and where a held twin exists it takes the twin's line. What its words leave open goes in `reading`: what 'biggest' names, and which payments the summary sums.
  - **Its ancestors' gates:** each reading names the route's parent, and I didn't look up ancestors' gates (rule 23). `method/held_router_gates.py` reads the held version, which lacks these routes, so it may need the later version for the 11 added routes. There, `money`'s gate also holds US, and the card routes are reached under `settings:organizations:partner-billing` or its second-tree twin, gated `PARTNER and 9a01b514` (this batch's SH-E-6572bd7e and the script's SH-E-e5c5e83d). Their ids hold that ancestor's id as a prefix, so a check that skips "an ancestor whose id the reading holds" may skip it.

## 4. New things

- **`new:Finance`**, SH-E-489462ac (`money`, `shows`) and SH-E-63a8e0ae (`finance:dashboard`, titled Finance, `core`). It is SH-12's and SH-39's `new:Finance` (`notes-SH-12.md`, section 3), whose lines 94 and 95 placed `money:home` ('Money') and `finance:transaction`.
  - **Its place of its own:** the router's section Finances. Its routes are `money`, the section's route over the Money dashboard, and `finance`, over the page titled Finance that the Help Center links as Finance (SH-S-6331).
  - **Proposed** as SH-12 did: domain C, area PAY, no parent, a container over CM-PAY-005 and CM-PAY-023 to CM-PAY-027. The other reading is CM-PAY-023's place (the check after SH-12).
  - **Its names:** English only, Finance and Money (the admin isn't held in Arabic, the digest's rule 40).
  - **What this batch adds:** the later version gates `money` on regions US too, beside beta 8c7faba1 and financesOverview. It also drops `finance:dashboard`'s beta d40a1c38 alternative home, a beta that neither held store lists.
  - **Terms searched:** 'Finance; Finances; financial account; finances overview; Money'. They found the money products' own capabilities (CM-PAY-003, CM-PAY-005, CM-PAY-009, CM-PAY-016, CM-PAY-023 to CM-PAY-028, CM-TAX-009, CM-APP-003, CM-PLN-006, CM-LOY-001, CM-RET-001), none of them the section itself.

## 5. Entries I couldn't tell, and what would settle each

- **`market:managed:biggest`** (SH-E-c699983c): what 'biggest' names, and whether its loader sends the merchant on. It is placed `core` by rule 11. A visit to `markets/managed/biggest/…` on a store with Managed Markets, under the later router, would settle it.
- **`analytics:reports:payments_summary`** (SH-E-6a04d241): which payments the report sums, the payment service's (CM-PAY-002) or all of the store's. It is on CM-ANL-002 alone, as 'Finances summary' is. The page, on a store with beta 1809038c, would settle it.
- **`markets:market:pick-changes`** (SH-E-64d94d93): its intent's input names a MarketCatalog customization, so it might also be a catalog's thing (CM-B2B-003 holds `catalog:list`, the script's SH-E-1a90b298). It is kept on CM-MKS-001 because its title and id name markets, and the intent's schema is the route's data (the digest's rule 41).
- **`option-definition:create`'s CM-SHP-001 line, and `editor`'s `shows`:** see R19.3.

## 6. A structure whose items and sources disagree

`admin-router-changes`' entries render `eligibility before` and `eligibility after` from the `eligibilityMatch` alone (R19.1). Ten of my 31 differ from the derived table so:
- four changed routes' own gates: `promise_summary`, `money`, `editor` and `order:write-off:create`;
- six added routes' own gates: `payments_summary`, `growth:attribution`, the two pickers, the void label's client and permission, and Konbini's permission. The other five added routes state no eligibility of their own, so their `[]` is right.

The source governs, and each line's reading names what it states. `show --meta` prints nothing for this structure, which is a derived table with no `meta.json`. I read its register row and the derived table instead.

## 7. What held files state that no entry holds (for the second stage)

- **Konbini at checkout:** `structures/shopify/open-source/theme-liquid-docs/main@f7a1b07e9f9c/files/theme-liquid-docs-f7a1b07e9f9c5ef051030aa07ce1dd83b9efa530/data/shopify_system_translations.json` holds what checkout shows for Konbini.
  - Line 1107 holds 'shopify.checkout.payment.konbini_label'.
  - Lines 1149 to 1159 hold the `lpm.konbini.voucher` labels: its outlets (FamilyMart, Lawson, Ministop, Seicomart, 7-Eleven), its payment and confirmation codes, and the steps at a FamilyMart.

  This is a lead for CM-PAY-017's cell: how a buyer pays a Konbini voucher.
- **Partner billing:** `docs/GAPS.md`, line 22, records that the partner billing routes added by 2026-10-07 answered 'There's no page at this address' to the partner signed in (run `20261008T053951Z-journey-partner-billing`, whose steps 1 to 3 opened `settings/partner-billing` and its `payment-methods`). The router asks the organization feature PARTNER and the flag 9a01b514. This is a lead for CM-PTN-004, whose cell holds only the route and its eligibility.

## 8. Problems with the brief or the scripts

- **`method/held_router_changes.py` has no `--help`.** Given one, it ran and printed '58 lines for 50 changes; 31 changes left for an agent'. The file's 58 lines are as the coordinator left them: the checker counted 50 entries placed before I added mine. Running it again on this batch may rewrite the file without my 34 lines. That is an assumption: I didn't read its code.
- **The checker seems not to search the derived table for quotes.** It flagged the added routes' titles 'Pick markets', 'Pick market changes' and 'Void shipping label' as found nowhere held, though they stand in the derived table's lines 31, 30 and 36. Its NOTE cleared once each reading named that file. Other titles quoted from it passed, presumably because run pages also hold them.
- **The message's three kinds:** they count `growth:channels` among the placed routes (2.2) rather than the concern-map routes, which is how I placed it.
- **The coordinator's lead count:** `money`, `finance:dashboard` and `route:home` are in the held version. What they lack is an `admin-router` entry (2.3).

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 81 of 81 entries, no problem and no `CHANGES`. `method/held_router_changes.py` placed 50 by script and the agent the other 31. With this batch the router's changes are placed whole.
- **R19.1 corrects the script's premise, and the script's lines still stand.** An entry's 'eligibility before/after' renders only the route's `eligibilityMatch` conditions, not its own `eligibility`. The agent read the derived table: of the script's 50, only `order:write-offs:reverse` has a change of its own, a staff permission, and its scope stands. The script's docstring now says it compares the rendered eligibility, and `--help` prints the usage instead of running.
- **The rules R19.2 to R19.4 stand.**
  - **R19.3:** `editor` is `shows`, its own betas false on both held stores (rule 29). The concern map's `core` (SH-S-5211) is already listed for Shopify's amendment.
  - **R19.4:** the gates script can't name the ancestors' gates of the 11 added routes, which the held router version doesn't hold. Their readings name the routes they sit under; the cards' ancestor's gate, `PARTNER and 9a01b514`, is the one partner billing's lines carry (R15.2).
- **The new thing** Finance takes two more lines: `money`, `shows` under its false beta; the Finance dashboard, `core`.
- **Cost:** 9.4 million tokens over 55 requests for the agent's 31 entries, about 303,000 each; with the script's 50, about 116,000 an entry for the batch. The context reached about 289,000 tokens.
