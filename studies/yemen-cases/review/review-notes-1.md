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

## Second review

- **Reviewed:** `studies/yemen-cases/axes.tsv` at commit `71ab056`, sha256 `0b7ef7ade6e5e96be8790a219a9d2581cd4681921dae243f9348cdae748f03aa`: the 71 axes in `changed-1.txt`, whose rows come from the groups of my first review (YG-001 to YG-223) and their splits.
- **Read:**
  - `brief.md` (Pass 2, with rule 2's new sub-bullets and step 2b's new label line);
  - `axes.tsv`, `groups.tsv`, `states.tsv`, `conditions.tsv`, `places.tsv` and `constants.tsv`;
  - `notes.md`, the review round;
  - quotes in `citations.tsv`.
- **Evidence opened** (read only):
  - `evidence/yemen/runs/20261010T072550Z-sanaa-operators-search/items/001-ymp.ye/raw.json`: the Cash wallet's about text, in both languages (YA-61);
  - `.../20261010T072550Z-sanaa-operators-search/items/015-play.google.com/text.txt`, lines 25 to 45: Cash's app listing (YA-225);
  - `evidence/yemen/runs/20261010T050304Z-cited-sources/items/154-sanaacenter.org/text.txt`: lines 1190 to 1250 (YA-70), and a search for the names it gives the new-rial area (YA-214).
- **Files and code:** no file under `studies/` or `evidence/` was changed. Python ran with `-I`, and nothing ran from inside `evidence/`.
- **Rows:** all 2,532 rows sit in exactly one group. The moves between groups match `notes.md`.
- **Returned:** 22 rows on 21 axes, in `returns-1b.tsv`:

  | Rule | Rows | Axes |
  | --- | --- | --- |
  | 1 | 3 | YA-17, YA-52, YA-210 |
  | 2 | 6 | YA-51, YA-78, YA-80, YA-220, YA-225, YA-226 |
  | 4 | 2 | YA-15, YA-106 |
  | 5 | 1 | YA-214 |
  | label | 10 | YA-33, YA-43, YA-57, YA-65, YA-70, YA-102, YA-213, YA-214, YA-223, YA-229 |

### Did the fixes resolve the first review's returns?

**Resolved, and no rule broken now (33 axes):**
- YA-01, YA-05, YA-08, YA-09, YA-10, YA-14;
- YA-25, YA-27, YA-32, YA-34, YA-36, YA-38;
- YA-41, YA-42, YA-45, YA-49, YA-54, YA-55;
- YA-58, YA-62, YA-68, YA-69, YA-75, YA-76;
- YA-81, YA-82, YA-83, YA-85, YA-89, YA-94;
- YA-95, YA-96, YA-98.

YA-01's own fix is right. The rows it sent to YG-562 include my error (see YA-210).

**Not followed, and the reason holds; no other breach (5 axes):** YA-06, YA-20, YA-24, YA-56 and YA-61 (see "Returns step 2a didn't follow").

**New axes from the splits, with no breach (12 axes):**
- YA-211, YA-212, YA-215, YA-216, YA-217, YA-218;
- YA-219, YA-221, YA-222, YA-224, YA-227, YA-228.

**Returned again (21 axes):**

| Axis | First return | Fixed? | What still breaks |
| --- | --- | --- | --- |
| YA-15 | old YA-16: 2, 1, label | yes; the label return not followed (reason holds) | 4: two rows of the Houthis' ban sit at Houthi-controlled areas |
| YA-17 | old YA-18: 2 | yes; the dispute is gone | 1: circulation and practice beside the rules |
| YA-33 | old YA-40: 2 | yes; IBY is at its service | label: the March 2025 decision with and without its count |
| YA-43 | old YA-51: label | yes, for the rows returned | label: YQ-D437 |
| YA-51 | old YA-60: 2 | yes; the D027 dispute is gone | 2: YQ-D028 beside YQ-D029, from one source |
| YA-52 | old YA-61: 2, 1 | yes | 1: YQ-C390 is the national switch |
| YA-57 | old YA-67: 4 | not followed (reason holds) | label: 'Up 300%' against 'Increased' |
| YA-65 | old YA-77: 2 | yes | label: the same count under two labels |
| YA-70 | old YA-84: 1 | yes | label: YQ-E207 |
| YA-78 | old YA-93: 2 | in part: counts and development split | 2: partial lists still hold together |
| YA-80 | old YA-96: 2 | yes, for Floosak and ONE Cash | 2: lists at place not stated |
| YA-102 | old YA-121: 2 | yes, for Hasseb | label: SabaCash against Hasseb |
| YA-106 | old YA-125: 2 | yes | 4: YQ-E115 and YQ-E116 |
| YA-210 | (from old YA-01) | | 1: three point rates among the period averages |
| YA-213 | (from old YA-10) | | label: one origin under two labels |
| YA-214 | (from old YA-16) | | 5: 'the south'; label: YQ-E180 |
| YA-220 | (from old YA-73) | | 2: survey fees beside providers' and channels' costs |
| YA-223 | (from old YA-84 and returns-2) | | label: 'low' |
| YA-225 | (from old YA-90) | | 2: Cash's hours, a dispute no source makes |
| YA-226 | (from old YA-93) | | 2: wallet counts, a dispute no source makes |
| YA-229 | (from old YA-112) | | label: 'none' against 'none, up to 3,000,000 rials' |

