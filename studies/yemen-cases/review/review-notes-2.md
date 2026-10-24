# Review of Stage 1's axes, part 2: YA-127 to YA-253

This is a draft for the coordinator. The review changes nothing. Each row of `returns-2.tsv` proposes returning one group to step 2a and names the rule it breaks. The coordinator decides.

## Scope

- **Range:** 127 axes (YA-127 to YA-253), one group each, 741 rows.
- **Checksum:** `studies/yemen-cases/axes.tsv` has sha256 cad03aa375e97aec1a93580485ecd80051db70852690c60fa8d32add1acdca79, checked at the start and again at the end.
- **Read:**
  - `brief.md`: Pass 2, meaning step 2a, step 2b and the build.
  - For each axis: its rows in `axes.tsv`, `groups.tsv`, `states.tsv` and `conditions.tsv`; their quotes in `citations.tsv`; `places.tsv`.
  - `notes.md` and `pass2/notes-1.md` to `notes-4.md`, for step 2a's and step 2b's reasons.
- **Not opened:** any evidence file, or anything on the brief's "Don't open" list.
- **Not edited:** anything under `studies/` or `evidence/`. Python ran with `python3 -I`, from scripts in the scratchpad.

## Returns

`/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/y-review/returns-2.tsv` has 60 rows over 58 groups. Two groups have two rows each: YG-224 (rule 2 and rule 1) and YG-513 (rule 2 and label).

| Rule | Rows | Groups |
|---|---|---|
| 2 | 43 | YG-224, 225, 229, 236, 240, 243, 244, 247, 278, 279, 280, 286, 291, 310, 331, 342, 347, 371, 388, 395, 401, 402, 408, 414, 415, 422, 431, 432, 439, 446, 473, 475, 480, 483, 490, 492, 502, 511, 513, 520, 551, 555, 560 |
| 1 | 11 | YG-224, 237, 423, 486, 508, 509, 521, 525, 552, 556, 561 |
| label | 4 | YG-255, 256, 343, 513 |
| 4 | 1 | YG-346 |
| 5 | 1 | YG-478 |

**The plainest sign.** Nine axes in this range have a `disputed` part in `today`. No source makes any of those nine disputes, and all nine groups are returned: YG-237, YG-240, YG-243, YG-244, YG-278, YG-280, YG-402, YG-473 and YG-475.

**By weight,** for choosing what to send back first:

- **9 rows:** `today` shows a dispute no source makes (the nine above).
- **40 rows:** one of these:
  - `today` keeps one of several states that hold together;
  - the axis reads two measures or two questions as one;
  - a label or a place breaks the rules.
- **11 rows:** `today` is right, but there is still a problem:
  - **The axis exists only because of detail or wording.** Rows state one thing at different detail or in different words.
  - **Or the axis swings** between such states in a way no source says happened.

  These rows are YG-256, YG-291, YG-347, YG-395, YG-401, YG-431, YG-502, YG-509, YG-513 (label), YG-520 and YG-555. They break rule 2 or the label rule as written, but they matter less than the rest.

## Systemic problems

1. **One party's pages, or parts of one source, tie on one date.**
   - A live page's state takes the capture date. So when two pages or sections of one party each give part of one list or requirement, they tie on 2026-10-10. The result is a dispute no source makes, at:
     - Jawali (YG-240);
     - Hasseb (YG-243);
     - CAC Bank's cards and card requirements (YG-278, YG-280).
   - The same happens with one Packagist listing (YG-237, YE-E080) and with one E-Pay client library dated 2025-05-26 (YG-244).
   - Step 2b's range 2 avoided this for availability by giving one label per service and date ("Availability labels", `pass2/notes-2.md`). Lists of requirements, cards and methods got no such label.
2. **Lists that add up.**
   - Where each row names only what one decision, post or report adds, the rows are parts of one list, and `today` keeps only the latest part: YG-224, YG-225, YG-310, YG-331, YG-342, YG-402, YG-473 and YG-480.
   - Step 2a's notes name the risk ("Lists that grow", `notes.md`) and already list YG-224.
   - Two fixes would work: one cumulative label per date, or one condition per item. YG-401 is the same problem in another form: one ban at two levels of detail.
3. **A law and its regulation, or two laws, at the unified Republic's area.**
   - Both instruments remain in force, but they share one place, so the later one's state becomes `today` and the earlier rule reads as replaced: YG-371, YG-408, YG-414, YG-415, YG-422, YG-439 and YG-446.
   - Not returned where the later text covers the earlier one: YG-365 and YG-409.
