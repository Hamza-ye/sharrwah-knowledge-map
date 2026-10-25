# M1 terms and scope checks: what was done with each finding

The coordinator's record of the independent checks of amendment 2's pass (`METHOD.md` section 6; amendment 3). Every finding was tested against its evidence before it was applied. The checked text was at commit `24961d6`.

## D-001 and D-004, level 3

`M1-terms-scope-check-D001-D004.tsv`: 51 claims. 26 hold, 23 fix, 1 not carried, 1 open.

**The evidence the findings rest on.** All 19 quotes the checker relied on were found, by script, in the records it cites. They are:
- Tabby and Tamara accounts requested through Salla (`SA-en:576`, `SA-ar:880`, `SA-en:29`, `SA-ar:865`, `SA-ar:881`);
- the PayPal account Shopify generates at sign-up (`HC:payments/paypal/set-up-paypal.md:3`, `:20`; `HC:payments/paypal.md:5`; `HC:payments/paypal/common-issues.md:33`);
- Shopify Balance payouts (`HC:finance/shopify-balance/payouts.md:3`);
- outside marketplaces as merchant of record (`HC:taxes/shopify-tax/automated-filing/considerations.md:26`);
- PayPal linked by email on Salla (`SA-en:793`);
- Tamara refunds (`SA-en:804`);
- the bank account for transfers (`SA-en:9`).

**The main finding holds, and it was the coordinator's error.** The founder's guard of 18 October reads: "No arrangement that holds sellers' money through Sharrwah goes live anywhere without the founder's decision". It names A and B as its forms. The glossary had narrowed B to "the platform's own payment service", and had added "Nothing else is held through Sharrwah". Both narrowed the founder's words. The pilot's own B includes "onboarding sellers to it" (D-001's options table).

**Applied:**

| Finding | What was done |
| --- | --- |
| C10, C02 (the line between B and C) | The glossary and D-001 define B by the guard's words. An account opened through Sharrwah is one the seller doesn't open with the company itself: with Sharrwah's own service, or one Sharrwah creates or requests for the seller. Salla's Tabby and Tamara requests and Shopify's generated PayPal account are B. A case between B and C goes to the founder. The founder's page shows the consequence: no opening or requesting of sellers' accounts from inside Sharrwah at launch. |
| C25, not carried | Resolved by C10. The line now follows the guard's words, so how S-07 places a provider can't change D-001. Its item is marked "Carried", with that reason. Re-checked below. |
| C26, open | Resolved by reading the guard's leading clause as covering arrangements it doesn't name, such as a courier collecting cash under Sharrwah's own contract. This is marked as the coordinator's interpretation, in the glossary, D-001's Scope and Gaps, and the founder's page, for the founder to confirm or correct. |
| C03 | "At launch" is per market on the founder's page, as in the Terms. |
| C04 | "Reserved, not built" is scoped to A and B, with "integrated" restored, on the page, in the Terms and in the glossary. |
| C05 | The page lists what confirming also settles, Shopify Balance-like business accounts included. |
| C06 | The page names the S-07 line case among what is left open. |
| C08 | The option C row covers all three of the outcome's cases. |
| C09, C41 | "Seller's own account" means an account the seller opened itself, into which the buyer's payment is received or settled. It is linked by the seller's own credentials, keys, account number or email. A payout-only bank account is not C. The wording is the same in both records and the glossary. |
| C11 | "Sellers' money" runs until the money reaches an account the seller holds outside Sharrwah, or the seller's hands. Payouts into an account opened through Sharrwah are still sellers' money. |
| C13 | Manual methods include cash paid to a courier, in the glossary and in both entries. |
| C14 | "Provider" names the courier apart; "provider or courier" means both. D-004 row 4 now reads "each provider or courier: the wallet, the courier, or the seller's own bank". |
| C16 | "Platform balance" includes cash on delivery collected by a platform's own labels. |
| C19 | Building A or B is a change to D-001, by the founder's decision. Switching either on is the founder's too. |
| C24 | The S-07 providers item sorts by who opened the account. |
| C29 | The S-10 item separates a marketplace Sharrwah runs from an outside marketplace the seller sells on under its own account. |
| C32 | "No licence is needed for C" is narrowed to "no licence to hold sellers' money". Whether a market licenses a platform that only links providers is read at S-08, and is listed under Gaps. |
| C35 | Gaps item 1: whether each provider opens accounts itself or through a platform decides which providers are C at launch. |
| C39 | D-004 row 8 covers payout times and couriers' transfer days, and manual methods. |
| C42 | D-004's provider fees and rows 6 and 9: each provider or courier charges on its own terms, deducting or invoicing. |
| C43 | D-004's refund and void: for a manual method, by the seller directly. How the platforms refund one is listed under Gaps. |
| C44 | "Agency role" is defined as being appointed the seller's agent to receive or hold buyers' payments. Sending the seller's instructions with its own keys is not one. |
| C47 | D-004 takes D-001's outcome "as proposed", and is confirmed with it or falls with it. |

**Not changed:**
- **The checker's note on D-001's drivers,** which call G1's B1 and B2 the founder's intent, against `founder-decisions.tsv`'s F-00 "In force: G1's B1". The G1 answer says of section B: "It is my intent, not a design and not decisions" (`founder-messages/2026-10-18-g1-answer.md`:5). F-00 is the decision in force, and B1 restates it as intent, so the two agree.

## D-002 and D-003, level 2

`M1-terms-scope-check-D002-D003.tsv`: 75 items. 39 hold, 23 fix, 6 not carried, 7 open.

**The evidence the findings rest on.** The review's new evidence was checked before anything was applied:
- by script: `SA-en:816`, `SA-en:923`, `HC:payments/shopify-payments/refunds-troubleshooting.md:91`, `HC:shopify-flow/reference/actions/charge-vaulted-payment-for-b2b-order.md:3`, `HC:sell-in-person/shopify-pos/payment-management/multiple-partial-payments.md:12`, `HC:your-account/users/roles/permissions/store-permissions.md:203`, `GQL:2354`, `SAPI:211`;
- by reading the schema: `settlementCurrencyRate` at `GQL:2447`; `GQL:2485`'s mandate types SUBSCRIPTIONS, ORDERS and DRAFT_ORDERS; and 47 failure codes at `GQL:2450`, 7 of them AMAZON_PAYMENTS_*;
- by reading the sources: E032:146–163, the buyer's email, phone, billing and shipping addresses in Shopify's payment request; and E036:54 and :60, the payment function's review requirement.

All of it holds. The count in D-003 (114 types, 38 reversals, 36 twins) was reproduced independently.

**"How it grows" is withdrawn.** The reviewer judged, as an interpretation, that it changed D-002's substance rather than making its first consequence explicit. It let attempt states, outcome kinds, reason categories and evidence levels grow, and the order side reads those. The coordinator agrees: it had been added in this pass to make open items carried, and it broadened the decision. With it gone, D-002's vocabularies are part of what it decides, and an item that needs a new value is not carried.

**What that means for D-002 and D-003.** D-002 doesn't carry nine of the items it leaves open, and D-003 four. Neither can be accepted now (`METHOD.md` section 6's acceptance rule). Both stay proposed, as the working basis. Each item is in their Scope, with its evidence and the subject that settles it, and their Gaps say the records are revised to carry them before acceptance. They weren't redesigned in this pass, because that is S-05's and S-07's work.

