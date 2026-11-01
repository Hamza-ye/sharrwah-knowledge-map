# Alternatives check: the review's recommendations and the coordinator's two notes

*1 November 2026. This page checks `decisions/review.md` and the coordinator's two notes on it. It was written by an agent that wrote none of them. Shopify's evidence was read in observed-sh at commit `04de369da9ac84ae530ae80a55749167ff4139d4`, through its own guides first (`README.md`, `docs/READING.md`, `index/`).*

## For the founder

**What this page does.** It takes each recommendation in the review of your earlier decisions, and the coordinator's two notes on it, and asks two things. Was a real alternative left out? Does any claim about Shopify's shape fail against Shopify's own evidence? Every verdict is a reading, for your veto.

**The count.** 47 recommendations were checked in full. 26 hold, 21 hold with a change, and none fails. The 16 that stay as they are are all still sound; 7 of them come with a remark.

**The changes that matter most.**
1. **Money (the coordinator's Note 1, and S-02's D9).** Shopify's own money library holds each currency as a record, found by its code, and lets a new currency be added under a code of its own. Neither the review nor the note offers this. Starting the money decision here costs nothing now, and a second currency area later is just a new code. The room also stays where you put it: in how every amount names its currency.
2. **Retiring the rules on how the work runs (Note 2).** The note says `PLAN.md` and `CLAUDE.md` already carry these rules. They don't carry the effort floor, the four-agent limit, capture requests or the budget rule. A row like that should be retired only once its substance is written there. The budget row is spending, which is on your own list, so it should stay.
3. **Who holds sellers' money (lines 16 and 19).** Shopify links a business entity only to its own payment service, on its Plus plan, and keeps third-party payment methods with the main business. The review's design still works, but the reason it gives says more than Shopify shows. Its platform part is also written three times. Keep Decision 1 in your own words, and state the platform part once, in line 19.
4. **The guard (line 8).** The new words narrow "anywhere" to "in any market". Dropping the last sentence, which line 19 already answered, is enough.
5. **Line 25.** The review's first page says to drop only the exception. Its proposed words drop the whole sentence. One of the two needs to change.
6. **Line 29.** The recommended go would come after the first decisions are written. You reserved a go before architecture starts. Your answer to this page, given before step 3, can be that go.

**Smaller changes:**
- Keep line 26's sentence "where an earlier decision differs, this one holds", because line 35 relies on it.
- Retire line 30 rather than split it, since each of its parts already lives elsewhere.
- Add to D7 that Shopify takes payment in a market's own currency only through its own processor or Adyen.
- Keep retired rows in the file, so their pinned links still work (line 22).

**Nothing here reopens** Decision 1, the guard, or your markets.

## How to read it

- "Line N" is the row's line in `founder-decisions.tsv`.
- "The review" means `decisions/review.md`, and its sections are named as it names them.
- S-01's and S-02's pages and registers are in `studies/subjects/`.
- "The go of 29 October" is `founder-messages/2026-10-29-go.md`. "The handoff" is `founder-messages/2026-10-29-intent-handoff.md`. Both are cited by line.
- F1 to F16 are Shopify's facts. Each is quoted once, below, with its pinned link.
- Every verdict is a reading. Other judgements are marked *Reading*, and assumptions are marked *Assumption*.

## Shopify's shape, where a recommendation rests on it

