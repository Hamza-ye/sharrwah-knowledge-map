# Step 2b, range 4: groups YG-332 to YG-561

## What was done

- 612 rows in 230 groups labelled in `pass2/states-4.tsv`: 605 `held`, 7 `proposed`, one `now` (YQ-D204).
- Read: `brief.md`, `conditions.tsv`, `citations.tsv`, `groups.tsv`, `places.tsv` and `notes.md`. No evidence file was opened: every row was settled from its row and its citations' quotes.
- `note` holds any comment of mine first, then the row's first citation, cut at about 220 characters where it is longer (marked `(cut)`).
- 83 groups carry more than one label; 81 of them on `held` rows.
- Rows placed `across Yemen`: YQ-E386 ("nationwide shortage of aviation fuel") and YQ-E223 ("across the country", on e-rial use).
- Places added in `pass2/places-4.tsv`: five products of parties already listed (`National Wallet (MEPS Yemen)`, `E-billing (MEPS Yemen)`, `Mobile Money Business (CAC Bank)`, `Yemen Wallet (Yemen Post)`, `Parcel service (Yemen Post)`), one party (`Torod`), and four authorities (`Governor of Aden`, `Ministry of Finance`, the Al-Mahra and Hadramawt local authorities).

## Places: how the rule was applied

- **Laws of the unified Republic.** Laws and decrees issued before the split, with no seat or side in their text, take `the unified Republic's area`: commercial register law 33 of 1991, companies law 22 of 1997 and its amendments of 2004, 2008 and 2009, agencies law 23 of 1997 and decree 276 of 2000, trade names law 20 of 2003, internal trade law 5 of 2007, consumer protection law 46 of 2008 and its 2010 regulation, sales tax law 19 of 2001 and law 42 of 2005, Finance Minister's decision 93 of 2002, zakat law 2 of 1999, law 40 of 2006, law 1 of 2008 and the 2010 investment law (127 rows).
- **The Sana'a side's texts.** Decision 79 of 2019 (the commercial register regulation), prime minister's decision 10 of 1446 (the boycott), investment law 3 of 1446 and law 7 of 2020 take `Houthis' area`. Each text cites a Supreme Political Council decision, or is issued by the council's president, and `places.tsv` groups the council with the Houthis.
- **The Tax Authority's consolidated sales tax law** (YQ-F162 to YQ-F166) is placed with the law it consolidates, `the unified Republic's area`, although it names law 7 of 2020 (a Sana'a amendment) as its latest amendment. The articles these rows read come from the 2001 and 2005 laws.
- **Levies and seizures.** A row moves from a named area to `Houthis' area` only where its quote says the Houthi authorities imposed it (YQ-E353, YQ-E363, YQ-E463, YQ-E506, YQ-E649, YQ-E655, YQ-E607, YQ-E188, YQ-E242, YQ-E134, YQ-E469; YQ-D233, YQ-E241). Reports of bribes, extortion or practice with no authority named keep the area pass 1 gives (YQ-E608, YQ-D555, YQ-D193, YQ-E507, YQ-E650).
- **Tax guides that report the law without naming it** (YQ-E693 to YQ-E698, a 2022 tax guide) keep `place not stated`. Their quotes do not say which law or authority sets the rule.
- **Party's service.** Procorners' posts, Torod's pages, Bab Al-Mandab, the Anayees store, Jawali, Binance, Yemenia's circulars, YemenNet, Yemen Mobile, Sabafon and the Public Telecommunications Corporation's Starlink sales take the party's service. Where a row names one product of a party with several, it takes the product's place.

## Rows that were hard to label

