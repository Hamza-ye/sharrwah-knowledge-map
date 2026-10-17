# S-01, phase C: notes

Read for this phase: `briefs/C-analysis.md`; `variation-points.tsv` and `variants.tsv`; each platform's `statements.tsv`, `terms.tsv` and `absences.tsv`, all without any `note` column. No `notes*.md` file, no `note` column and no other file of the study was read. The gap rows' contents (`gaps.tsv`) are not on the brief's list, so a `gap` variant is read only as "this part is not answered".

For the third run, as the coordinator asked, I also read the independent review's six findings on `analysis.tsv` (`review.md`, findings 1 to 6). I found which variants phase B had changed by comparing `variants.tsv` with its second-run version in git, not from `notes-b.md`.

## Step 0: what the subject is about

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

**The product.** The question asks which party, inside a platform's own flow of funds, holds the money between the buyer's payment and the payout: a balance, a wallet, a processor's or acquirer's account, a BNPL provider, a carrier. Each reference answers it in its own payment documentation, terms and admin. It does not ask what a market requires: laws and regulators appear in some answers, and step 3 tests them as causes. It does not ask about the company either (Sharrwah's people, money, licences or choices). So nothing in step 0 goes to the founder as a company question.

## How the brief's rules were applied

These readings are mine where the brief leaves room. Each one is also listed under "Problems with the method" below. They describe the third run, which follows the brief as amended on 17 October 2026.

- **Answer.** A variant's answer is the who or what its excerpt puts in the variation point's role. Phase B's `basis_evidence` now names that role on every VP ("answers (role: …)"), and I took the answer from it:
  - a party, an account, an agreement or a licence on VP-01 to VP-13;
  - a schedule (VP-14), a time (VP-15), an amount (VP-16), a condition (VP-17, VP-18, VP-21), what is taken (VP-19), what happens to the funds (VP-20), when the merchant is paid (VP-22) or a currency (VP-23).

  A platform's set of answers is the answers of its variants that are not `gap` or `not covered`. An `absent` variant is an answer: it rests on a complete list. As the brief now says under test 1, a bullet (d) statement names no one filling the role; phase B marks these in `basis_evidence`. V-623 rests on a statement recorded under bullet (a), so I counted it as an answer (problem 15).
- **Same.** As the brief now reads, two answers are the same when they use the same words, or one is the platform's own translation of the other in `terms.tsv`, or they name the same party or identifier (an amount or a currency code counts as an identifier). The merchant, the buyer and the platform itself are each one party on every platform. I counted as the platform itself:
  - its name (سلة, زد, Shopify, BigCommerce, WooCommerce or Woo, and "we" or "us" in its own pages);
  - its own payment product, with that product's balances, wallets and accounts (مدفوعات سلة and رصيد المدفوعات الإلكترونية; زد باي and محفظة زد; Shopify Payments; BigCommerce Payments; WooPayments);
  - its own company (for example شركة زد, the Shopify entities, WooCommerce, Inc.).

  Every other party is the same only by name, so Stripe, Stripe PSP and SPC are three names, and so are "Payment Processor" and "payment provider". Two role terms in partners' agreements refer to the platform in context but are none of the three things above: "Stripe Connect Platform" (S01-SH-131, S01-WC-104) and "Platform" (S01-SH-125). I counted them only by those names. As the brief now says, the rule compares platforms in step 3 and does not merge one platform's own variants in step 4.
- **Gaps.** When a platform has a `gap` variant, its set is incomplete. A difference counts as shown only when one platform has an answer that the other's set lacks *and* that other platform has no gap. Agreement is never shown while either side has a gap. A `not covered` variant (V-655, Salla on VP-06) is read the same way as a gap.
- **Like with like.** Declarations (`stated`, `official page`, `shipped`) are compared with declarations, and `observed` with `observed`. A variant whose `kind` holds both counts in both classes.
- **Scopes.** I count two scopes as overlapping when they name the same country, or when at least one names no country. A scope naming only a product, provider, plan or order type (for example "تمارا", "WooPayments", "باقة بلس") names no country, so I treat it as general for this test.
- **Test 2 ("names a law or a regulator's rule").** The brief now states the reading I used in the first run: a particular law, or a particular regulator with its rule. I counted the Retail Payment Activities Act and the Personal Property Securities Act 2009 (Cth). I also counted the Saudi Central Bank with the Ministry of Commerce and Investment, the Bank of Canada, the Central Bank of Ireland and the UK Financial Conduct Authority, each with its restriction, authority or authorisation. The statement must also present the law or rule as the reason for the variant or its condition. Generic wording did not count: "Law", "applicable law", "to the extent permitted by law", "legally required", "Legal Process", "financial regulations", "a regulatory authority", "the laws of the Kingdom of Saudi Arabia", "U.S. Law", or a country's unnamed "requirements" (S01-SH-065).
- **Test 3.** Of the eleven statements with a `marker`, only S01-BC-059 (`beta`) is cited by a variant, V-567 in VP-13.
- **Coexistence letters.** The brief allows one letter per platform, but many platforms bind their variants in two ways at once: some per market, store or plan, and several of them together in one store. I gave the letter for the binding that governs most of the platform's variants on that VP, citing the statements that show it, and wrote the other binding in the `note` column. `B` needs a statement that ties the variants to the market, store settings or plan. `A` needs a statement that shows two or more of them in force in one store. I read `C` ("one per product") as one per catalog product, and no variant was bound that way. `D` needs a statement saying the platform offers only one, or an `absent` variant, and none qualified. I gave `unknown` in three cases: the platform has a single variant that answers; it has only a gap or is not covered; or the statements do not show how its variants bind (for example, Salla's تابي and تمارا on VP-22). Letters bind a platform's own variants as `variants.tsv` records them, as the brief now says. Since the third run, no BigCommerce letter rests on S01-BC-001 and S01-BC-047 alone: they describe a store's gateways in general and show no two of its variants together (review finding 6). Each BigCommerce letter now cites statements about the variants it binds.
- **Expensive to change.** I filled `expensive_because` on every row, including rows whose cause selects no expensive/cheap rule (market causes, no difference), so that every VP has the same columns.