Where the breaches come from:
- **The fix round:**
  - YA-210: step 2a added YQ-E447 and YQ-E392 to my YQ-D187.
  - YA-213, YA-223 and YA-229: the new axes' labels.
  - YA-214: a place left ungrouped.
  - YA-225 and YA-226: the disputes left after the splits.
- **My first review's fixes:** YA-78 and YA-220. I proposed "which wallets or providers are named" and "the cost by channel or provider" as conditions, and their lists hold together.
- **Missed in my first review:**
  - YA-15, YA-17, YA-51, YA-52 and YA-80;
  - YA-65: YQ-D356 and YQ-D211 already gave the same count under two labels.
- **Under step 2b's new label line** (a measure with and without its figure or list): YA-33, YA-43, YA-57, YA-70, YA-102, and YQ-E180 in YA-214. In YA-57, YA-70, YA-102, YA-213 and YA-229, one label makes the group a constant, because the labels are its only difference.

### Corrections to my first review

- **YQ-D187.** My return on YA-01 listed it among "averages over a stated period". Its quote, "متوسط أسعار صرف الدولار في عدن" (YE-D203), is the average of dealers' quotes on one page, with no period. Step 2a followed me. It is returned under YA-210, together with YQ-E447 and YQ-E392.
- **Cash's hours.** My first notes listed them as a dispute the sources make (old YA-90). Cash's own English page gives cash-out "through Automatic Teller Machine (ATM) during off work times" (YE-E774). So "official working hours" at agents (YE-C110) and cash "على مدار الساعة" (around the clock, YE-C155) hold together. Returned under YA-225.
- **YQ-E115 and YQ-E116.** My first notes left them unreturned (old YA-125). Step 2a has since kept item 154's account of the same two models at the two authorities' areas (YQ-E152, YQ-E153). Step 2b's place rule takes a rule an authority sets to that authority's area, whatever area its text names. Returned under YA-106. At the IRG's area, the move makes "banks only" (September 2025) today, a disagreement that the current places hide.

### Constants from my returned groups

I checked only that each split kept every condition whole. The returned groups now give 102 groups: 18 are axes, all in the list above, and 84 are constants.
- 19 returned groups became constants: YG-020, YG-027, YG-030, YG-042, YG-044, YG-047, YG-049, YG-072, YG-080, YG-111, YG-123, YG-127, YG-134, YG-140, YG-149, YG-162, YG-164, YG-188 and YG-202.
- 65 are new groups from the splits.

Each constant keeps its rows together, and they answer one question under one label. Apart from the three cases below, no sibling holds a row that is an earlier or later state of the same question.

In these three cases a condition reaches into a sibling, because a row goes in one group only. I did not return them:
- **YK-354 (YG-567), the customs rate for luxury and non-essential goods.**
  - Its 2025 state, the general 750 and then 700, stays in YG-022. The May 2026 decision raised the rate "from YR750" (YE-E390).
  - So the constant shows no change, though YQ-E377's own state records the rise.
  - YG-022's name, "goods other than luxury and non-essential goods", fits its rows only from May 2026. In 2025 the rate covered all goods: the planned increase "will not include basic food items" (YE-E360).
