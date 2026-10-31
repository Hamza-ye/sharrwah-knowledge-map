# SH-9: Shopify's admin router, 85 entries of Batches and Billing (notes)

**What this batch is.** The second held-pass batch on `admin-router`, after SH-8. Its 85 entries are the manifest's items at lines 164 to 280 of `structures/shopify/admin-router/items.jsonl` (observed-sh at `e38dc17e3`), less the routes the concern map already cites. They come from two sections: Batches (2) and Billing (83). The Billing routes fall in six groups: the app charge approval's steps, the inactive store's pages (`access_account/…`), the store pending termination's pages (`account_review/…`), Settings > Plan (`settings/plan/*`), the subscribe pages (`settings/subscribe/…`) and Settings > Billing (`settings/billing/…`).

- **Entries:** 85. 84 are placed on capabilities, 1 also takes a `new` line (SH-E-e548d845), and 1 is `out` (SH-E-ca7a8ac4).
- **Lines:** 99, since 13 entries take two lines and one takes three. By support: 93 `core` (one of them the `new` line), 5 `shows` (the redirects, section 2) and the `out` line.
- **The checker's last run:** no problem, no `CHANGES` line, one `NEW` line (Plus trial). Every cell the lines touch already holds `core`, and the 5 `shows` lines change no placement.
- **`held_entries.py earlier`** printed no earlier line for any key of the batch.
- **No entry of the batch carries an `intent`.**