- **F1. The business entity.** "A legal entity through which a merchant operates." Each "can be associated with its own" Shopify Payments account, and markets "can be assigned to a business entity to determine payment processing and" order attribution ([admin schema 2026-10, L217](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L217)).
- **F2. Business entities serve Shopify's own payment service, on Plus.** "Business entities are available on the Plus plan only." ([Help Center, business entities in markets, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L3)) "A business entity is the legal entity that processes payments for orders in a market." ([L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L6)) "Business entities are relevant only for stores using Shopify Payments with multiple accounts." ([L18](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L18)) "Existing orders continue to be associated with the business entity that was active when the order was placed." ([L19](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L19))
- **F3. Third-party methods stay with the main business.** "Selling with multiple entities is available only with Shopify Payments." ([Help Center, selling with multiple entities, L28](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L28)) "Certain features such as adding a third-party payment method are available only for the primary entity." ([L35](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L35)) "Additional third-party payment methods are displayed only on checkouts and for markets associated with the primary entity, with the exception of PayPal." ([L38](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L38))
- **F4. Each payment names its gateway; Shopify's payments account is a record apart.** An order transaction "represents a payment transaction that's associated with an order", with the fields "gateway" and "manualPaymentGateway", and an optional "shopifyPaymentsSet" ([admin schema, L2447](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2447)). The payments account is "Financial account information for merchants using Shopify Payments." ([admin schema, L3193](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3193))
- **F5. A payment taken outside any provider.** "After you receive payment for a customer's order, you can mark the order as paid" ([Help Center, manual payments, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md?plain=1#L10)).
- **F6. Payment providers plug in as apps.** Shopify's payments apps API has the mutations "paymentSessionResolve", "refundSessionResolve" and "paymentsAppConfigure" ([payments apps schema 2026-10, L26](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl?plain=1#L26)). A payment session is "A unique payment transaction." ([L27](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl?plain=1#L27))
- **F7. Shopify's own fees.** "If you don't activate Shopify Payments as your payment provider, then you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify." ([Help Center, getting paid, L11](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/getting-paid.md?plain=1#L11)) Its card fees are "deducted from your payouts rather than billed on your Shopify bill" ([Help Center, types of charges, L12](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L12)).
- **F8. The country is locked while money is attached.** "you need to deactivate all financial services before you can change your business entity." ([Help Center, managing business entities, L20](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/business-entities.md?plain=1#L20)) "The country of your billing address must match the country of one of your active business entities." ([L21](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/business-entities.md?plain=1#L21)) "you need to deactivate all financial services before you can change your store's country in your Shopify admin." ([L31](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/business-entities.md?plain=1#L31))
- **F9. The seller's area within a country.** The entity's address "Represents the address of a merchant's Business Entity.", with a "province" field ([admin schema, L218](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L218)). A fee is taxed by the seller's province: "If your legal business address is in Canada, then GST, HST, QST, PST, or RST is added to the Managed Markets fee, depending on your province." ([Help Center, Managed Markets, L78](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/international/managed-markets/overview.md?plain=1#L78))
- **F10. Market kinds and their order.** The market types include "REGION", "LOCATION", "COMPANY_LOCATION" and "CHANNEL" ([admin schema, L2004](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2004)). "B2B markets are more specific than retail markets. Retail markets are more specific than country or region markets." ([Help Center, market types, L105](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L105)) "Catalogs from all applicable markets are combined" ([L108](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L108)).
- **F11. A market for part of a country.** "Sub-region markets are available as an early access feature." ([Help Center, market types, L27](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L27)) "On a sub-region market, you can customize only the shipping options." ([L32](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L32))
- **F12. The primary market.** It "represents the default customer experience for your store" ([Help Center, managing markets, L113](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/managing-markets.md?plain=1#L113)). "All changes to your store's default settings apply to your primary market automatically." ([L117](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/managing-markets.md?plain=1#L117)) "Your primary market is determined by your store currency" ([L118](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/managing-markets.md?plain=1#L118)).
- **F13. Money in Shopify's API.** An amount "Combines a decimal amount with a three-letter currency code" ([admin schema, L2266](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2266)), drawn from "The currency codes that represent the world currencies throughout the Admin API." ([L985](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L985)) The pair "contains the equivalent in the shop's base currency" ([L2263](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2263)).
- **F14. Money in Shopify's own library.** It "Provides a `Money::Currency` class which encapsulates all information about a monetary unit." ([money README, L11](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L11)) "Currencies are consistently represented as instances of `Money::Currency`." ([L92](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L92)) "To load custom currencies from a YAML file:" ([L186](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L186)), through a setting named "experimental_custom_currency_path" ([L189](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L189)). "Custom currencies are looked up after ISO and crypto currencies, so they cannot shadow built-in currencies." ([L205](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L205))
- **F15. Paying in a market's own currency.** "To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor." and "If you use a different provider, then customers in all markets pay in your store" ([Help Center, local currencies, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md?plain=1#L3)).
- **F16. Gift cards.** "You can't create gift cards in a specific market's local currency." ([Help Center, discounts and gift cards, L51](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/discounts-and-gift-cards.md?plain=1#L51))

---

## The coordinator's two notes

### Note 1 · Money: start from Shopify's way
- **The recommendation:** start first decision 7 (money) from an amount with a standard currency code, Shopify's way. Keep the review's extension, amounts that refer to a currency record, only if it costs almost nothing now; otherwise it waits for the market that needs it.
- **The genuine alternatives:**
  - (a) The review's: "Amounts refer to a currency record, one per currency code at launch", stated in first decision 7 as an extension of Shopify's shape, with its cost (the review, 'D9', platform part).
  - (b) Note 1's: Shopify's code first, and the record only if it's nearly free.
  - (c) *Not named by either:* the form of Shopify's own money library. An amount carries its currency, and the currency is a record found by its code and held as data. A currency outside ISO's list is added under a code of its own (F14). A second currency area under one ISO code then gets a new code and its own record. Where a provider takes only ISO codes, the new code maps back to the ISO one.
  - (d) Wait entirely, under line 35's "Sharrwah extends it, case by case", with no room now.
- **The evidence:**
  - *For (b) and (c):* Shopify's API names an amount's currency by a three-letter code from Shopify's own list (F13). First decision 7 cites ISO 4217 as practice (`first-decisions.md`, '7. Money').
  - *For (c):* in Shopify's library, every currency is a record found by its code, and new currencies load from data (F14). *Reading:* the Money pattern that first decision 7 needs already keeps each currency's details somewhere (minor units, rounding, symbol), so (c) adds nothing now. *Condition:* the library names its custom-currency setting experimental (F14).
  - *Against (a)'s second record under one code:* Shopify's library won't let a custom currency reuse an ISO code (F14), and Shopify's API carries the code alone (F13). *Reading:* if two records share one code, a reader of the API can't tell them apart. So the API (first decision 6) must change later either way, and the record doesn't spare that change.
  - *For (a):* S-02 counts a bare code in every amount as "a redesign", since "every money record, rate and report would then have to learn the area" (S-02 `decisions.md`, D9, 'Changing course later'). *Reading:* that is only true if the code must stay ISO's. Under (c), the area travels in the code itself. Records, rates and reports need no change; only the payments area's border maps the new code to ISO's. That is one module.
  - *Against (d), and on where the room sits:* the go of 29 October (line 12) says "the room S-02 recommends for D9 is in the core: how every amount names its currency". Line 29 calls D9 "the worked example". *Reading:* (c) keeps that room in the core, as a new code in the platform's currency list. (d) moves it to a market's setup.
- **Left out, or not borne out:** yes, (c). The note's "an amount with a standard currency code" describes Shopify's API (F13). Shopify's own library also holds the currency as a record (F14). So the note's choice between a code and a record is narrower than Shopify's actual shape.
- **Verdict: holds, with a change.** Start first decision 7 from (c): Shopify's API form, over currencies held as data, as Shopify's library holds them. First decision 7's record then compares two things, with their cost: (a)'s second record under one code, and a new code. If it drops the room, it says so for your veto, because the go of 29 October places that room in the core. *Assumption:* a code of Sharrwah's own fits Shopify's three-letter form. None is chosen here.

### Note 2 · Retire the rules that only govern how the work runs
- **The recommendation:** retire the kept rows that only govern how the work runs, such as effort levels, agents at once, capture requests, the evidence guides and budgets, "since PLAN.md and CLAUDE.md carry them". Keep only business decisions and the platform's.
- **The genuine alternatives:**
  - (a) The review's: keep every working-method row that still holds.
  - (b) The note as written.
  - (c) Retire a working-method row only once `PLAN.md` or `CLAUDE.md` carries its substance, and say where.
  - (d) Keep any row that is spending, or a choice only the founder can make.
- **The evidence:**
  - I searched both files for these terms. `PLAN.md` and `CLAUDE.md` say nothing about effort levels, agents at once, capture requests or budgets. The nearest is `PLAN.md` line 28: each decision reports its cost.
  - They do carry four rules:
    - credentials: `CLAUDE.md` line 37, which is line 4 almost word for word;
    - code: `PLAN.md` line 23, which cites your decision of 24 October;
    - history: `CLAUDE.md` line 19, which is line 12's rule;
    - in part, the evidence guides: `CLAUDE.md` line 17 names three guides, while line 33 names seven.
  - Budgets: line 26 puts "spending" on your own list. The review files line 23 under "your list (spending), applied to the method" (the review, 'Line 23'). So the note's own test keeps line 23.
  - Line 32 is your floor on a choice you had delegated (line 6). You set it because "Previous work has shown that lower effort can miss substantial evidence and leave important gaps." (line 32, its basis). Retired, with nothing carrying it, effort could drop again.
  - Line 24 includes a step of your own: "the founder hands it on".
  - For retiring: `CLAUDE.md` line 25 says "Keep only what a decision needs now", and lines 13 and 26 make the method engineering's.
- **Left out, or not borne out:**
  - The note's reason doesn't hold for four of its five examples.
  - The review, for its part, never considered retiring the working-method rows that `CLAUDE.md` or `PLAN.md` already carry (lines 4, 10 and 12).
- **Verdict: holds, with a change.**
  - Retire now: lines 4 and 10, and line 12 (its history rule is in `CLAUDE.md` line 19).
  - Retire once their rules are written into `PLAN.md`'s method: lines 32, 33 and 34, and line 24 (with your hand-on step written there too).
  - Retire only with their substance carried: lines 7, 9, 13 and 14.
  - Keep line 23, because it is spending, and line 11, your own choice, which engineering can't make for you.

---

## The review's first page: what it asks of you

### 1. Approve the new words as written
- **The recommendation:** approve the new words for the 12 reworded rows and the parts of the 2 split rows, as written.
- **The genuine alternatives:**
  - (a) As written.
  - (b) With the changes on this page.
  - (c) Fewer: only the rows on your list and the platform's, once Note 2 retires the working-method rows.
  - (d) None: leave the earlier rows as they are, with line 35 holding where they differ ("where they differ, the later holds", line 35, its basis).
- **The evidence:**
  - Line 13 says you are "not asked to audit lists of practices or decisions".
  - `CLAUDE.md` line 24 allows only approved words into the file.
  - *Reading:* (d) would leave dead pointers in the file, such as `PLAN.md` sections that no longer exist (lines 13 and 32).
- **Left out:** (c) and (d).
- **Verdict: holds, with a change.** Approve with this page's changes, and fewer of them if Note 2 retires the working-method rows. (d) is the weaker choice.

### 2. Line 8: drop its last sentence
- **The recommendation:** drop "Whether the design provides for either arrangement is for the work to recommend …".
- **The genuine alternatives:**
  - (a) Drop it.
  - (b) Keep it.
- **The evidence:** you answered that sentence yourself on 26 October with "Keep room, as recommended." (line 19).
- **Left out:** none. The words proposed around it are checked under Line 8 below.
- **Verdict: holds.**

### 3. Line 25: drop the exception
- **The recommendation:** drop "without a genuine, justified reason".
- **The genuine alternatives:**
  - (a) Drop the exception.
  - (b) Keep it.
- **The evidence:**
  - Line 35 says a market's limits "never define the platform".
  - Line 26's "Launch and today's resources decide when, never whether" covers today's capacity.
- **Left out:** none. But the proposed words for line 25 do more than this item says: see Line 25 below.
- **Verdict: holds.**

### 4. Line 26: read the class as Shopify's model
- **The recommendation:** yes.
- **The genuine alternatives:**
  - (a) Yes, with new words.
  - (b) No new words: line 26's own review column already says that where it "differs from the decision of 1 November, that one holds".
- **The evidence:** line 35 is later and replaces the class with Shopify's model.
- **Left out:** (b). It is weaker, because it leaves several platforms named in a row that still binds.
- **Verdict: holds.** One sentence of the new words needs fixing: see Line 26.

### 5. Line 29: your go on the first decisions' records is that go
- **The recommendation:** your go on the first decisions' records (`PLAN.md`, the steps, 3) is the go that line 29 reserved before architecture starts.
- **The genuine alternatives:** see Line 29 below. The left-out one is to make your answer to this page, before step 3, that go.
- **The evidence:**
  - Line 29: "architecture starts on my go on that plan".
  - The first decisions' records are the first architecture work (`PLAN.md` line 22).
- **Left out:** yes.
- **Verdict: holds, with a change.** As under Line 29.

### 6. Line 23: keep the budget rule for every step
- **The recommendation:** keep "a budget must never cost evidence", now about Shopify's evidence, for every step.
- **The genuine alternatives:**
  - (a) Keep it, reworded.
  - (b) Retire it, as Note 2 would.
- **The evidence:** "spending" is on your list (line 26), and nothing else carries the rule (Note 2).
- **Left out:** none.
- **Verdict: holds.**

### 7. A veto on the 11 retirements, and on D9 going to first decision 7
- **The recommendation:** both are engineering's call, for your veto.
- **The genuine alternatives:** your approval, rather than a veto, for retiring rows that touched your own list: line 3 (business model) and line 18 (business scope).
- **The evidence:**
  - Line 26 carries both questions: "plans and prices", and "Sharrwah rules out nothing the class shows".
  - So retiring those rows changes nothing on your list (*reading*).
- **Left out:** none of weight. D9's starting point changes with Note 1, but D9 still goes to first decision 7.
- **Verdict: holds.**

---

## Part 1: the rows built on Decision 1's frictions

### Line 8 · The guard (stays, with new words)
- **The recommendation:**
  - Drop the last sentence.
  - Change "goes live anywhere" to "goes live in any market" (the review, line 57).
  - Add "The platform keeps room for both, as the decision of 29 October keeps room for each such service; how is engineering's."
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Drop only the last sentence, and keep everything else word for word.
  - (c) Keep the row as it is, its last sentence already answered.
- **The evidence:**
  - Line 19 answered the last sentence on 26 October. The review credits line 26, three days later.
  - The handoff, line 43, says: "Don't: reopen Decision 1 or the guard".
  - *Reading:* S-02's E5 attaches the holding arrangement to the business, not to the market. So "anywhere" is the wider guard, and "in any market" narrows yours.
  - The added sentence repeats lines 19 and 26.
- **Left out:** (b).
- **Verdict: holds, with a change.** Take (b). Keep "anywhere", and don't add the sentence.

### Line 15 · One Yemen row per decision (retired)
- **The recommendation:** retire it, because line 35 makes a market's facts that market's setup.
- **The genuine alternatives:**
  - (a) Keep the Yemen row.
  - (b) Retire it.
  - (c) Check a market's facts only at its setup. This is what line 35 and `PLAN.md` line 5 already do.
- **The evidence:**
  - D8 and D9 are the needs "the Yemen row found that no platform meets" (S-02 `decisions.md`, line 7).
  - Line 35 says a market's facts "never define the platform".
- **Left out:** none.
- **Verdict: holds.**

### Line 16 · Decision 1 (split)
- **The recommendation:** split it into three parts.
  - A platform part: "a place in the platform, set for the business that takes the payment", with C as its value.
  - Your part: A and B off, and the three defaults.
  - A market part: the providers, couriers and channels that fill C.
- **The genuine alternatives:**
  - (a) The split.
  - (b) Keep line 16 word for word. Line 19 then carries the platform's place, and the couriers, transfers and cash in line 16 read as your description of C, filled at each market's setup. The handoff, line 43, asks not to "take my wording as the design".
  - (c) Split it differently. Line 16 keeps your part, with one added sentence: "The providers, couriers and channels that fill C in a market are that market's setup." The platform part is stated only in line 19.
- **The evidence:**
  - The review's platform part for line 16 says what its words for line 19 and S-01's E1 say, so the same part is written three times. Line 16 calls it "a place in the platform"; line 19 says "it is not a property of the platform".
  - Shopify, under C: each payment names its own gateway (F4). Providers plug in as apps (F6). A payment outside any provider is marked paid (F5). A business entity matters only for Shopify's own payment service (F2, F3).
- **Left out:** (b) and (c).
- **Verdict: holds, with a change.** Take (c): your choice stays in your own words, and the platform part is stated once.

### Line 17 · Decisions 2 to 12 (stays, with new words)
- **The recommendation:** keep the row, with its subject pointers replaced. "Installments (Decision 13) are decided with the payments area's design, and currency (Decision 14) with first decision 7, Money."
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it, since it follows from line 16 and S-01's register keeps each answer, with its reopening (S01-D2 to S01-D12).
  - (c) As the review proposes, but with installments split. The platform part goes to the payments area. The question of which installment providers, and on what terms, goes to each market's setup, with your partners.
- **The evidence:**
  - Under C, "the question narrows to which providers, on what terms" (S-01's register, S01-D13).
  - "Commercial agreements and partners" and "financing" are on your list (line 26).
  - *Reading:* (b) would lose your acceptance of "no agency role" and "no security interest", which touch the company's legal structure, also on your list.
- **Left out:** (c).
- **Verdict: holds, with a change.** Take (c).

### Line 19 · Keeping room for A and B (stays, with new words)
- **The recommendation:** "Who holds sellers' money is a setting of the business that takes the payment …; it is not a property of the platform. C is its value everywhere at launch …". The review's reason: "The new words key it on the business, as Shopify's shape does."
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Keep line 19 as written, "a market's setting", read as you asked: "my words of 26 October were a working description" (the handoff, line 39). S-02's E5 already reads it that way, and you didn't veto E5 (line 30).
  - (c) Narrower, in Shopify's terms. The business carries whether a holding service run through Sharrwah (A or B) may be switched on, as Shopify ties its own payments account to a business entity (F1, F2). Under C, each payment records who holds it, as Shopify's transaction names its gateway (F4).
- **The evidence:**
  - Shopify does assign markets to entities "to determine payment processing" (F1). But this applies only on Plus, and only with Shopify's own payment service (F2).
  - Third-party methods stay with the main business (F3).
  - So under C, the value everywhere at launch, Shopify's shape doesn't tie anything to the business at all.
  - *Reading:* "who holds" read as one value per business sits badly with Decision 1's own words, "Each payment method's provider holds the money" (line 16).
- **Left out, or not borne out:** (b) and (c). The claim "as Shopify's shape does" holds only for Shopify's own payment service.
- **Verdict: holds, with a change.** Keep the design, and state its reason with Shopify's conditions (F2, F3). Better, take (c)'s words: "Whether a holding service run through Sharrwah (A or B) may be switched on is a setting of the business that takes the payment, which each market reaches through the business assigned to it. Each payment records who holds it." The rest of the review's words stay.

### Line 21 · No test against Shopify alone (retired)
- **The recommendation:** retire it, because line 35 means the holding place is read from Shopify's shape anyway, at first decisions 5, 7 and 12.
- **The genuine alternatives:**
  - (a) Keep declining the test.
  - (b) Retire it.
  - (c) Run the test now.
- **The evidence:**
  - A test without Yemen already reached C (`decision-1.md`, 'A test, not a source').
  - F2 and F3 are what a test against Shopify alone would read. They now go to first decision 5.
- **Left out:** none. (c) is what first decision 5 does.
- **Verdict: holds.**

### Line 22 · B1 to B8 left in history (retired)
- **The recommendation:** retire it. Questions that B1 to B8 raise are taken up later "through the pinned link in line 22".
- **The genuine alternatives:**
  - (a) Retire the row and delete it.
  - (b) Retire it but keep it in the file, its review column marked retired.
  - (c) Move its pinned link into the record that will need it.
- **The evidence:**
  - History is used only through a link "pinned to a commit in a working file" (`CLAUDE.md` line 19).
  - The review never says what retiring does to a row.
- **Left out:** the choice between (a), (b) and (c). Under (a), the review's own route to B1 to B8 disappears.
- **Verdict: holds, with a change.** Say that retired rows stay in the file, marked retired (b). The same applies to lines 12, 29 and 31.

### Line 25 · Sharrwah's markets (stays, with new words)
- **The recommendation:** keep the market list and the basis for competing. The rule on Yemen's circumstances goes, because "The dropped sentence is replaced by line 35" and line 26.
- **The genuine alternatives:**
  - (a) Drop the whole sentence, as Part 1's words do.
  - (b) Drop only the exception, as the review's first page (item 3) says. This keeps "Yemen's present circumstances and today's business capacity don't become permanent product or architectural constraints".
  - (c) Keep the row as it is, with line 26's test ("an engineering reason with evidence") and line 35 governing.
- **The evidence:**
  - Line 35 covers a market's limits and the platform. It doesn't name "product" constraints or today's capacity.
  - Line 26 covers capacity with "when, never whether".
- **Left out:** the review proposes (a) in Part 1 and (b) on its first page, so you would be approving two different things.
- **Verdict: holds, with a change.** Take (b): it does what item 3 says, and it keeps your protection in your own row.

### Line 30 · No veto on S-02's rulings (split)
- **The recommendation:** split it into three parts.
  - A platform part: D1 to D7 and E1 to E5 go to first decisions 5 and 7, with a reopening rule.
  - Your part: plan limits on markets.
  - A market part: D8's and D9's extensions wait.
- **The genuine alternatives:**
  - (a) The split.
  - (b) Retire the row. Each of its parts lives elsewhere:
    - the plan limits under "plans and prices" (line 26);
    - the reopening rule in line 14 and in `PLAN.md` line 29;
    - D8's and D9's market parts in their own verdicts;
    - D1 to D7 in first decisions 5 and 7, each record for your veto (`PLAN.md` line 14).
  - (c) Keep it as it is.
- **The evidence:**
  - S-02's rulings are "engineering's rulings, for your veto" (S-02 `decisions.md`, line 9).
  - Only approved decisions go in the file (`CLAUDE.md` line 24).
  - Line 26 says "Everything else is engineering's".
  - *Reading:* the split's platform part is routing, not a decision.
- **Left out:** (b).
- **Verdict: holds, with a change.** Take (b).

---

## Part 2: the other rows

### Line 2 · Go on the plan of 12 October (retired)
- **The recommendation:** retire it.
- **The genuine alternatives:**
  - (a) Retire it.
  - (b) Keep it.
- **The evidence:** it was replaced by line 12 and by line 35, on which `PLAN.md` rests (`PLAN.md` line 3).
- **Left out:** none.
- **Verdict: holds.**

### Line 3 · No standing business model (retired)
- **The recommendation:** retire it. The review's reason is "Replaced by line 35: the model is Shopify's".
- **The genuine alternatives:**
  - (a) Retire it, as replaced by line 26's list.
  - (b) Keep it, as a record that no business model is set.
- **The evidence:**
  - Line 3 is about the business model.
  - Line 35's "Shopify's model" is the platform's shape (`PLAN.md` line 4: "its records, flows and extension points").
  - "Plans and prices" are yours (line 26).
- **Left out, or not borne out:** the reason given mixes the two models.
- **Verdict: holds, with a change.** Give the reason as line 26: the business model stays yours, and it is still open. Line 35 doesn't adopt Shopify's.

### Line 5 · Q3's two sets of rows (retired)
- **The recommendation:** retire it.
- **The genuine alternatives:**
  - (a) Retire it.
  - (b) Keep its caution that an agent's list is not a requirement.
- **The evidence:** that caution is carried by the rule that every claim is a fact, a reading or an assumption (`PLAN.md` line 8).
- **Left out:** none.
- **Verdict: holds.**

### Line 6 · Agents' effort, delegated (retired)
- **The recommendation:** retire it.
- **The genuine alternatives:**
  - (a) Retire it.
  - (b) Keep the delegation.
- **The evidence:** line 32 assumes the delegation ("where the coordinator sets it"), and line 13 makes the method engineering's.
- **Left out:** none.
- **Verdict: holds.**

### Line 7 · How work comes to you (stays, with new words)
- **The recommendation:** keep the rule, without its answer about the pilot. "Method rulings" becomes "engineering's rulings".
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it, as Note 2 would.
- **The evidence:** nothing else carries it. `CLAUDE.md` line 23 only asks for a reading of your message.
- **Left out:** (b), which needs the rule carried into `CLAUDE.md` first.
- **Verdict: holds.**

### Line 12 · The reset of 25 October (stays, with new words)
- **The recommendation:** keep only its rule on history, because "no other decision of yours states it".
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it.
- **The evidence:**
  - `CLAUDE.md` line 19 states the same rule.
  - O-01's question, which company contracts with sellers, is on your list (line 26: "the company").
  - F-00 to F-06 bind nothing once they are outside the working files.
- **Left out:** (b).
- **Verdict: holds, with a change.** Retire it (Note 2), unless you want the rule in your own file.

### Line 13 · Who decides what (stays, with new words)
- **The recommendation:** keep it, pointing to line 26's list instead of a `PLAN.md` section.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it, because line 26 and `PLAN.md` line 31 carry the list and the veto.
- **The evidence:** nothing else carries "is not asked to audit lists of practices or decisions".
- **Left out:** (b), which needs that clause carried first.
- **Verdict: holds.**

### Line 18 · The subjects S-02 to S-11 (retired)
- **The recommendation:** retire it.
- **The genuine alternatives:**
  - (a) Retire it.
  - (b) Keep the scope it set: evidence for all ten subjects.
- **The evidence:** line 26 carries that scope: "Sharrwah rules out nothing the class shows".
- **Left out:** none.
- **Verdict: holds.**

### Line 23 · A budget never costs evidence (stays, with new words)
- **The recommendation:** keep it, now about Shopify's evidence, for every step.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it, as Note 2 would.
  - (c) Widen it to all the evidence the decisions use.
- **The evidence:**
  - Spending is on your list (line 26).
  - *Reading:* published practice is cited, not captured, so it doesn't cost the budget the way capture does. That leaves (c) adding little.
- **Left out:** none.
- **Verdict: holds.**

### Line 24 · Evidence not held is a request (stays, with new words)
- **The recommendation:** keep the row as written, with two changes: "observed-sh or observed-sa" becomes "observed-sh", and "a subject" becomes "a decision".
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it, as Note 2 would.
- **The evidence:**
  - The decision text also says "the repositories' journey catalogs" and "into that repository". Both are still plural, or vague, with only observed-sh left.
  - It includes your own step, "the founder hands it on".
- **Left out:** (b), which needs the procedure written into `PLAN.md` first.
- **Verdict: holds, with a change.** Make it "observed-sh's journey catalogs" and "into observed-sh".

### Line 26 · Sharrwah's intent (stays, with new words)
- **The recommendation:** new words, with Shopify's model in place of the class, and added lines (1), (2) and (4) folded in.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Leave the row as it is, with line 35 holding where they differ.
  - (c) Make only the smallest edits.
- **The evidence:**
  - The new words drop "where an earlier decision differs, this one holds" (line 26). Line 35's basis relies on that sentence: "where they differ, the later holds, as that row says of the decisions before it".
  - The review itself uses line 26's precedence (under Line 8).
- **Left out:** the dropped sentence.
- **Verdict: holds, with a change.** Keep "Where an earlier decision differs, this one holds."

### Line 27 · The class's model before architecture (retired)
- **The recommendation:** retire it. Its order survives, because Shopify's shape is read before any first decision is recorded.
- **The genuine alternatives:**
  - (a) Retire it.
  - (b) Reword it for Shopify.
- **The evidence:**
  - First decision 2 divides the platform into areas by Shopify's own components (`first-decisions.md`, '2. Areas and their borders').
  - First decisions are derived from Shopify's shape (`PLAN.md` line 20).
- **Left out:** none.
- **Verdict: holds.**

### Line 29 · Architecture's own plan (retired)
- **The recommendation:** retire it. Your go on the first decisions' records is the go that line 29 reserved.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Your go on `PLAN.md` and on the list of fifteen, given with your answer to this page, before step 3. These state what line 29 asked of an architecture plan:
    - what it needs to know, and where each part comes from (`PLAN.md` lines 8 and 20);
    - who decides, and how each decision is made and recorded (`PLAN.md` lines 14 and 31);
    - what comes first (`first-decisions.md`, 'Their order').
  - (c) A separate architecture plan.
- **The evidence:**
  - Line 29 says "architecture starts on my go on that plan".
  - The records are the first architecture work (`PLAN.md` line 22).
  - Each record comes to you for veto anyway (`PLAN.md` line 14).
  - *Reading:* (a) puts your go after the work it was meant to come before.
- **Left out:** (b).
- **Verdict: holds, with a change.** Take (b).

### Line 31 · What comes at GM (retired)
- **The recommendation:** retire it, because "Your view of each step is now its one page".
- **The genuine alternatives:**
  - (a) Retire it.
  - (b) Keep its purpose, reworded for Shopify: your view of the platform's extent, "as my view of the extent: its areas and capabilities" (line 31), and a check for what the platform misses.
- **The evidence:**
  - Each step's page reports decisions, not the extent.
  - First decision 2 will set out the areas.
- **Left out:** (b).
- **Verdict: holds, with a change.** Say that the view of the extent isn't carried, or that it comes with first decision 2's record. Then your veto is informed.

### Line 32 · The agents' effort floor (stays, with new words)
- **The recommendation:** keep it, without its last sentence, which points to a table that no longer exists.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it once `PLAN.md` carries the floor.
- **The evidence:** nothing else carries the floor (Note 2).
- **Left out:** (b).
- **Verdict: holds.**

### Line 33 · Read the evidence through its guides (stays, with new words)
- **The recommendation:** observed-sh only, with the seven guides named, and without `held_index.py`.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Retire it once `CLAUDE.md` line 17 names all seven guides.
- **The evidence:** all seven named guides exist in observed-sh at this commit. `CLAUDE.md` line 17 names three of them.
- **Left out:** (b).
- **Verdict: holds.**

---

## Part 3: beneath the rows

### S-01's E1 · The holding arrangement (stays, with new words)
- **The recommendation:** use line 19's new words.
- **The genuine alternatives, the evidence and what was left out:** as for Line 19 (F1 to F4).
- **Verdict: holds, with a change.** As for Line 19.

### Default 2 · Sharrwah's fees billed apart (stays, with new words)
- **The recommendation:** reword default 2 with line 20 folded in. Line 20 also "stays", and line 16's part reads "default 2 as line 20 narrows it".
- **The genuine alternatives:**
  - (a) Fold line 20 into default 2 and retire line 20.
  - (b) Keep default 2 as written and line 20 as it is.
- **The evidence:** Shopify's fees go on its bill when its own payment service is off (F7).
- **Left out:** the review does both at once, so the same rule would sit in two places.
- **Verdict: holds, with a change.** Pick one. *Reading:* (b) needs no new words.

### S-02's rulings: one alternative for all
These rulings are engineering's, for your veto (S-02 `decisions.md`, line 9). They are re-read from Shopify's shape at first decisions 5 and 7 anyway (`PLAN.md` line 22). So there is a genuine alternative for each of them: put no new words to you now, and let those records restate them from Shopify's evidence, with S-02's page as input. That is the Line 30 change above. Each ruling below is checked on its own merits.

### D1 · Where a store's country is held (stays, with new words)
- **The recommendation:** a business record holds the country, "as Shopify's business entities do". It drops the seat, which is a Salla setting.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) The store's own field.
- **The evidence:**
  - Shopify's entity holds an address with a country (F1, F9) and locks the country while money is attached (F8).
  - Several entities per store are a Plus feature (F2).
- **Left out:** none.
- **Verdict: holds.**

### D2 · When a seller moves country (stays, with new words)
- **The recommendation:** the country never changes in place, and the checks run first.
- **The genuine alternatives:**
  - (a) A new record.
  - (b) A change in place, once the checks pass.
- **The evidence:** Shopify locks the entity and the store's country until every financial service is off (F8).
- **Left out:** none.
- **Verdict: holds.**

### D3 · What follows the seller's country (stays, with new words)
- **The recommendation:** one entry point, keyed on the business serving the order or market.
- **The genuine alternatives:**
  - (a) One entry point.
  - (b) A country per feature.
- **The evidence:**
  - Shopify assigns markets to entities "to determine payment processing" (F1).
  - Orders keep their entity (F2).
- **Left out:** none.
- **Verdict: holds.**

### D4 · What a market can be (stays, with new words)
- **The recommendation:** Shopify's market kinds, without BigCommerce's storefront kind and customer group.
- **The genuine alternatives:**
  - (a) Shopify's kinds.
  - (b) Keep the other platforms' kinds.
- **The evidence:**
  - Shopify's market kinds: region, location, company location and channel (F10).
  - Line 35: "No other platform's reading shapes the model".
- **Left out:** none.
- **Verdict: holds.**

### D5 · How markets overlap (stays, with new words)
- **The recommendation:** markets nest; across kinds, the most specific market wins and lists combine; the order between kinds is stated as Shopify states it.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) One country per market only.
- **The evidence:** F10.
- **Left out:** none.
- **Verdict: holds.**

### D6 · Settings that vary by market (stays, with new words)
- **The recommendation:** the store's value, overridden by a market. Each area names which of its settings a market may hold.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) Keep S-02's list of 18 settings.
- **The evidence:**
  - Markets inherit and override the store's settings (`first-decisions.md`, '5. Markets').
  - A market for part of a country can change only its shipping (F11).
- **Left out:** none.
- **Verdict: holds.**

### D7 · Currency and prices per market (stays, with new words)
- **The recommendation:** keep D7. A market's currencies and rate sources become that market's values, set at its setup.
- **The genuine alternatives:**
  - (a) As the review proposes.
  - (b) As the review proposes, plus Shopify's condition. Under Decision 1, whether buyers can pay in a market's own currency depends on that market's providers, and is set at its setup.
  - (c) Leave it to first decision 7.
- **The evidence:**
  - Shopify's pair of amounts (F13).
  - Shopify takes payment in several currencies only through Shopify Payments or Adyen (F15).
  - `PLAN.md` line 13 says a condition "is read at the source every time".
- **Left out:** (b).
- **Verdict: holds, with a change.** Take (b).

### D8 · A seller's area within a country (split)
- **The recommendation:**
  - The platform keeps "Tax rules may use an area within a country, as Shopify's do".
  - The dated area field, the payment and currency rules keyed on an area, and a move's checks on an area all wait for the market that needs them.
- **The genuine alternatives:**
  - (a) The split.
  - (b) Keep D8 whole, since "a dated area costs little now, and past records without one can't recover it" (S-02 `decisions.md`, D8).
  - (c) Leave tax by area to the tax area's design.
- **The evidence:**
  - Shopify taxes a fee by the seller's province, and its entity address carries a province (F9).
  - No Shopify market for part of a country carries a currency (F11).
  - S-02 itself says "whether they need it isn't shown" (S-02's register, S02-D8).
  - *Reading:* because the address already holds a province, waiting costs less than S-02 counted.
- **Left out:** none. (c) is what the review's platform part comes to.
- **Verdict: holds.**

### D9 · Two currency areas under one code (split)
- **The recommendation:** "Amounts refer to a currency record, one per currency code at launch". The review's words say "First decision 7's record states it as an extension of Shopify's shape". The second record waits for the market that needs it.
- **The genuine alternatives:**
  - (a) to (d) as for Note 1.
  - (e) Retire D9, until a reference shows the need. This is S-02's own condition for reopening it: "A reference found to sell two areas of one country under one currency code at two rates" (S-02's register, S02-D9). Shopify doesn't show that: its market for part of a country takes its parent's currency (F11).
- **The evidence:** as for Note 1 (F13, F14).
- **Left out, or not borne out:**
  - (c) is left out.
  - The review calls one record per code an extension of Shopify's shape. In Shopify's own library it is the shape (F14). Only a second record under one code goes beyond Shopify, and Shopify's library rules that out (F14).
- **Verdict: holds, with a change.** As for Note 1. D9 still goes to first decision 7, starting from (c).

### S-02's E1 · How a per-market setting is read (stays, with new words)
- **The recommendation:** keep it, without the customer-group clause.
- **The genuine alternatives:**
  - (a) Without the clause.
  - (b) With it.
- **The evidence:**
  - The clause is BigCommerce's (S-02 `decisions.md`, D4).
  - Line 35 says "No other platform's reading shapes the model".
- **Left out:** none.
- **Verdict: holds.**

### S-02's E2 · How a rule keyed on the seller's country is read (stays, with new words)
- **The recommendation:** keep it, without the area input, which waits with D8.
- **The genuine alternatives:**
  - (a) Without the area input.
  - (b) With it.
- **The evidence:** F1 and F2. Orders keep the entity that was active when they were placed.
- **Left out:** none.
- **Verdict: holds.**

---

## What stays as it is, one line each

- **Line 4 · Credentials:** sound. `CLAUDE.md` line 37 carries it almost word for word, so Note 2 can retire it.
- **Line 9 · Following the work:** sound.
- **Line 10 · Code:** sound. `PLAN.md` line 23 carries it, so Note 2 can retire it.
- **Line 11 · No merchant interviews:** sound. It is your own choice, so keep it whatever Note 2 retires.
- **Line 14 · No decision holds because it was accepted before:** sound. This check applies it too.
- **Line 20 · Default 2 while a market runs C:** sound (F7). It should live in one place only (see Default 2).
- **Line 28 · Which quality wins:** sound. `PLAN.md` line 16 relies on it.
- **Line 34 · Up to four agents at once:** sound. Nothing else carries it, so Note 2 would first have to write it into `PLAN.md`.
- **S-01's E2 · One payment record, a separate ledger:** sound. It matches Shopify's shape at this commit (F4).
- **S-01's E3 · Sharrwah's fees in a billing part apart:** sound (F7).
- **S-01's E4 · Who carries out a refund:** sound. It belongs to the payments area's design (F6).
- **Default 1 · An account asked for through Sharrwah:** sound. It names no market, and it is your choice.
- **Default 3 · No balance that sellers pay into:** sound. It names no market.
- **S-02's E3 · One main market:** sound (F12). First decision 5's record should say how the main market's place is set: Shopify sets it from the store's currency (F12), while D1 keeps the currency from setting the business's country.
- **S-02's E4 · The store's own currency:** sound (F13). The review's summary leaves out S-02's clause keeping a gift card in a market's currency open. Shopify rules that out (F16), so under line 35 it should be dropped or named as an extension.
- **S-02's E5 · Who holds sellers' money, by business:** sound as a design. Its reason, "Shopify's business entities carry payment processing", needs Shopify's conditions (F2, F3): see Line 19.

## What was read

- `decisions/review.md`.
- `founder-decisions.tsv`.
- S-01's `decision-1.md` and register.
- S-02's `decisions.md` and register.
- `decisions/first-decisions.md`.
- `PLAN.md` and `CLAUDE.md`.
- Five founder messages that rows cite: the go of 29 October and the handoff (lines 26 to 29), and the messages of 30 October on effort, agents at once and the evidence guides (lines 32 to 34).
- Shopify's evidence in observed-sh at `04de369`, read through its own guides first.

Nothing else was read: no other platform's evidence, and no git history.