4. **Different measures in one group:**
   - a count and a density (YG-286);
   - credit, debit and all cards, and a change (YG-279);
   - users and subscriptions (YG-560);
   - mobile internet and all internet (YG-551);
   - wheat and all food imports (YG-502);
   - a figure and a qualitative state (YG-513, YG-551, YG-555, YG-561).

   Step 2b labels measures by their figure (`pass2/notes-4.md`), so every difference in what is measured becomes a state of one axis.
5. **Condition names that join two questions.** The group's own wording often shows it. Returned:
   - "must or do" (YG-423);
   - "available, and where" (YG-509);
   - "issued and honoured" (YG-525);
   - "reliable … and where it reaches" (YG-552);
   - "the providers, and who controls them" (YG-556);
   - "what wholesalers prefer" (YG-521);
   - "and how many have access" (YG-561);
   - "licensed and registered" (YG-371);
   - "whether integration code exists" (YG-237).

   YG-502 also joins "whether markets are supplied". Not returned: "may be sold and used, and is available" (YG-559), whose parts sit at different places.
6. **Coarse labels hide the sizing.**
   - Where step 2b gave one coarse label to rows that answer different questions, the axis looks sound, but the group is still too wide:
     - YG-508: "few use it" covers a share of e-money value, a lack of know-how and low use;
     - YG-511: "low" covers how widely, what for and by whom.
   - YG-307 (delivery apps) gave up "what it delivers" the same way (`pass2/notes-3.md`). It is not returned, because its rows now agree.
7. **Procorners's per-store posts sit at one service.**
   - Item 086 is its post on buying from Alibaba, item 087 from SHEIN and item 088 from Noon. Each also shows excerpts of its other posts (Amazon, AliExpress, eBay, iHerb).
   - Every row goes to Procorners's service, so the posts' terms add up or compete in YG-315, YG-331, YG-337, YG-340, YG-342, YG-343 and YG-344. Returned: YG-331, YG-342 and YG-343.
   - One condition per store, or one label per post with the store in note, would settle all seven.
8. **Year-only dates.**
   - Item 046 (BTI, dated "2026", shown) ties with every 2026 row at its place. That makes three of the nine disputes in `today`: YQ-D201 with YQ-D530 (YG-402), YQ-D191 with YQ-E649 (YG-473), and YQ-D193 with YQ-E507 (YG-475).
   - Its rows sit in 15 groups of this range.
9. **Rows about several parties at `place not stated`.**
   - Such rows keep their grouped place and add up there as lists, for example YQ-E009, YQ-E583 and YQ-F078 in YG-237.
   - The rules allow no fix short of one row per provider.
10. **A rule beside practice.**
    - A rule goes to its authority's area, and reports of practice keep their area. So a rule and a report on one subject sit at different places: YG-422, YG-559, and the split between Houthis' area and Houthi-controlled areas in YG-473 and YG-475.
    - The parts overlap by design, so none is returned on that ground.
11. **Dates outside the review's rules** (pass 1 dates; not returned):
    - **YG-512.** YQ-B049 restates the figure for 2019 to 2020 ("ما يقارب 800,000 … ما بين 2019 و 2020"), but it takes its 2026 source date. So `today` shows about 800,000, above the count for 2025-06 of 2,102,484 subscribers.
    - **YG-227.** YQ-F080 (750 million) and YQ-D119 (700 million) rest on the same September 2022 instructions but carry dates a week apart. So a disagreement between sources reads as a change.

## Unsure, not returned

- **YG-224.** YQ-E162 at `place not stated` names licences from two authorities ("by the CBY, and CAC Bank by CBY-Sana'a").
- **YG-238.** "Nearly stopped since the war" (YQ-E829, online payments processed by banks) and "lacking" (YQ-D180, reliable gateways) are close, but they are not plainly the same statement.
- **YG-248.**
  - Floosak's community client gives two credential sets on one date (YQ-F024 and YQ-F025; YQ-F025 is in a file the main class does not call). The two tie in a 2024 case.
  - E-Pay's two community clients list credentials at different detail: YQ-F065 adds webhook credentials, and YQ-F053 does not.