- **YQ-D171** (Bab Al-Mandab approved by "the Ministry"). Pass 1 placed it at the seatless ministry's area. I left it there; it could equally be the store's own service.
- **YQ-D061 and YQ-E843** (the Prime Minister's pricing directives of 2 August 2025) are `proposed`: one quote says a pricing mechanism still has to be set (ما يستوجب وضع آلية), and the other says the Prime Minister "called for" the policy. They keep their area places, since no rule had been set.
- **YQ-B188.** The zakat authority's deputy says local authorities no longer collect zakat. The amended law had been passed and was awaiting issue by the Supreme Political Council's head. I labelled it `held` on his present-tense account.
- **YQ-B190** (zakat privileges "granted", implementation under discussion) is `held`. No `holds` value fits a decision whose effect is still being worked out.
- **YQ-E710** (a 2020 forecast of mobile penetration) is `proposed`, the nearest value: a forecast is not a state any source shows held.
- **YQ-E132** (the government "stated it would" block only violent content and pornography on AdenNet) is `proposed`.
- **YQ-E488** (Hadramawt "said it would" deposit revenue with CBY-Aden) is `proposed`.
- **YQ-A007** (a cybercrime bill awaiting approval) is `proposed`.
- **Labels made alike on purpose.** Some sources give compatible statements on one date and would otherwise read as disputed, so their rows share a label:
  - YQ-E090 with YQ-E138 (channels of online selling, one source);
  - YQ-E120 with YQ-E146 (no specific e-commerce law, one source);
  - YQ-E538 with YQ-E539 (general commercial laws apply);
  - YQ-D374 with YQ-D387 (exchange companies first, then banks);
  - YQ-E137 with YQ-E331 (Hudaydah port damaged, shipping suspended);
  - YQ-E233 with YQ-E237 (internet cost high);
  - YQ-D212 with YQ-E804, and the other rows of YG-508 (`few use it`);
  - YQ-E166, YQ-E214 and YQ-E223 (`low`, YG-511);
  - YQ-E155 with YQ-E208 (`10 percent`, YG-513).

  The figures stay in `note`.
- **Measures** (YG-491, YG-502, YG-512, YG-513, YG-551, YG-560, YG-561) are labelled by their figure. Numbers that differ get different labels, so these groups become axes with many states.
- **YQ-D204** has `now`: its source gives the coalition's control of imports to 2022 (YQ-D203) and the easing of its blockade in 2022.

## Disagreements

- YG-340: Procorners' SHEIN post offers free delivery in its heading (YQ-C531) and adds delivery and customs in its body (YQ-C538). Same place and date, so this is disputed.
- YG-551: one source on 14 September 2023 says connectivity is sparse (YQ-E706) and that the internet is widely available (YQ-E707). Disputed.
- YG-360: the law gives a company sixty days to register (YQ-B132, unified Republic's area). The Sana'a ministry's page gives thirty days (YQ-B134, Houthis' area). They fall at different places, so the build will show two parts, not a dispute.
- YG-452: decision 108 of 2002 sets the prevailing rate (YQ-F139). The undated guide sets the official rate on the sale date (YQ-F143). Being undated, the guide cannot be today.
- YG-512: the latest count, about 800,000 e-money accounts (YQ-B049, February 2026), is below the central bank's 2,102,484 subscribers for the first half of 2025 (YQ-D272). The build will take the later, lower figure as today.
- YG-432 (Houthis' area): CAC Bank was permitted to collect customs in e-rials in early 2021 (YQ-E196). The same report says revenues were accepted only in cash in 2022 (YQ-E241). The two have different dates.
- YG-401: the American goods ban is dated 23 April 2025 (YQ-E358, YQ-B123) and 25 April 2025 (YQ-E438). Labels differ only where Israeli goods are added.
- YG-488: the electricity corporation says Hadramawt Tribal Alliance checkpoints held back fuel; the alliance denies it (YQ-E453, one row with both claims).

## Problems with the method

- **Rule or report.** "A rule an authority sets" has no clear edge for levies, seizures and bans that sources report rather than quote. Following the quote's wording leaves `Houthis' area` and `Houthi-controlled areas` as two parts of one axis (YG-473, YG-475, YG-559, YG-422), as step 2a foresaw.
- **Unified laws beside restatements.** Pre-split laws sit at `the unified Republic's area`. The Sana'a ministry's pages restating the same rule sit at `Houthis' area`. Axes such as YG-358, YG-359, YG-363 and YG-388 therefore have two parts for one rule.
- **No `holds` value for forecasts, or for decisions whose implementation is pending** (YQ-E710, YQ-B190).
- **The product rule** adds a place for each product named (Yemen Post's wallet and parcel service, MEPS Yemen's wallet and e-billing), so one party can appear under several places on one axis.
- **New authorities.** Local authorities and governors (Aden, Al-Mahra, Hadramawt) are not tied to either governing body in the rows' quotes, so they stand alone. Step 2c may group them only on a source.

## Problems with the brief

- `note` is to hold "the source's own words", but rows often have several citations, some over 300 characters. I kept the first citation, cut short. Where the full wording matters, it is in `citations.tsv`.