**What I read:**
- the brief, SH-8's notes and placements, and `review-H-rulings.md`;
- B-extent.md's "Cells and evidence" and "Conventions from the dry run";
- the evidence map;
- observed-sh's `README.md`, `docs/READING.md`, `docs/GAPS.md`, `structures/README.md`, `REGISTER.tsv`'s two router rows, `index/ledger-summary.tsv` and `index/ledger/admin-route.tsv` (each route's joined path and visits);
- the structure's `meta.json`, `items.jsonl` (lines 160 to 282) and `source.jsonl` for six routes;
- `structures/shopify/admin-betas/` (both held stores), for beta 7aca6635;
- the run steps the ledger joins to the routes, listed in sections 4 and 6;
- the concern map's statements SH-S-5062 to SH-S-5108, SH-S-5224, SH-S-7134 and SH-S-7135 (`class_slice.py key`);
- the cells of CM-PLN-001 to 007, CM-ONB-001, CM-ONB-002, CM-ACC-001, CM-ACC-006, CM-APP-003, CM-SHP-010, CM-TAX-003, CM-TAX-009, CM-POS-001, CM-PAY-002, CM-PAY-005, CM-ORD-001, CM-ORD-008 and CM-SFR-003.

## 1. Lines by capability

| Capability | Lines | Entries |
| --- | --- | --- |
| CM-PLN-001, subscription plans | 34 `core`, 2 `shows` | the plan pickers, subscribe checkouts, pricing, Plus, Settings > Plan and its terms pages, the subscribe containers; second lines on the reactivate and reopen checkouts, the `pos-plan` routes and the subscription confirmation; `shows` for the legacy redirect and `subscribe:index` |
| CM-PLN-005, paying the platform's bills | 19 `core`, 1 `shows` | payment method modals, every complete-authentication route, the subscription payment steps; `shows` for `authenticate_payment` |
| CM-PLN-004, platform billing | 16 `core` | Settings > Billing (container), statement of charges, upcoming bill, billing profile, charges, a bill's fees, expense reports, invoices, billing history, credit note export, the currency and address modals |
| CM-POS-001, point of sale | 5 `core` | the five 'Try POS Pro' routes |
| CM-ONB-002, store status | 4 `core` | reactivate, reopen, Account review, and the plan's cancel modal |
| CM-PLN-002, plan term and renewal | 4 `core` | the Plus trial, promotion and renewal terms, and the self-renewal confirmation |
| CM-PAY-005, payouts | 3 `core` | the pending-termination store's payout bank account, payouts and payout details |
| CM-PLN-007, taxes on the platform's charges | 2 `core` | the two add-tax-info modals |
| CM-TAX-009, tax forms | 2 `core` | the inactive and pending-termination stores' 1099-K forms |
| CM-APP-003, CM-PAY-002, CM-ACC-001 | 1 `core` each | the charge approval with `:externalId`; the title 'Payments'; the business address after subscribing |
| CM-ORD-001, CM-SHP-010 | 1 `shows` each | the two Batches redirects, on their targets |
| new:Plus trial | 1 `core` | SH-E-e548d845 |

## 2. Rules I followed for kinds of route SH-8's rules don't cover

These are for the coordinator to align with SH-10 to SH-18. Each is a reading.

1. **A redirect whose target is a generic list.** `batches:details` (`batches/:batchId`) redirects to `/orders`, the orders list.
   - I placed it `shows` on CM-ORD-001, the target's capability, by the ruling after SH-8, although its own words name a batch (CM-SHP-010).
   - The concern map placed `batches:index`, which also redirects to `/orders` (`items.jsonl`, line 163), `core` on CM-SHP-010 (SH-S-7134). It is a case for the reading again that the ruling announces for SH-S-5044.
   - `batches:edit-workflow:redirect` redirects to a batch's edit workflow in Orders, so it is `shows` on CM-SHP-010.
2. **A component named for a redirect that shows a message.** `inactive-account-authenticate-payment:list` renders `PaymentAuthenticationRedirect`.
   - The ended-trial store saw 'Redirecting for credit card verification.' there (`derived/step-text-from-html/20261003T220553Z-sweep-ended-trial/019.html.txt`, line 4).
   - So I read its target as the bank's verification of the card that pays the bills: `shows` on CM-PLN-005 (SH-8, 2.4).
   - The concern map placed `billing:payment-auth-redirect:approval:list`, with the same component, `core` (SH-S-5064). No cell changes either way.
3. **A not-found catch-all is `out`.** `inactive-account-subscribe:not-found` (path `*`) renders `render-common.js`'s `NotFound` (`source.jsonl`). It has no title, gate or resource, and its id names only its role (SH-8, 2.9). A splat path isn't a place's own path.
4. **A beta in the route's own `eligibility`, `enabled: true` in both held stores.** `inactive-account-billing-charges:list` is gated by beta 7aca6635, `enabled: true` in `2jiwxs-gr` and `fake-demo-sharrwah`.
   - I followed the brief ('that store its `scope`'): `core`, with the scope `2jiwxs-gr;fake-demo-sharrwah` and the beta in `reading`.
   - SH-8's 2.5 also writes betas as `beta <hash>` in `scope`, so the coordinator may prefer `beta 7aca6635` there.
5. **Hashed `organizationFlags` in `eligibility`** are written as they stand: `7351e1b4` on `settings:plan:plus:downgrade` and `settings:plan:shop_plus_self_renewals:confirmation`. Both are `core`.
6. **A step or modal of one capability's page whose words name another capability's thing** takes that thing's capability alone (SH-8, 2.7). The app charge approval's `add-payment-method` and `complete_authentication` steps go on CM-PLN-005, not CM-APP-003.
   - The concern map lands their shared eligibility, SH-S-5067 (`clients: web`), in SH-C-019, CM-APP-003's concern. It names `billing:charge:approval:complete-authentication` and the two managed-pricing steps.
   - CM-APP-003's cell doesn't cite SH-S-5067. The merged `interfaces.tsv` lists it for CM-APP-003 'by landing'.
   - If the coordinator reads these steps as the charge approval's own, each takes a CM-APP-003 line too. No cell changes either way.
7. **A title that is the section's name** ('Billing' on `billing:payment-method-auth-complete:list`) says where the route is, as a group does (M-6 refined). It gives no line. The concern map placed `billing:invoice-complete-auth:list`, also titled 'Billing', on CM-PLN-005 alone.
8. **An index route's title shared with its parent** still names the route's page. 'Payments' on `pending-termination:payments:bank-account` gives a CM-PAY-002 line beside the payout bank account's CM-PAY-005, as the admin link Payments is CM-PAY-002's.
9. **Routes that render another route's page.**
   - The three `settings/plan/*/plus/…/terms` routes load `settings:plan`'s loader and component, `BillingPlan` and `Plan`.
   - `billing:charge:approval:withThemeParameters` loads its parent's.
   - Each takes the page's capability by its title, and a line for what its own path names (the terms, the trial).
10. **An anchor on the route's own capability** (`billing-upcoming-bill:list`'s 'Current billing cycle charges') goes in the route's line, in its `terms` and `reading`, not in a second line on the same capability. The ruling after SH-34 allows a second line on one capability only where the entry names another thing of it under its own condition, and this anchor has no condition of its own.
11. **The `pos-plan` routes** (`resource: pos-plan`, titled 'Try POS Pro') take CM-POS-001 for POS Pro and CM-PLN-001 for the plan the resource names. SH-S-5071's note names these four routes, and CM-PLN-001 cites SH-S-5071.
    - `inactive-account:checkout:select-plan:pos` has `resource: pos`, not `pos-plan`, so it takes CM-POS-001 alone.
    - The model keeps the POS Pro plan row (SH-S-7018) on CM-POS-001 alone.