**Applied:**

| Finding | What was done |
| --- | --- |
| D2-05, open | A bank that only receives a transfer, with no integration, sends no provider's record, and its payments are manual (D-002's Terms; the glossary). |
| D2-06 | The manual payment method entry and kind 2 already include cash paid to a courier (the C13 fix). |
| D2-07 | Cash on delivery's outcome includes the seller's attestation where the seller's own staff collect. |
| D2-10 | The outcome kinds left out include Salla's undescribed `reverse`, and the money a lost dispute moves. |
| D2-13, D2-47 | The manual reversal quote is given whole: Shopify also resolves one by store credit or a gift card. |
| D2-14 | The custodian is who holds the money when the outcome is recorded; later custody is in payments' records. A carrier may deduct its invoices from the cash it holds. |
| D2-18 | Shopify's payment function can also add a review requirement (E036:54). Rules setting payment terms are S-11's; rules rejecting or holding for review are S-07's. |
| D2-22 | Live and test: real or test mode. |
| D2-23 | "Reserved, not built" names the settlement contract and stored permissions to charge later. |
| D2-27 | B7 is cited through F-03's row of `founder-decisions.tsv`, as the founder's intent that row records as prevailing. The market guard is cited to its own row. |
| D2-38 | "Option 1 wins": the schema fields are named without overclaiming. The Amazon codes are noted, and the conclusion is marked as an interpretation. |
| D2-39 | Amounts: Shopify's order amounts are MoneyBags, and a transaction names its settlement currency and rate (`GQL:2447`). |
| D2-40 | Withdrawn, as above. |
| D2-43 | The first consequence holds only "as long as its interface fits the elements", which isn't shown yet (E032:146–163). A new capability changes the record. |
| D2-44 | *Reversed 25 October, after the founder asked whether it was sure.* The review's claim that Salla ties review to bank transfer "only for Salla's own subscription renewals" held for the help articles alone. All four Arabic articles that put review beside a bank transfer concern Salla's own billing (`ar:81`, `ar:689`, `ar:700`, `ar:1628`). Salla's dashboard settings tie it to sellers' orders: the "Under review" status "Applies to orders paid by bank transfer or cash on delivery, and to online payments when the ‘Set status to Completed for online-paid orders’ option is turned off." (`STR:settings.json`; the Arabic at `STR-ar:settings.json`). The coordinator had accepted the absence claim after checking only the article cited. The precedent is restored, refined to say that cash on delivery and some online orders start under review too, in D-002's guard and in the glossary. |
| D2-48 | The seam's figures and words are quoted as the seam has them (seam.md:17–18, 28, 33). For Salla, the no-polling point is marked as the seam's reading only. |
| D2-49 | Shopify's provider contract is E030 to E032. The missing buyer data is a new gap. |
| D3-01 | The guard's condition, "without the founder's decision", is restored in driver 1. |
| D3-02 | "Break reconciliation" is marked as an interpretation. |
| D3-06 | New entry types: the rules hold for every type, and what posts a new type changes the record. |
| D3-12, open | Fixed. The posting key is the outcome id with the entry's type. The provider's reference is carried, not used as the key, since one Salla transaction can carry several partial refunds (`SAPI:211`). |
| D3-14 | The glossary's Salla line on Sharrwah's fees: what Salla invoices is the VAT on its own service's processing fees, a precedent for invoicing apart only. |
| D3-18 | D-003 takes D-001's outcome "as proposed, that at launch …". |
| D3-26 | Gaps: lost disputes, and fees with no sale. |

