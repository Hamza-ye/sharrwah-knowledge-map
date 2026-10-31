# SH-16: notes

Shopify's `admin-router`, 81 entries (`structures/shopify/admin-router/items.jsonl`, lines 996 to 1100, less the routes the concern map cites), observed-sh at `e38dc17e3`: the second OrganizationSettings tree's partner billing (4) and its redirect to Organization (1), a legacy gift-card redirect (1), Payments (51: its settings tree, its own tree, the orphans and `shopify-payments`) and Plus (24: three trees, an inactive account's, Settings' and `plus`).

**Read:** the brief; the router digest, `held/rules/admin-router.md`, whole with its section 6; the rulings' last section; observed-sh's `README.md`, `docs/READING.md` (runs, structures, indexes, limits), `docs/GAPS.md` (its Admin section), `structures/README.md`, the router's `REGISTER.tsv` row and its ledger rows; the evidence map's Shopify parts; the selection row; `show --meta`; B-extent.md's "Cells and evidence" and "Conventions from the dry run". **No batch's notes were read**: the digest covered every case. Earlier lines read by their twins: SH-15's partner billing and Organization lines (SH-E-4eddcce2, SH-E-29c5a7da, SH-E-cf578934, SH-E-4c6188c0, SH-E-a9c9772f), SH-10's Capital twins (SH-E-84b47f6c's `capital:mfaLandingPage`; SH-E-3073acdb, SH-E-abc7fa48, SH-E-e4401668's profile assessment), SH-9's Plus lines (SH-E-b1cdc806, SH-E-e548d845) and the NotFound catch-all SH-E-ca7a8ac4.

**Count:** 104 lines on 81 entries: 69 entries on capabilities alone, 8 on a capability and `new:Plus trial`, 4 `out`. Supports: 85 `core`, 15 `shows`. No line changes a cell (the checker prints no `CHANGES`).

## The new thing

**`new:Plus trial`** (SH-9's name, kept), 8 lines, all `core`:
- the inactive account's tree, at `access_account/plus/trial…`: SH-E-8f7a8700 ('Try Plus for less'), SH-E-a0e8ddbf (review), SH-E-56442cef (confirmation);
- Settings' tree, at `settings/subscribe/plus/trial…`: SH-E-30d08df8 (review), SH-E-c88ece4e (review/currency), SH-E-7eba660b ('Try Plus for less'), SH-E-eaf6b7a8 (confirmation), SH-E-4ae820dd (ineligible, whose title 'Subscribe to Plus' is CM-PLN-001's).

**Its place of its own:** the routes `trial` titled 'Try Plus for less', with their review, confirmation and ineligible pages, in two trees: entries of the route manifest with their own paths (B-extent, "What a place of its own is"). The page at `settings/subscribe/plus/trial` heads it 'Plus trial', beside 'Plus' after it (`raw/runs/20261002T003931Z-sweep-capture-advanced/steps/429.aria.yaml`, lines 88 to 103). Each entry also takes CM-PLN-001 `core`: the trial leads onto the Plus plan, and its review is a subscribe checkout (the digest's rule 33).

**Proposed:** domain A, area PLN. Its parent is CM-PLN-001, or an ONB trial if one is made: CM-PLN-001's note reads 'A free trial and the inactive and pending-termination states are the ONB batch's.', and no ONB capability holds a trial. Name: 'Plus trial', English only, as the admin isn't held in Arabic (the digest's rule 40). Decide it with the platforms' other trials (the check after SH-9).