12. **The `access_account/` and `account_review/` prefixes** give no line (SH-8, 2.3). Where a route's own words name reactivation, reopening or the account review, it takes CM-ONB-002, as the concern map's SH-S-5070 and SH-S-5079 do.

## 3. The new thing

**new:Plus trial** (SH-E-e548d845, `settings:plan:plus:trial:terms`, at `settings/plan/*/plus/trial/terms`).
- **What it is:** the terms of a trial of the Plus plan, shown on the Plan page. The route takes CM-PLN-001 for its title 'Plan' and CM-PLN-002 for the terms, as the Plus Terms page `plus/terms` is CM-PLN-002's (SH-S-7150). The trial itself is held by no capability.
- **Why `new`:** CM-PLN-001's note says 'A free trial and the inactive and pending-termination states are the ONB batch's', and no ONB capability holds a trial. CM-ONB-002 is the store's restriction, suspension, inactivity, termination, reactivation and closure.
- **Its place of its own:** the admin route above, an entry of the manifest with its own path (B-extent, "What a place of its own is"). So it is `core`. If the coordinator reads the place as the Plan page's alone, it is `shows`, with no place of its own.
- **Proposed domain, area and parent:** A, PLN, under CM-PLN-001, or a wider capability for a plan's trial.
- **Its name:** 'Plus trial', from the path. Shopify's admin is held in English only: `docs/GAPS.md` lists the admin in Arabic as not held, its scope to be decided with the founder.
- **Terms searched** (`class_slice.py caps --terms`, `search`): 'free trial; trial store; paid trial; Plus trial; trial; trial period; introductory price; trial expired; trial ended'. They found CM-PLN-001 (by its note), CM-APP-004 (an app's trial) and CM-SHP-010 (a trial store's feature value). No capability holds the trial.
- **Leads for a wider trial capability** (run steps, not placed, M-12):
  - the ended-trial store's plan picker: 'Your trial has expired. Select a plan.' and '3-month trial' on each plan (`derived/step-text-from-html/20261003T220553Z-sweep-ended-trial/008.html.txt`, lines 9, 11 and 21);
  - the plan payment page: '3-month trial', 'Introductory price 1.00 US dollars per month' (`raw/runs/20261007T115110Z-journey-unvisited-routes/steps/014.text.txt`, lines 23 and 26);
  - the inactive store's modules named for a trial: `InactiveAccountTrialExpiredReactivation`, `TrialReactivationNext` and `TrialReactivationNextPickPlan` (`items.jsonl`, lines 176, 182 and 185);
  - the router's plan names `trial`, `starter_2022_trial`, `grandfather-trial` and `paid_trial` (`items.jsonl`, line 193, `eligibilityMatch`).

## 4. Entries I couldn't tell, and what would settle each

- **SH-E-c246996b, `billing:charge:approval:withThemeParameters`.** It is placed `core` on CM-APP-003, as the charge approval page again, since its loader and component are the parent's.
  - What 'withThemeParameters' carries isn't stated. It may be a theme's charge, which would make it CM-SFR-003's: Theme fees is a billing charge category (SH-I-1354).
  - What would settle it: the page, which no run opened (needs an instance on all 13 stores).
