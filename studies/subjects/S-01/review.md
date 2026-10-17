# S-01 independent review (pilot, step 5)

**17 October 2026.** An independent review under `briefs/F-review.md`, by an agent that produced none of the pilot's files.

- **Reviewed:** the repository at `c15b44f`. The S-01 files are unchanged since `0cf1487`: the two later commits change only `STATE.md` and `method-report.md`.
- **What I read:**
  - the F brief;
  - `briefs/B-variation-points.md`, `C-analysis.md` and `D-yemen-marks.md` as they now read, with the coordinator's additions;
  - everything in `studies/subjects/S-01/`;
  - Stage 1's output in `studies/yemen-cases/`.
- **Sources read to check them:**
  - `questions/Q2-yemen-stress-test.md`;
  - `evidence/product-class/to-save-for-s01.md`;
  - the Torod FAQ capture behind YK-203 and YA-130;
  - the run manifests and `observed-sa` metadata that give the addresses behind `kinds.tsv`;
  - the two entries in `PLAN.md` section 11 that record the coordinator's additions. Both are recorded there.
- **How I checked:** with scripts of my own in my scratchpad, run with `python3 -I`. I ran nothing from inside `evidence/` or the observed repositories, and changed no file but this one.
- **Severity:**
  - `must fix`: the files or the briefs' rules show the claim or record is wrong, and the founder or a later phase would act on it.
  - `optional`: wording or completeness, or a fault that changes no cause, letter, rule, mark or founder item.

## Verdict

**Not yet.** The entry is clear and well cited, and every recommendation in it is marked as the coordinator's. Every quotation of a platform statement, a variant or a Stage 1 state matches its source, except one translation quoted as if it were the source's words (finding 22).

But each of the root decision's options rests on a claim the files don't support:
- **A:** "banks only" in the government's area. Stage 1's own instruments say licensed non-bank companies may be payment providers there (finding 14).
- **A2:** that Zid holds merchants' sales proceeds abroad, under another country's licence. This is not shown (16).
- **B:** its reference examples and the phase D support claimed for it are misattributed (17, 18).
- **C:** "no reference processor serves a merchant there". Phase D leaves BitPay open (15).

There are two further gaps:
- Items 2 to 12 have no answer line, and no recommendation under A2, C or defer (19).
- The Yemen facts behind the options were neither marked nor checked, and Stage 1's cases vary them (13).

Three rule outcomes upstream also look wrong:
- VP-08's cause (1) and VP-10's mark (25) would each add an item for the founder.
- Whether VP-01's own Yemen mark holds depends on a matching ruling that hasn't been made (26).

Once the must-fix findings are settled, the entry should let the founder decide.

**Must fix:** 1, 2, 12 to 20, 25, 26 and 28.

## Findings

### Heading 1. Readings

1. **`analysis.tsv`, S01-VP-08.** `must fix`
   - **Problem.** The cause, `market, named rule`, does not follow under the same-party rule as the C brief now reads.
     - The reading rests on Salla saying it may delay transfers because of the restrictions of the Saudi Central Bank and of the Ministry of Commerce and Investment (V-148, S01-SA-089), "and no other platform names Salla ... as the one withholding".
     - VP-08 is under bullet (a), so its answers are the party that withholds, not the reason.
     - Under the rule, Salla naming Salla is the platform itself. Other platforms name the platform itself as withholding too. So V-148 is not "a variant that differs from the others", and test 2 doesn't apply.
     - Phase C's second run re-derived nine readings, but not this one (`notes-c.md`, "Second run").
   - **Evidence.**
     - Zid names the platform itself: V-144 "يجوز لزد باي احتجاز المدفوعات لفترة غير محددة" (S01-ZD-016) and V-146 "يحق لشركة زد احتجاز بعض أو كل الأموال" (S01-ZD-086).
     - So does WooCommerce: V-142 "We may refuse, condition, or suspend any transaction or account (including your use of WooPayments)" (S01-WC-018), and V-143 "We reserve the right to withhold revenue from all Partner Products" (S01-WC-080).
     - BigCommerce has only a gap (V-151). So tests 4 and 5 can't be shown, and Shopify can't be compared with BigCommerce.
     - Going on down the list, the cause depends on V-149 (S01-SA-120, "This endpoint allows you to temporarily withhold a specific amount of money for settlement from the Merchant's wallet"):
       - if its "you", the app calling Salla's endpoint, is a party Zid's set lacks, the Saudi pair differs and the cause is `vendor choice`;
       - otherwise the cause is `unknown`.
     - With the recorded `expensive_because` ("money flows and legal structure"), each adds a row to `follows`:
       - `vendor choice` adds "a decision for the founder, on a recommendation", which would be a 13th founder item;
       - `unknown` adds "kept open as a variation point until evidence settles it".
     - `entry.md` repeats the current row.