**Not carried, now marked in the records:** D2-29 (stored value), D2-30 (methods and providers), D2-33 (statuses and edits), D2-35 (payment terms), D3-21 (stored value in the ledger), D3-22 (fees with no sale). D2-31 (capture timing), D2-32 (seller rules' messages), D2-36 (split payment), D2-42 (a courier's deductions) and D3-11 (lost disputes) were open. They are marked "Not carried", because a record can't claim to carry what is unsettled.

## Re-check of D-001 and D-004, level 3

`M1-terms-scope-recheck-D001-D004.tsv`: a fresh agent, given the records and the evidence but not the earlier checks. 65 claims: 37 hold, 20 fix, 3 not carried, 5 open.

**The evidence its findings rest on was checked first:**
- Shopify's PayPal pays into the seller's own PayPal account at the store's email, or one it signs up for (`HC:payments/paypal/set-up-paypal.md:3`, `:5`);
- Salla's wallet lets sellers "Add funds" and "Transfer balances between accounts" (`SA-en:1240`);
- Shopify Capital is repaid "from a daily percentage rate of your daily sales" (`HC:finance/shopify-capital/united-states.md:5`, `:9`);
- both platforms offer providers from a list (`HC:payments/third-party-providers/configuring-providers.md:30`; `SA-en:807`);
- Torod on Salla is linked by installing its app (`SA-en:1181`), and Collectpluss issues the seller a username and password (`SA-en:234`);
- Salla has the seller "contact the customer to agree on the refund method" for a bank transfer (`SA-en:994`);
- Tamara's request goes through Salla: "إرسال طلب فتح حساب أعمال" (`SA-ar:881`).

**Why the B/C line goes to the founder.** The guard of 18 October names B in its words as "an account opened through Sharrwah", and its notes define B as "the entry's options A and B" (`founder-messages/2026-10-18-g1-answer.md`:20, :95). The entry's B is "A payment processor holds, in an account the merchant opens through Sharrwah", with platforms' own payment products as its examples (`studies/subjects/S-01/entry.md`:119), and its Decision 7 counted an account "opened through Sharrwah" as "B or C" (:238). Salla's Tabby articles tie the merchant's fees and settlement to the merchant's agreement with Tabby (`SA-en:576`; `SA-en:28`, corrected below). The first check's fix (C10) had applied the words. Under the evidence standard (amendment 3), a conflict between a decision's words and its recorded reason is surfaced, not settled by the older wording, so D-001 puts both readings to the founder as choice 1, recommending the source's. The founder asked the same question on 25 October, for their own assessment; it is not made a rule here. Choices 2 and 3 were first written as the same kind of choice. The page check corrected that (below).