- **YG-291.** The group also joins the fast payment system and the real-time gross settlement system. It is returned only for YQ-D175.
- **YG-292.** "None" (YQ-E231), "difficult" (YQ-E663, YQ-E555) and "almost none between banks and wallets" (YQ-B050) may be one state in different words. YQ-E663's label adds a reason ("for lack of national infrastructure") that its quotes don't give.
- **YG-300.** YQ-C560 ("for all customers in the capital Sana'a") is labelled "available", while rows of the same scope at Yes Media, Anayees and Dakhm say "available inside Sana'a". This has no effect on the axis.
- **YG-301.** "Cash on delivery, preferred by many" (YQ-E752) sits between "mostly cash on delivery" rows. It is weaker, not contrary.
- **YG-302.** YQ-C486's label "the Rasidi service" leaves out the cash on delivery that its quote also names.
- **The Procorners pattern without a return.**
  - YG-315, YG-337 and YG-344 differ only in detail, or may be offers bound to a time.
  - In YG-340, free delivery against delivery costs is the same post's own contradiction (group note).
- **YG-365 and YG-409.** The later law covers the earlier list or rule.
- **YG-395.** "Prime Minister in Sana'a's area" stays apart from Houthis' area, because no cited source names him with a body grouped there (`places.tsv`). Its label matches, so this has no effect.
- **YG-401.**
  - YQ-B067 (decision 10) is at the seatless "Prime Minister's area", while YQ-F131 is at Houthis' area.
  - Cited sources use the bare title for Aden's prime minister (YE-A059) as well as Sana'a's (YE-B293), so the one-area limit keeps it apart. Not a rule 5 return.
- **YG-403.** "Banned" (April 2025) and "banned and enforced by designations" (June 2025) hold together, but the axis records a development that a source dates.
- **YG-467.** "File the 2019 return by 30 April 2022" and "renewed automatically every three years" may answer two questions: how a business gets the certificate, and how it is renewed.
- **YG-498.** "IRG-controlled ports" (YQ-D418) and "government-controlled ports" (YQ-E361) carry the same report at two ungrouped places. No single source uses both names, and "government" is not strictly "IRG" respelled.
- **YG-507.**
  - YQ-E664's "mostly cash and cheques" sits between "mostly cash" rows. It may not be the same statement, since it is about cash and cheques together.
  - The undated YQ-E575, "entirely cash", cannot become `today`.
- **YG-523.** "Unpaid" (YQ-E416) and "in arrears up to four months" (YQ-E491) at the internationally recognized government's area are one state at different detail. The axis stands anyway, on "suspended" at Houthis' area.
- **YG-557.** "The Northern region" stays apart, because it is not a variant of "the North".
- **YG-559.** A rule against practice, at different places by design.
- **YG-561.** Aden's YQ-E398 ("15-hour daily blackouts", throughout 2025) ties at year precision with YQ-E494 (December 2025) in a past case. The figures differ, so this may be a real difference.
- **YG-478 (returned under rule 5).**
  - "The north" is the same word as "the North", so a variant needs no source. But step 2a kept it apart because no cited source uses it for the Houthi-controlled areas.
  - If any cited source uses "the north" for a different area, the one-area limit applies and the return falls. I found none.
  - Item 271 itself uses "الشمال" for the zone where the dollar costs 531 rials against 1,554 in the south (YE-E1285), and where the Sana'a bank's ban keeps the old notes stable (YE-E1288).
  - Other quotes use "the north" for the Houthi side too: YE-D477, YE-E1090 and YE-E1308.

## Second review

This round reviews the axes at commit `71ab056`. I checked that `axes.tsv` has sha256 0b7ef7ade6e5e96be8790a219a9d2581cd4681921dae243f9348cdae748f03aa. The 45 axes listed in `changed-2.txt` are renumbered, and all of them rest on rows from YG-224 to YG-561.

### What was read

- **`brief.md`, again,** for two new rules:
  - rule 2's new sub-bullets: lists that grow, instruments in force together, and parts of one source;
  - step 2b's new label line on one thing at different detail.
- **`notes.md`, section "Review round":** how the fixes were made, the fixes by group, and the returns not followed.
- **The current tables:** `axes.tsv`, `groups.tsv`, `states.tsv`, `constants.tsv` and `places.tsv`. I compared them with the same files at commit `233a74c`, which the first review read, to see each row's change.
- **Quotes:** from `conditions.tsv` and `citations.tsv`.
- **Nothing else.** I opened no evidence file and edited nothing under `studies/` or `evidence/`.

### Results

Step 2a followed every first-round return in this range, either in full, in another form or in part. Each fix removed the breach it named. The nine disputed parts in `today` that the first review found are all gone. None of the 45 axes has a `disputed` or `unknown` part in `today`.