2. **`analysis.tsv`, S01-VP-05.** `must fix`
   - **Problem.** The cause `no difference` fails test 1 as written: "every `variant` excerpt names the same who or what".
     - V-105's excerpt names WooPayments, not the merchant: "WooPayments does not possess the capability to interface with the BACS processing system" (S01-WC-094, bullet d).
     - The reading itself says Salla and WooCommerce "also name the platform itself".
     - Phase C kept the tag on a reading of its own (`notes-c.md`, problem 4). The brief has no such rule.
   - **Evidence.**
     - If V-109 counts only for the merchant, the four hosted platforms' sets are all {the merchant}. WooCommerce then differs through V-105, and S01-WC-094 says what WooPayments doesn't provide. That is test 4, `business model`.
     - If V-109 also counts for "وليس هناك أي علاقة حينئذٍ لمنصة سلة", Salla and Zid differ, and the cause is `vendor choice`.
     - Both are `cheap`, as `expensive_because` records. Either way, `follows` replaces "a commonality, carried as the references carry it" with "left to the build"; the A row stays.
     - **Fix:** re-derive the cause, or the coordinator rules, as the coordinator's own in `PLAN.md` section 11, that a bullet (d) "no part" variant doesn't break test 1. The entry's table repeats the current row.

3. **`analysis.tsv`, S01-VP-12, `cause_reading`.** `optional`
   - **Problem.** The reading says the licensed parties "differ from one platform to the next". By the same-party rule, Salla's and Shopify's are one party, the platform itself:
     - Salla's own transfers are under the Saudi Central Bank's authority (S01-SA-089);
     - Shopify Payment Activities Inc. is Shopify's own company (S01-SH-036).
   - **Evidence.** The cause still holds through Stripe PSP, which no other platform's set contains. The Central Bank of Ireland and the FCA authorised it (V-213, V-214). Only the wording needs changing.

4. **`analysis.tsv`, S01-VP-04, `cause_basis`.** `optional`
   - **Problem.** It cites S01-ZD-095. That is no VP-04 variant's statement, and it says nothing of Zid collecting the buyer's payment. It is about Zid Pay deducting financing repayments: "ستستقطع زد باي من قيمة كل عملية بيع ... ما يفي به التزامات السداد لجهة لتمويل".
   - **Evidence.** The reading's "Zid ... names the platform itself as a collector" rests on V-094, V-096 and V-097 (S01-ZD-002, S01-ZD-069, S01-ZD-071). Cite those instead.

### Heading 2. Coexistence and what follows

Given the causes and letters as recorded, every `follows` cell holds exactly the rows the rule table gives. None is missing and none is extra. Findings 1 and 2 change two of them.

5. **`analysis.tsv`, S01-VP-03, -11, -18 and -19.** `optional`
   - **Problem.** Every platform has `A` on these four, so `follows` lacks "a variation point behind one interface, bound per market, store or plan". Yet their own `note` cells record binding per market:
     - VP-03: "JCB in Japan (V-535) is bound by country";
     - VP-11: Hong Kong (V-183), Network International in the UAE (V-555) and SMCC in Japan (V-556);
     - VP-18: "the bank account's currency is set per market", and Shopify's EU/EEA and UK terms;
     - VP-19: Shopify's EU/EEA and UK terms, and Stripe in the US.
   - **Evidence.** The brief allows one letter per platform, so this follows the brief; it is `notes-c.md` problem 6. It wants a ruling before the next subject, because VP-03, VP-11 and VP-19 are founder items.

6. **`analysis.tsv`, S01-VP-01, `bigcommerce=A`.** `optional`
   - **Problem.** The letter rests on S01-BC-001 and S01-BC-047, which describe a store's gateways in general. The row's own note says the standalone PayPal gateway (V-026) "gives way to BigCommerce Payments, one per store" (S01-BC-080).
   - **Evidence.** No cited statement shows V-027 and V-532 in force together. `follows` doesn't change, because other platforms carry both A and B.

### Heading 3. Marks

The marked cases are right. Each variation point has `YC-00` and every case whose `name` lists one of its axes, with no row missing, extra or duplicated.
- Under the D brief's three sources of a condition, each mark's condition is the one it cites.
- `Q2` is applied as the coordinator's addition says, including to "خارج المملكة".
- The 99 rows outside `YC-00` match `YC-00` in every field but `note`.