- **Swaid & Sons' designation** is in YK-376 (YG-591, one row with Al-Omgy) and in YK-377 (YG-592).
- **The bar on exchange companies** is in YK-423 (YG-652, YQ-D117). YQ-F079 also states it, from YG-222.

The unnamed restorations (YK-371, YK-372) can't be tied to any ban, since their sources are headlines (YE-C376, YE-C378).

### Returns step 2a didn't follow

**Place not stated: the reason holds under the brief.**
- **The returns:**
  - YG-007: YQ-E749;
  - YG-031: YQ-D066, D283 and B159;
  - YG-040: YQ-E606;
  - YG-114: YQ-D478.
- **Why it holds:**
  - Step 2b's last branch gives a row that is no rule, no party's service and not across Yemen its pass 1 place, as `places.tsv` groups it.
  - Rule 5 groups no authority's area or named area into `place not stated`.
- **What remains:** market facts sit at an authority's area, against rule 4's kinds. This is the brief's problem, as `notes.md` records.

**Routes and the corridor: the reason holds.**
- **The returns:** YG-113, YG-120 and YG-123.
- **Why it holds:**
  - Rule 5 joins a route to no area.
  - Step 2b keeps the pass 1 place of a row that is no rule and no single party's service.
  - For YQ-A008 (YA-61), step 2b's own line decides it: "A row about several parties' services keeps its grouped place, and its label names the parties."
- **What remains in today:**
  - YA-56: one direction's fee at five places;
  - YA-219: the Saudi corridor's cost at two places (2.70% at the corridor, 2.4% at place not stated);
  - YA-24: 3.3 trillion at three places.

**Followed in part:**
- **YG-024 (no label per list of parties): the reason holds.**
  - YG-571 is sized to banks and exchange firms, which every row names.
  - The other parties stay in note, because a row can't be split.