| Outcome | Axes |
|---|---|
| Resolved, nothing left | YA-112, 115, 125, 127, 146, 162, 164, 169, 177, 181, 185, 193, 195, 198, 230, 231, 239, 240 |
| Still breaks a rule: `returns-2b.tsv` | YA-108, 118, 123, 124, 159, 163, 165, 170, 175, 178, 197, 206, 209, 232, 233, 241 |
| Label wording only | YA-153, 205 |
| Unsure, not returned | YA-110, 129, 151, 180, 234, 235, 236, 237, 238 |

**The returns.** The 16 returns are in `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/y-review/returns-2b.tsv`: 11 under the label rule and 5 under rule 2.

- **Eleven matter more,** because the axis shows a change or a measure that no source states, or `today` carries another condition's fact: YA-108, 118, 123, 124, 165, 170, 175, 197, 206, 209 and 241.
- **Five matter less.** In YA-159, 163, 178, 232 and 233, `today` is right, but the axis exists only because rows word one state differently.

Several of the remaining breaches come from fixes that followed my first returns as written, or from rows those fixes left behind:
- **YA-206.** My first return put YQ-D190 with reliability.
- **YA-241.** My first return joined grid supply with access to electricity.
- **YA-165.** My first return listed YQ-E196 under public revenue generally.
- **YA-123.** My first return proposed the site's whole card list as the shared label.
- **YA-209.** The fix relabelled YQ-E436 but left YQ-E366, which gives the same figure.

**The two label-wording cases:**
- **YA-153.** YQ-E536's label keeps "at one store selling Shein and Amazon goods". Those are words about the place, which the build now adds at the EB store's service.
- **YA-205.** YQ-E826 gives 26.7 percent but is labelled "27 percent", which is the label of YQ-E121's different 2017 figure.