25 and 26, under heading 7, change marks through the variants they name.

7. **`yemen-marks.tsv`, S01-VP-02 and S01-VP-04 (18 rows).** `optional`
   - **Problem.** YA-130's Torod part, cited as case evidence, doesn't show the courier collecting a merchant's sales: "on pickup, on delivery, or by Jaib, Jawali, Floosak or Kuraimi wallet" (YE-E612).
   - **Evidence.**
     - In the capture (`items/180-torodexpress.com/text.txt`), it answers "ما هي طرق الدفع المتاحة؟". That question comes among the questions on Torod's own shipping charges, after "هل تتوفر أسعار خاصة لحسابات الأعمال؟".
     - The role the marks need, collecting from the recipient for business accounts, is YK-203's quote alone: "وإمكانية تحصيل الأموال من المستلمين" (YE-E613). The marks stand on YK-203.
     - Drop YA-130 from these rows' case evidence, and from the entry's "couriers that collect cash on delivery (YA-128, YA-130, YK-203 ...)".

8. **`yemen-marks.tsv`, the eight marks through Zid's wallet (S01-VP-01, -09, -11, -14, -15, -18, -19, -23).** `optional`
   - **Problem.** The marks show only that the wallet's place condition is met: "استخدام المحفظة متاح لجميع التجار خارج المملكة" (S01-ZD-121). They don't show that a buyer's payment can reach the wallet for a merchant outside the Kingdom. The marks are right under the brief; finding 16 is about how the entry reads them.
   - **Evidence.**
     - The wallet is described as one the merchant adds balance to and uses "في شراء المنتجات، أو الخدمات المعروضة في منصة زد" (S01-ZD-057).
     - Zid Pay is for "تجار المملكة العربية السعودية و دولة الكويت" (S01-ZD-112).
     - The wallet's cash-on-delivery inflow, through Zid Ship (S01-ZD-069), is "غير متاح" for international shipping (S01-ZD-126).

9. **`yemen-marks.tsv`, S01-VP-05 (11 rows).** `optional`
   - **Problem.** The mark is "carried unchanged" through direct bank transfer (V-102). But YA-126's state at `YC-00` is "none, only cash, cheques or within one institution @ government-controlled areas".
   - **Evidence.**
     - YA-131's evidence is payment into the seller's account at one bank, the Dakhm store's Kuraimi accounts (YE-D400 to YE-D407). The variant may need configuration, an account at the buyer's institution.
     - The note also lists V-105, which says WooPayments has no part, as qualifying unchanged.

10. **`notes-d.md`, "YC-155", against `yemen-marks.tsv`, `YC-155`.** `optional`
    - **Problem.** The notes say that in that case's unknown rows, `what_would_show_it` "adds evidence that settles PayPal's state". Every `YC-155` row's `what_would_show_it` equals `YC-00`'s.
    - **Evidence.** YK-514, "cannot receive money", is a constant, so it holds in `YC-155` too. PayPal variants could be read as failing there, not as unsettled. No mark changes either way.

11. **`notes-d.md`, "The nine (e) statements marked `none stated`".** `optional`
    - **Problem.** The notes say no such statement's identifier appears in a variant's statements. But S01-SA-189's identifier is "countryOther.description (منصة سلة; …)", and "منصة سلة" appears in S01-SA-074, -077 to -080, -082, -086, -088 and -124.
    - **Evidence.**
      - Read as a condition, S01-SA-189 ("منصة سلة متاحة حاليًا في السعودية والإمارات فقط", observed) fails, among others, V-109, V-495 and V-504 on `Q2`, and S01-SA-124's part of V-123. No mark changes, because another variant stays unsettled in each variation point concerned.
      - The three marks "carried only with a partner" (VP-02, -03, -04) name Salla variants. They should say that Salla offers its platform in Saudi Arabia and the UAE only, and that the marks are about the arrangement, not about Salla.

### Heading 5. The register entry, `entry.md`

12. **`entry.md`, "Variation points that aren't founder decisions", the S01-VP-12 and S01-VP-17 row.** `must fix`
    - **Problem.** "What follows" reads "a variation point bound per market". That is the "D with a market cause" row, and no platform has `D`.
    - **Evidence.** `analysis.tsv` gives both "a variation point behind one interface, bound per market, store or plan", the B row (Shopify `B`, WooCommerce `B`).

