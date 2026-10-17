# Review of Stage 1's axes, part 1: YA-01 to YA-126

- **Reviewed:** `studies/yemen-cases/axes.tsv`, sha256 `cad03aa375e97aec1a93580485ecd80051db70852690c60fa8d32add1acdca79`, axes YA-01 to YA-126. Each rests on one group (YG-001 to YG-223).
- **Read:** `brief.md` (Pass 2), `axes.tsv`, `groups.tsv`, `states.tsv`, `conditions.tsv`, `places.tsv`, `notes.md`, `pass2/notes-1.md` to `notes-4.md`, and the quotes in `citations.tsv` where a row left a question open. No evidence file was opened. No file under `studies/` or `evidence/` was changed.
- **Returned:** 82 rows on 70 groups, in `returns-1.tsv`:

  | Rule | Rows |
  | --- | --- |
  | 2 | 53 |
  | 4 | 13 |
  | 1 | 8 |
  | label | 7 |
  | 5 | 1 |

- **Disputes left alone, because the sources make them:**
  - YA-05, the government's area, February 2026: fixed against floating.
  - YA-23, Aden: short against no real shortage, in one article.
  - YA-70, Houthis' area: two rules that one source says both "persisted".
  - YA-74: Wise's two pages.
  - YA-78, Aden and Sana'a, 2023: the counts differ.
  - YA-89: ONE Cash, 30 days against 14.
  - YA-90: Cash's hours (YQ-C127 against YQ-C178).
  - YA-71: Cash's international transfers (see below).

## Systemic problems

### 1. States that hold together (rule 2): the commonest breach

The build takes the latest state at each place as today. Where states add up, today drops facts that still hold, and ties show disputes that no source makes. The breach takes four forms.

- **Lists that grow.** Each decision, designation or post names only what it adds:
  - YA-30 and YA-33: bans and designations;
  - YA-16: the 2018 bans;
  - YA-60: networks barred;
  - YA-96: one wallet's pages;
  - YA-98: wallets named;
  - YA-121: offers.

  `notes.md` already names the problem. The brief's rules leave no clean fix:
  - cumulative labels would need a source that states the whole list (no inference);
  - one condition per barred party is close to the per-institution naming that rule 1 warns against. Here, though, the party is what is barred, not a service.

  **The coordinator needs to rule which fix step 2a should use.**
