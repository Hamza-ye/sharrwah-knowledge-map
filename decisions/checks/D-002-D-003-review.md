# Review of D-002 and D-003

An independent review, 24 October 2026, of `decisions/D-002-the-payment-boundary.md` and `decisions/D-003-the-seller-ledger.md` as committed in 9621a46. It was done from the brief and the files it names, and nothing else.

**Result: 9 must fix, 15 optional.**

## Locators

| Short form | File |
| --- | --- |
| `D-002:n`, `D-003:n` | the two records, line n |
| `FA:n` | `evidence/shopify-engineering/finding-aids/20261010-shopify-engineering-sources.tsv`, line n. E030 to E036 are lines 31 to 37, and E040 is line 41. |
| `E0xx:n` | the captured text of that source: `evidence/shopify-engineering/runs/20261010T083026Z-engineering-sources/items/0xx-shopify.dev/text.txt`, line n. That run's `manifest.tsv`, lines 31 to 37, maps each E id to its folder. |
| `AM/…:n` | E040's capture: `evidence/shopify-engineering/runs/20261010T083203Z-repositories/activemerchant__active_merchant/…`, line n. The commit is `ca45b1b063ce2e1495e1427e0a1d42dcb482d57d` (`repos.tsv`:4). |
| `seam:n` | `git show 8946887:studies/payment-seam/seam.md`, line n |
| `sh-note:n` | `git show 8946887:studies/payment-seam/notes/shopify-crossings.md`, line n |
| `sa-note:n` | `git show 8946887:studies/payment-seam/notes/salla-crossings.md`, line n |
| `Q7:n` | `studies/proposals/drafts/Q7/draft.md`, line n |

## The must-fix findings at a glance

| # | Record and line | Finding |
| --- | --- | --- |
| 1 | D-002:31; D-003:27, 58 | E034 and E035 show idempotency for refund creation and inventory, not for "money-moving requests". The evidence for payment requests is E031 and E032. |
| 2 | D-002:91 | The precedent for long-pending payments cites the seam's element 3, which gives those examples as precedents for evidence levels. The seam's own entry says neither platform shows long pending (seam:86). |
| 7 | D-002:47–55, 87–89 | The attempt loses v0's obligation reference, and the change is not listed. Outcomes carry no outcome id and no links to their attempt or to the outcome they draw on, although both platforms have these links and D-003 needs them. |
| 8 | D-002:57, 106–111 | No capability says whether an order may be placed before payment (seam rule 11). Without one, the cash-on-delivery scenario can't be answered without naming the method. |
| 9 | D-002:50, 57 | The "status query" capability and evidence level expose polling, which D-002:47 keeps inside payments and which the seam finds on neither platform. |
| 14 | D-002:80, 88 | The currency edition is recast as "a provider's own variants" and moved behind the boundary, but the seam makes it a foundation value. "Nothing more" also rules out the two-currency amounts that both platforms carry. |
| 16 | D-003:28, 32, 38–47, 65 | The ledger's owner is not stated. Rule 19 is quoted without "Each ledger's content belongs to its owner". The payouts and provider fees it records have no path across D-002, and the seam keeps them and reconciliation inside payments. |
| 17 | D-003:41 | Per-currency "balances" that "move between currencies" read as money held. They are summed across custodians, so they can't be reconciled with any single provider. |
| 18 | D-003:40, 42 | The record doesn't say which outcomes post. The posting key must be permanent, because the cited mechanism expires keys after 24 hours, and a second posting with the same key but different content must be refused. |

---

## 1. Accuracy

### Statements checked and found accurate

| Record and line | Statement | Locator |
| --- | --- | --- |
| D-002:18 | The seam's contract, version 0, written on 10 October | seam:22; commit 8946887 is dated 2026-10-10 |
| D-002:32 | Payment methods are customized through a function (E036) | E036:52–54, 62–64 |
| D-002:33 | In Active Merchant, processors sit behind one adapter interface (E040) | AM/README.md:5–7; AM/lib/active_merchant/billing/gateway.rb:9–18 |
| D-002:46 | The offer is v0's element 1 without the edition | seam:28 |
| D-002:47 | The attempt id is also the idempotency key | seam:29; E032:198 |
| D-002:48–54 | The outcome record is v0's element 3, with "rail" changed to "provider", and without the edition | seam:30 |
| D-002:55, 56, 58–61 | Elements 4, 5 and 7 | seam:31, 32, 34. Shopify's check of stock and price before the debit is its "Inventory confirmation" (E032:1049–1077). |
| D-002:63, 73–75 | What the order side owns, and what is reserved | seam:36, 38–40 |
| D-002:98 | E030 to E036 were fetched on 10 October 2026 and cover these subjects | FA:31–37; `manifest.tsv`:31–37 |
| D-002:101 | 178 crossings for Shopify and 81 for Salla | seam:17–18; sh-note:5, 73; sa-note:5 |
| D-002:102 | "one query and 16 mutations, with no order id and no line items"; "Salla holding the money" | seam:17, 18 |
| D-003:54 | The Q7 draft's proposal, as quoted | Q7:129 (only the bold markup differs) |
| D-003:59 | The Q7 draft's "seller ledger" | Q7:78–80 |