13. **`entry.md`, "In short" and "What would change this entry".** `must fix`
    - **Problem.** Two claims hold only for the axes in `bears-on.tsv`, while the options and recommendations rest on others:
      - "Yemen's variation across places and time doesn't change how this subject fares";
      - "The axes this subject rests on were checked against their quotes before the marks".
    - **Evidence.**
      - Nine Stage 1 ids the entry cites are in no `bears-on.tsv` row: YA-01, YA-15, YA-44, YA-86, YA-102, YA-103, YA-105, YA-106 and YA-109. So phase D marked no case for them.
      - Stage 1's cases vary several of them, and the variation bears on the options:
        - YA-102 is "banks and licensed non-bank institutions @ the internationally recognized government's area" in YC-183, YC-283 and YC-284;
        - YA-105's capital for a system operator is 750 million in YC-185 and YC-283;
        - YA-15 is "notes printed before 2016 withdrawn" in YC-101;
        - YA-86 is "the rial only @ the internationally recognized government's area" in YC-177 and YC-284;
        - YA-01 varies in 80 cases;
        - YA-26, which bears on the "licensed wallets" behind option B and which the entry doesn't cite, has 12 named wallets barred in YC-119, YC-287, YC-291 and YC-326, and Mobile Money warned against as unlicensed in YC-118.
      - The "Check of S-01's axes" in `review-independent.md` covered only YA-27, YA-62, YA-126, YA-128, YA-130, YA-131, YK-22 to YK-24, YK-161, YK-167, YK-184, YK-203, YK-206 and YK-513.
      - YA-105 still carries that review's finding 11: `today` gives the news report's 700 million against the instrument's 750 million.
      - **Fix:** check these axes as the pilot checked the marked ones, or say in the entry which Yemen facts are unchecked and which cases vary them.

14. **`entry.md`, "In Yemen today" and Decision 1's option A.** `must fix`
    - **Problem.** The entry says holding others' funds is "reserved to banks in the government's area" (YA-102), and that option A means "banks only in the government's area". Stage 1's own states for YA-102 give the Aden central bank's instruments allowing licensed non-bank companies. The entry's own YA-105, "a joint-stock company ... for a provider licence", comes from the same 2022 instructions, which license specialised companies as well as banks. So the two lines contradict each other.
    - **Evidence.**
      - The instruments:
        - YQ-F079 (13 September 2022, YE-F129 to YE-F133);
        - YQ-F088 (8 August 2023, YE-F157 to YE-F159);
        - YQ-D116, YE-D114: "ممثلة بالبنوك المرخص لها بالعمل، والشركات المتخصصة في هذا المجال";
        - YQ-E809, YE-E950: "Resolution No. 547/CBY/2023: Regulated the provision of mobile money services by non-banking financial institutions".
      - `today` instead takes YQ-E116, a 2025 report: "the bank-led model in government-controlled areas" (YE-E126, YE-E1011). It is the same pattern as Stage 1 review finding 11, a later report overriding the instrument.
      - YA-102 was not in the S-01 axes check.
      - Option A's feasibility, including a licensed non-bank provider, turns on this.

15. **`entry.md`, "In Yemen today", Decision 1's "Yemen's mark", option C, and the recommendation.** `must fix`
    - **Problem.** Three claims go beyond what YA-62, YK-514 and phase D show:
      - "the processors the references use don't serve a merchant in Yemen";
      - "None of the references' processors does today";
      - "no reference processor serves a merchant there".
    - **Evidence.**
      - YA-62 and YK-514 cover Stripe, WooPayments, Zid Pay Kuwait and PayPal. They don't cover Adyen, Global-e, Braintree, Network International, Tap, Geidea or BitPay.
      - Phase D leaves BitPay unsettled (S01-V-042, S01-V-067; S01-BC-033, "cryptocurrency payments are enabled for all merchants"). `notes-d.md` says that read as met, these "would make S01-VP-02 `carried unchanged`, and ... the same for S01-VP-03".
      - VP-01's `YC-00` note lists variants naming processors that "state no condition", among them S01-V-004, -005, -008 and -011.
      - V-026's PayPal business account can't be shown to fail either. Its S01-BC-023 and S01-BC-077 state no condition; only S01-BC-090 fails, on YA-62 and YK-514.
      - Say which processors the evidence covers.

