# H-002: the countries a new Salla merchant's onboarding offers

**Repository:** observed-sa. **Instrument:** a new merchant account, made for this run.

**Narrowed on 27 October 2026.** The audit of Salla's claims of absence (phase A3) found the list held, so step 2 is no longer needed (`studies/subjects/S-02/salla/absence-audit.tsv`, S02-SA-G03, contradicted). The page `s.salla.sa/persona/qna` asks "من أي دولة تسجِّل متجرك؟", with Saudi Arabia, the UAE, Kuwait, Qatar, Oman, Bahrain and another country. The answer it fetched, `GET api.salla.dev/admin/v2/onboarding/persona-country`, holds the same options (S02-SA-312, S02-SA-313). What isn't held is what a choice other than Saudi Arabia leads to.

**What to capture:**
1. A new merchant's sign-up, through phone verification, to the onboarding step that asks the store's country (دولة المتجر).
2. ~~The full list of countries it offers, and what it shows for the other choice (`countryOther`).~~ Held (above).
3. What the next step shows for a country other than Saudi Arabia, such as the United Arab Emirates, and for "another country": the documents it asks for, or what it says. Stop before submitting any document.

**Extended on 27 October 2026** by gap-closing (phase A2), with two gaps whose evidence is on the same journey's later screens. Where the onboarding reaches the new store's dashboard within the stop below:

4. The store's currency and language settings (`general/currencies` and `general/languages`): the default currency and the default language they show for a store whose country isn't Saudi Arabia (gap S02-SA-G07). Held: the merchant sets and changes both (`studies/subjects/S-02/salla/statements.tsv`, S02-SA-387 to S02-SA-393); nothing held says whether the store's country sets them.
5. The dashboard's app list (التطبيقات) and its filter of supported countries (الدول المدعومة): the countries the filter offers, and the apps it lists for the store's own country (the first half of gap S02-SA-G09). Held: an app's developer selects its supported countries, from a list of seven, and the dashboard's app list has a filter by them (S02-SA-409 to S02-SA-412); nothing held says whether they are matched against the store's country or its markets.

**Stop before** submitting identity or business documents, or anything that creates a real store in the founder's name beyond the account itself.

**Already held:**
- the onboarding's country question and its options: run `20261008T125139Z-sweep-merchant-routes-ar`, steps 23 and 24, and its saved answer `responses/0535.json`; in English, `20261008T133523Z-sweep-demo-store-en/responses/5134.json`;
- the sign-up form of an existing merchant (run `20261008T101404Z-stage0-merchant-sign-in`, step 3), which has no country field;
- the onboarding's own strings (`structures/salla/dashboard-translations/{ar,en}/onboarding.json` and `persona.json`), which name `countryOther` but not the list;
- the help articles on creating a store outside Saudi Arabia (`help-articles/ar/texts.jsonl` lines 220 to 222).

**Why:** S-02, root decision 1: the countries Salla serves merchants in, and how it holds them (gap S02-SA-G03); and what the store's country sets: its default currency and language (S02-SA-G07), and the apps offered to it (S02-SA-G09).

**Needs:** a phone number that can receive Salla's verification code, if the local agent has none.

**Done when** a run holds the step after the country question for one country other than Saudi Arabia, and for "another country"; and, where the onboarding reaches the dashboard, steps 4 and 5 for that store.