**Applied:**

| Finding | What was done |
| --- | --- |
| BC-1 | Shopify's PayPal is shown as a case between B and C, with the seller's own account at the store's email. |
| BC-2, BC-3 | C's test, on the page and in the terms, is: the seller's own agreement, linked by its own keys, account email or the provider's own app (`SA-en:1181`). |
| BC-4, open | A courier account asked for through Sharrwah is placed by choice 1: C under the seller's own agreement. |
| BC-5 | The Tabby placement is shown as a reading, both readings with the evidence, and the founder chooses. |
| BC-6, open | Added to D-001's Gaps: whether the first market's wallets link by the seller's own keys. |
| FP-1 | "A would need a licence" is marked as the coordinator's reading; the definitions are unread. |
| FP-2 | D-002's room for A and B is "as proposed". |
| FP-3, R-9, S-10, DS-3, S-8 | Choice 2 on the page and in D-001's outcome: fees, and anything owed to Sharrwah or its partners, billed apart, never taken from sellers' money. D-004 rows 6 and 9 take it from D-001. |
| FP-4 | The page lists a Sharrwah-run marketplace, and merchant-of-record holding as Global-e's, and states D-004's answers on agency, security interest and terms. |
| FP-5, open | Holds. The level 3 check of 24 October read Stage 1's Torod page as "خدمات طرود للشحن والتوصيل في اليمن" (`D-001-D-004-level3-pass3.tsv`, row 42). The Torod on Salla appears to be another company with a common name. |
| S-5 | Building B and switching it on is the founder's decision in a record of its own, which D-001 provides for, so how S-07 places a provider doesn't change D-001. |
| T-1 | "Sellers' money" runs until an account the seller holds under its own agreement. Money paid into an account held through Sharrwah is still sellers' money. |
| T-2 | "Platform balance" includes money sellers pay in; choice 3 rules such a balance out at launch. |
| T-3 | Manual payments are recorded by hand, or reported by an integrated courier. |
| T-4 | D-004's cash on delivery includes the seller's own staff. |
| T-5, open | D-004's agency definition is marked as the record's, not a legal one; counsel at S-08 is listed under Gaps. |
| T-6 | The Tamara quote shows the request going through Salla (`SA-ar:881`). |
| O-2 | The option C row's "from outside" adds Sharrwah's own integration agreement with any provider that requires one, since both platforms offer providers from a list they keep (`configuring-providers.md:30`; `SA-en:807`). |
| DG-1 | D-004's gap is corrected: Salla has the seller agree a refund method with the customer (`SA-en:994`). |
| R-2, R-3, R-4 | D-004 rows 2 to 4 name couriers, and row 4 names the seller, not its bank, for a manual method. |
| R-7 | D-004 row 7: the seller's own accounts under choice 1, and no money held in the seller's account with Sharrwah (choice 3). |

## Check of D-001's page for the founder, level 3

`M1-founder-page-check-D001.tsv`: a fresh agent checked each sentence of the page "For the founder", as at commit `f2003c7`, against the record, the glossary and the evidence. 44 claims: 23 hold, 18 fix, 3 open. It processed 1.0 million tokens (`method/count_tokens.py`).

**The evidence its findings rest on was checked first:**
- **Tabby.** The request through Salla is for stores in Saudi Arabia only (`SA-en:576`; `SA-ar:880`, `SA-ar:881` for Tamara). The article with the request says "Fees depend on the agreement between the merchant and Tabby" (`SA-en:576`). The sentence the page quoted on the agreement is from Salla's article for the UAE, whose stores set their account up directly with Tabby (`SA-en:28`; `SA-ar:865`). The page's English was the coordinator's rendering of the Arabic, not Salla's own English, and it joined the two articles.
- **Shopify Capital** is for "merchants in the United States" (`HC:finance/shopify-capital/united-states.md:3`). For loans accepted from 9 March 2026, repayments are "collected directly from your Shopify Payments balance" (:131). Otherwise they are debited from a bank account, including "The external bank account that you set up in your Shopify Capital settings (for non-Shopify Payments users)." (:179).
- **Shopify's fees.** Its fee on sales through other providers goes on its bill (`HC:payments/getting-paid.md:11`; `HC:your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/third-party-transaction-fees.md:1`). Its card fees are "deducted from your payouts rather than billed on your Shopify bill" (`HC:your-account/manage-billing/billing-charges/types-of-charges.md:12`). Its bills can be paid by a seller's Shopify Balance card (`HC:your-account/manage-billing/paying-your-bills/making-payments/payment-methods-for-bills.md:30`).
- **The backlog.** S-04 is "Markets and currency, as configuration", and S-03 covers area A-03, plans and fees (`decisions/subjects.tsv`).