### Finding 1 (must fix): E034 and E035 are cited for more than they show

- **Record and line:** D-002:31, "its money-moving requests carry idempotency keys (E034, E035)". D-003:27, "Shopify makes money-moving requests idempotent (E034, E035)". D-003:58, "Shopify's idempotency for money-moving requests". D-003:11 lists only E034 and E035.
- **Evidence:**
  - E034 applies only to Admin API mutations that support the `@idempotent` directive (E034:71). Its list, "last updated 2 February 2026" (E034:472), is inventory and location mutations plus `refundCreate` (E034:474–490).
  - E035 makes the directive mandatory from API 2026-04 for the same set (E035:38–56). Its only money-moving mutation is `refundCreate` (E035:40, 66).
  - The general claim is true of a different source. In the payments-app contract, the payment, refund, capture and void ids are each "Used as the idempotency key" (E032:198, 867, 952, 1033), and "Idempotency keys don't expire" (E031:277).
  - The two mechanisms differ. The Admin API keeps keys for 24 hours, then treats a retry as a separate operation (E034:109, 137). This matters to D-003 (finding 18).
- **Suggested change:**
  - D-002:31: "the payment, refund, capture and void requests it sends to a payments app each carry an id used as the idempotency key, and those keys don't expire (E031, E032); its Admin API makes idempotency mandatory for creating refunds (E034, E035)".
  - D-003:27 and 58: narrow the claim in the same way, and add E031 and E032 to D-003's evidence.
  - For D-003:27's "edited in place … lose their history", a closer precedent is Shopify's settlement ledger, where each balance-transaction type has "a reversal twin" (sh-note:141).

### Finding 2 (must fix): the precedent for long-pending payments cites the wrong place

- **Record and line:** D-002:91, "Long-pending payments. Shopify's manual payment methods, and Salla's bank transfer 'under review' (seam, element 3)."
- **Evidence:**
  - The seam's element 3 gives Shopify's "mark as paid" and Salla's "under review" as "precedents for evidence levels" (seam:30), not for long pending.
  - The seam's own entry on long pending says "Neither platform shows this, and Shopify never polls" (seam:86; also sh-note:254).
  - The examples can still stand as precedents for long pending, but at other locators:
    - a bank transfer on Shopify is a "Manual method, then 'mark as paid'", and on Salla a "Native 'under review' state with a receipt" (seam:76);
    - Shopify transactions can be PENDING or UNKNOWN (E033:781–794), and "pending" reaches the order (sh-note:140);
    - a payments app reports results asynchronously and may retry for up to 24 hours (E031:296–298);
    - Salla transactions can be pending (sa-note:49), and payment can be deferred (sa-note:111), with a window that ends (sa-note:144).
- **Suggested change:** cite these instead, and add: "The seam found no platform precedent for long pending with polling (seam:86). This record keeps polling behind the boundary (element 2), so only long pending crosses."

### Finding 3 (optional): the citations of E030 to E033 run slightly ahead of the captures

- **Record and line:** D-002:29, 30.
- **Evidence:**
  - E030 to E032 show the requests (E032:76) and the mutually exclusive resolve and reject (E031:289). They hold no list of states. The states that reach the order are in sh-note:140.
  - E033's capture is the status page (E033:762–794), with one sentence on kinds (E033:824). The kind values appear only in the finding aid's description (FA:34), whose kind page was checked by HTTP status but not captured.
- **Suggested change:** at D-002:29, write "requests, and resolve or reject results (E030 to E032)". At D-002:30, note that E033's kinds rest on FA:34, or capture the kind page.

### Finding 4 (optional): some locators are missing

