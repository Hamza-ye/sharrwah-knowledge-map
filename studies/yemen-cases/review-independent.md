# Independent review of Stage 1: Yemen's axes and cases

An independent review, 17 October 2026, by an agent that produced none of Stage 1.

**Reviewed.** The files at commit `e894f8d`. HEAD is now `f913355`, which changes only `STATE.md` and the capture list, so the study files are the same.
- `axes.tsv`: sha256 `47b5c642765d2e25db20f0795fceebbce3e175a6ffdfa884271f005dadf8c735`, the file the third axes review let through.
- `cases.tsv`: sha256 `74ed252adb0287885a9afce407751378f1b50d2ef65b62009f442981289dfd74`.

**What I read.**
- `brief.md` and `questions/Q2-yemen-stress-test.md`.
- The outputs: `axes.tsv`, `constants.tsv`, `cases.tsv`, `unknowns.tsv`, `notes.md` and `review-axes.md`.
- What they rest on: `conditions.tsv`, `citations.tsv`, `groups.tsv`, `states.tsv` and `places.tsv`.
- Evidence under `evidence/yemen/`, wherever a quote left a question open. Each opening is named in the finding it supports.

**What I did not read:**
- `PLAN.md` and `STATE.md`;
- `method/`, `pass1/`, `pass2/`, `review/` and `first-run-stopped/`;
- `evidence/yemen/README.md` and `finding-aids/`.

All checks were scripts of my own, kept outside the repository and run with `python3 -I`. No file but this one was changed.

## Verdict

**Not yet.** The files are mechanically complete and well cited. Every state, `today` part, constant and case cites evidence that exists. Every quote is found in its file. YC-00 equals every axis's `today`.

But `today`, the anchor, is wrong or misleading on axes at the centre of Q2's examples:
- **Bank bans.** The 2024 bans on banks are shown as standing, though four sources report them cancelled on 23 July 2024 (YA-25).
- **Old notes.** The withdrawal of pre-2016 notes is shown as in force, though the evidence gives only a decision with a 60-day window (YA-15).
- **Exchange rates.** Stale rates sit beside current ones under overlapping place names (YA-01, YA-03).
- **PayPal.** PayPal shows as `Available`, which hides the only evidence on receiving: Yemen is send-only (YA-62).

Six of the 23 `in force` cases are not in force by the evidence's own dates or words.

In my sample of 45 axes:
- 12 have an error that changes `today` or a case in a way a marker would act on;
- 10 have minor faults;
- 23 are faithful.

Marks made against YC-00 now would inherit these errors.

**Before phase D,** do the eight things listed at the end: they fix findings 1 and 3 to 7, and YA-40's unknown from finding 8. Then rebuild and check the changed axes. Until finding 2 is fixed by method, markers should read each `today` part with its date in the axis's `note`, and treat a part as stale where a later part names the same ground. With that done, the cases can carry the pilot's marks. The rest can follow.

## Findings, ranked by how much each would mislead

### 1. YA-25: the 2024 bank bans are shown as standing, though the evidence says they were cancelled

**What `today` says:** "6 Sana'a-based banks barred @ Central Bank of Yemen's area + 13 Aden-based banks barred @ Houthis' area", beside "both sides' bans on banks cancelled" at two other places. A reader marking which partners a platform can use sees the bans in force.

**What the evidence says.** Four sources give the cancellation, and the same reports give the bans:
- YE-E654 (item 192, 23 July 2024): "He said the agreement included cancelling all recent decisions and procedures against banks by both rivals and refraining in the future from any similar procedures."
- YE-E467 (item 163): "Both the Houthis and the government agreed to reverse recent measures taken related to banks, including the CBY-Aden’s revocation of the licenses of six entities based in Sana’a".
- YE-D713 (item 085, 2025): "However, the decision was canceled later following external mediation."
- YE-E934 (item 249): "Some restrictions were partially reversed in July 2024 under a de-escalation agreement between the IRG and Houthi authorities."

**Why the build gets it wrong.** Three faults combine:
- **`holds` is inconsistent.** YQ-E586 is `held`, though its own source, item 192, reports the cancellation (YE-E652 and YE-E654). Its twins YQ-D537 and YQ-E722 are articles of the same day with the same structure, and they are `ended`.
- **A year-only date ties.** YQ-E793 has `2024` (YE-E933: "In response, HC-CB banned dealings with 13 Aden-aligned banks"). It ties with the `ended` row YQ-E723 of 23 July 2024, so "barred" stays at the Houthis' area.
- **The cancellation sits at a joint place.** It is placed at "the Yemeni government's and the Houthi group's areas" (YQ-D539, E587, E721), which supersedes neither side's own area.

