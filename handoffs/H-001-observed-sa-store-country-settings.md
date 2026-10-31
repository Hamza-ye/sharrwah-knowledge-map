# H-001: where Salla's merchant store shows its country, and whether it can be changed

**Repository:** observed-sa. **Instrument:** the merchant store (store-1-da), as its owner (`docs/PLAN.md`, Instruments).

**What to capture:**
1. The dashboard's settings for the store's own details: Settings > General and Settings > Store information (`settings-center` sections `general` and `general/store-information`), and any page that names the store's country (دولة المتجر).
2. Whether the country shows there, and whether it can be edited. If an edit is offered, open it and record what it shows, the list of countries and any condition or warning, and stop before saving.
3. Salla's own help in the dashboard, if it answers whether a store's country can be changed: record the answer as shown.

**Stop before** saving any change to the store's country or details.

**Already held:**
- `structures/salla/settings-center/merchant@en`, sections `general` and `general/store-information`: they don't name the country;
- the sign-up form (run `20261008T101404Z-stage0-merchant-sign-in`, step 3): no country field;
- the help articles on creating a store outside Saudi Arabia (`help-articles/ar/texts.jsonl` lines 220 and 221), which say the country is chosen at sign-up.

**Why:** S-02, root decision 1, the store's own country: who can change it, and on what conditions (gap S02-SA-G01, in `studies/subjects/S-02/salla/gaps.tsv`).

**Needs:** nothing from the founder.

**Done when** a run holds the settings pages that would show the store's country, with what they show or don't, and the edit form if one is offered.