- **Record and line:** D-002:18, "with the founder's F-06", and the ids KM-PAY-01 and KM-PAY-02. D-003:18, KM-ENG-05. D-002:99, "pinned at a commit".
- **Evidence:**
  - The seam names its question as "item 1 in `NEXT.md`" (seam:3) and doesn't mention F-06. None of the named sources holds F-06 or the KM ids.
  - E040's row in the finding aid describes the repository, and records that its page answered 403 (FA:41). The pinned capture is in the repositories run (`repos.tsv`:4).
- **Suggested change:** give a path for F-06 and for each KM id. For E040, give `20261010T083203Z-repositories/activemerchant__active_merchant/lib/active_merchant/billing/gateway.rb` at commit `ca45b1b`.

### Finding 5 (optional): parts of the column of notes for the first market are adopted

- **Record and line:** D-002:89, "Its column of notes for the first market is not part of this decision."
- **Evidence:** several notes are adopted in a neutral form:
  - "never reads live core data" (seam:28) becomes D-002:46;
  - partner cut-offs (seam:28) become D-002:70;
  - long pending (seam:29) becomes D-002:47;
  - deriving the payment status (seam:30) becomes D-002:54;
  - "never names a wallet or bank" (seam:33) becomes D-002:57.
- **Suggested change:** "It is adopted only where restated without the market, at D-002:46, 47, 54, 57 and 70."

### Finding 6 (optional): "flagged by the guard" is not at the cited line

- **Record and line:** D-003:54.
- **Evidence:** Q7:129 holds the proposal, not a flag by the guard. It does show why the guard applies: it names a market's currency and a zone ("Cash and electronic rials", "@ Sana'a").
- **Suggested change:** cite where the flag was recorded, or write "is set aside under the guard".

---

## 2. Completeness of D-002's seven elements

### Finding 7 (must fix): the obligation reference is dropped, and outcomes have no ids or links

- **Record and line:**
  - D-002:47 starts an attempt "with an attempt id, which is also the idempotency key, and the amount".
  - The outcome record (D-002:48–52) has no id of its own, and no link to its attempt or to the outcome it draws on.
  - D-002:87–89 lists the edition and the notes column as the only changes from v0, and D-002:18 and 38 present the record as v0 after the market guard.
- **Evidence:**
  - v0's attempt carries an "attempt id (also the idempotency key), obligation reference and amount" (seam:29). Dropping the reference has nothing to do with the guard, and the change is not listed.
  - Both platforms tie attempts to what they pay:
    - on Shopify, `group` is "shared across payment sessions, representing attempts to complete the same checkout or deferred payment capture" (E032:202–204), and the attempt id "must be surfaced to the merchant so that they can correlate Shopify orders with payments" (E032:198);
    - on Salla, "The order holds `payment_method` and `transaction_reference`" (sa-note:45), and the Salla note's proposed payment request carries an "Order reference" (sa-note:126, marked as inference).
  - Later money actions point at the original. Shopify's refund names "the original payment", and its captures and voids name the authorized payment (E032:871–873, 956–958, 1037–1039).
  - The seam's rules need these links:
    - for split tender (seam:133–136);
    - for refund plans that name "which outcomes it draws on" (seam:146–147);
    - for sellers' reconciliation "through the identifiers that cross: obligation reference, attempt id, outcome id and provider reference" (seam:157).
  - D-003:40 needs a stable id from the source to build its posting key (finding 18).
- **Suggested change:**
  - D-002:47: "…with an attempt id (also the idempotency key), the reference of the amount owed, and the amount".
  - D-002:48–52: add "its outcome id; the attempt it belongs to; for a capture, refund or void, the outcome it draws on".
  - D-002:55: "each request names the outcome it draws on".
  - Otherwise, list the removal under D-002:87, with its reason.

### Finding 8 (must fix): no capability says an order may be placed before payment

- **Record and line:** D-002:57 lists the capabilities. None says whether an order may be placed while its payment is pending.
- **Evidence:**
  - The seam's rule 11: "The order is created when the attempt succeeds, or when it is accepted as pending and the method's capabilities allow an order before payment, as with cash on delivery or transfer-with-proof" (seam:137).
  - Both platforms make this crossing:
    - Shopify: a manual method, later marked as paid (seam:76), and payment terms that "allow buyers to pay for their order at a later date" (E036:56–58);
    - Salla: payments report a "review hold or deferred payment", which the order turns into a status (sa-note:111); there is a deferred-payment window (sa-note:144); and a bank-transfer order showed "Partially paid" while awaiting review (sa-note:175).
  - D-002's own scenario, "cash on delivery with refusal at the door", is to be "answered from the seven elements alone" (D-002:108–111). When an attempt is pending, the order side has to decide whether to confirm and ship. Without this capability it can only decide by naming the method, which D-002:57 forbids.