## Second run, after the same rule changed

**No variation point's cause, letters, `follows` or founder item changed.** The causes are still:

- vendor choice: 14;
- market, named rule: 4;
- unknown: 3;
- maturity: 1;
- no difference: 1.

The 12 founder items, all the letters and every `follows` cell are as in the first run. The amended test 2 is the reading the first run already used, so it moved nothing.

What changed is what nine causes rest on: `cause_basis`, `scopes_compared` and `cause_reading`. On VP-04 the coexistence basis also changed.

- **S01-VP-01.** Before, the reading rested first on Salla and Zid naming different holders: Salla's رصيد المدفوعات الإلكترونية against the balance of the merchant's account in زد باي. Now both are the platform itself, and Zid's gap (V-025) stops the two being shown to agree. The cause rests on the global pair only: Global-e (S01-SH-099) against a PayPal business account (S01-BC-023).
- **S01-VP-02.** Before, the reading counted the BigCommerce Payments account among BigCommerce's differences. That account is now the platform itself, as Shopify's Shopify Payments account is. The cause rests on the acquirer (S01-SH-058) against BitPay (S01-BC-021).
- **S01-VP-03.** Before: سلة against زد باي. Now both are the platform itself, and the Saudi pair differs through ترينديول (S01-ZD-097), which Salla's set, with no gap, does not contain. The global pair still differs through BitPay.
- **S01-VP-04.** Before: for cash on delivery, Salla's shipping companies against زد and زد شب. Now زد and زد شب are the platform itself, which Salla's set also names. The Saudi pair differs through ترينديول (S01-ZD-097). The global pair still differs through Braintree.
  - Coexistence basis for Zid: S01-ZD-109 and S01-ZD-142 named تابي and تمارا, which are not VP-04 variants of Zid. I replaced them with S01-ZD-083, which puts مزيد's gateway beside the store's gateway, and S01-ZD-002. The letter stays `A`.