- **SH-E-d436cf76, `settings:plan:cancel`.** It is placed on CM-ONB-002, as the store's closure, a reading of `CancelFlowModal`.
  - The alternative is CM-PLN-001, cancelling the plan as a change of plan.
  - What would settle it: the modal's text, which no run opened (computed path on all 13 stores).
- **SH-E-af59ec0e, `subscribe:address`.** Its second line is on CM-ACC-001: the Account Terms list the business address among what registration requires (SH-S-0017).
  - The page says the address unlocks 'location-specific features and apps' (`raw/runs/20261007T174307Z-sweep-staff-pos-user-administrator/steps/105.text.txt`, line 19). CM-ONB-001, the merchant's location, is the other candidate: its cell holds the location the merchant keeps current in the admin (SH-S-0038).
  - The coordinator may prefer it.
- **SH-E-115038f5, `pending-termination:payments:bank-account`.** The payout bank account (CM-PAY-005) is a reading of its id and its component `PendingTerminationBankAccount`. The visits on the paid store came from a staff user's sweep, which isn't the owner's view.
- **SH-E-d2d7e0fc and SH-E-12978a67, the `verify-bank-account` modals,** are placed on CM-PLN-005: a bank account that pays the bills. This reads their place among the billing profile's payment method modals. No run shows their text.
- **SH-E-b68b1297 and SH-E-e12269b9, `add-tax-info`,** are placed on CM-PLN-007: the Tax registration for Shopify's bills (SH-S-0279), a reading. CM-TAX-003's note names the homonym.
- **SH-E-51307435, `settings:plan:plus:promotion:terms`.** Its promotion is read as an offer on the Plus plan's price, CM-PLN-001's, with the terms on CM-PLN-002.
  - I made no new thing for the promotion, since CM-PLN-001 holds the plans' prices and its note excludes only the free trial.
  - If the coordinator makes a plan promotion a thing apart, this route is its only entry here.
- **The loader-only routes** are `core` on CM-PLN-005, and whether each shows a page isn't stated (SH-8, 2.4): SH-E-6eda712b, SH-E-0cabd831, SH-E-a8862475, SH-E-72cb9c88, SH-E-3dfc6e4e and SH-E-29bae7c9.

## 5. The checker's `NOTE` lines, answered

- **Containers.** Lines 6, 11, 13, 16, 18, 25, 56, 71, 84 and 90 are routes with children. Each is placed on the capability its title or words name, `core`, with its children named in `reading` (SH-8, 2.6). None names only a grouping.
- **Line 8: 'path plus begins 5 other entries' paths'.** This is a false match. SH-E-b1cdc806's `plus` is `access_account/checkout/select-plan/plus`. The five other paths are `settings/plan/*/plus/…`, under another parent, and the checker compares relative paths.
- **Line 49: 'path bills begins 2 other entries' paths'.** `account_review/bills` begins its sibling `account_review/bills/expense-report`, so it is a container by its path alone, and its reading says so. The second match, `access_account/bills/expense-report`, is under another parent.
- **Line 61: 'a new thing whose entry has leads'.** I read the cells of CM-PLN-001 and CM-PLN-002 before writing the new line. Neither holds a trial (section 3). CM-APP-003 and CM-PLN-004 are word leads, by `billing`, which every Billing route's `sliceName` holds.

## 6. What sources state that no entry holds, for the second stage

These are run steps the ledger joins to this batch's routes. They are not placed (M-12).
- **The billing threshold:** 'Next bill in 29 days or when your $1,280 USD threshold is reached. You have $1,280 remaining.' (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/112.html.txt`, line 123). A lead for a quality of CM-PLN-004.
- **The plan's introductory price and renewal:**
  - 'Change or cancel your plan anytime. Auto-renews Jan 2, 2027 with Basic plan ($27.00/mo) plus applicable taxes.', 'Renewal price 27.00 US dollars per month' (`raw/runs/20261007T115110Z-journey-unvisited-routes/steps/014.text.txt`, lines 21 and 24);
  - 'Get back to business for $1' and '3 months for $1/mo, and earn $8,000+ in credits' on the ended-trial store's plan picker (`…/20261003T220553Z-sweep-ended-trial/008.html.txt`, lines 4 and 5).

  Leads for CM-PLN-001, CM-PLN-002 and CM-PLN-007.
- **Credits toward the subscription:** 'Earn credits toward your Shopify subscription', 'Get 0.5% back on every sale, up to $4,500 in credits. Terms apply' (`…/20261003T220553Z-sweep-ended-trial/009.html.txt`, lines 54 and 56). No capability holds them, so they are a lead for the coordinator.
- **POS Pro against the plan's own POS features** (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/102.html.txt`, lines 76 to 92):
  - 'Unlimited POS staff with permissioning', 'Daily sales reports' and the other POS Pro lines;
  - 'Included in your plan', with 'Limited staff accounts' and the other lines of the plan's own POS features;
  - a price of '$0 USD/month per location' on that development store.

  Leads for CM-POS-001.
