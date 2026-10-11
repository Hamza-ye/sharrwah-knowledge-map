# Measurements, 11 October 2026

These measurements were taken on the paused Q1 outputs in `platforms/`. They are why Q1's placement step is being reshaped before the work resumes. Each was taken with a read-only script, and nothing in the outputs was changed.

## 1. The placement labels are our vocabulary, not the platforms'

Q1 asks for each concern to be placed with a fixed set of values: where it lives in the software, who decides, and who is legally responsible. The agents translated almost everything into those values.

**Our values, not the platforms' words.** Of the 1,261 shown values for those three placements:
- 95% use our category names;
- 34 (under 3%) are in the platform's own words, written as `other:`.

**Many placements cite only that an entry exists.** The citation is only the list entry itself: a webhook name, a menu link or a sitemap URL. The placement is the agent's reading of that entry.

| | Where it lives | Who decides | Boundary |
| --- | --- | --- | --- |
| Shopify | 98 of 196 | 68 of 281 | 115 of 183 |
| Salla | 92 of 129 | 91 of 134 | 95 of 133 |
| WooCommerce | 34 of 116 | 24 of 114 | 28 of 106 |

**A sample of 18 of those, read by hand.** It is too small to be a rate:
- 6 are carried by the platform's own structure, through list membership, code location or data;
- 4 are carried partly;
- 5 are the agent's reading;
- 3 are plain force-fits: Shopify's 24/7 support and Community filed as "core" software, Partner Dashboard payouts filed as "core", and a sitemap URL cited as showing that Salla decides.

**One question, three different encodings.** "Who decides" allowed a single value, so each agent encoded a staged decision differently:

| | Concerns where "who decides" names two or more parties | How it was recorded |
| --- | --- | --- |
| Shopify | 86 of 188 | One row per party for 75 concerns, combined values for 42 |
| Salla | 93 of 134 | Combined values, such as "merchant; operator per plan" |
| WooCommerce | 0 of 114 | One party kept. At least 26 notes name a second decider, for example PayPal Standard: "merchant", with the note "the platform at build hides it otherwise". |

"Legally responsible" names two or more parties for 60 of Shopify's 131 concerns, 5 of Salla's 22 and none of WooCommerce's 108.

**The concern names hold up.** The platform's own terms for a concern were found word for word in its own entries or quotes for:
- 195 of 196 Shopify concerns;
- 142 of 148 Salla concerns;
- 107 of 118 WooCommerce concerns.

## 2. The two-party values come from the platforms' own structures

**Salla.** Salla's dashboard keeps a registry of 568 features, and 349 of them list the plans they are on. Of the Salla concerns whose "who decides" names two parties, 55 of 91 cite Salla's plan-features list.

**Shopify.**
- 185 plan-comparison lines and 291 staff role and permission entries.
- The two-party values counted here come to 73 concerns. This uses a narrower party word list than the 86 above.
- Of those 73, 66 rest on help-centre statements, 16 on plan lines and 12 on staff permissions.

**WooCommerce.** No plans, 9 capability entries and 35 settings.

## 3. observed-sh at `e49840729`, against the Q1 Shopify run

The Q1 Shopify run read observed-sh at `b46731d0`, using 24 of its structures. Since then, observed-sh has added the following.

**Admin answers.** 110,945 GraphQL answers as received (`raw/runs/<run>/answers/`), indexing 526,753 calls of 2,011 operations.

**Seven new structures, each in Shopify's own field names:**
- `shop-request-details`: each store's plan, resource limits, entitlements and features;
- `plan-feature-set`;
- `plan-page-admin` and `plan-page-public`;
- `admin-permission-tree`: 142 permissions in 20 categories;
- `dev-access-lines`: 2,884 lines on 1,941 shopify.dev pages that state an access scope or permission;
- `app-store-built-in-features`.

**Joins, on identifiers Shopify states:**
- `derived/eligibility-by-store.tsv`: route eligibility × store values, 11,418 rows;
- `derived/help-admin-links.tsv`: help pages × admin routes, 4,704 rows;
- `derived/intents.tsv`, 126 rows;
- `derived/admin-route-operations.tsv`, 32,928 rows;
- `derived/staff-gates/`: per role and route, the permissions stated and whether the role holds them.

**Shopify's entitlements differ by plan.** The shop carries 70 named entitlements, and 29 of them differ between the recording stores by plan. For example:
- `maximumLocations` is 2, 10 or 200;
- `dutiesAndImportTaxes.transactionRate` is 0.015 or 0.0085;
- `partialOrderPayments` is true only on Plus stores;
- `checkoutExtensibility` is `LIMITED` or `FULL`.

When `fake-demo-sharrwah` moved from trial to Advanced, `abandonedCartRecovery` went from false to true and `maximumLocations` from 2 to 10.

**The router's eligibility was available to Q1, and the placements barely used it.** The admin router at `b46731d0` already stated eligibility on 494 of its 1,364 routes. It used 12 kinds of condition:
- permissions (282);
- oneOf (98);
- features (89);
- entitlements (79);
- organization permissions (45);
- betas (41);
- clients (36);
- organization features (16);
- organization flags (8);
- excluded (6);
- oneOf failure status (6);
- plans (2).

72 Q1 Shopify concerns are tied to router sections, and the routes behind 60 of them state eligibility:

| Routes behind the concern state | Concerns | Q1's "who decides" names it |
| --- | --- | --- |
| an entitlement | 41 | 6 (plan or entitlement) |
| a staff permission | 49 | 3 (staff, permission or role) |

**12 entitlement subjects, compared with Q1's Shopify placements:**
- **Confirmed (5):** locations, checkout customization, staff accounts, headless storefronts, custom apps.
- **A plan stage Q1 missed (5):** abandoned-checkout recovery, partial payments and deposits on draft orders, duties and import taxes, discount stacking, merchant support.
- **Not in Q1 (2):** ACH billing, and Balance, which is entitled on trial stores while the docs say US residents only.

**Concerns with no Q1 Shopify concern:**
- the merchant's own legal entities (`LegalEntity`, primary and assignable entities, `multiLegalEntitiesPhase`);
- destinations;
- policy-completeness requirements;
- server intents.

**Permission names.** 114 of the permission tree's 130 distinct ids were already in Q1's permission entries. The tree adds Shopify's own categories and nesting.

## 4. One fact for Q2

Every recording store's own answers state country `YE` and currency `YER`, including the store named `capture-gb-plus`. Two consequences follow:
- **For Q2,** the answers are direct evidence of how Shopify treats a store registered in Yemen. For example, `threeDSecureEligibilityForCountry` is false and `multiLegalEntitiesPhase` is `INELIGIBLE`.
- **For Q1,** the answers can separate effects of plan, but not effects of country. That would need a store registered elsewhere.

## Limits

- **What observed-sh holds.** It holds what has been observed, not the platform's full limits. A key or value absent from it is "not shown", never "does not exist".
- **Store values are as observed.** Values come from the recording stores at the times recorded.
- **The router's eligibility is as stated.** Neither observed-sh nor these measurements evaluate it.