- **S01-VP-05.** Wording only. V-105 and V-109 now read as naming the platform itself, which has no part. The cause stays `no difference`.
- **S01-VP-06.** The reading now says that on Shopify the platform itself is the agent, and on BigCommerce it is not. `scopes_compared` notes that Salla (V-123) and Zid (V-122) now name the same party, but one is an observation and the other a declaration, so the two are still not compared.
- **S01-VP-09.** Before: تمارا against زد باي and its service provider. Now the reading uses only answers that do not depend on the platform itself: تمارا (S01-SA-106) against ترينديول and أمازون (S01-ZD-098, S01-ZD-101).
- **S01-VP-11.** A clarification, not caused by the new rule. The first-run reading put Shopify's PayPal Express Checkout account beside its Global-e account, which could be read as a difference. PayPal is the same party by name on both platforms. The reading now uses only the Global-e account (S01-SH-098) against the Braintree account (S01-BC-105).
- **S01-VP-22.** The reading now names Shopify's answer as the platform itself (Shopify Payments pays in full), against PayPal on BigCommerce.

Why nothing more moved:

- Wherever Salla and Zid differed only by naming themselves, either another party still separates them (ترينديول on VP-03 and VP-04), or the global pair carries the cause (VP-01).
- On the other vendor-choice VPs, the Saudi difference is in things, not in the platform itself: schedules (VP-14), timings (VP-15), amounts (VP-16, VP-19), what happens to funds (VP-20) and currencies (VP-23).
- Tests 4 and 5 still need equal sets and no gap on either side, and no Saudi pair meets that. The nearest is VP-06, where like with like keeps the pair apart.

## Third run, after the independent review

Three things changed:
- phase B re-checked `variants.tsv`: since the second run it has 46 fewer variants and 6 new ones, and every `basis_evidence` now names the VP's role;
- the brief gained test 1's line on bullet (d) statements;
- the independent review sent six findings on `analysis.tsv`.

I re-applied steps 3 to 5 to all 23 VPs.

**Causes, before and after:**

| Cause | Second run | Third run |
| --- | --- | --- |
| vendor choice | 14 | 15 |
| market, named rule | 4 | 3 |
| unknown | 3 | 3 |
| maturity | 1 | 1 |
| no difference | 1 | 1 |

Founder items: 12 before, 13 after.

**VPs whose cause, letters, `follows` or founder item changed:**

- **S01-VP-08 (review finding 1).**
  - Cause: `market, named rule` → `unknown`.
  - `follows`: "the platform carries all the variants at once" → "the platform carries all the variants at once; kept open as a variation point until evidence settles it".
  - Why: under the same rule, Salla's V-148 names the platform itself, as Zid's V-144 to V-146 and WooCommerce's V-142 do. So the variant whose statement gives the Saudi Central Bank's restrictions as the reason (S01-SA-089) does not differ from the others, and test 2 does not apply.
  - V-149 and V-150, on which the review's other possible outcome (`vendor choice`) rested, are no longer in `variants.tsv`.
  - BigCommerce has only a gap (V-151), and Salla's issuing bank (V-546) is an observation, so no later test can be shown (see the unknowns below).
  - Letters unchanged.
- **S01-VP-21.**
  - Cause: `unknown` → `vendor choice`.
  - `follows`: "the platform carries all the variants at once; kept open as a variation point until evidence settles it" → "the platform carries all the variants at once; a decision for the founder, on a recommendation".
  - New founder item: "On what conditions should funds Sharrwah holds go back to the buyers instead of to the merchant: a breach of the platform's terms, verification or registration not completed in time, payments whose legitimacy is not shown, or a demand by a processor or regulator?"
  - Why: phase B now gives the role as "the condition on which the funds go back to the buyers", not who receives them.
    - Salla names one condition, a breach of the first clause of its Article Ten (S01-SA-082).
    - Zid names three others: activation data not corrected, legitimacy not shown, and registration not completed (S01-ZD-011, S01-ZD-014, S01-ZD-024). Salla's set, which has no gap, contains none of them.
    - Zid's gap (V-509) does not stop a difference shown from Zid's side.