**Fix:**
- make YQ-E586 `ended`;
- give the agreement to each side's area, since it is both sides' rule;
- date YQ-E793 within 2024 as its source allows, or drop it as `today` against the dated cancellation.

All 350 cases carry the two wrong parts. The three cases that vary YA-25 (YC-115, YC-289, YC-345) replace only the government's-area part.

### 2. `today` keeps stale and contradictory parts for overlapping place names and for `place not stated`

**The rule that causes it.** `today` takes the latest state for each place name. Sources name the same ground many ways, and a part for one name is never superseded by a later part for a wider name that includes it. The result is that `today` reads as if old states still hold.

**Currency (YA-01).** `today` has six parts for the government's side:
- "YER 1,562 buying, 1,567 selling @ Aden" (10 October 2026);
- "over YER 1,800 @ Aden and areas under the Yemeni government's control" (28 June 2024; YE-D685: "surpassing 1,800 rials per US dollar");
- "over YER 1,768 buying, 1,776 selling @ Aden and the occupied governorates" (1 June 2024);
- "YER 1,560 @ areas controlled by the legitimate government", "YER 1,628 @ government-controlled areas" and "YER 1,562 @ the new-rial zone".

**The official rate (YA-03).** `today` shows "official rate YER 250 @ place not stated", which is mid-2017. YE-B046: "كانت قيمة الريال حينها تساوي 250 ريالاً للدولار الواحد وفق السعر الرسمي."

**Electricity (YA-200).** `today` shows "over 20 hours a day of supply @ Aden" (February 2026; YE-E415). Beside it are two later parts that name Aden:
- YE-E394: "Since May, Aden, Hadramawt, and other areas had endured up to 20 hours without power each day."
- YE-E393 and YE-E392: "In Aden and other cities under the control of the internationally recognized government, electricity supplies increased slightly starting in mid-June." "Blackouts have reportedly been cut to six hours for every two hours of supply."

**Other axes.**
- YA-56: fees between the zones of "About 30% or more" (2020, three places) sit beside "Up to 180% @ Sana'a and Aden" (July 2026).
- YA-20: "disputed @ Aden" (February 2026) sits beside "short @ the internationally recognized government's area" (March 2026).

**Scale.** 86 of the 766 parts in `today` are dated before 2023. Many are laws still in force. Some are stale market facts, such as YA-56 and YA-57 (2020), YA-120 (2019) and YA-204's "new notes in use @ Aden" (2019).

**Fix (a method change):** mark a part as superseded when a later state's place names it, or when the two places are on record as covering the same ground. Until then, markers must read each part's date.

### 3. YA-15: the withdrawal of pre-2016 notes is shown as in force in the government's area

**What `today` says:** "notes printed before 2016 withdrawn @ the internationally recognized government's area" (1 June 2024). It rests on two rows, both `held`:
- YQ-B003, YE-B002: "قرار إلغاء التعامل بالعملة النقدية المطبوعة قبل العام 2016م";
- YQ-D054, YE-D060: "سحب الطبعة القديمة من العملة".

**What the evidence says.** Three sources, one of them B003's own file, give the decision a 60-day window:
- item 012, line 34: "توريد العملة القديمة ما قبل 2016م إلى بنك عدن خلال ستين يوما";
- F12, line 64: "إلى سرعة إيداع النقود الورقية من الطبعة القديمة التي تعود لما قبل العام 2016، خلال فترة أقصاها 60 يوماً";
- item 022, line 35: "فيما قضى الثاني بسحب الطبعة القديمة من العملة اليمنية في غضون شهرين".

Both rows' sources are dated inside the window, and no source shows the withdrawal in effect. Under the brief they are `provided for`.

**What `today` would then show** at that area: YQ-C070, the Aden bank's notice that all notes are legal tender. YE-C048: "تعتبر عملة قانونية ملزمة حسب قيمتها كوسيلة للدفع في جميع المعاملات الداخلية في الجمهورية اليمنية."

**`provided for` is never used.** No row of the 2,532 is `provided for` (2,505 `held`, 15 `proposed`, 12 `ended`). Step 2b should check other decisions that carry a deadline.

### 4. Six of the 23 `in force` cases are not in force, and five more are doubtful

Every `in force` case is a disputed state, as rule 8 allows, or a combination. Each one checked:

