# H-002: the countries a new Salla merchant's onboarding offers

**Repository:** observed-sa. **Instrument:** a new merchant account, made for this run.

**Narrowed on 27 October 2026.** The audit of Salla's claims of absence (phase A3) found the list held, so step 2 is no longer needed (`studies/subjects/S-02/salla/absence-audit.tsv`, S02-SA-G03, contradicted). The page `s.salla.sa/persona/qna` asks "من أي دولة تسجِّل متجرك؟", with Saudi Arabia, the UAE, Kuwait, Qatar, Oman, Bahrain and another country. The answer it fetched, `GET api.salla.dev/admin/v2/onboarding/persona-country`, holds the same options (S02-SA-312, S02-SA-313). What isn't held is what a choice other than Saudi Arabia leads to.

**What to capture:**
1. A new merchant's sign-up, through phone verification, to the onboarding step that asks the store's country (دولة المتجر).
2. ~~The full list of countries it offers, and what it shows for the other choice (`countryOther`).~~ Held (above).
3. What the next step shows for a country other than Saudi Arabia, such as the United Arab Emirates, and for "another country": the documents it asks for, or what it says. Stop before submitting any document.

**Stop before** submitting identity or business documents, or anything that creates a real store in the founder's name beyond the account itself.

**Already held:**
- the onboarding's country question and its options: run `20261008T125139Z-sweep-merchant-routes-ar`, steps 23 and 24, and its saved answer `responses/0535.json`; in English, `20261008T133523Z-sweep-demo-store-en/responses/5134.json`;
- the sign-up form of an existing merchant (run `20261008T101404Z-stage0-merchant-sign-in`, step 3), which has no country field;
- the onboarding's own strings (`structures/salla/dashboard-translations/{ar,en}/onboarding.json` and `persona.json`), which name `countryOther` but not the list;
- the help articles on creating a store outside Saudi Arabia (`help-articles/ar/texts.jsonl` lines 220 to 222).

**Why:** S-02, root decision 1: the countries Salla serves merchants in, and how it holds them (gap S02-SA-G03).

**Needs:** a phone number that can receive Salla's verification code, if the local agent has none.

**Done when** a run holds the step after the country question for one country other than Saudi Arabia, and for "another country".