16. **`entry.md`, Decision 1's "Yemen's mark", option A2, the recommendation, and "What the references do" for Zid.** `must fix`
    - **Problem.** Three claims read more into the V-024 mark than the files hold:
      - "a platform-held balance, held by Zid outside Yemen and in Saudi riyals";
      - A2, "held outside Yemen under another country's licence (what Zid does for merchants outside Saudi Arabia)";
      - "A2 works for Zid".
    - **Evidence.**
      - What the files show (finding 8): Zid's wallet is open to merchants outside the Kingdom in Saudi riyals (S01-ZD-121), and is described as one the merchant tops up to buy Zid's services or transfers out of (S01-ZD-057).
      - Nothing shows a buyer's payment reaching the wallet for such a merchant:
        - Zid Pay is for Saudi and Kuwaiti merchants only (S01-ZD-112, S01-ZD-113);
        - the wallet's cash-on-delivery route, Zid Ship, is "غير متاح" for international shipping (S01-ZD-126).
      - No file names the licence or bank behind the wallet. `to-save-for-s01.md` section 3 still asks for "the bank and account holder behind the wallet's IBAN".
      - The table gives Zid's answer as the wallet (V-024). Phase C's reading uses Zid Pay's balance, V-023 (S01-ZD-034, "المبالغ المتوفرة في رصيد حسابك في زد باي").

17. **`entry.md`, "In short" (three arrangements) and option B.** `must fix`
    - **Problem.** The split, "the platform holds a balance: Salla and Zid; a payment processor holds it: Shopify, WooCommerce and BigCommerce; the provider of each payment method: couriers ..., buy-now-pay-later companies, and the gateways ... on BigCommerce", doesn't trace to phase C's sets. It contradicts the same-party rule.
    - **Evidence.**
      - In VP-01 each of the three global platforms names its own payment product's balance or account, which phase C counts as the platform itself (`notes-c.md`, "Same", and problem 12):
        - Shopify: V-002 and V-003, Shopify Payments;
        - WooCommerce: V-015, "your WooPayments account balance";
        - BigCommerce: V-027, "your new BigCommerce Payments account", which the entry's own table quotes.
      - Salla's and Zid's products run through partners: "توفّر منصة سلة عبر شركائها نظام الدفع والسداد" (S01-SA-078), and Zid Pay works "من خلال مقدمي خدمات الدفع" (S01-ZD-002).
      - No VP-01 variant names a courier or a BNPL company as holder; the only provider answer is BigCommerce's V-532.
      - Option B's "(... Salla's and Zid's cash on delivery through couriers)" is wrong for Zid. Zid collects cash on delivery itself and pays it into the merchant's wallet, which is option A:
        - "تقوم زد بتحصيل المبلغ نيابة عن التاجر" and "التاجر لا يستحق أي مبالغ مباشرة من شركات الشحن أو العملاء" (S01-ZD-069);
        - "سيتم تحصيل مبالغ الدفع عند الاستلام من قبل زد شب" (S01-ZD-071).
      - Mark the classification as the coordinator's reading, and reconcile it with phase C's sets.

18. **`entry.md`, the recommendation for Decision 1, and option B's "What it needs from outside".** `must fix`
    - **Problem.** "B is what phase D shows working: with a partner for cash on delivery (S01-VP-02 and S01-VP-04's marks), and through licensed wallets ..." misstates phase D.
    - **Evidence.**
      - VP-02 and VP-04 are about who settles and who collects. On who holds, VP-01, phase D's only mark is V-024, a platform-held wallet.
      - No mark names a phone wallet. YA-68 is listed only for VP-05, VP-11 and VP-13, where no mark rests on it. YA-109 is listed for none. Neither says "licensed".
      - Stage 1 shows wallet licensing split by authority:
        - YA-26: in June 2024 the Aden central bank named Cash, Jawali, Floosak, Jaib and eight others as unlicensed. `today` gives that ban as reversed (YQ-D109), and four cases keep it (finding 13);
        - YA-217: ONE Cash, the entry's YA-109 example, is "licensed by CBY-Sana'a" and its "licence request not accepted by CBY-Aden".

19. **`entry.md`, "In short" and "Decisions 2 to 12".** `must fix`
    - **Problem.** Three of the entry's lines read as fact but are the coordinator's reading, and aren't marked as such:
      - "They aren't independent. One of them decides most of the others";
      - "which mostly follow from Decision 1";
      - "The other eleven answers follow from that choice".
    - Decisions 2 to 12 have no answer line, and give recommendations only "if you choose B" or, in brackets, A.
    - A founder choosing A2, C or defer gets no recommendation for eleven of their twelve items. Tying the eleven to Decision 1 decides for the founder that they depend on it.
    - **Evidence.** `method-report.md` section 10 says the entry "gives each dependent item the answer each option implies", but the entry gives the answers only for A and B. Give each item its own answer line, and either the implication for every option or a plain statement that the dependency is the coordinator's reading.