- **Suggested change:** add to element 6 "whether an order may be placed before payment succeeds (paid on delivery, or by a due date the order side sets)". Add rule 11's sentence to element 2.

### Finding 9 (must fix): "status query" is broader than either platform needs

- **Record and line:** D-002:57, "status query" among the capabilities. D-002:50, "provider status query" as an evidence level beside "provider confirmation".
- **Evidence:**
  - D-002:47 says "How payments learns the result, by callback or by asking the provider, stays inside payments". The order side therefore has no use for knowing whether a method can be queried, or how the provider's answer was obtained.
  - Neither platform has this crossing. On long pending with polling, the seam says "Neither platform shows this, and Shopify never polls" (seam:86; sh-note:254).
  - It comes from the first market: the seam notes that its rails "have no callbacks and payments has to poll them" (seam:29, notes column). So it is also a Built element shaped by one market's facts (see section 3).
- **Suggested change:** remove "status query" from D-002:57. At D-002:50, merge "provider confirmation" and "provider status query" into one level, "the provider's record". Keep long pending as D-002:47 states it, since the guard allows it.

### Finding 10 (optional): "Payments owns" leaves out parts of the seam's list

- **Record and line:** D-002:65–71.
- **Evidence:** compared with seam:46–53, the list leaves out:
  - settlement, payout and custody ledgers (seam:49);
  - dispute mechanics and identity checks (seam:50);
  - partner relationships, licences and Sharrwah's position on each setup (seam:51);
  - tax on fees (seam:48).
  The custody ledger matters because D-002:93 keeps "a courier holding cash", and D-003:42 names couriers as custodians.
- **Suggested change:** add these items, or say why each is left out.

### Finding 11 (optional): the seam's rules and choices are neither adopted nor set aside

- **Record and line:** D-002:42–75.
- **Evidence:** the seam's rules (seam:104–168) and its six choices refine the elements. The seam calls the choices "proposals … until a decision record settles it" (seam:68–79, 70). The ones that bear most on the elements are:
  - rule 6: an attempt's timeout reaches core "as an expired or failed attempt" (seam:119–121), and Shopify's order sees "timed-out" (sh-note:140). D-002:47's states have no "expired".
  - rule 8: the seller's rules to hide, reorder or rename methods are applied by core's checkout (seam:127–129). D-002:32 cites E036 as a driver, but the decision doesn't say who applies them.
  - rule 11: rejection and pending reasons cross "as a closed set of categories" (seam:137). Shopify "works from closed lists of states and reasons" (sh-note:180), and Active Merchant has standard error codes (AM/lib/active_merchant/billing/gateway.rb:63–101).
  - rule 12, capture policy (seam:138–141), and rule 14, the refund's destination and its ceiling (seam:145–148).
- **Suggested change:** add a short list of "Rules and choices adopted from the seam", and state any that are set aside.

### Finding 12 (optional): the outcome record has no flag for test or live

- **Record and line:** D-002:48–52 and 71; D-003:39–42.
- **Evidence:**
  - Payments owns "simulated outcomes for testing" (D-002:71), but the outcome record can't tell them apart from live ones.
  - D-003 posts from these records, so it would post simulated sales that no provider's report contains.
  - Shopify sends `test` on every payments-app request (E032:214–218), and carries the flag "on orders, transactions and balance entries" (sh-note:171). Active Merchant's response carries `test?` (AM/lib/active_merchant/billing/response.rb:7, 17–19).
- **Suggested change:** add "test or live" to element 3. In D-003, post live outcomes only.

### Finding 13 (optional): the change scenario leaves out the settlement contract

- **Record and line:** D-002:112, "adds B behind the boundary, with no change to the elements".
- **Evidence:** B needs the settlement contract, which D-002:75 reserves; the Shopify note calls it "a second contract" (sh-note:237).
- **Suggested change:** "adds B, and the settlement contract beside the seven elements, which do not change".

---

## 3. The guard

### Passed

