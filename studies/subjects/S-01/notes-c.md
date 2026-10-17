# S-01, phase C: notes

Read for this phase: `briefs/C-analysis.md`; `variation-points.tsv` and `variants.tsv`; each platform's `statements.tsv`, `terms.tsv` and `absences.tsv`, all without any `note` column. No `notes*.md` file, no `note` column and no other file of the study was read. The gap rows' contents (`gaps.tsv`) are not on the brief's list, so a `gap` variant is read only as "this part is not answered".

## Step 0: what the subject is about

> Who holds the merchant's funds between the buyer's payment and the merchant's payout?

**The product.** The question asks which party, inside a platform's own flow of funds, holds the money between the buyer's payment and the payout: a balance, a wallet, a processor's or acquirer's account, a BNPL provider, a carrier. Each reference answers it in its own payment documentation, terms and admin. It does not ask what a market requires: laws and regulators appear in some answers, and step 3 tests them as causes. It does not ask about the company either (Sharrwah's people, money, licences or choices). So nothing in step 0 goes to the founder as a company question.

## How the brief's rules were applied

These readings are mine where the brief leaves room. Each one is also listed under "Problems with the method" below. They describe the second run, which follows the brief as amended.

- **Answer.** A variant's answer is the who or what its excerpt puts in the variation point's role: a party, an account, a balance, an agreement, an amount or a schedule. A platform's set of answers is the answers of its variants that are not `gap`. An `absent` variant is an answer: it rests on a complete list.
- **Same.** As the brief now reads, two answers are the same when they use the same words, or one is the platform's own translation of the other in `terms.tsv`, or they name the same party or identifier (an amount or a currency code counts as an identifier). The merchant, the buyer and the platform itself are each one party on every platform. I counted as the platform itself:
  - its name (سلة, زد, Shopify, BigCommerce, WooCommerce or Woo, and "we" or "us" in its own pages);
  - its own payment product, with that product's balances, wallets and accounts (مدفوعات سلة and رصيد المدفوعات الإلكترونية; زد باي and محفظة زد; Shopify Payments; BigCommerce Payments; WooPayments);
  - its own company (for example شركة زد, the Shopify entities, WooCommerce, Inc.).

  Every other party is the same only by name, so Stripe, Stripe PSP and SPC are three names, and so are "Payment Processor" and "payment provider". Two role terms in partners' agreements refer to the platform in context but are none of the three things above: "Stripe Connect Platform" (S01-SH-131, S01-WC-104) and "Platform" (S01-SH-125). I counted them only by those names.
- **Gaps.** When a platform has a `gap` variant, its set is incomplete. A difference counts as shown only when one platform has an answer that the other's set lacks *and* that other platform has no gap. Agreement is never shown while either side has a gap.
- **Like with like.** Declarations (`stated`, `official page`, `shipped`) are compared with declarations, and `observed` with `observed`. A variant whose `kind` holds both counts in both classes.
- **Scopes.** I count two scopes as overlapping when they name the same country, or when at least one names no country. A scope naming only a product, provider, plan or order type (for example "تمارا", "WooPayments", "باقة بلس") names no country, so I treat it as general for this test.
- **Test 2 ("names a law or a regulator's rule").** The brief now states the reading I used in the first run: a particular law, or a particular regulator with its rule. I counted the Retail Payment Activities Act and the Personal Property Securities Act 2009 (Cth). I also counted the Saudi Central Bank with the Ministry of Commerce and Investment, the Bank of Canada, the Central Bank of Ireland and the UK Financial Conduct Authority, each with its restriction, authority or authorisation. The statement must also present the law or rule as the reason for the variant or its condition. Generic wording did not count: "Law", "applicable law", "to the extent permitted by law", "legally required", "Legal Process", "financial regulations", "a regulatory authority", "the laws of the Kingdom of Saudi Arabia", "U.S. Law", or a country's unnamed "requirements" (S01-SH-065).
- **Test 3.** Of the eleven statements with a `marker`, only S01-BC-059 (`beta`) is cited by a variant, V-567 in VP-13.
- **Coexistence letters.** The brief allows one letter per platform, but many platforms bind their variants in two ways at once: some per market, store or plan, and several of them together in one store. I gave the letter for the binding that governs most of the platform's variants on that VP, citing the statements that show it, and wrote the other binding in the `note` column. `B` needs a statement that ties the variants to the market, store settings or plan. `A` needs a statement that shows two or more of them in force in one store. I read `C` ("one per product") as one per catalog product, and no variant was bound that way. `D` needs a statement saying the platform offers only one, or an `absent` variant, and none qualified. I gave `unknown` in three cases: the platform's only answer is a single variant or restatements of one answer; it has only a gap; or the statements do not show how its variants bind (for example, Salla's تابي and تمارا on VP-22). Letters bind a platform's own variants as `variants.tsv` records them. The same rule sits under step 3's rules for comparing, and I did not use it to merge one platform's variants (see problem 14).
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

## Causes recorded as `unknown`, with why

- **S01-VP-07 (who or what fills "Reserve").** Salla's only variant is a gap (V-134), and so is BigCommerce's (V-135). So neither Salla against Zid nor Shopify against BigCommerce can be compared. Test 4 cannot show that the four hosted platforms agree, and test 5 cannot use Salla. No statement cited for the VP names a law or regulator, and none carries a marker. Unchanged in the second run.
- **S01-VP-10 (who or what fills "security interest").** Zid's only variant is a gap (V-171), and so is BigCommerce's (V-172). Salla has a gap (V-170) beside its one answer (V-550). So neither pair can be compared, and tests 4 and 5 cannot be shown. No named law and no marker. Unchanged in the second run.
- **S01-VP-21 (who or what fills "refunded to your customers").** Salla's answer (V-504) and Zid's known answers (V-505 to V-508, V-510) all name one party, the buyer, whom Zid calls "the source". Zid also has a gap (V-509), so the two can be shown neither to agree nor to differ. BigCommerce's only variant is a gap (V-511), so Shopify against BigCommerce cannot be compared either. The legal wording cited (S01-SH-106 "applicable law and Network Rules", S01-WC-010 "regulatory authority", S01-ZD-014 "الجهات المعنية") names no particular law or regulator. Unchanged in the second run.

## Problems with the method

1. **Settled by the amended brief.** *Same-ness had no notion of role.* In the first run, Salla and Zid each naming themselves counted as different parties. The brief now makes the platform itself, the merchant and the buyer one party each on every platform. In the second run this changed what nine readings rest on, but no cause. 14 of 23 VPs still end at "vendor choice", because the remaining differences are in other parties or in things.
2. **Settled by the amended brief.** *"Names a law or a regulator's rule" was not defined.* The brief now says "a particular law, or a particular regulator with its rule", which is the reading the first run used. Test 2 fires for VP-08, VP-12, VP-17 and VP-18 only.
3. **One marked statement decides VP-13.** The cause there is `maturity` because V-567 cites S01-BC-059 (`beta`). The difference itself is about which agreement governs the merchant's payments, not about a release stage.
4. **Test 1 and "doesn't" answers.** On VP-05, every excerpt names the merchant as the one paid directly, except V-105. V-105 names the platform itself (WooPayments), but only to say it has no part in BACS, as V-109 says of Salla. I read it as naming no other holder, so VP-05 is `no difference`. Read strictly, V-105 would break test 1, and the VP would go on to the later tests.
5. **Strict set equality hides shared answers.** On VP-16, Salla and Zid name the same minimums for Saudi Arabia (100 riyals) and Kuwait (1 dinar). Their sets still differ through Zid's مزيد minimum and Salla's move of small amounts to the wallet. The rule therefore reads "vendor choice". After the second run this is also what separates the Saudi pair on VP-03 and VP-04: both name the platform itself, and only Zid's ترينديول answers differ.
6. **One letter per platform** cannot carry a platform that binds some variants per market and runs several in one store. The second binding is only in `note`, and the `follows` rows are built from letters only.
7. **`general_variant` holds one id per VP.** On VP-14, three platforms each have a general, configurable variant (Salla V-292, Shopify V-286, WooCommerce V-276).
8. **"Product" in letter C** can mean a catalog item or a payment product (WooPayments, Salla Payments). I took the first.
9. **Scopes without a country** (a provider, a plan, an order type) are not covered by "the same country, or general". I treated them as general.
10. **Gap contents are outside the reading list.** I could not check whether a gap could hold another platform's answer, so I assumed it could.
11. **Market causes have no expensive/cheap row.** For VP-08, VP-12, VP-17 and VP-18, `follows` comes from letters alone, and no row asks for a decision.
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
