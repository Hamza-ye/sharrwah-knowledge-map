# Step 2b, range 1: groups YG-001 to YG-076

## What was done

- 633 rows in 76 groups labelled in `pass2/states-1.tsv`: 624 `held`, 8 `ended`, 1 `proposed`; `now` set on 2 rows; 3 rows placed `across Yemen`.
- 49 groups carry more than one label among their `held`, `ended` and `provided for` rows; 27 carry one.
- Four places added in `pass2/places-1.tsv`, each grouped with itself: `Sana'a-Based Authority (SBA)'s area` (YQ-D528), `Ministry of Justice's area` (YQ-E631, YQ-E889), `Arab Bank's service` (YQ-E502) and `Kuraimi Islamic Bank's service` (YQ-C397, YQ-C398). Step 2c may find the SBA a variant of `the Sana'a authorities' area (سلطات صنعاء)`, and Kuraimi Islamic Bank one with `Kuraimi Islamic Microfinance Bank's service`. I did not join them, since no source here uses both names.
- **Sources opened: none.** Every judgment rests on the rows, their notes and their citations' quotes in `citations.tsv`.
- Each row's `note` starts with pass 1's state and `held_at`, which give the source's words. Where I moved a row to an authority's area or a party's service, the note names who set the rule or whose service it is, citing the quote.

## How labels were made