- **One state at different detail:**
  - a figure against a pair (YA-01, Sana'a);
  - a measure with and without its figure or list (YA-14, YA-47, YA-75, YA-77, YA-91, YA-95, YA-113);
  - one party's pages on one date (YA-90, YA-99, YA-100, YA-102, YA-106; step 2b recorded these and kept the labels apart);
  - one decision or instruction stated twice (YA-29, YA-39, YA-125).
- **Two different facts or rules in one group:**
  - a mechanism and its status (YA-08, YA-61);
  - a period average and a point rate (YA-01);
  - a rule and the practice that breaches it (YA-16, YA-79);
  - several instruments in force together (YA-52, YA-82, YA-97, YA-114, YA-116, YA-118);
  - different parties (YA-35, YA-41, YA-45, YA-49, YA-68, YA-112);
  - different measures (YA-43, YA-58, YA-72, YA-73);
  - different currencies (YA-65);
  - different goods (YA-15);
  - an origin and a channel (YA-10);
  - different rules on one day (YA-09).
- **Disputes in today that no source makes:** YA-01 (Sana'a), YA-09, YA-14, YA-18, YA-22, YA-60, YA-73, YA-99, YA-100, YA-102 and YA-106. In YA-90 the place stays disputed through Cash's hours, but it also joins plain `Available` rows that no source sets against the others.

### 2. Rule or report (rule 4), in both directions

**Market outcomes or assessments placed at an authority's area (returned):**
- YA-06: YQ-E749, the currency "improved markedly";
- YA-23: YQ-D066, YQ-D283 and YQ-B159 on cash shortage;
- YA-67: YQ-D478, transfer fees "increased".

**Borderline, not returned:**
- YA-78: counts of companies registered with each central bank (YQ-D347, YQ-D348), while another source's counts sit at Aden and Sana'a;
- YA-40: YQ-E635, "most banks moved", which its source frames as the Aden government's act;
- YA-61: UNMONEY's membership, at the government's area.

**Authorities' own acts left at areas, against step 2b's placement of rows like them (returned):**
- YA-28: YQ-D537 is the same gulfnews text as newarab's YQ-E722, which step 2b moved. YQ-D537 stayed at `government-controlled areas` and gives today `unknown @ government-controlled areas`. YQ-C369 is part of the Sana'a circular whose other rows are at `Houthis' area`.
- YA-08: YQ-E270 and YQ-E773.
- YA-49: YQ-E779, the IGC's "HC-CB".
- YA-50: YQ-E788 and YQ-E789.
- YA-81: YQ-A036, whose ended state gives today an `unknown` part.

**One circular placed two ways across step 2b's ranges.** Circular No. 11 of 2014:
- range 2 kept YQ-E202 and YQ-E220 at `place not stated`, since their quotes name no issuer;
- range 3 read item 154, line 516, and put YQ-E113, E175, E191, E203, E218 and E219 at `Central Bank of Yemen's area`.

Returned under YA-83 and YA-98.

### 3. Places the rules don't give (rule 4)

Step 2a listed routes and a corridor as `area` places:
- `from Sana'a to Aden`;
- `government-controlled areas to Houthi-controlled areas`;
- `from areas under 'occupation' control to areas of 'national control'`;
- `Saudi Arabia to Yemen (corridor)`.

Rule 4 gives authorities' areas, parties' services and areas a source names. In YA-66, one direction's fee sits at three places, and one row (YQ-D622) gives both directions under one. Returned under YA-66, YA-71 and YA-73.

### 4. The seatless central bank and council (not returned: the seat rule allows it)

`Central Bank of Yemen's area` collects rows from both sides and eras: Circular No. 11 of 2014, item 197's 2026 Aden measures, the centralbank.gov.ye headlines, and the governor's 2024 decision on six banks. Effects on today:
- **YA-03:** the 15 February 2026 fixed rate appears twice.
- **YA-04:** the August 2025 rate (425/428) stands beside the February 2026 rate.
- **YA-13:** the 10,000-riyal ceiling appears twice.
- **YA-28:** today keeps "6 Sana'a-based banks' licences suspended" (10 July 2024), although both sides cancelled such measures on 23 July 2024.
- **YA-19:** the group is named for the central bank in Aden, but YQ-E604 sits seatless.

**Question for the coordinator:** does YE-E668 give the side for YQ-E599, E600, E601 and E604? It says the bank's measures began, and banks "في عدن ومناطق إدارة الحكومة المعترف بها دولياً" started buying currency.

The council's case is similar (YA-24):
- decision No. 13 of 2025 sits at three places: the Council of Ministers', the Ministry of Justice's and the government's area;
- the founder's page that reports it is titled "الحكومة تحظر التعامل بالعملات الأجنبية…", but no citation quotes the title, so rule 5 has no basis;
- `Council of Ministers' area` also holds item 033's 2018 decision (YA-126), whose side no source gives.

### 5. Unknown parts that only reflect placement

A place whose only rows are `proposed` or `ended` takes `unknown`:
- YA-48: the House in Sana'a;
- YA-61: `Houthis' area`, from YQ-C435;
- YA-96: National Wallet Company;
- YA-108: `place not stated`, from YQ-E118, which states the same 15% rule as YQ-E191;
- YA-122: Cash.

These break no rule I review. The unknown parts in YA-28 and YA-81 come from misplacements, which I returned.

### 6. Precision ties

YA-01's `disputed @ place not stated` ties "YER 2,000" (2 August 2025) with "YER 3,000" and "YER 2,065" (both dated 2025). These are rates at different moments of one year. The states are alternatives, so this is not a rule 2 breach, and I did not return it. No source makes the dispute, though.

### 7. Labels that turn a constant into an axis

- **YA-57:** Kuraimi's row at its service, beside a row naming several banks at a joint area. This follows step 2b's rule for rows on several parties.
- **YA-62:** YQ-E636's label names its own place ("Kuraimi Express, among the largest networks").
- **Returned:** YA-29, YA-75, YA-95 and YA-113.

### 8. One user's report as a state

Users' reviews dated before the capture date become earlier states of a service, though they hold together with its availability:
- YA-86: YQ-C425 (returned);
- YA-84: YQ-C165;
- YA-100: YQ-E016.

### 9. Naming per institution (rule 1)

- **YA-19** is named for "the central bank in Aden" (returned).
- **YA-61** is named for one network and also holds the Sana'a side's planned network (returned for YQ-C435).
- **YA-32** is named for Ansarallah. The US designations are split by target: banks (YA-28), exchange companies (YA-30), Ansarallah (YA-32) and others (YA-33). Each split still holds lists that grow.

## Axes I wasn't sure about

**Returned with lower confidence.** The rows' words show the states hold together, but nothing shows in today:
- rule 2: YA-10, YA-41, YA-43, YA-58, YA-64, YA-91, YA-112 and YA-125;
- rule 4: YA-27, which rests on reading "النقد المتداول خارج البنك في عدن" as "outside the bank in Aden", as the same sentence names the central bank, not as "in Aden".

**Not returned:**
- **YA-01 and YA-06, `the new-rial zone` (pass 1's name).**
  - Item 162 says the new rial "circulates in government-held areas" (YE-E435).
  - Item 155 says the new notes "circulate in the south" (YE-E266).
  - The sources tie the name to two areas, so the one-area limit seems to keep it apart. The old-rial zone has one source and is returned (YA-05, rule 5).
- **YA-02:** an undated average (YQ-D188) beside point rates. It is the same mix as YA-01, but undated, so it never ties.
- **YA-21:** "old notes worn out" against "about 10% of notes sound". This is a measure with and without its figure, but on different dates, and today loses nothing.
- **YA-30:** "a company, two exchange establishments and a transfer agent suspended" (YQ-C378, 26 September 2026) may be decision No. 18 (YQ-C075, YQ-D234, YQ-E689), but no row says so.
- **YA-34:** the label "general licences of 5 March 2025 (22A to 26A, 28A)" sits on YQ-E008 and YQ-E514. Neither row's quotes name 28A; only YQ-E705's YE-E1142 does.
- **YA-71:** Cash's "with the possibility of International Transfers" (YE-C028) may mean available now. The next phrase in the same text, "the possibility of adding many services to the Wallet in future", supports pass 1's reading, so I took the dispute as made by the sources.
- **YA-76:** these may each be one rule at different detail:
  - YQ-D452 (2022 capital figures) against YQ-D354 ("Higher minimum capital…", 2024);
  - YQ-D355 against YQ-D339.

  No row says so.
- **YA-87:** a review saying the ONE Cash app needs internet (YQ-D149), against transfers "without an internet connection" (YQ-E054, YQ-E073). These may conflict or hold together.
- **YA-120:** an undated review on Mastercard cards (YQ-D148) against Visa cards (YQ-E053, YQ-E072). This may be a change, or both may hold.
- **YA-125:**
  - YQ-E115 and YQ-E116 give the two models "emerging from the two competing central bank branches" (YE-E126). Range 3 kept them at areas as descriptions.
  - At the authority's area, YQ-E116 ("banks only", September 2025) would replace the 2023 instructions (YQ-F088) as today.
  - This is a disagreement between sources that the current placement hides.

**Outside this review's rules, not checked:** `holds` values and dates, except where they produce an `unknown` part.