**Choices 2 and 3: "at launch", not "never".** The page offered both as readings of the guard, with the other way ruled out for good. The check found that neither is a reading of the guard (FP-18, FP-28): in neither does Sharrwah hold sellers' money as the glossary defines it. Shopify's evidence shows both ways for fees, divided by who holds the money: deducted where its own payment service holds it, billed apart where another provider does. Billing apart is what C allows at launch without any provider's support. It is not the more restrictive of two ways that both references take. Each choice now holds at launch, and the other way stays reserved, like A and B, for the founder's decision in a record of its own. D-001's outcome and Scope, D-004's rows 6, 7 and 9 and its Scope, and the glossary's *Sharrwah's fees*, *platform balance* and *reserved, not built* say the same. This refines the earlier dispositions FP-3 ("never taken") and T-2 above. The "never" was found while testing a concern the founder raised on 25 October, held as a hypothesis for their assessment. The correction rests on the evidence above, and no rule is made of the concern.

**Applied:**

| Finding | What was done |
| --- | --- |
| FP-04 | The line stays as the method words it (`METHOD.md` section 14). The page's *Reserved, not built* now says that, because the line says "not built", building A or B is the founder's decision too, not only switching it on. |
| FP-05 | The courier in *What it means* is one "the seller contracts with". |
| FP-08 | A's licence is "a licence or permission", or perhaps a licensed partner, and no source read shows which. |
| FP-09 | B: none is shown for the first market yet, with the three reasons, and the pilot's own words, "unsettled, not unmet". |
| FP-10 | C's examples are dated and show where the money lands. Whether the first market's wallets link a seller's own account is asked at S-07. |
| FP-11 | The glossary's sources are named: the guard, the pilot's entry, and the platforms' help and structures. |
| FP-18 | Choice 1 sets the guard's words against its source. Choices 2 and 3 are left open by C itself. |
| FP-19 | The Tabby example keeps the Saudi request and the UAE article apart, quotes Salla's own English from each, and says that neither shows whose agreement covers an account asked for through Salla. The glossary's entry is corrected the same way, with the question marked open. |
| FP-20 (holds, note) | The page adds that Shopify's PayPal help names no agreement. |
| FP-22 | The source's own title for B is quoted. "Inside the platform's own payment product" is marked as the coordinator's reading, with BigCommerce's linked PayPal account against it. The glossary is corrected too. |
| FP-25, FP-26 | Choice 2 shows Shopify's two ways, with Capital's US scope and how its repayments are collected. Billing apart "needs nothing from the sellers' providers"; Sharrwah still needs a provider for its own billing (choice 3). |
| FP-28 | A balance sellers pay into holds the seller's own funds, like A, and is not sellers' money as defined. The glossary's *platform balance* and D-001's Terms say the same. |
| FP-30 | "At launch, and until you decide otherwise in a record of its own" replaces "the first version", on the page and in the Scope. |
| FP-36 | D-004 is named as a record of its own, which the founder's answer accepts with D-001 unless they say otherwise. |
| FP-37 (open) | S-04 is named, with its title. |
| FP-38 | The list of what is left open adds money products (S-02), selling in person and on outside marketplaces (S-10), what sellers are shown of their providers' balances (S-07), installments (D-005) and currencies (S-04). |
| FP-39 | The page says that buyers' money is outside the line and would come to the founder on its own. |
| FP-40 | Licensing at S-08 includes whether a platform that only links sellers' own providers needs a licence. |
| FP-41 | The risk is "in my assessment", with what A and B would each need. |
| FP-43 (open) | *Door and risk:* one-way under the method, because it decides about money (`METHOD.md` sections 2 and 6), and low risk in the coordinator's assessment because it keeps the arrangement that holds nothing. |
| FP-44 (open) | The answer line adds "defer", which the record weighs as an option and the founder chose at G1. |

**Not changed:** the line's own words (FP-04, above). **The cost to the founder:** the page grew from about 1,070 words to about 1,640.