**Unsure, not returned:**
- **YA-110 (YG-229).** The axis rests only on Jawali's "matched in guarantee accounts", against "pre-funded and held in a pooled account at a settlement bank" elsewhere. If Jawali's guarantee accounts are pooled accounts at a settlement bank, the rows need one label. Jawali's terms don't say where the accounts are held.
- **YA-129 (YG-291).** The group still joins the fast payment system and the real-time gross settlement system. No part conflicts now.
- **YA-151 (YG-343).** The Noon post's "through transport offices" (YQ-C553) stands against the Alibaba and SHEIN posts' next-day delivery from the Sana'a warehouse. These may be processes for different stores, as in YG-342, or a change in 2023.
- **YA-180 (YG-483).** "Only those loyal to the powerholders" and "licences granted to traders loyal to the Houthis" state one rule at two places. The parties-named line allows naming the Houthis.
- **YA-234 (YG-670).** "The buyer, from the provider's app" (E-Pay) and "the buyer, from the buyer's own wallet app" (YemenPay) both answer yes. Which app it is may be part of the state, as the group's `what_varies` has it.
- **YA-235 (YG-704).** "Extra fees demanded by officials" and "bribes and continuous levies on transport companies" both answer the group's only state, "demanded", at different places. The labels name who pays and what.
- **YA-236 (YG-713).** The move from "removal ordered" (February 2026) to "being closed" (April 2026) is a development that a source dates. YQ-E484's label still carries "illegal checkpoint tolls", which is YG-486's fact.
- **YA-237 (YG-719).** Two rows state account holding without a figure, rather than access: YQ-D099 ("most have accounts", a bank manager's claim) and YQ-D213 ("private bank accounts are the exception"). My first return put them here. YQ-D099's contrary claim is a dispute its source makes.
- **YA-238 (YG-722).** "Sparse" (YQ-E706) may be "coverage gaps" in other words.

### Returns step 2a didn't follow in full

- **YG-224, cumulative labels not used.** The reason holds. No row states the whole list at each date, and the new sub-bullet on lists that grow gives each decision its own condition, as the fix did.
- **YG-243, followed in another form.** The reason holds, since rule 3 puts each row in one group. The label of what both pages state matches the new label line.
- **YG-310, transport links not split from roads and fuel.** The reason holds: YQ-E135 and YQ-E145 each state all three.
- **YG-446, importers' registration not split.** The reason holds for the split, because every such row also states a threshold. But the new label line would still keep the importer clause out of YQ-E857's label (YA-170).
- **YG-502, market supply not split.** The reason holds, and the labels now give the change only.
- **YG-508, YQ-E226 sent to its own condition rather than YG-510.** The reason holds and my suggestion was wrong: e-money's share of all payments (YQ-E225) is a different measure on the same date.

### Constants made from the returned groups

Each split kept its conditions whole, except:
- **YG-659 and YG-660 are probably one instrument.** YE-E178 says the CBY issued Circular No. 11 of 2014 "In late 2014" for the bank-led e-money model. YE-E655 dates the CBY's "new mobile banking regulations" to 11 December 2014. If they are one instrument, YQ-E589 belongs in YG-659, under rule 1.
- **YG-654 and YG-655 both give SBYB's and IBY's licences.** YQ-E195's early-2021 permissions ("such as IBY, SBYB, One and Tamkeen") repeat YQ-E163's January licences. The two constants agree, so this is a note only.
- **YG-659 lacks the Sana'a side.** YQ-E881 says Circular No. 11 stays in force there, but the row sits in YG-661, whose label still carries "with Circular No. 11 of 2014 still in force".
- **YG-672 (credit cards) lacks YQ-E160's 1,206 for 2019.** That figure is in YG-279's label, which is YA-124's return.
- **Two labels the splits left behind no longer answer their new conditions:**
  - YG-631 ("Who uses phone wallets") keeps "low" for YQ-E546, whose source limits use to the launching banks' customers.
  - YQ-E223 keeps "low" in YG-630 ("What buyers use phone wallets for", YA-223, which is on part 1's list), though its source names the uses.

### Disputed parts

- **In today:** none of the 45 axes has one. The ten axes that do (YA-01, 05, 20, 60, 61, 63, 66, 74, 225 and 226) are outside this list.
- **Past states that tie:**
  - **YA-238 on 2023-09-14** ("sparse" and "widely available"). Its source makes this dispute: one article says both.
  - **YA-197 in 2022** ("12 percent of adults", "8.8 percent" and, at year precision, "10 percent"). The sources don't make this dispute: they measure adults on one side and the whole population on the other. This is YA-197's return.
  - **YA-209 at Aden in 2025.** "15-hour daily blackouts throughout the year" ties with the October and December figures. These cover different spans of time, so they are not a dispute.

## Third review

This round reviews the axes at commit `f3ed2df`. I checked that `axes.tsv` has sha256 02850db51259fb99cdb706c2f5b7580c2136a5c0cb98c3238b2b9166e6812375. It covers the nine axes listed in `changed-3-2.txt`.

I read three things:
- `notes.md`, section "Second review round";
- the current tables, compared with the same files at commit `71ab056`;
- the rows' quotes in `citations.tsv`.

I opened no evidence file and edited nothing under `studies/` or `evidence/`.

**Second-round returns.** Step 2a followed all 16 second-round returns in my range. Each fix removed the breach it named:
- **Four groups are still axes:** YA-104 (YG-225), YA-114 (YG-247), YA-119 (YG-278) and YA-120 (YG-279).
- **YG-432 is still an axis, YA-159.** YQ-E196 moved out to its own constant, YG-736.
- **Three groups are still axes:** YA-164 (YG-446), YA-189 (YG-513) and YA-200 (YG-561).
- **YG-513's split made a new axis, YA-227 (YG-737).**
- **Eight groups became constants:** YG-401, YG-422, YG-473, YG-480, YG-552, YG-665, YG-668 and YG-728.
- **Three groups split off as constants:** YG-736, YG-738 and YG-739.

**Still a breach.** One row, YA-200, is in `/tmp/claude-0/-home-user/9f45def8-b710-5f9c-84f3-6a0fa7e617c8/scratchpad/y-review/returns-2c.tsv`, under the label rule.
- The fix gave YQ-E366 and YQ-E436 the label "prolonged outages". YQ-E379 gives the same up-to-20-hours outages and comes from YQ-E366's own source, but it keeps "outages up to 20 hours a day".
- This matters little. YQ-E379 sits at another place ("Aden, Hadramawt and other areas"), so `today` shows no change that no source states. It still breaks "word for word".

**The disputed part in `today`.** YA-227's disputed part is made by its sources. Both rows are 2022 figures for the whole population, and they tie at year precision:
- YQ-D365: "about 8.8 percent of the population owned an account of any type";
- YQ-E661: "Ninety percent of the population is unbanked".

The two figures can't both hold, so the dispute stands.

**The return step 2a followed in another form.** This is the second round's YA-159 (YG-401), and its reason holds. Step 2a opened the archive entry for YQ-B067 and found that it links the file of decision No. 10 of 1446, the decision of YQ-F131. So YQ-B067 states that decision, which bans American goods, and takes the label all the rows state. The alternative, "goods boycotted under decision 10", would misname YQ-E358's directive of 23 April 2025, which came before the decision.