| Case | State | In force? |
| --- | --- | --- |
| YC-53, YC-54, YC-57 | YA-01: YER 3,000, 2,065 and 2,000 @ place not stated | No. These are 2025 rates. The "dispute" is a precision tie: a year-only "2025" ties with 2 August 2025. YE-D657: "after the exchange rate of the Yemeni Rial had reached 3,000 YER per USD." YE-E719: "During 2024 and 2025, its exchange rate fell from 1,540 rials to the dollar to 2,065." |
| YC-152 | YA-59: "In the currency sent @ Houthis' area" | No. See finding 7. |
| YC-154 | YA-60: Cash, international transfers "Named as a possibility" | No. A planned feature. See finding 7. |
| YC-157 | YA-62: "Available @ Wise's service" | No. See finding 5. |
| YC-89 | YA-05: "floating @ the internationally recognized government's area" | Doubtful. See finding 6. |
| YC-106 | YA-20: "no real shortage, cash poorly distributed @ Aden" | Doubtful. It cites only the economist (YE-E672, E673, E1081). The label's "cash poorly distributed" is the central bank's claim, not the economist's (YE-D068: "وإنما يرتبط بسوء توزيع النقد"), and the same bank reported a shortage in March 2026 (YQ-D283). |
| YC-161, YC-163, YC-304 | YA-64: "91 companies @ Aden", "415 companies @ Sana'a" | Doubtful. Two measures under one label. See finding 7. |
| YC-91, 105, 153, 155, 158, 162, 164, 175, 176, 286, 288, 302 | | Supported, for the date their sources give. |

### 5. YA-62: PayPal shows as `Available`, which hides send-only; Wise's `Available` is inferred

**PayPal.** `today` shows "Available @ PayPal's service". It is built from PayPal's generic Yemen page, YQ-E728. YE-E842: "يلزم وجود حساب لإرسال وتلقي المدفوعات." That page says nothing about whether a Yemeni account can receive.

The only source on receiving is YQ-D634. It is undated, so it can never be `today`. YE-D997: "الدول العربية التي تستطيع إرسال الأموال فقط (أي لا تستطيع استقبال الأموال) عن طريق هذه الخدمة هي: جزر القمر، جيبوتي، موريتانيا، الصومال، اليمن."

For a marker asking whether a platform's merchants in Yemen can be paid through PayPal, `today` answers wrongly.

**Wise.** YQ-E580 is labelled `Available` because a Wise listicle lists Wise among options. YE-E635: "That’s why we have curated the most popular and best payment options for you to use in Yemen." No quote says that Wise serves Yemen. Wise's own terms exclude it (YE-E638 lists Yemen; YE-E639: "send or receive money to or from these countries and regions"). The dispute, and in-force case YC-157, rest on an inferred label.

### 6. YA-05: the dispute in the government's area ignores a later statement, recorded on another axis

**What `today` says:** "disputed @ the internationally recognized government's area", dated February 2026. The two sides of the dispute:
- "fixed and enforced": YE-D067, Al-Ayyam, 13 February 2026;
- "floating": YE-E893, "Government CBY permits the Yemeni riyal to fluctuate in line with market conditions". YE-D666 says the same in December 2025, but its own source goes on (YE-D667): "Re- cently, the IRG of Yemen implemented new measures".

**What later evidence says.** YQ-E427 (24 April 2026) sits on YA-03. YE-E427: "The CBY-Aden also elected to adopt a fixed exchange rate policy, setting the price of one Saudi riyal at YR410, down from YR420."

That row answers YA-05's question and is later than both sides. In-force case YC-89 ("floating") is contradicted by it.

**Inference in the labels.** YQ-E645, E757 and E784 are labelled "fixed and enforced" from "a less volatile rate" and "stabilising the nominal exchange rate" (YE-E894).

### 7. Disputes no source makes, which `today` and the in-force cases present as real