- **YG-106 (UNMONEY's rule and the closure of own networks kept as one rule): the reason holds.** From 26 June 2024, one decision states both.
- **YG-107 (owners and status as one condition): the reason holds.** YQ-E748, D120 and D284 each state both.
- **YG-046:** followed in substance, by lists that grow.
- **YG-147 (YQ-D105 to its own condition rather than YG-508): the reason holds.** In YG-508, it would hold together with how widely buyers pay.

### Disputed parts in today

**In my axes:**
- **YA-01, place not stated: not made by the sources.**
  - "YER 2,000" (YQ-D056, 2 August 2025) ties by precision with "YER 3,000" and "YER 2,065" (YQ-D458, YQ-E644, dated 2025).
  - These are rates at different moments of one year. They are alternatives, so no rule is broken. The dispute comes from the build's precision rule.
- **YA-05, the IRG's area: made by the sources.**
  - Al-Ayyam (13 February 2026): all must keep to the rate the central bank sets (YQ-D065).
  - The IGC (February 2026): the rate is "allowed ... to fluctuate with market conditions" (YQ-E756, YQ-E783).
- **YA-20, Aden: made by the source.** Item 197 quotes banking sources ("short", YQ-E602) and an economist ("no real shortage, cash poorly distributed", YQ-E603).
- **YA-61, Cash e-wallet's service: made by the sources.**
  - The about page lists international transfers through MoneyGram and Western Union among services that may be added in future: "مع إمكانية إضافة العديد من الخدمات إلى المحفظة مستقبلاً ... والتحويلات الدولية". This is the Arabic text of the field that YE-C028 quotes in English.
  - The app listing offers withdrawing remittances of "الشبكات المحلية والدولية" (local and international networks) now (YE-C151).
- **YA-225, Cash e-wallet's service: not made by the sources.** Returned.
- **YA-226, place not stated: not made by the sources.**
  - Each article gives 8 to 10 and a possible total over 15, side by side.
  - Returned.

**Outside my list:** YA-60, YA-63, YA-66 and YA-74 hold the other disputed parts in today.

**Unknown part:** YA-80 has `unknown @ National Wallet Company's service`, from a proposed row only. No rule is broken.

### Seen and not returned

- **YA-10:**
  - "money exchangers" (YQ-D361, 2024) may overlap "the parallel market".
  - Today is unaffected.
- **YA-25, Houthis' area:**
  - YQ-E793 (2024) ties by precision with the ended YQ-E723 (23 July 2024), so "13 Aden-based banks barred" stays in today.
  - The 23 July 2024 cancellation sits at a joint place, `the Yemeni government's and the Houthi group's areas`, which supersedes neither side.
  - YQ-E586 stays at the seatless central bank. Item 192 gives no seat.
- **YA-41:**
  - "Sana'a banks pressed by the Houthis to leave SWIFT" (YQ-E449) holds together with "connected".
  - It is not today, since `across Yemen` supersedes it.
- **YA-49:** "Largely absent" and "Very little" state the same scarcity at different places. With no effect on today or cases, I left it.
- **YA-54:** YQ-E754 and YQ-E803 tie in February 2026. Their states are alternatives, and neither is the latest.
- **YA-83:** Floosak's reply on updating identity data (YQ-E017) may hold together with its activation steps (YQ-C246). It is not today.
- **YA-89:** the same three currencies carry "more than one currency" at Cash and "the rial, Saudi riyal and US dollar" at ONE Cash, as the new label line gives each service's pages. Today is unaffected.
- **YA-221:** the Civil Status Authority in Sana'a stays apart from Houthis' area, since no source joins them.

## Third review

- **Reviewed:** `studies/yemen-cases/axes.tsv` at commit `f3ed2df`, sha256 `02850db51259fb99cdb706c2f5b7580c2136a5c0cb98c3238b2b9166e6812375`: the 15 axes in `changed-3-1.txt`. I read `notes.md`, "Second review round". All 2,532 rows sit in exactly one group. No evidence was opened, and nothing under `studies/` or `evidence/` was changed.
- **Returned:** nothing. `returns-1c.tsv` has its header only.

### Each axis

| Axis now | Group | My second-round return | Resolved? |
| --- | --- | --- | --- |
| YA-01 | YG-001 | YA-210, rule 1: YQ-D187, E447 and E392 came back as rates at one time. They make no new tie. | yes |
| YA-15 | YG-024 | rule 4: YQ-E620 moved; YQ-D220 stays (below) | in part; the reason holds |
| YA-17 | YG-026 | rule 1: YQ-E317 and E605 went to YG-729 | yes |
| YA-33 | YG-061 | label: one label for the March 2025 decision; the 15 March tie is gone | yes |
| YA-43 | YG-079 | label: YQ-D437 | yes |
| YA-51 | YG-106 | rule 2: YQ-D028 went to YG-730 | yes |
| YA-52 | YG-107 | rule 1: YQ-C390 went to YG-731, my second fix | yes |
| YA-75 | YG-160 | rule 2: one label for the four lists, my second fix | yes |
| YA-77 | YG-163 | rule 2: one label for the lists at place not stated | yes |
| YA-102 | YG-222 | rule 4: YQ-E115 and E116 at the two authorities' areas | yes |
| YA-201 | YG-562 | rule 1: only period averages remain | yes |
| YA-204 | YG-568 | label: YQ-E180. Rule 5: not followed (below) | label yes; the rule 5 reason holds |
| YA-212 | YG-630 | label: YQ-E223 now names its uses | yes |
| YA-214 | YG-640 | rule 2: one count, 8 to 10; YQ-C462 went to YG-735 | yes; the dispute is gone |
| YA-226 | YG-729 | new, from my YA-17 return | breaks no rule |

None of the 15 axes breaks a rule now. My other returned groups (YG-114, YG-130, YG-147, YG-212, YG-566, YG-623, YG-638 and YG-645) are now constants, so they are outside this list.

### Returns step 2a didn't follow

- **YA-15, YQ-D220 at Houthi-controlled areas: the reason holds.**
  - Item 046 says the new notes "were banned" in Ansar Allah-controlled areas, and names no authority that banned them.
  - Step 2b's first branch needs a rule that an authority sets, so its pass 1 place stands without inference.
  - The part says what the Houthis' area part says. Parts may overlap, and these two don't conflict.
- **YA-204, 'the south' left apart: the reason holds.**
  - Item 155 says the notes "now circulate in the south" (YE-E266). About 300 lines later it says they "flooded into government-controlled areas" (YE-E296). It never uses the two names for one area.
  - Item 274 calls the government's areas "the IRG-controlled south and east of Yemen", which is more than the south.
  - Rule 5's `source` needs a single source that uses both names for the same area. Without one, the two parts stand. Both state "new notes in use".