- Neither record names a market in its "Decision outcome" (D-002:42–75; D-003:36–43) or "Consequences" (D-002:77–82; D-003:45–49). This was checked by searching both records for market, currency and zone names. The only matches are in "The guard" (D-002:88, 93).
- Both records are typed Built, "the same in every market" (D-002:86; D-003:53).
- The general mechanisms the guard allows are present: long pending (D-002:47), evidence levels (D-002:50) and a courier holding cash (D-002:60; D-003:42). Manual reversal (D-002:55) has a Shopify precedent (seam:89).
- "The type of buyer action" (D-002:57) has a Shopify precedent: each of the five types of payments extension either collects fields on checkout or redirects the buyer (E030:119–126).
- D-003:49 leaves the cash-and-electronic question to S-04 and decides nothing about it.

### Built and shaped by one market's facts

The "status query" capability and evidence level (finding 9).

### Finding 14 (must fix): the currency edition is misdescribed and still needed in a neutral form

- **Record and line:**
  - D-002:80: "Seller and buyer amounts carry a currency and nothing more on the order side. How a provider's own variants of a currency are handled stays behind the boundary (subject S-04)."
  - D-002:88 removes the edition from the offer and from every amount, on the authority of "G1's B7", which is given no path.
- **Evidence:**
  1. **The seam's edition is not a provider's variant.** It is "its edition where a market's currency circulates in more than one" (seam:59). It belongs to the shared foundations, not to payments: "Other values per market, such as currency edition, rate policy, civil calendar and tax, are foundations" (seam:161; also seam:88).
     - Moving it "behind the boundary" contradicts that placement without saying so.
     - It would also let payments decide what an amount is worth, although D-002:63 gives the order side "what was agreed and is due".
  2. **"Nothing more" also rules out a general mechanism that both platforms carry on their amounts.** Shopify's amounts are a `MoneyBag` (shop and presentment) (sh-note:160). Salla's orders carry `exchange_rate` and `scope_exchange_rate` (sa-note:77). This is a crossing both platforms make that the elements, as worded, exclude.
  3. **Element 6 also drops "editions"** (seam:33), and D-002:88 doesn't list that change.
  4. **"G1's B7" can't be checked** from any path given.
- **Suggested change:**
  - Replace the first two sentences of D-002:80 with: "Every amount carries its currency as the money-and-currency foundation defines it (S-04). Where the amount agreed and the amount charged or settled are in different currencies, the record carries both, with the rate used."
  - Which currencies a market has then becomes a value configured per market, and the Built outcome is the same everywhere.
  - Give G1's B7 a path, and list the change to element 6 at D-002:88.

### Finding 15 (optional): the precedents in the guard's list need more care

- **Record and line:** D-002:90–93.
- **Evidence:**
  - **Evidence levels** are "partly shown … neither platform names the levels" (seam:85). Salla's "under review" with a receipt is a second precedent (seam:76).
  - **Shopify's cash custody** is "at the counter (S112)" (seam:87). The Shopify note finds "no Shopify crossing" for custody by a courier or agent, because "the cash model ends at the drawer" (sh-note:255). The precedent for a courier is Salla's (sa-note:60).
  - **Manual reversal** (element 4) is a general mechanism with a Shopify precedent (seam:89, S103), but it is not listed.
- **Suggested change:** add "partly shown" and Salla's precedent for evidence levels. Present Shopify's precedent as cash held at the counter. Add manual reversal to the list.

---

## 4. D-003

### Finding 16 (must fix): the ledger's owner is not stated, and its inputs have no path across D-002

- **Record and line:**
  - D-003 doesn't say whether the order side or payments owns the ledger.
  - It posts fees and "a payout reported by a provider" (D-003:39), names custodians (D-003:42), and reconciles "with each provider's reports" (D-003:47, 65).
  - It presents rule 19 as something the seam "found" (D-003:28).
  - Its option 1 is a ledger "separate from who holds the money" (D-003:32).