- **Rates (YG-001 to YG-004, YG-010).** A label is the figure the source gives, as `YER n`, with buying and selling where both are given. I dropped "about", "around" and "near" so that, for example, "about 1,590" and "1,590" share one label. I kept "over", "up to" and "average", because they state something else. A single figure and a buy/sell pair stay different labels even where the single figure equals one side of the pair (YQ-E882 `YER 533` and YQ-D185 `YER 531 buying, 533 selling`, Sana'a, 8 October 2026). The build will therefore show Sana'a's rate today as disputed.
- **Lists of barred or designated parties (YG-041, YG-044 to YG-047).** Each label names the list, or the decision that names it: for example, `13 Aden-based banks barred`, `Kuraimi Islamic Microfinance Bank barred`, `Yemen Kuwait Bank and International Bank of Yemen designated`. A US designation that adds to an earlier one is labelled with the cumulative list where its source gives it.
- **Banknote prints (YG-024).** Any ban covering every party and all new Aden notes is `old notes only, Aden's new notes barred`. Partial bans keep their own labels: one denomination, banks and exchange firms only, or importers and wholesalers only. Reports of which notes circulate are `old notes in use` and `new notes in use`.
- **Bans and designations on Ansarallah (YG-046).** Rows naming both designations are `FTO and SDGT`. Rows naming only the 2025 FTO redesignation (YQ-E111, YQ-E295, YQ-E509) are `FTO`.

## Places

- **Rules moved to the authority's area.** Rules whose row names the authority that set them were moved to that authority's area, whatever area the text names.
  - The Houthi side's note bans (YG-024: YQ-B024 to B030, D037, D077, D327, D624, E099, E183 to E185, E287, E316, E324, E326, E614, E621, E769, E884).
  - CBY-Sana'a's import-financing bans (YQ-E279, E282, E424).
  - Circulars on Kuraimi (YQ-B011, C368, C381, E354, B012).
  - The Council of Ministers' decision No. 13 of 2025 (YQ-A019, A020, E730, E848).
  - Aden central bank circulars that pass 1 gave the Republic as their place (YQ-C068, C070, D081, D275, F114, F118).
  - Laws of the Republic (YQ-B064, B065, B066, B097), placed at `the unified Republic's area`.
  - OFAC designations that pass 1 placed at `United States` (area), moved to `the United States' area`.
- **Seatless central bank.** Where a source names only "the central bank" (البنك المركزي اليمني) fixing a rate or approving an issue, the row is at `Central Bank of Yemen's area` (YQ-E599, E600, E601, E604, A021).
- **"Government CBY".** The IGC source (item 249) places Government CBY "under the Internationally Recognised Government from Aden" (YE-E892). Its acts therefore go to `the internationally recognized government's area` (YQ-E756, E783, E792, E822), and the acts of HC-CB, "the Houthi-controlled Central Bank based in Sana'a", go to `Houthis' area` (YQ-E757, E784).
- **Party services.** Kuraimi Bank's own rate table, home page and branch statements, and reports of Al-Kuraimi's own branches, withdrawals and headquarters, are placed at `Kuraimi Islamic Microfinance Bank's service`, whose note lists the bank's branches. The other party services used are the Dakhm store's payment page (YQ-D296), Cash e-wallet's terms (YQ-C125), CAC Bank's Sana'a branch (YQ-D345) and IBY's SWIFT access (YQ-D472, D534, D550).
- **`across Yemen`,** with the source's words quoted in the note: YQ-D217 ("Throughout Yemen, there is a severe shortage of foreign currency"), YQ-B052 ("الاقتصاد اليمني ككل") and YQ-E780 ("commercial banks across Yemen maintained their SWIFT connections").

## `holds` and `now`

- `ended` where the row's own source says the measure was cancelled or reversed:
  - YQ-D494 (YE-D713);
  - YQ-D537 and YQ-D538, by the agreement of 23 July 2024 (YE-D807);
  - YQ-E443 (YE-E467);
  - YQ-E722 and YQ-E723;
  - YQ-E319;
  - YQ-E529.

  Rows of the same measures whose own sources don't report the cancellation stay `held`. The cancellations themselves are their own states (`both sides' bans on banks cancelled`, `the bar on the 6 Sana'a-based banks cancelled`, `the ban on the 12 wallets reversed`).
- `proposed`: YQ-B063. The source reports the bill's passage by the House of Representatives in Sana'a, not its promulgation.
- **Estimates stay `held`.** Under the coordinator's corrected ruling, only a forecast or projection of a future value is `proposed`. A source's estimate of a present value says the state holds, so it is `held`: YQ-C450 and YQ-C464 (a banker's estimate that about 10% of notes are sound, YE-C479), YQ-E289, and the rates given as "approximately". No row in this range forecasts or projects a future value.
- `now`:
  - YQ-C391: Saturday's rate in Al-Ayyam, against the previous week's rate (YQ-C392) in the same article, both March 2024.
  - YQ-E599: the new fixed rate of 15 February 2026, against the previous fixed rate (YQ-E600) in the same article.
- **No `now` for history tables.** The Aden central bank's currency-history page (YQ-D236 to D260) and the 2018 list in item 024 (YQ-B027 to B031) give several states on one date. Neither presents any one of them as current, and none is the latest at its place.

## Hard rows

- YQ-E882 and YQ-D185: one figure against a pair (above).
- YQ-D402 (`capped`) and YQ-E425 (`capped at US$2,000 a person, with documents proving the purpose`) report the same August 2025 measure at the same place. One gives the figure and the other doesn't, so their labels differ and the build will show them disputed.
- YQ-E291 (Sana'a banks barred from using the new rials for trade finance) names no authority, so it stays at Sana'a.
- YQ-D220, E620 and B032 report bans without naming who set them, so they stay at their areas.
- YQ-C397 and YQ-C398 belong to a bank whose page names it Kuraimi Islamic Bank. I kept them apart from Kuraimi Islamic Microfinance Bank, so that 12 branches and 243 branches are not shown as a dispute.
- YQ-E295 dates the FTO redesignation to an executive order of 22 January 2025. Other sources give 4 and 5 March 2025. Each is labelled as its source states it.

## Disagreements (today's latest rows that differ at one place)

- YG-006, the IRG's area, February 2026: fixed and enforced (YQ-D065, 13 February) against floating (YQ-E756, YQ-E783, February). This is the disagreement step 2a recorded. Moving the IGC rows to the authority's area makes it a dispute at one place.
- YG-031, Aden, 15 February 2026: short (YQ-E602) against no real shortage (YQ-E603), in one article.
- YG-001, place not stated, 2025: YER 2,000 (YQ-D056, 2 August), YER 3,000 (YQ-D458) and YER 2,065 (YQ-E644). Year-only dates tie with the dated row.

## Problems with the method

- **States that are not alternatives.** Several groups' latest rows can hold together, so the build will show disputes that no source makes. Step 2a may want to resize these groups under rule 2.
  - YG-013, Houthis' area, 17 February 2026: banks barred from the Aden central bank's mechanisms (YQ-E268), and banks made to finance imports for Houthi-aligned companies (YQ-E282), in one source.
  - YG-026, `Central Bank of Yemen's area`, undated: the 200-rial note acceptable (YQ-A004), and the 50-rial coin issued (YQ-A005), headlines about two different items.
  - YG-030, place not stated, 10 October 2026: five providers' pages each list different drawbacks of cash (YQ-C177, C193, C266, C325, C342). These are lists that add up, not alternatives.
- **Head office or service.** The service rule covers "what a source says of one named party's own service". A bank's headquarters (YQ-E633) and its branch count (YG-063) were treated as the bank's own, which keeps them from disputing reports about all banks. The brief doesn't say whether that is meant.
- **Joint agreements.** The 23 July 2024 agreement cancelling both sides' bank measures was set jointly by two authorities. A rule has one authority's area, so these rows (YQ-D539, E587, E721, E794) keep their areas, which name both sides.