20. **`entry.md`, Decisions 9 and 11, the "Yemen" lines.** `must fix`
    - **Problem.** Two Yemen lines misstate what they cite:
      - Decision 9 reads "carried unchanged, through S01-V-480: Zid's transfer fee, 50 riyals for a bank outside Saudi Arabia". V-480 is the 9-riyal fee for transfers inside Saudi Arabia.
      - Decision 11 reads "The references' providers fail there". Phase D shows only some failing.
    - **Evidence.**
      - V-480's excerpt is "تفرض زد رسوم تحويل من المحفظة وقدرها 9 ريال ... في حال كانت الحوالة داخل السعودية". The 50 riyals is another clause of S01-ZD-058 and S01-ZD-150. V-481, Zid's automatic deduction from wallet deposits, also qualifies unchanged, and its basis holds (finding 26).
      - Decision 11: VP-22's `YC-00` row fails PayPal (V-653) and WooPayments (V-515) on YA-62 and YK-514, and V-512 and V-519 on `Q2`. Tabby (V-516), Tamara (V-517, V-518) and Shop Pay Installments (V-514) "can't be shown either way", and V-513 states no condition.

21. **`entry.md`, "Variation points that aren't founder decisions".** `optional`
    - **Problem.** The table says "The `follows` column says what the build does", but it gives only one rule of each row's `follows`.
    - **Evidence.** It leaves out:
      - VP-05's "the platform carries all the variants at once";
      - VP-13's A and B rows;
      - VP-14's and VP-16's A or B rows;
      - VP-07's, VP-10's and VP-21's A or B rows.

22. **`entry.md`, several lines.** `optional`
    - **Problem.** Some lines claim more than their sources, or present translation and glosses as the source's own words:
      - "Each line gives the question as phase C wrote it", but Decisions 2, 3, 4 and 6 abridge `founder_item`. Decision 4, for example, drops "(a BNPL company, a shipping company for cash on delivery)".
      - "through the service provider" is quoted as if it were S01-SA-113's words. It is a translation of "من خلال مزود الخدمة", and isn't marked as one.
      - "(a PayPal account)" for the BigCommerce Payments account rests on S01-BC-069 (V-612), not on the cited S01-BC-051.
      - "with other gateways" isn't in S01-BC-088, an FAQ headed "Where do I manage my funds?".
      - "The courier collects cash on delivery (S01-SA-090 ...)": S01-SA-090 says only "لا تتولى سلة تحصيل مبالغ الدفع عند الاستلام في هذه الحالة".
    - **Evidence.** The cited statements, as quoted.

23. **`entry.md`, Decision 10, the recommendation.** `optional`
    - **Problem.** "Zid's terms show one way: hold ... (S01-V-498), then transfer the balance (S01-V-496)" joins two different services.
    - **Evidence.** V-498 is Mazeed's hold when a merchant cancels a Mazeed account (S01-ZD-087, "إلغاء ربط الحساب الخاص بك في مزيد"). V-496 is the FAQ on turning Zid Pay off (S01-ZD-041).

### Heading 6. Coverage

24. **`variants.tsv`, statements under no variation point.** `optional`
    - **Problem.** Of 603 statements under (a) to (d), 11 are under no variation point. `notes-b.md` names all 11 with reasons, and the reasons mostly hold. But three placements are inconsistent:
      - S01-BC-058 ("funds are conveniently managed within a dedicated balance dashboard directly inside BigCommerce", bullet a, `beta`) and S01-WC-161 ("the payments that we manage for you", bullet a) are left out, while V-017 went into VP-01 on the same word "إدارة" (manage).
      - S01-SA-057 and S01-SA-149 imply that in the UAE and Kuwait, cash-on-delivery amounts are with "شركة الشحن التي فعّلتها بعقد خارجي" or the store's own courier. They bear on the entry's claim about Salla's couriers (finding 17).
      - S01-BC-047 ("Each provider has its own application process") fits VP-11's answer of an account with each provider.
    - **Evidence.** Placing any of them changes no cause, because each names the platform itself or a party already in its set.

### Heading 7. Matching