**YA-59 (remittance payout currency, Houthis' area).** YQ-E790 and YQ-E791 come from one paragraph of item 249 that gives them in order:
- YE-E929: "In February 2024, the Sana’a-based Yemeni Money Exchange Association mandated that remittances be disbursed in the original currency sent, such as USD".
- YE-E930: "In March 2024, HC-CB further restricted financial flexibility by requiring all transfers to be disbursed in SAR."

Both were dated to the report, so they tie. The latest the source shows is the March 2024 rule. YQ-D034 (2024) and YQ-E334 (2025) say dollars are not paid out there. YC-152 should not be `in force`.

**YA-64 (exchange businesses).** The dispute sets two measures against each other. The World Bank report gives them as different things:
- YE-D478: "The number of money exchangers in Sana’a rose from 179 in 2014 to 415 in 2023, while the number in Aden rose from 34 to 91."
- YE-D475: "over 170 companies registered with the CBY-Sana’a".

YQ-D351/D352 label the first as "companies". A later report restating it says "exchange companies" (YE-D613, YQ-D431/D432). The labels follow that loose wording, not the report the figures come from, and so the two counts collide.

**YA-60 and YA-99 (Cash).** One paragraph of Cash's listing on ymp.ye (item 001, `data.4.about.ar`) lists services the wallet may add in future:
- "مع إمكانية إضافة العديد من الخدمات إلى المحفظة مستقبلاً", among them "والتحويلات الدولية عبر أكبر شركات التحويلات العالمية (موني غرام , ويسترن يونيون)";
- "وغيرها من الحلول التي ستقدمها الشركة مستقبلاً مثل NFC".

The NFC row (YQ-C043) is `proposed`. The transfers row (YQ-C041, YE-C028: "with the possibility of International Transfers across the largest global transfers companies like (Money Gram or Western Union)") is `held` "Named as a possibility". That makes the dispute at Cash's service, and in-force case YC-154. Make YQ-C041 `proposed`.

`review-axes.md` says each disputed part left in `today` "is made by its sources, or is a tie under the precision rule". That does not hold for YA-59 or YA-60, and holds only loosely for YA-64.

### 8. Held evidence not recorded, which changes a `today` or an unknown

**YA-55 (sending money between the zones).** `today` is "Stopped at exchange companies, open only through Kuraimi @ the liberated areas", from a one-day report of 16 March 2024 (YE-C392, C394). Line 26 of the same file ties the halt to the start of the unified network. Later held evidence is recorded nowhere on this question. Item 249, lines 1028-1030 (February 2026), says of hawala agents:

> "Their ability to operate across frontlines and in remote areas makes them particularly effective in Yemen’s conflict environment. This adaptability has made them indispensable for both household remittances and internal money transfers between the South and North."

Lines 1304-1305 add: "different currency notes in the North and South have fragmented Yemen’s financial system, making internal transfers nearly impossible."

**YA-40's unknown can be closed from held evidence.** The House of Representatives in Sana'a passed the anti-usury bill (YQ-B063). Item 073, line 7226, held and readable, says: "In light of the 2023 Anti-usury law issued by the Sana’a parliament".
- The same report says the law "came into effect in early 2023" (YE-D433).
- The unknown's `why_not_held` itself names line 7226, but gives `who_can` as `founder`.
- Commit `f913355` has queued a capture from inside Yemen for it.
- A pass-1 row from line 7226 would serve. "Sana’a parliament" translates "مجلس النواب بصنعاء", so under step 2a's rule 5 the two names group as a `variant`, and the House's area would no longer be `unknown`.

**What can be cut off overnight: internet shutdowns.** No row records the concrete shutdowns, only "frequent outages" (YK-355, from two general sentences):
- item 153, lines 430-431: "In 2020, the underwater FALCON cable was damaged, leading to a temporary shutdown of 80 percent of Yemen’s internet capacity.";
- item 154, lines 1742-1745: "knocked out power to the country’s primary internet access point, causing a large-scale and complete blackout of internet connectivity for four days in many areas of the country."

### 9. Time-limited and transitional measures shown as standing rules

**YA-210 (expired ID cards).** `today` is "Expired ID cards accepted for one more month @ Houthis' area", from a circular of 14 March 2026. YE-B022: "لمدة شهر إضافي". By its own terms it lapsed around mid-April 2026, and no source shows a later extension. `today` presents it as current in October 2026.

**YA-65 (unclaimed transfers).** `today` is "Report them to the Aden central bank within twenty days". That is a one-off duty attached to the shutdown of the transfer networks (YE-D693: "On June 26th, 2024, the bank issued a decision to completely and permanently cease operations of several local money transfer networks"; YE-D696: "within a period not exceeding twenty days from the specified date"). It is not a standing rule on unclaimed transfers, which YQ-D358 gives as "after two months".

### 10. Inference in labels and states

- **YA-40.** "allowed @ the internationally recognized government's area" (YQ-E417, E450) is inferred from treasury-bill offers. YE-E434: "it was supposed to sell one-year treasury bills". Item 162, same line: "While the outcomes of the auctions were not announced". No source says interest is allowed there.
- **YA-190.** "1 percent" is computed from "99% of women" unbanked (YE-D426).
- **YA-227.** "10 percent" (YQ-E661) is computed from "Ninety percent of the population is unbanked" (YE-E738). It then ties with 8.8 percent and makes a dispute.
- **YA-160.** YQ-F162's state gives fuel at 5 percent, cigarettes 90, qat 20 and telephone services 10 percent. Its OCR quotes show ")40(" for fuel (YE-F457) and name the other items without rates (YE-F467 to F470). The label, "5 percent", is supported.
- **YA-05.** See finding 6.

### 11. YA-105: a later news report overrides the instrument it reports

**What `today` says:** "a joint-stock company with paid-up capital of at least 500 million rials, 700 million for a system operator". That is the news report YQ-D119 (YE-D117: "ولمشغل نظام الدفع عن 700 مليون ريال"), published 21 September 2022.

**What the instrument says.** The Aden central bank's instructions of 13 September 2022, which the report describes, give 750 million. YE-F135: "ولمشغل/مدير نظام الدفع عن سبعمائة وخمسون".

A disagreement between a report and its own source reads as a change over time, and the instrument's figure becomes an `occurred` case.

### 12. YA-75: the list of wallets in `today` is from 2019, while the 2026 list sits on another axis

**What `today` says:** "Mobile Money, Quality Connect and M Floos @ Sana'a and the governorates under the Supreme Political Council and the National Salvation Government". That is the Sana'a bank's 2019 list of wallets that took in the banned notes (YE-B032). Beside it is "Yemen Wallet being rolled out @ Houthis' area" (2025).

**Where the best list went.** The founder's capture from inside Yemen of the central bank's list of 16 wallets, YQ-A003 (10 October 2026), is grouped into YA-214, "How many phone wallets there are". Rule 1 puts it on the axis whose question it answers by name.

**The seat.** YQ-A003's place is kept seatless, although `unknowns.tsv` itself calls `centralbank.gov.ye` "the Sana'a central bank's pages".

### 13. Axes with no alternatives

The states of these axes hold together, at different detail or for different things:
- **YA-85:** "three at most" against "three, each on a different mobile number". The brief's label rule gives them one label.
- **YA-95:** a 48-hour acknowledgement against a 10-day decision.
- **YA-30 and YA-165:** a law and a decision or a guide stating the same rule.
- **YA-155:** a ban and its enforcement.
- **YA-170:** duties on different goods: grain at one port in 2020, clothing in 2024, general levies in 2026.
- **YA-205:** a list that grows, 3 suspended on 27 June and 12 more on 4 July. It builds an `occurred` case in which only the first three are suspended.

None of these changes YC-00 except YA-205. They add axes that a marker will look for variation in, and find none.

### 14. Places, minor

- **kibanks.com.** YQ-C400 places it at "Kuraimi Islamic Microfinance Bank's service". Step 2b added "Kuraimi Islamic Bank's service" for the same site (YQ-C397, C398, on YA-35).
- **Seatless "Central Bank of Yemen's area".** It also holds Cash's terms citing the Sana'a bank's Decision No. 1 of 2020 (YQ-C112, YA-85).
- **The House of Representatives in Sana'a.** It stays its own place, which gives YA-40's `unknown` part. See finding 8.

### 15. Quotes and dates, minor

**Quotes.**
- All 4,052 quotes are in their files:
  - 3,761 under the brief's stated normalisation;
  - 169 more after Unicode compatibility folding of Arabic PDF text and bidi marks;
  - 77 more after JSON decoding or tag handling.
- 45 quotes, all in part B, are not byte-verbatim. They drop tatweel (ـ), use straight for curly quotes, or (YE-B298) a hyphen for an en dash.
- Line locators check out: 3,540 of 3,548 point at their quote. The other 8 are code or table cells.

**Dates.**
- YQ-C207 dates a ONE Cash marketing line about cash ("التي أصبحت هذه الأيام تتوفر بشكل محدود") to the capture day as a "live page". The line describes the market, not ONE Cash's own service, and the page metadata says published 2020-08-31, modified 2025-06-04. `today` (YA-20) is unchanged by it.
- YQ-C080 rests on a spun blog paragraph (item 004 of the operators run, line 59): "قام البنك المركزي اليمني صنعاء بتحديد سعر صرف العملة الجديدة". It is not `today`.

## The six questions

### 1. Done when

**Mechanically, yes.** Each check was run on every row:
- **Axis states.** 227 axes, 1,047 state labels: each carries cite ids, and each id is one of the 4,052 citations.
- **`today`.** 766 parts: each is a state on its axis whose cites are in `today_cite_ids`, or `unknown @` (5) or `disputed @` (10).
- **Constants and cases.** 512 constants and 350 cases: each carries cite ids, all of which exist.
- **YC-00.** It equals every axis's `today` (227 of 227).
- **Rows.** All 2,532 pass-1 rows have a state, sit in exactly one group, and sit on exactly one axis or constant.
- **Unknowns.** The 5 `unknown` parts are the 5 rows of `unknowns.tsv`.
- **Quotes.** See finding 15.
- **The build.** I re-derived each place's latest state from `states.tsv` and `conditions.tsv`. It agrees with the build everywhere I modelled the rules. I checked across-Yemen supersession and the proposed-only places by hand (YA-20, YA-41, YA-56).

**By reading, mostly.** The sampled citations exist and say what is quoted. Where they fail, it is labels that say more than their quotes (finding 10) and `holds` values that the quotes contradict (findings 1, 3, 7).

Items with no citation:
- 53 items of the cited-sources run, 20 of the Sana'a rules run and 10 of the operators run carry no citation.
- I opened the 14 that looked on-topic: Payoneer, PayPal, Visa, STC Pay, Jaib, Salla, three Shopify pages, FATF, the Remittance Prices page and three Aden central bank pages.
  - Thirteen are failed fetches or say nothing of Yemen.
  - Item 066 is the Aden bank's headline list. Its licence suspensions are cited from three other copies of the same list (YK-383).
- The Sana'a bank's pages (items 001 to 010 of the rules run) hold no text, and the Saba pages hold only a security check.

### 2. Faithfulness

**How the sample was chosen.** I took every fifth axis by number, YA-05 to YA-225: 45 axes. Before choosing, I had printed YA-01 to YA-03 to learn the format and listed the `in force` cases. The rule is by position, so neither could steer it. For each axis I read every row's pass-1 state, label, place, `holds`, date and quotes, and opened the source wherever a quote left a question.

| Result | Axes |
| --- | --- |
| Misleading: `today` or a case is wrong (12) | YA-05 (finding 6), YA-15 (3), YA-20 (4, YC-106), YA-25 (1), YA-40 (8, 10), YA-55 (8), YA-60 (7), YA-65 (9), YA-75 (12), YA-105 (11), YA-200 (2), YA-210 (9) |
| Minor: no effect on `today` (10) | YA-10 (its two states can hold together), YA-30, YA-85, YA-95, YA-155, YA-165, YA-170, YA-205 (13), YA-160, YA-190 (10) |
| Faithful (23) | YA-35, 45, 50, 70, 80, 90, 100, 110, 115, 120, 125, 130, 135, 140, 145, 150, 175, 180, 185, 195, 215, 220, 225 |

**Parts of `today` that are not the latest state the evidence shows for their place:**
- YA-05: the government's area;
- YA-15: the government's area;
- YA-25: the Houthis' area and the Central Bank of Yemen's area;
- YA-55: the liberated areas;
- YA-75: Sana'a and the governorates of the Supreme Political Council;
- YA-105: the government's area;
- YA-200: Aden;
- YA-210: the Houthis' area, lapsed.

The other sampled parts are the latest for their place.

### 3. The cases

**YC-00** matches every axis's `today` exactly. It is as faithful as those `today`s, so findings 1, 2, 3, 5, 6, 8, 9, 11 and 12 are all errors in YC-00. Each such error is also in every further case that keeps that axis at `today`. For YA-25, that is all 350 cases.

**The `in force` cases.** All 23 were checked (finding 4): 12 hold for their sources' dates, 6 are not in force, and 5 are doubtful.

**The other cases:**
- 326 are `occurred` and none `provided for`. That follows from finding 3: the category is never used.
- The 61 combination cases are each built from one source and one date, as rule 7 says. YC-302 differs from YC-00 only by dropping one part of YA-11.

### 4. The unknowns

All five rows say what would show the state, who can close it, by what route, what was read (each path, and whether it could be read), and why the state isn't held. The read lists check out where I tested them. For instance, items 011, 021 and 061 of the Sana'a rules run (saba.ye) hold only a security check.

**One `who_can` is wrong.** YA-40 says `founder`, but held evidence closes it (finding 8).

**Two unknowns come from the place model, not missing evidence:**
- YA-40: a legislature's own area;
- YA-88: a rule with no authority, whose only row ended.

Neither is wrong under the brief, but a reader should know these places duplicate ones that `today` already answers.

### 5. Q2's example axes

| Example | Axes | Constants | What the evidence holds that none covers, or hides |
| --- | --- | --- | --- |
| What the law allows | YA-15–17, 21, 23, 25–30, 32, 40, 44–46, 51, 63, 65, 84–85, 88, 93, 95, 102–106, 150–157, 160–168, 172, 176–177, 199, 205, 210–211, 217–218 | YK-17–28, 39–45, 64, 70–76, 87, 95, 100–110, 122–130, 159, 200, 209–304 (register, companies, consumer protection, tax and zakat; YK-273: no e-commerce law), 341–350 (cybercrime bill, electronic transfers and signatures, crypto), 364–394, 436–448, 464–467, 472–480 | Nothing found beyond findings 3 and 10 |
| Which partners will work with a platform | YA-25, 26, 31, 41, 43, 60, 62, 107, 109–118, 143–144, 217 | YK-21, 24, 27, 46, 131–158, 161–162, 311, 335, 369–392, 450 | PayPal's send-only is recorded but can't reach `today` (finding 5). The bank bans' cancellation is recorded but doesn't reach `today` (finding 1). |
| What the payment rails can do | YA-47, 51–57, 68–74, 77, 86–87, 98–100, 108, 112–114, 116–132, 186–188, 212–213, 219 | YK-56–60, 77–171, 342–345, 504–505 | The 2026 statements on transfers between the zones are not on YA-55 (finding 8) |
| The currency situation | YA-01–24, 59, 149, 166, 201–204, 226 | YK-01–16, 56, 59–60, 143, 164, 350, 363–368, 407 | Covered, but `today` misleads (findings 2, 3, 6) |
| What can be cut off overnight | YA-12, 25, 32–34, 38–39, 41, 43, 155, 174–175, 182–183, 197–200, 202, 205, 207, 213, 224 | YK-17–20, 102–103, 152, 355, 360, 369–394, 396, 401–404, 504, 511 | The documented internet shutdowns of 2020 and January 2022 (items 153 and 154; finding 8) |

### 6. Anything else that would mislead

These are findings 2 (places), 7 (disputes no source makes), 9 (dates of time-limited measures), 10 (inference) and 13 (axes that don't vary). The most general is finding 2. The states use 188 distinct places, and `today` lists the latest state per place name, not per ground. A reader who takes a `today` as one picture of the market will mistake old states for current ones.

## What must be fixed before phase D

1. **YA-25:** make YQ-E586 `ended`, place the July 2024 agreement at each side's area, and settle YQ-E793's year-only date (finding 1).
2. **YA-15:** make YQ-B003 and YQ-D054 `provided for` (finding 3). Check other decisions with a deadline for the same fault.
3. **YA-59:** date YQ-E790 and YQ-E791 by the source's own sequence. **YA-60:** make YQ-C041 `proposed`, as YQ-C043 is. **YA-64:** relabel the money-exchanger counts. Then YC-152, YC-154, YC-161, YC-163 and YC-304 change (finding 7).
4. **YA-62:** label PayPal by what its page shows, and give YQ-D634 a basis that lets send-only stand. Relabel YQ-E580, which states no availability (finding 5).
5. **YA-05:** put YQ-E427's statement of policy on YA-05 (finding 6).
6. **The `in force` basis:** don't let markers treat YC-53, YC-54 and YC-57 as in force. They are 2025 rates at `place not stated` that are disputed only by a precision tie. Whether a precision tie should make a dispute at all is for the coordinator to decide; as built, it does.
7. **YA-40:** change `who_can` and add the pass-1 row from item 073, line 7226 (finding 8), so the founder is not asked for it.
8. **Reading `today`:** until finding 2 is fixed by method, tell markers to read each part's date and to treat a part as stale where a later part names the same ground.

**Can follow:**
- the rest of finding 8 (YA-55 and the internet shutdowns), and findings 9, 10, 11 and 12;
- the axes that don't vary (13);
- the minor place and quote faults (14, 15).

## Check of S-01's axes

**Checked, 17 October 2026.** The axes and constants that phase D's `studies/subjects/S-01/bears-on.tsv` names, at commit `900c24a` (`axes.tsv` sha256 `ef7e2d6c70aae0e46218cc95c1dd9e14c15a8beec43428f7fe1e69d1f4837f06`):
- axes YA-27, YA-62, YA-126, YA-128, YA-130 and YA-131;
- constants YK-22, YK-23, YK-24, YK-161, YK-167, YK-184, YK-203, YK-206 and YK-513.

**How.** For each one I read every row's pass-1 state, label, place, `holds`, date and quotes, and opened the source where a quote left a question. I also checked the 9 cases that vary these axes: YC-120, 121, 155, 200, 201, 203, 309, 336 and 339.

**Result.** What isn't listed below says what its quotes say, and each `today` part is the latest the evidence shows for its place. I sampled YA-130 in the first review and called it faithful; the Wagbat fault below is one I missed.

### Must fix before phase D marks on

1. **YA-62, PayPal: the fact a merchant needs, that an account in Yemen can't receive, is only in a note.**
   - `today` reads "Sending from Yemen @ PayPal's service". YQ-D634 and YQ-E728 share that label, and the source's "only" stays in YQ-D634's `note`.
   - YE-D997: "الدول العربية التي تستطيع إرسال الأموال فقط (أي لا تستطيع استقبال الأموال) عن طريق هذه الخدمة هي: جزر القمر، جيبوتي، موريتانيا، الصومال، اليمن."
   - "Can't receive" is not the same thing at more detail. YQ-E728's page says nothing of receiving (YE-E842: "يلزم وجود حساب لإرسال وتلقي المدفوعات."). It is a second fact of the same source, which step 2a's rule 2 ("parts of one source") makes its own condition.
   - **Fix:** split it off, as YK-513 was for Wise: a condition "whether a PayPal account in Yemen can receive payments", holding YQ-D634's "not received" at PayPal's service. Add it to `bears-on.tsv` for the PayPal value propositions. YA-62's `what_varies` still names "send only", which no state now carries.
   - YC-155 ("Available @ PayPal's service", `occurred`) rests on the Wise guide's "Is PayPal available in Yemen? Yes, PayPal is accepted in Yemen." (YE-E634). Its label follows its quote, but a marker must not read it as receiving.
2. **YK-23: the label drops the source's purpose limit.**
   - Label: "allowed if the recipient is not on a sanctions list".
   - YE-D420: "وفقًا للوائح وزارة الخزانة الأمريكية، التحويلات لأغراض شخصية أو إنسانية مسموحة طالما أن المستلم ليس مدرجًا على قوائم العقوبات الدولية."
   - The source speaks only of personal or humanitarian transfers. It says nothing of payment for a merchant's sales.
   - **Fix:** "personal or humanitarian transfers allowed if the recipient is not on a sanctions list".
3. **YA-62, Zid Pay: the state comes from Zid Pay's Kuwait terms, but its place is Zid Pay as a whole.**
   - YQ-E897: "Unavailable @ Zid Pay's service".
   - YE-E1332: "Terms and Conditions for Zed Pay – Kuwait". YE-E1333: "as outlined by Zid Pay or the State of Kuwait or the merchant's country of activity". The page's address ends `zidpay-terms-conditions-kw`.
   - **Fix:** under step 2b's place rule, place it at the product: "Zid Pay Kuwait (Zid)'s service". S-01's Zid Pay value propositions (VP-16, VP-20, VP-21) should not read it as Zid Pay's terms everywhere.
4. **YA-130, Wagbat: the label leaves out cash on delivery, which its own quote names.**
   - YQ-C486: "the Rasidi service @ Wagbat's service". YE-C520: "الدفع نقدًا عند الاستلام أو عبر خدمة رصيدي."
   - The axis lists the methods each seller accepts, and its other parts include cash on delivery where the source gives it.
   - **Fix:** "cash on delivery or the Rasidi service".

### Minor

- **YA-126.** YQ-E663 shares the label "difficult, for lack of national infrastructure", but its quotes (BPC, July 2022) give only "the large number of people who face daily" (YE-E746) and "difficulties in transferring funds between" (YE-E747). No `today` or case changes.
- **YA-128.** Awsan's cash on delivery is "لجميع العملاء في العاصمة صنعاء" (YE-C636, YQ-C560), but its label is "available". Three other stores' Sana'a-only cash on delivery reads "available inside Sana'a".

### Other axes and constants on the same services and rails, left out of S-01's list

- **Cards** (beside YK-161):
  - YA-107: MEPS Yemen's gateway lets banks give merchants acceptance of "Mastercard - Visa - American Express  UnionPay" (YE-E814). At place not stated it is "nearly stopped" (YE-E973, 2023) and "lacking" (YE-D187, 2025).
  - YK-162: online stores that accept cards.
  - YK-335 (YE-E974, 2023): "Yemeni people no longer use MasterCards or Visas, which was not the case before the war broke out."
- **Online payment through a bank or wallet** (beside YA-130 and YA-131):
  - YA-68, which carries Bazzarry's own listing (YQ-D123, 10 October 2026): "يمكنك الآن الدفع بأمان عبر بنك القطيبي من خلال تكامل أونلاين كامل". It is later than YA-130's 2025 part for Bazzarry, and shows the bank payment that YC-203 gives only as `occurred`.
  - YK-131: the payment APIs merchants can use.
- **Bank transfers** (beside YA-126 and YA-131):
  - YK-61: wires from abroad come only through intermediary banks. YE-E323: "direct wire transfers from western banks to Yemen have not been possible".
  - YK-168: the Aden bank's count of SWIFT transfers between local banks, 356 in Q3 2024.
  - YK-505: the national switch for transfers, launched with seven banks in March 2024.
- **Cash on delivery** (beside YA-128 and YK-203):
  - YA-129 (YE-E622, Bazzarry's customers in Aden): "Cash on delivery was the preferred payment method for 74.44% of respondents".
- **Sanctions** (beside YA-27 and YK-22 to YK-24). YK-22 records an assurance withdrawn, not a prohibition. What YK-22's source says remains allowed sits elsewhere:
  - YA-28: the general licences.
  - YK-392 (YE-E550): "FAQ 1219 indicates that non-US persons will not expose themselves to secondary sanctions risk if they engage in or facilitate transactions for which a US person would not require a specific license".

  From other sources:
  - YK-21: secondary-sanctions risk for significant transactions with designated persons.
  - YK-370: Yemen Kuwait Bank is designated, and its own page presents ONE Cash, Floosak and Cash (YQ-A048).

### Anything else

`bears-on.tsv` still quotes YA-62's old labels, "Available @ PayPal's service" (today) and "Send only @ PayPal's service". The rebuild replaced both, so its basis needs redoing against `900c24a`.
