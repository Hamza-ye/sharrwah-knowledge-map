# H-002: the countries a new Salla merchant's onboarding offers

**Repository:** observed-sa. **Instrument:** a new merchant account, made for this run.

**What to capture:**
1. A new merchant's sign-up, through phone verification, to the onboarding step that asks the store's country (دولة المتجر).
2. The full list of countries it offers, and what it shows for the other choice (`countryOther`).
3. What the next step shows for a country other than Saudi Arabia, such as the United Arab Emirates: the documents it asks for. Stop before submitting any document.

**Stop before** submitting identity or business documents, or anything that creates a real store in the founder's name beyond the account itself.

**Already held:**
- the sign-up form of an existing merchant (run `20261008T101404Z-stage0-merchant-sign-in`, step 3), which has no country field;
- the onboarding's own strings (`structures/salla/dashboard-translations/{ar,en}/onboarding.json` and `persona.json`), which name `countryOther` but not the list;
- the help articles on creating a store outside Saudi Arabia (`help-articles/ar/texts.jsonl` lines 220 to 222).

**Why:** S-02, root decision 1: the countries Salla serves merchants in, and how it holds them (gap S02-SA-G03).

**Needs:** a phone number that can receive Salla's verification code, if the local agent has none.

**Done when** a run holds the onboarding step with its full country list, and the step after it for one country other than Saudi Arabia.