25. **`variants.tsv`, S01-V-550 (S01-VP-10).** `must fix`
    - **Problem.** V-550 answers a different X. Without it, VP-10's mark becomes `no placement`.
      - S01-SA-187, "احصل على استثمار مبني على بيانات أداء متجرك على سلة، بلا أوراق ولا ضمانات" (scope صندوق سلة), is about collateral for Salla's financing product. VP-10's X is a security interest over the merchant's processed funds.
      - Its own `basis_evidence` says "the statement names no holder", so `answers` doesn't hold either.
      - It is the only variant keeping VP-10's mark at `unknown` (`notes-d.md`: "In S01-VP-10 every other variant fails, but S01-V-550 ...").
    - **Evidence.**
      - Without V-550, every VP-10 answer variant fails at `YC-00`, and in the five other marked cases:
        - V-167 and V-168 fail on `Q2`;
        - V-169 and V-549 fail on YA-62.
      - The mark is then `no placement`. The D brief's rule 2 then asks for a product gap and a founder item, which the entry would have to carry.
      - The cause stays `unknown`, because Salla would have only a gap (V-170).

26. **`variants.tsv`, `answers` resting on different words.** `must fix`
    - **Problem.** Rule 0 calls two things the same when they use the same words, the platform's own translation, or the same party or identifier, and rule 4's `answers` needs "words that name the same X". Yet 83 variants claim only `answers` while their own `basis_evidence` says "the words differ". Others show no shared word without saying so. Phase B kept them on meaning (`notes-b.md`, problem 1); the method report lists this as open.
    - **Evidence.**
      - Marks and readings depend on such rows:
        - VP-01's mark V-024: "keeping and managing the amounts" against "holds the funds";
        - VP-03's mark V-059: "turned into a bank transfer ... through" against "payouts";
        - VP-14's mark V-579: "more than one withdrawal a day" against "payout schedule";
        - VP-18's mark V-445 and VP-19's mark V-480: both say "the words differ";
        - the readings of VP-01 to VP-04 cite V-026, V-032, V-067 and V-620, all "the words differ".
      - **If the ruling is strict:**
        - VP-18 and VP-19 keep their marks, through V-446 ("held") and V-481 ("deduct").
        - VP-01, VP-03 and VP-14 have no other variant shown to qualify, so they become `unknown`. VP-01's is the root decision's own Yemen mark. Its other variants above V-024 would give no mark: V-027 fails on `Q2`, and V-026 and V-532 can't be shown either way, because V-026's S01-BC-023 and S01-BC-077 and V-532's S01-BC-088 state no condition.
        - The four readings keep their causes through other parties: Global-e, BitPay (V-042), Stripe (V-615), and Adyen and Bridge.
      - **Fix:** a ruling, as the coordinator's own in `PLAN.md` section 11, on whether `answers` may rest on meaning; or re-place the rows.

27. **`variants.tsv`, other placements under a different X.** `optional`
    - **Problem.** These variants answer a question other than their variation point's X:
      - V-017, Salla's store wallet, in VP-01. S01-SA-056 and S01-SA-015 say it serves Salla's subscriptions and services, and that sales proceeds sit in the e-payments balance.
      - V-054 (VP-03) and V-469 (VP-19), Woo Marketplace payments to extension vendors.
      - V-430 to V-432 and V-590, bank-account currency and type, in VP-18 "held".
      - V-645, a card authorisation hold, in VP-18.
      - V-331, V-350 and V-525, a table header that names no time, amount or currency.
      - V-007, V-051 and V-536, which name who does not fill X but aren't the platform's own (d) statements.
    - **Evidence.** The excerpts and their statements, as cited. None changes a cause or mark.

### Heading 8. Kinds

28. **`kinds.tsv`, terms pages given `stated`.** `must fix`
    - **Problem.** Two of the builder's rules give `stated` ("the address is a docs, help or other page") to statements whose source is a terms, legal or pricing page.
    - **Evidence.**
      - **Salla's terms.** S01-SA-074 to S01-SA-089 have the rule "structures/salla/com-policies holds https://salla.com/marketing-tools". But their file, `com-policies/terms/text.txt`, holds `https://salla.com/terms` (its `meta.json` in `observed-sa` at `4ca2e89`).
      - **Captured copies.** The rule "a captured copy in this repository" always gives "docs, help or other page", whatever the copy's address:
        - S01-SH-147 and -158 come from `shopify.com/legal/terms-shopify-payments`, the same address S01-SH-001 has as `official page`;
        - S01-SH-148 to -150 and -159 to -161 come from `shopify.com/legal/terms-payfac`;
        - S01-ZD-152 comes from Zid Pay's terms;
        - S01-BC-062 to -064 come from `bigcommerce.com/pricing/`;
        - S01-BC-123 and -124 come from the Help Center's "Pricing" article;
        - S01-BC-128 comes from `www.commerce.com/terms/` (manifest item 108).
      - The analysis cites S01-SA-077, -080, -082, -084, -086 and -089, S01-SH-148, S01-SH-158, S01-BC-124 and S01-BC-128. Among them are the basis of VP-08's, VP-12's and VP-18's cause (S01-SA-089) and VP-06's no-agency clause (S01-BC-128).
      - No cause changes, because both kinds are declarations. But `variants.tsv` copies the wrong kinds, and the rules will misfile later subjects.