- **Evidence:**
  - Rule 19 is one of the rules "added after tagging" (seam:104–106). It continues: "…form a shared foundation used by core's order money and payments' custody and settlement ledgers. Each ledger's content belongs to its owner." (seam:163). D-003:28 leaves this out, and its quotes also change the seam's capitals.
  - The seam keeps "Settlement and payout ledgers. Custody ledgers, such as cash held by couriers and sellers" inside payments (seam:49). It also says "Reconciling outcomes against rails, partners and custodians stays inside payments" (seam:156).
  - Both platforms do the same:
    - Shopify keeps its settlement ledger, payouts and fees inside payments (sh-note:141–142);
    - Salla's balance, fees, payouts and COD remittance ledger are among what "never reaches the order or checkout" (sa-note:38, 53–60).
  - D-002 gives these facts no path. Fees stay inside payments (D-002:68), payouts are in the reserved settlement contract (D-002:75), and none of the seven elements carries a fee or a payout (D-002:46–61). D-003's scenario "a provider's payout report reconciles with the entries" (D-003:65) can't be run.
  - Sharrwah's bills to sellers are core obligations (seam:116–117).
- **Suggested change:**
  - **State the owner.** Recommended: the seller ledger is the order side's ledger of what is owed, recording who owes whom. Sales and refunds come from D-002's outcome records, and Sharrwah's fees are added to them.
    - Provider fees, payouts and custody stay in payments' records, and reconciliation with providers' reports happens there.
    - Sellers' statements join the two through the identifiers that cross (seam:157; finding 7).
    - Change D-003:39, 47 and 65 to match.
  - **Add "two ledgers, one per owner" as a considered option.** It is stronger than option 1 as written (see section 5).
  - **Quote rule 19 in full,** and call it a rule.
  - If D-003 keeps payouts and provider fees instead, D-002 needs a read-only element that carries them as the provider reports them, with no holding, netting or balance debits. The record must then say why it departs from the seam's placement.

### Finding 17 (must fix): per-currency "balances" read as money held and can't be reconciled

- **Record and line:** D-003:41, "Balances are per currency, and never added across currencies. They move between currencies only by a recorded conversion." Read with D-003:18, 26, 33, 42 and 43.
- **Evidence:**
  - **The record contradicts itself.**
    - It rejects option 2 because "a balance per seller … reads as money Sharrwah holds" (D-003:33), and requires that the ledger "must not become a balance Sharrwah holds" (D-003:26). It then adopts per-currency balances that "move between currencies".
    - A ledger that holds no money has nothing to convert, because only a custodian converts money.
    - D-003:18 also leaves currency conversion to S-04, while D-003:41 decides it.
  - **The wording comes from the Q7 draft** (Q7:78). The draft's platform precedents include wallets that, by its own next line, "hold their sellers' proceeds" (Q7:79–80).
  - **The balances can't be reconciled per provider.**
    - As written, balances are split only by currency, although each entry names a custodian (D-003:42). No subtotal therefore matches any one provider's report (D-003:47).
    - Nothing stops Sharrwah's fees (D-003:43) from being netted, in the same balance, against money that a provider holds for the seller. Netting belongs to the reserved settlement contract (D-002:75).
- **Suggested change:**
  - Replace D-003:41 with: "Amounts owed are summed per seller, counterparty, custodian and currency. They are never netted across counterparties or custodians, and never added across currencies. The ledger converts nothing. Where a custodian converts money and reports it, both amounts and the custodian's rate are recorded as reported."
  - This also keeps cash held by a courier apart from money held by a provider, without naming a market. It answers the concern of Q7:129 with a general mechanism.

### Finding 18 (must fix): the posting rules are missing

- **Record and line:** D-003:40, "Entries are posted once, by an idempotency key, and never edited", and D-003:42, "from the outcome records of D-002".
- **Evidence:**
  - **Which outcomes post is not said.** D-002's outcomes include authorizations (D-002:49), pending or unknown states that "may last a long time" (D-002:47), and evidence as weak as a buyer claim (D-002:50). An entry posted from a buyer claim or an unconfirmed outcome, with a provider named as custodian, records money that the provider's report will never show.
  - **The cited key expires.** D-003's only cited mechanism keeps keys for 24 hours; after that, "retries … will be treated as separate operations" (E034:109, 137). A provider's report imported again later would post twice. Shopify's payments-app keys "don't expire" (E031:277).
  - **A reused key with different content must not be dropped.** Shopify refuses it with `IDEMPOTENCY_KEY_PARAMETER_MISMATCH` (E034:357–383; E035:124). A ledger that silently keeps the first posting would hide a corrected line in a report.
- **Suggested change:** add:
  - "An entry is posted only from an outcome that moved money and succeeded: a sale, a capture or a refund. Authorizations and pending or unknown outcomes post nothing. A later failure or reversal posts a reversing entry."
  - "Each entry carries the outcome id, the provider's reference and the evidence level. A provider is named as custodian only on the provider's own record."
  - "The posting key is derived from the source (the outcome id or the provider's reference, with the entry type) and never expires. A second posting with the same key and different content is refused and raised for review."

