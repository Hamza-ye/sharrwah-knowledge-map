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
| D2-44 | Corrected, and it was the coordinator's error. Salla's review status and receipt aren't tied to bank transfers by the held structures, and its articles tie review to bank transfer only for Salla's own subscription renewals (`SA-en:816`). D-002's guard precedents and the glossary now say so. |
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

## Re-check

The changed wording is re-checked by a fresh independent agent, which tries to refute it. Pending.