- **The staff account limit by plan:** 'User account limit reached. Remove users from your stores or view pricing for plans with higher limits.' (`…/20261002T003931Z-sweep-capture-advanced/099.html.txt`, line 92). It is on the organization account page where the subscribe routes landed, not on a page of this batch. A lead for CM-STF-001.
- **The expense report's filters:** 'Stores', 'Charge categories' and 'Date range' (`…/123.html.txt`, lines 124 to 128). The statement of charges is 'Last 90 days' (`…/110.html.txt`, line 121).
- **The access_account routes on active stores.** Visits from the development stores' sweeps landed on the store's home or `settings/general` (`index/ledger/admin-route.tsv`). Only the ended-trial store (`ibx5bt-xy`) and the paid store's staff sweep opened them. This agrees with CM-ONB-002, and is no gap for the model.

## 7. Homonyms

- **'checkout'** in this batch is the merchant's subscription checkout, paying Shopify for a plan. It is not the buyers' checkout (CM-CHK-*). The readings say so.
- **'promotion'** is an offer on Shopify's plan to the merchant. It is not CM-MKT-001's or CM-MKT-003's offers to buyers.
- **'bank account'** in the billing profile pays the bills (CM-PLN-005). The pending-termination store's bank account receives Shopify Payments payouts (CM-PAY-005).
- **'Tax info'** is tax for Shopify's bills (CM-PLN-007), not the store's tax registrations (CM-TAX-003).
- **'Charges'** and **'fees'** are Shopify's charges to the merchant (CM-PLN-004). They are not CM-PAY-007's payment processing fees, nor CM-APP-003's app charges, though app charges are billed among them.

## 8. This brief, B-extent.md and the scripts

- **B-extent.md:** no rule of the brief read differently from it on these entries.
- **The brief and SH-8 on betas in `eligibility`.** They differ in form ('that store its scope' against `beta <hash>`). I followed the brief (section 2, rule 4).
- **The checker's container test compares relative paths,** so a route's path matches the paths of routes under other parents (section 5, line 8).
- **`show` leaves out the modules' names,** and the readings rest on them often in this section: `CancelFlowModal`, `PaymentAuthenticationRedirect`, `POSPlan`. They are read from `items.jsonl` at each entry's locator.

## The coordinator's check (31 October 2026, after the batch)

- **No cell changes.** One new thing, Plus trial. It is decided in `held/new.tsv` with the platforms' other trials: Salla's 14-day trial, read again at its amendment, and the held run steps the notes list, toward a wider capability for a plan's trial.
- **SH-8's rules hold, and this batch's additions stand:** a redirect to a generic list, a component named for a redirect, the charge approval's steps, and the anchor on the route's own capability.
- **One line is aligned to SH-8's 2.5.** The charges route's gate is written as it stands, `beta 7aca6635`, as its scope. The two stores where it is enabled stay in `reading`.
- **Ancestors' gates:** 12 lines of 12 routes now name them in `reading`, added by `method/held_router_gates.py`.
- **Read again at Shopify's amendment:** the concern map's `core` on `batches:index` (SH-S-7134) and on the other `PaymentAuthenticationRedirect` route (SH-S-5064). Both redirect, as SH-S-5044 does.
- **The checker's false container note** (line 8, `plus`) comes from comparing relative paths, and is set aside.
- **Cost:** 17.2 million tokens over 71 requests, about 202,000 an entry, the router's second batch. It was no cheaper than the first (SH-8, 156,000): its 83 billing routes needed the concern map's billing evidence read route by route.