**Terms searched** (`caps --terms`): trial; free trial; paid trial; Plus trial; Try Plus. They found CM-PLN-001 (the note above), CM-APP-004 (an app's trial, a homonym) and CM-SHP-010 (no match of meaning).

## Rules I followed that the digest doesn't cover

- **R16.1:** a redirect may land on its target filtered to one provider's records. SH-E-9ad06662 sends `payments/shop-pay-installments` to `payments/payouts-next?ledger_type=ShopifyPayments%3A%3AProvider%3A%3AAffirm%3A%3AAccount`.
  - It takes `shows` on the target's capability (CM-PAY-005).
  - Where its own words name that provider's thing, and a cell holds the filtered records as that thing's, it takes a second `shows` line there: CM-PAY-015, whose cell holds the instalment orders' payouts inside Shopify Payments payouts (SH-S-0317).
  - This extends R15.4 from an anchor to a filter in the landing's address. The provider named only by the address (Affirm) goes in `reading`.
- **R16.2:** an index route is `out` where its component is `render-common.js`'s `NotFound$1` (named only in `source.jsonl`) and it has no title, path, gate or resource. SH-E-ca7a8ac4's catch-all with NotFound is `out` the same way (the digest's rule 37).
  - Cases: SH-E-5e46c744, SH-E-d006d32d and SH-E-80b1e158 (`source.jsonl`, lines 1076, 1085 and 1096). Every visit answered “There's no page at this address”.
  - Their containers keep their own lines: `plus:settings` (SH-E-f22f7387), and `plus_inactive_account` and `plus`, which the concern map cites.
- **R16.3:** a container with a `redirect` key isn't only a redirect where its `eligibilityMatch` alternative brings a loader and a component, and visits stayed at its address. It is `core` on its path's capability, with the redirect and the `eligibilityMatch` in `reading` (rule 26).
  - Case: `payouts-next` (SH-E-bdd7e918), whose seven visits stayed on `payments/payouts-next`.
- **R16.4:** a pathless top-level wrapper whose id names only its role in the code is `out` where it sits over several capabilities' routes (rules 37 and 38; the rulings after SA-22 and SA-28). It is `out` even though it holds the section's resource.
  - Case: `payments:orphans` (SH-E-f461b491), over Amazon Pay's dashboard, the Shop Pay Installments terms, Shopify Protect, the requested documents and the identity verification.
- **R16.5 (a reading, for the coordinator):** the profile assessment and identity verification in Payments' trees take CM-PAY-003 beside CM-TRU-002. I read rule 32's "its capability" as the payment service's verification, CM-PAY-003, which is a child of CM-PAY-002.
  - Cases: SH-E-d8252e28, SH-E-d2bf47fe, SH-E-acd8f02b, SH-E-f2c4fe7a and SH-E-798dd2a9.
  - The alternative is CM-PAY-002. The concern map places their sibling `payments:settings:worldfirst-setup` ('Set up Shopify Payments', behind a beta) `shows` there (SH-S-5250). CM-PAY-003's note cites the generic `profile-assessment` route there only as `shows`.

## Entries I couldn't tell, and what would settle each

- **SH-E-9af6f72d 'Order transactions'** (`payments/payouts/transactions`) is on CM-PAY-005 (the transactions under Payouts) and CM-PAY-020 (the title's order transactions). Its redirect SH-E-8f3f1994 follows it, a line on each.
  - Every visit answered “There's no page at this address” (`derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/403.html.txt`).
  - A visit on a store with Shopify Payments (`capture-us-plus` once onboarded, GAPS.md) would show which it lists: the balance's transactions, or orders' payment transactions.
- **SH-E-e051cda1 'Move money'** (`payments/payouts/claim`) is on CM-PAY-005, by its title under Payouts. No capability names moving money (`caps --terms`: move money; instant payout; claim).
  - Its visits answered no page (`404.html.txt`, the same run).
  - A store with a Shopify Payments balance would show where the money moves, perhaps to Shopify Balance (CM-PAY-023).
- **SH-E-7dbcde35 and SH-E-3ca2cda4** ('Authorize.net Legacy Gateway', 'Adyen Legacy Gateway'): what `legacy_subscription` names in their paths isn't stated, whether a legacy subscription of the merchant's or buyers' subscriptions. The pages offer only activation, with the account's credentials and a test mode.
- **SH-E-1f15f0f8** (`settings/payments/shopify-payments-accounts`, loader only) is `shows` on CM-PAY-001, from the six owners' landings on `settings/payments`. On a store with Shopify Payments accounts it may land on an account's page (CM-PAY-002). A visit there would settle it.
- **SH-E-c5d8b549** (`payments/bank_account/*`, loader only) was never visited (splat), so it stays `core` on CM-PAY-005 (rule 11). If a visit shows it redirects to `settings/payments/bank-account/*`, it becomes `shows` on SH-E-ba95ec8e's two capabilities.
- **SH-E-f4eda63b 'Payment methods'**, under Shopify Payments' settings, is on CM-PAY-001 (its title) and CM-PAY-002 (its anchor 'Shopify Payments payment methods'). The coordinator may keep one.
- **SH-E-ba95ec8e 'Shop Payments Settings'** (`settings/payments/bank-account/*`) is on CM-PAY-005 (its path and module name the bank account) and CM-PAY-002 (its title, read as Shopify Payments, as its breadcrumbs place it). Both are readings.
- **SH-E-b6788a69** (`settings/payments/paypal-express-checkout/:businessEntityId`) takes CM-ACC-005 beside CM-PAY-013, a reading of its id's `business-entity`.
- **SH-E-ecfd05b0** (the legacy `gift_cards/*` redirect) takes CM-LOY-002 `shows` beside CM-PAY-001, by R15.4. The rest of this point is in the next section.

## The anchors of a route the concern map cites: no line

`payments:settings:index` (`items.jsonl`, line 1004) is cited by the concern map only for its eligibility (SH-S-5246). Its anchors are no batch's entries, so none has a line:
- 'Payments';
- 'Apple Wallet Passes';
- 'Gift card expiration', with the intent `edit settings/GiftCardExpiration`, which the Intents API documents (`derived/intents.tsv`);
- 'Manual payment methods';
- 'Additional payment methods';
- 'Payment capture method', with an intent;
- 'Payment method customizations'.

SH-E-ecfd05b0's CM-LOY-002 line rests on the gift-card anchor. The anchors are a lead for the coordinator: gift card expiry (CM-LOY-002), Apple Wallet passes and the capture method (CM-PAY-020's capture setting).

## What a source or run step states that no entry holds (for the second stage)

- `derived/step-text-from-html/20261002T003931Z-sweep-capture-advanced/391.html.txt`, line 94: “If two-step authentication isn't turned on, your account may be less secure. You may also have your payouts paused.” This ties two-step authentication (CM-TRU-001) to payouts (CM-PAY-005, CM-PAY-006).
- `raw/runs/20261002T003931Z-sweep-capture-advanced/steps/429.aria.yaml`, on capture-advanced, a development store:
  - lines 92 to 96: the Plus trial's length and price ('For 2 months', '$399', 'USD/mo'), with “Downgrade anytime. We'll send you a reminder before your trial ends.”;
  - lines 98 to 102 and 119 to 124: Plus after the trial ('1-year or 3-year term with all Plus features', '$2,300', 'on a 3-year term', 'Starting at Starts at $2,300 USD/mo + variable fees').

  These are qualities for `new:Plus trial`, CM-PLN-001 and CM-PLN-002. They aren't in `quality`, since they come from a run step, not the entry or its structure's source.
- `raw/runs/20261002T003931Z-sweep-capture-advanced/steps/428.aria.yaml`, line 102: 'You will automatically roll onto a Plus term with these scheduled changes at the end of the trial.' This is CM-PLN-002's renewal at the trial's end.
- `raw/runs/20261007T115110Z-journey-unvisited-routes/steps/015.text.txt`, on fake-demo-sharrwah's Payments settings:
  - line 47: '0.6% transaction fee • Card rates set by ONERWAY (Direct)'. This is a third-party provider's fee, a lead for CM-PAY-011 and CM-PLN-003;
  - line 51: 'More ways to pay';
  - line 59: 'Apple Wallet passes'.

## Structure and sources

- **`items.jsonl` leaves out a module's export name.** For an import such as `./render-common.js`, it gives the file only. `source.jsonl` names the export, `NotFound$1`, and governs: R16.2 rests on it.
- **Visits joined by address.** The ledger joins one address's visits to every route at it:
  - `settings/partner-billing` in both OrganizationSettings trees;
  - `settings` for `organization-settings:organization:settings`, whose visits landed on `settings/general`;
  - `settings/payments` for the pathless `payments:settings:secondary-gateways`.

  They are read as the other route's visits (R15.5).

## Problems with the brief or the script

- **`earlier` found no line** for any of the 81 entries. The twins were looked up by hand: the second OrganizationSettings tree's paths in SH-15, as the message asked; the Capital twins in SH-10, which `earlier` reached for `mfa-landing-page` by its name alone; and SH-9's Plus lines.
- **SH-S-5092 is one statement cited under many concerns, each with another route as its key:** `plus_inactive_account` (SH-C-015), `payments:settings:shopify-payments-accounts` (SH-C-063), `market:update:managed` (SH-C-110) and others. A reading that cites it should name the concern too. SH-E-1f15f0f8's names SH-C-063's capability, CM-PAY-002.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 81 of 81 entries, no problem and no `CHANGES`. `method/held_router_gates.py SH-16 --apply` named the ancestors' gates in 4 lines.
- **R16.5 is settled as placed:** the Payments profile-assessment and identity-verification routes are CM-PAY-003, beside CM-TRU-002. CM-PAY-003 is 'the checks a store passes before it can take payments through the platform's service, its KYC and underwriting', and its terms already hold ProfileAssessment. CM-PAY-002, the service itself, is its parent. The concern map's `worldfirst-setup` on CM-PAY-002 (SH-S-5250) is read again at Shopify's amendment.
- **The rules R16.1 to R16.4 stand** and join the digest's section 6.
- **The new thing** keeps SH-9's name, Plus trial, with its place of its own: the trial routes in two trees, headed 'Plus trial'. Its prices and length are second-stage leads.
- **Open, as placed:** the two pages that answered 'There's no page at this address' (Order transactions, Move money), placed by their words; `legacy_subscription`.
- **Cost:** 18.8 million tokens over 95 requests, about 232,000 an entry. The context reached about 333,000 tokens.