### Finding 19 (optional): minor units, and amounts as reported

- **Record and line:** D-003:39, "amounts are kept in the currency's minor units".
- **Evidence:**
  - The number of minor units differs by currency. Active Merchant lists currencies without fractions and with three decimals (AM/lib/active_merchant/billing/gateway.rb:128–131).
  - Providers send amounts as decimal strings (E032:210).
  - E040 is a precedent for integer minor units (AM/README.md:59; AM/lib/active_merchant/billing/gateway.rb:263), but D-003 doesn't cite it.
- **Suggested change:** say that the number of minor units comes from the currency foundation. Record provider amounts exactly as reported, never recomputed and never passed through floating point. Cite E040.

### Finding 20 (optional): store credit owed by a seller is not an entry type

- **Record and line:** D-003:39.
- **Evidence:** the seam names store credit owed by a seller as a core obligation (seam:116). Salla refunds to a customer wallet (sa-note:49, 98–100).
- **Suggested change:** add it to the entry types, or set it aside explicitly.

The flag for test or live (finding 12) also affects reconciliation in D-003.

---

## 5. The options and drivers

### Stronger options missing

- **D-003:** "two ledgers, one per owner" (finding 16). The order side keeps what is owed, payments keeps custody and payouts, and the two are joined by the identifiers that cross. This is the seam's own design (seam:49, 156–157, 163), and it keeps D-003's option 1 "separate from who holds the money", as its title says.
- **D-002:** no option stronger than option 1 was found, but a fairer alternative is missing (finding 22).

### Finding 21 (optional): option 2 cites leaks that don't show what it claims

- **Record and line:** D-002:39, "Shopify's experience is the leaks it lists, such as installment orders that can't be edited."
- **Evidence:**
  - The leaks (sh-note:221–228) happen on Shopify, which already has a narrow provider contract (seam:17; sh-note:177–182). They are core features checking which arrangement was used.
  - The note's remedy is a capability profile (sh-note:228), which is D-002's element 6. The leaks say nothing about an order side calling providers directly.
- **Suggested change:** say that the leaks argue for element 6, and give the locator. Argue option 2 on its own terms: every new provider changes the order side.

### Finding 22 (optional): a fairer alternative to option 1 is missing

- **Record and line:** D-002:36–40.
- **Evidence:**
  - The driver at D-002:33 describes a different design from option 1: the order side calls one uniform adapter library, in process. Active Merchant is "a simple and unified API to access dozens of different payment gateways" (AM/README.md:5–7), "in production use since June 2006" (AM/README.md:12).
    - It has one base class, with purchase, authorize, capture, void, refund and verify (AM/lib/active_merchant/billing/gateway.rb:9–18).
    - Its response carries flags for success, pending, fraud review and test (AM/lib/active_merchant/billing/response.rb:7–33).
  - It is simpler than option 1, but it is synchronous, and it has no offer, verdicts or evidence levels. Shopify's own contract with providers is asynchronous (E031:296).
- **Suggested change:** add it as an option and compare it fairly with option 1. Option 1 should still win, on long pending and asynchronous outcomes.

### Finding 23 (optional): a driver has no evidence

- **Record and line:** D-002:27, "Providers and their protocols change often."
- **Evidence:**
  - E032 shows request fields added in API versions 2024-01, 2024-07 and 2024-10 (E032:207, 321, 532).
  - E035 is a breaking change for 2026-04 (E035:24–30).
- **Suggested change:** cite these.

### Finding 24 (optional): a driver's wording contradicts element 1

- **Record and line:** D-002:34, "nothing on the order side names a market".
- **Evidence:** element 1 passes "the buyer's and the seller's market" (D-002:46).
- **Suggested change:** "no rule or type on the order side refers to a particular market, currency variant, wallet or bank".

The other drivers are fair. D-003's three options are fairly stated, apart from the clash between option 2's objection and the adopted "balances" (finding 17).

---

## Not checked

- Statements that rest on files outside the brief: D-001, D-004, F-06, the KM ids, G1's B7, the founder's guard of 18 October, subject S-04, and risks W-07 and R-06.
- The crossing counts were checked against the seam and the two notes, not by counting the rows of the `.tsv` files, which the brief doesn't name.