- **S01-VP-01 (review finding 6).** BigCommerce: `A` → `B`.
  - The letter rests on S01-BC-067 (BigCommerce Payments needs the right plan and store location), S01-BC-080 (it takes the standalone PayPal gateway's place on migration) and S01-BC-047 (other gateways are added by configuration).
  - `follows` unchanged: Salla, Zid and Shopify keep `A`, and WooCommerce `B`.
- **S01-VP-02.** Zid: `unknown` → `A`.
  - Phase B added V-658: Zid settles زد شب dues to the wallet.
  - S01-ZD-061 shows one merchant holding both that wallet and the Zid Pay balance of V-039.
  - BigCommerce stays `A`, now on S01-BC-069 and S01-BC-070.
  - `follows` unchanged.
- **S01-VP-03.** BigCommerce: `A` → `unknown`.
  - The letter rested on S01-BC-001 and S01-BC-047, the general statements of review finding 6.
  - No cited statement shows BitPay, Stripe OCS and the standalone PayPal gateway (V-067, V-615, V-616) together in one store, or one per market, store or plan.
  - `follows` unchanged.
- **S01-VP-14.** BigCommerce: `A` → `B`, on S01-BC-080 and S01-BC-073 (the payout frequency chosen in settings).
  - Every platform is now `B`, so `follows` loses the `A` row: "the platform carries all the variants at once; a variation point behind one interface, bound per market, store or plan; left to the build" → "a variation point behind one interface, bound per market, store or plan; left to the build".
- **S01-VP-22.** Founder item reworded. Phase B now gives the role as when the merchant is paid, not who pays.
  - Before: "For installment payments, which party should pay the merchant up front and carry the buyer's installments in Sharrwah: a BNPL provider under its own agreement with the merchant, or the platform's own payment service?"
  - After: "Under instalment or pay-later payments, when should a Sharrwah merchant be paid: in full after capture with the platform's other payouts, up front while the buyer owes the instalment provider, or on the instalment provider's own schedule under its agreement with the merchant?"
  - The cause stays `vendor choice`, now on the timing: "full payment" after capture (S01-SH-054) against "paid up front" (S01-BC-024, S01-BC-094). See problem 16.
  - `expensive_because` now speaks of when the merchant is paid.

**Same cause, letters, `follows` and founder item, with a new basis or reading:**

- **S01-VP-05 (review finding 2).** Stays `no difference`, now on the brief's new line rather than a reading of mine (old problem 4). V-105 and the second part of V-109 are bullet (d) statements and name no one filling X, so every filler named is the merchant.
- **S01-VP-04 (review finding 4).** `cause_basis` cited S01-ZD-095 by mistake. For Zid naming the platform itself it now cites S01-ZD-002, S01-ZD-069 and S01-ZD-071 (V-094, V-096, V-097), and the reading cites them too. BigCommerce's `A` now rests on S01-BC-051 and S01-BC-066.
- **S01-VP-12 (review finding 3).** The reading no longer says the licensed parties all differ: Salla's and Shopify's are both the platform itself, under two different statuses. The cause rests on Stripe PSP (S01-WC-113, S01-WC-114) and تاب (S01-ZD-082), parties no other platform's set contains. The reading also no longer names تاب's regulator "the Saudi Central Bank", since S01-ZD-082 says only "البنك المركزي".
- **S01-VP-06.** Salla's V-123 is gone. Salla is now `not covered` (V-655), read as a gap, so Salla and Zid are still not compared.
- **S01-VP-09.** Salla's observed V-164 is gone. The reading rests on V-165 alone.
- **S01-VP-10.** Salla's one answer (V-550) is gone. Salla, Zid and BigCommerce are all gap only. Still `unknown`.
- **S01-VP-16.** Salla's V-360 (moving small amounts to the wallet) is gone. The Saudi pair now differs only through Zid's 500-riyal minimum for مزيد (S01-ZD-088).
- **BigCommerce's `A` on VP-13, VP-15, VP-19 and VP-22** no longer rests on S01-BC-001 and S01-BC-047. It now rests on:
  - S01-BC-039 and S01-BC-059 (VP-13);
  - S01-BC-074, S01-BC-081 and S01-BC-082 (VP-15);
  - S01-BC-075 and S01-BC-076 (VP-19);
  - S01-BC-024, S01-BC-094 and S01-BC-022 (VP-22).
- **Removed variants.** No cell cites them any more. Before, cells cited V-054, V-123, V-164, V-360, V-550 and V-594, and these statements of removed variants:
  - S01-WC-027 (VP-03);
  - S01-SA-120, S01-SA-125 and S01-SH-088 (VP-08);
  - S01-SH-143 (VP-09);
  - S01-SA-187 (VP-10);
  - S01-SA-013 (VP-16);
  - S01-SA-060, S01-SA-065 and S01-SA-184 (VP-18's note);
  - S01-BC-124 (VP-19's coexistence basis).

  S01-BC-124 stays in VP-19's `expensive_because`, where it is cited for fees billed apart, not as a variant.
- **VP-07, VP-11, VP-17, VP-20 and VP-23.** Phase B's changes there (removed variants on VP-11 and VP-23, and `stated` turned to `official page`, which stays a declaration) leave cause, basis and reading as they were.

**Review finding 5, not applied.** It asks for a ruling on VP-03, VP-11, VP-18 and VP-19. On each, every letter given is `A`, while some variants bind per market (problem 6). The brief gives one letter per platform, so the letters and `follows` stay as the brief gives them until the coordinator rules.

## Causes recorded as `unknown`, with why

- **S01-VP-07 (the party that sets or holds a reserve).** Salla's only variant is a gap (V-134), and so is BigCommerce's (V-135). So neither Salla against Zid nor Shopify against BigCommerce can be compared. Test 4 cannot show that the four hosted platforms agree, and test 5 cannot use Salla. No statement cited for the VP names a law or regulator, and none carries a marker. Unchanged in the second and third runs.
- **S01-VP-08 (the party that holds back the merchant's funds).** New in the third run.
  - Salla's and Zid's declarations both name only the platform itself (V-147, V-148; V-144 to V-146), so the Saudi pair agrees on declarations.
  - V-148's statement names the Saudi Central Bank's restrictions (S01-SA-089), but V-148 does not differ from the others, so test 2 does not apply.
  - Salla's other answer, the issuing bank (V-546, S01-SA-181), is an observation, and Zid has none, so like with like cannot set it against Zid.
  - BigCommerce's only variant is a gap (V-151), so tests 4 and 5 and Shopify against BigCommerce cannot be shown.
  - No cited statement carries a marker.
- **S01-VP-10 (the holder of a security interest).** Salla's, Zid's and BigCommerce's only variants are gaps (V-170, V-171, V-172), since Salla's one answer (V-550) is gone in the third run. So neither pair can be compared, and tests 4 and 5 cannot be shown. No named law and no marker.

S01-VP-21 was `unknown` in the first and second runs. In the third run it is `vendor choice` (see above).

## Problems with the method

1. **Settled by the amended brief.** *Same-ness had no notion of role.* In the first run, Salla and Zid each naming themselves counted as different parties. The brief now makes the platform itself, the merchant and the buyer one party each on every platform. In the second run this changed what nine readings rest on, but no cause. In the third run it moved VP-08 from `market, named rule` to `unknown` (review finding 1). 15 of 23 VPs now end at `vendor choice`, because the remaining differences are in other parties or in things.
2. **Settled by the amended brief.** *"Names a law or a regulator's rule" was not defined.* The brief now says "a particular law, or a particular regulator with its rule", which is the reading the first run used. Since the third run, test 2 fires for VP-12, VP-17 and VP-18 only. On VP-08 the regulator is named for a variant that, under the same rule, does not differ from the others.
3. **One marked statement decides VP-13.** The cause there is `maturity` because V-567 cites S01-BC-059 (`beta`). The difference itself is about which agreement governs the merchant's payments, not about a release stage.
4. **Settled by the amended brief (third run).** *Test 1 and "doesn't" answers.* On VP-05, V-105 names WooPayments only to say it has no part in BACS, as part of V-109 says of Salla. In the first two runs I read these as naming no other holder, a reading of my own. The brief now says a bullet (d) statement names no one filling X, and VP-05 stays `no difference` on that line.
5. **Strict set equality hides shared answers.** On VP-16, Salla and Zid name the same minimums for Saudi Arabia (100 riyals) and Kuwait (1 dinar). Their sets still differ, since the third run only through Zid's 500-riyal minimum for مزيد (S01-ZD-088), because Salla's move of small amounts to the wallet (V-360) is no longer a variant. The rule therefore reads "vendor choice". This is also what separates the Saudi pair on VP-03 and VP-04: both name the platform itself, and only Zid's ترينديول answers differ.
6. **One letter per platform** cannot carry a platform that binds some variants per market and runs several in one store. The second binding is only in `note`, and the `follows` rows are built from letters only. The review's finding 5 asks the coordinator to rule on this for VP-03, VP-11, VP-18 and VP-19, three of which carry founder items. I have not applied it.
7. **`general_variant` holds one id per VP.** On VP-14, three platforms each have a general, configurable variant (Salla V-292, Shopify V-286, WooCommerce V-276).
8. **"Product" in letter C** can mean a catalog item or a payment product (WooPayments, Salla Payments). I took the first.
9. **Scopes without a country** (a provider, a plan, an order type) are not covered by "the same country, or general". I treated them as general.
10. **Gap contents are outside the reading list.** I could not check whether a gap could hold another platform's answer, so I assumed it could.
11. **Market causes have no expensive/cheap row.** For VP-12, VP-17 and VP-18, `follows` comes from letters alone, and no row asks for a decision.
12. **New with the same rule: a product's name decides the party.** Some products the platforms name as their own are, in their own words, powered or processed by another party:
    - BigCommerce Payments is "powered by PayPal", with "the merchant's payment relationship ... directly with PayPal" (S01-BC-066, S01-BC-039);
    - WooPayments "is powered by Stripe" (S01-WC-002);
    - زد باي runs "من خلال مقدمي خدمات الدفع" (S01-ZD-002);
    - Shop Pay Installments comes with Affirm's agreement (S01-SH-040);
    - صندوق سلة runs "بالشراكة مع تنامي" (S01-SA-130).

    Each such product now counts as the platform itself, and the partner as a second party in the same set. So the set of a platform whose own product a partner powers holds two parties for that product, where another platform's holds one.
13. **New with the same rule: role terms are not covered.** "Stripe Connect Platform" (S01-SH-131, S01-WC-104) and "Platform" in the Adyen terms (S01-SH-125) mean the platform in context, but they are not its name, payment product or company. I counted them by name. No cause in this run depends on them (VP-06, VP-09, VP-19 rest on other answers).
14. **New with the same rule: it does not say whether it also applies inside one platform.** I applied it across platforms (step 3) and left step 4 on the variants as recorded. If it also merged one platform's own variants, these letters would turn `unknown`, each because that platform's variants become one answer:
    - VP-01, Zid: V-023 and V-024 are both the platform itself;
    - VP-05, BigCommerce: V-111, V-621 and V-622 all name the merchant;
    - VP-08, Zid: V-144 to V-146 are all the platform itself;
    - VP-21, Zid: all its answers name the buyer.

    The `follows` cells of VP-05 and VP-21 would then lose "the platform carries all the variants at once".
