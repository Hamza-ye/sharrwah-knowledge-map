# Q3's check, batch Q-01: notes

Rows: km:ACC-01 to ACC-05, km:STF-01 to STF-07, km:ONB-01 to ONB-04 (16), placed on the merged model at 513aebd8. They follow the brief as revised at 7f6d2060 and c8d6ef9e. `q3.py check --batch Q-01` prints `16 of 16 rows placed; 0 problems`.

**Results.** 15 covered, 1 beyond the class (STF-07, `engineering:build`), and no candidate miss. Every covered row has detail beyond the cells, named under `what_would_settle_it` as `detail:`.

**Time bombs.**
- ACC-04: `wrong time`. Its `needed_by` is `slice`, read as at the area's build, while its subjects (S-02, S-04, S-07) answer before build.
- ACC-05 and STF-05: `bundles;wrong time`. The model answers before build and the founder before release, against `needed_by` `model` and `slice`.
- No other row has a time bomb.

## What the revisions changed in this file

**Second pass (7f6d2060, c8d6ef9e).**
- Engineering was dropped from the 13 rows that had it only by the old "names neither asks both" rule.
- STF-07 is now `engineering:build`.
- S-02's rulings left `basis` where they rule only Sharrwah's shape.
- ACC-04 lost `market fact`: it doesn't ask what the product should do.

**Third pass (68fc7eaf).** A row's words now decide engineering's part only. A subject or the founder answers wherever the row's thing is one they hold. Restored and added:
- **ACC-04:** `subject:S-07`, `subject:S-02` and `subject:S-04`. What a merchant must declare, and what each declaration unlocks, varies by market.
  - S-02's register answers part of it: S02-D3, engineering's ruling in force, says every rule keyed on the seller's country reads the business record's country (`ruled`).
  - S02-M4 moved the documents and checks to S-07, and S02-M2 moved the verification of the business for payment services to S-04.
  - Adding S-04 is my own, by the same test.
- **STF-05:** `founder`. How many staff a plan allows is plans and prices.
- **ONB-03:** `subject:S-08`. How long a market requires a closed store's data kept is S-08's.
- **ACC-05:** `founder`, my own by the same test. What Sharrwah charges for several stores under one owner is plans and prices. This is a reading; if the coordinator reads "how are they billed" as only the platforms' billing structure, the row is model-only again and loses its two time bombs.

**Checked by the same test and left as they are.**
- **ACC-02:** a trial's terms would be plans and prices, but the row asks the store's states, not a trial's terms.
- **STF-06:** Salla gates role management by plan (SA-S-2079, plan سلة بلس), but the row asks the constraints on custom roles, not their plan.
- **STF-07:** the values of plan entitlements are the founder's, but the row asks how authorization composes them, which is engineering's.
- **ONB-01:** a new store's defaults per market are S-02's engineering rulings (E3, E4), not a market's rules.
- **ACC-01, ACC-03, STF-01 to STF-04, ONB-02 and ONB-04:** the row's thing is held by no subject and is not on the founder's list.

## Rows that were hard to place

- **ACC-02 (store states).** The model has no single state machine. Its states are spread over six capabilities, all of kind `class`: CM-ONB-002 (suspension, inactivity, termination, reactivation), CM-PLN-001 (trial: Salla `plan-free-trial`, SA-C-004/decides/SA-S-3452), CM-PLN-002 (frozen: Salla's annual-subscription freeze, SA-S-2085), CM-ACC-007 (temporary closure), CM-ACC-009 (pre-launch visibility) and CM-ACC-001 ("transferred": Salla `store.owner.changed`, SA-S-1622, cited in CM-ACC-001@salla). That "transferred" is Salla's change of owner is a reading. Shopify's change of store owner isn't held: the searches for transfer, ownership and owner in English, and نقل ملكية, نقل الملكية, تغيير المالك and مالك المتجر in Arabic, found only Salla's event. Capturing it would add detail, not a capability.
- **STF-06 (location-scoped access).** No capability is "staff access scoped to a location". I read it as a constraint on custom roles, so detail of CM-STF-002, not a held miss. The only statement found is Salla's `salla_point_assign_branch` (SA-I-1448), cited in no cell, whose concern (SA-C-095) lands in CM-POS-001. If the coordinator reads location scope as a thing of its own, it would be a held miss on SA-I-1448, sitting in CM-STF-002. I'm not sure of this one.
- **STF-04 (how a missing permission shows).** I read it as detail of CM-STF-002 and CM-API-003. On the API side, Shopify requires the user's permission beside the app's scope (SH-S-6215, cited in no cell, its concern SH-C-158 in CM-API-003). The mobile admin's behaviour isn't held.
- **ONB-01, ONB-02, ONB-04 (signup and onboarding).** CM-ONB-004 is held only for WooCommerce. Shopify's, Salla's and Zid's sign-up pages, setup guides and onboarding branches aren't held. I searched sign up, signup, setup guide, sample data, onboarding, get started, first sale and checklist in English, and إنشاء متجر, التسجيل, دليل الإعداد, خطوات الإعداد, تجهيز المتجر, أول طلب, نوع النشاط and ماذا تبيع in Arabic. The rows are still `covered`, since a capability with nothing held on a platform still answers. Capturing those pages would fill in the detail.

## Candidate misses

None. Before settling each doubtful thing, I ran `search` in English, and in Arabic for Salla and Zid. The searches covered: trial, pause, frozen, transfer and owner; custom roles, POS roles and location access; permission denied; invitation and staff limits; signup and onboarding; termination and retention. I also ran `outscope` on transfer, owner, trial, pause, closed, ملكية and المالك, which returned only Salla's group heading SA-I-1519. Then I ran `q3.py where` on every statement the searches found that bore on a row. Each landed in, or was cited by, a capability that is the thing asked, except SA-I-1448 (STF-06, above).

## Problems for the coordinator

1. **Problems 1 to 9 of the first pass are taken in at c8d6ef9e.** They were engineering's time in the checker, the "asks both" rule, `slice` against `later`, rulings in force, `key` with bare ids, a cell printed whole, and a subject without a register.
2. **The revised rule leaves this batch's market and founder sides unasked by any row.** These are: which declarations each market requires (S-07, for ACC-04), how long a closed store's data is kept (S-08, for ONB-03), and how many staff a plan allows (plans and prices, for STF-05). This is right by the rows' words, but Q3 will then not show these subjects as asked by the Knowledge Map's questions on accounts and onboarding. If the coordinator wants them visible, it would take a rule for rows whose class answer implies a market's or the founder's setting.
3. **STF-02 is framed for two vocabularies** ("the two"), while the model holds five platforms. No time-bomb type fits this, so it is only noted under the row.