29. **`kinds.tsv`, WooCommerce's "Our policies" pages.** `optional`
    - **Problem.** It is borderline whether these are policy pages. Statements from `woocommerce.com/document/woopayments/our-policies/...` are given `stated`: S01-WC-015, -054, -058, -060, -065 and -161.
    - **Evidence.** The addresses are documentation, in a section titled as policies. A ruling would settle it.

### Heading 9. What each variation point bears on

30. **`bears-on.tsv`, S01-VP-03.** `optional`
    - **Problem.** The SoftPOS card condition of V-059, "الدفع بالبطاقة في كاشير سلة بوينت (SoftPOS)" (S01-SA-113), bears on more than YK-161 and YK-335. It also bears on:
      - YA-122, the card and point-of-sale switch;
      - YA-120, active debit cards;
      - YA-124, card terminals.
    - **Evidence.** So YC-190, YC-191, YC-192, YC-193, YC-195, YC-327 and YC-309 are unmarked for VP-03. Their states leave SabaCard's own switch and acquiring in place, so the mark would not change.

31. **`bears-on.tsv`, other conditions.** `optional`
    - **Problem.** Some conditions bear on Stage 1 ids their rows don't list:
      - Zid Pay's prohibited-activity conditions bear on YA-27 and YA-28. These are S01-ZD-110, and S01-ZD-111, which names "اليمن" among "البلدان الخاضعة للعقوبات الدولية". They condition variants in VP-03, VP-09, VP-14, VP-16, VP-19, VP-20 and VP-21, whose rows don't list those axes, so YC-120 to YC-123 are unmarked there.
      - VP-05's bank-transfer conditions bear on YA-125, the instant payment system, beside YA-126.
      - BitPay's and Coinbase's conditions bear on the crypto constants YK-127, YK-350 and YK-352 to YK-354, which phase D says don't exist ("Stage 1 has nothing on BitPay").
    - **Evidence.** The conditions and Stage 1 states, as cited. No mark changes: the Zid Pay variants already fail on `Q2`, YA-131 carries VP-05, and the crypto constants don't settle "all merchants".

## Items checked under each heading

| Heading | Items checked | Must fix | Optional |
| --- | --- | --- | --- |
| 1. Readings | 23 cause readings, against their 80 `cause_basis` statements. For tests 2 and 3, every statement of the 23 variation points' variants, scanned for named laws, regulators and markers | 2 | 2 |
| 2. Coexistence and what follows | 23 rows, with 115 letters against 129 `coexistence_basis` statements, 23 `follows` cells against the rule table, and 23 `expensive_because` cells | 0 | 2 |
| 3. Marks | 122 marks. The 23 at `YC-00` I read in full: their 13 named variants' conditions traced to (e) statements and scopes, and their case evidence read against Stage 1 and the Torod capture. The 99 others I compared field by field with `YC-00` and with the axis state their case changes | 0 | 5 |
| 4. Rows | none: Q3 runs at close-out | 0 | 0 |
| 5. The register entry | 12 founder items and their options, 73 quotations, 89 S01 ids, 22 Stage 1 ids and `Q2`, every recommendation, and every line that frames a decision | 9 | 3 |
| 6. Coverage | 603 statements under (a) to (d), and the 11 under no variation point, against `notes-b.md`'s reasons | 0 | 1 |
| 7. Matching | 653 variants (616 answers). I read every excerpt against its variation point's X and scanned every `basis_evidence` for its bases. In full, I read the variants that the marks, readings and entry name, and all of VP-10's | 2 | 1 |
| 8. Kinds | 235 statements the analysis cites, each traced to its citation's address: through the run manifest for captured copies, and `observed-sa`'s `meta.json` for Salla's structures | 1 | 1 |
| 9. What each variation point bears on | 23 rows. Each variation point's answer-variant scopes and (e) conditions I grouped by topic, and compared with the listed ids and with Stage 1's 228 axes and 514 constants | 0 | 2 |
