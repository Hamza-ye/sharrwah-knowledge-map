# Alternatives check: your kept decisions, the review's other recommendations, and the coordinator's two notes

*1 November 2026. This page checks `decisions/review.md` and the coordinator's two notes on it. It was written by an agent that wrote none of them. Shopify's evidence was read in observed-sh at commit `04de369da9ac84ae530ae80a55749167ff4139d4`, through its own guides first (`README.md`, `docs/READING.md`, `index/`).*

## For the founder

**What this page does.** It checks the review of your earlier decisions, starting with the 22 decisions of yours that it recommends keeping in some form: 8 as they are, 12 with new words, and 2 split. For each one it says:
- what the decision closes off;
- which real alternatives exist;
- whether keeping it shuts out something the platform needs.

After that, more briefly, it covers the 11 retirements, the coordinator's two notes, and the rest of the review.

Your own business choices are not second-guessed. Every alternative named here is supported by your decisions file, the pages, the first decisions or Shopify's evidence. Every verdict is a reading, for your veto.

**Your 22 kept decisions.** 14 hold as the review recommends, 8 hold with a change, and none fails. Kept as the review words them, none shuts out something the platform needs, with one exception: line 19.

**The eight changes.**
- **Line 19 (room for A and B):** read as one value per business, the new words would shut out a business that takes some payments through a service run through Sharrwah and others through its own providers. Shopify's shape allows exactly that. The fix is to say that *whether* A or B may be switched on is a setting of the business, and that each payment records who holds its money.
- **Line 16 (Decision 1):** keep your own words, with one added sentence that sends the providers, couriers and payment channels to each market's setup. State the platform's part once, in line 19, rather than three times. Leave default 2 as written.
- **Line 8 (the guard):** drop only its last sentence, which line 19 already answered. The proposed words would also narrow "anywhere" to "in any market".
- **Line 25 (your markets):** the review's first page drops only the exception, but its proposed words drop the whole sentence. Dropping only the exception keeps your protection in your own row.
- **Line 26 (your intent):** keep the sentence "where an earlier decision differs, this one holds", because line 35 relies on it.
- **Line 17 (Decisions 2 to 12):** which installment providers Sharrwah works with, and on what terms, is a question for each market's setup, with your partners, not for the payments area's design.
- **Line 30 (no veto on S-02):** retire it rather than split it. Each of its parts already lives elsewhere, and the rulings go to the first decisions' records for your veto.
- **Line 24 (capture requests):** two more phrases in it still assume several evidence repositories.

**The rest.** Of the 11 retirements, 7 hold and 4 need a change:
- line 3 needs a corrected reason;
- line 22: retired rows should stay in the file, so their pinned links keep working;
- line 29: your answer to this page, given before step 3, can be the go you reserved before architecture starts;
- line 31: the review should say where your view of the platform's extent now comes.

Both of the coordinator's notes hold with a change:
- **Note 1 (money):** Shopify's own money library holds each currency as a record found by its code, and adds new currencies under codes of their own. Starting from this costs nothing now, and it keeps D9's room where you put it.
- **Note 2 (retiring the working-method rules):** most of these rules are not yet carried by `PLAN.md` or `CLAUDE.md`, so retire a row only once they are. Keep the budget row, because spending is yours. Keep line 10, because `PLAN.md`'s version is narrower than yours.

**In all,** 63 recommendations were checked: 41 hold, 22 hold with a change, and none fails. Nothing here reopens Decision 1, the guard, or your markets.

## How to read it

- *Line N* is the row's line in `founder-decisions.tsv`. *The review* means `decisions/review.md`.
- *The handoff* is `founder-messages/2026-10-29-intent-handoff.md` and *the go of 29 October* is `founder-messages/2026-10-29-go.md`, both cited by line.
- F1 to F16 are Shopify's facts. Each is quoted once, below, with its pinned link.
- Other judgements are marked *Reading*, and assumptions are marked *Assumption*.
- **The verdicts:**
  - **Holds:** the recommendation stands. Any alternative it left out is named, and is weaker or no better.
  - **Holds, with a change:** it stands only with the change given.
  - **Doesn't hold:** it fails on the evidence. None does.

## Shopify's shape, where a recommendation rests on it

- **F1. The business entity.** "A legal entity through which a merchant operates." Each "can be associated with its own" Shopify Payments account, and markets "can be assigned to a business entity to determine payment processing and" order attribution ([admin schema 2026-10, L217](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L217)).
- **F2. Business entities serve Shopify's own payment service, on Plus.** "Business entities are available on the Plus plan only." ([Help Center, business entities in markets, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L3)) "A business entity is the legal entity that processes payments for orders in a market." ([L6](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L6)) "Business entities are relevant only for stores using Shopify Payments with multiple accounts." ([L18](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L18)) "Existing orders continue to be associated with the business entity that was active when the order was placed." ([L19](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/business-entities.md?plain=1#L19))
- **F3. Third-party methods stay with the main business, beside Shopify's own service.** "Selling with multiple entities is available only with Shopify Payments." ([Help Center, selling with multiple entities, L28](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L28)) "Certain features such as adding a third-party payment method are available only for the primary entity." ([L35](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L35)) "To use Shopify Payments alongside the third-party provider on the primary entity" ([L36](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L36)). "Additional third-party payment methods are displayed only on checkouts and for markets associated with the primary entity, with the exception of PayPal." ([L38](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/shopify-payments/onboarding/selling-with-multiple-entities.md?plain=1#L38))
- **F4. Each payment names its gateway; Shopify's payments account is a record apart.** An order transaction "represents a payment transaction that's associated with an order", with the fields "gateway" and "manualPaymentGateway", and an optional "shopifyPaymentsSet" ([admin schema, L2447](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2447)). The payments account is "Financial account information for merchants using Shopify Payments." ([admin schema, L3193](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L3193))
- **F5. A payment taken outside any provider.** "After you receive payment for a customer's order, you can mark the order as paid" ([Help Center, manual payments, L10](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/manual-payments.md?plain=1#L10)).
- **F6. Payment providers plug in as apps.** Shopify's payments apps API has the mutations "paymentSessionResolve", "refundSessionResolve" and "paymentsAppConfigure" ([payments apps schema 2026-10, L26](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/payments-apps-graphql-schema/2026-10/items.jsonl?plain=1#L26)).
- **F7. Shopify's own fees.** "If you don't activate Shopify Payments as your payment provider, then you're charged third-party transaction fees for all orders that aren't brokered financially by Shopify." ([Help Center, getting paid, L11](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/payments/getting-paid.md?plain=1#L11)) Its card fees are "deducted from your payouts rather than billed on your Shopify bill" ([Help Center, types of charges, L12](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/manage-billing/billing-charges/types-of-charges.md?plain=1#L12)).
- **F8. The country is locked while money is attached.** "you need to deactivate all financial services before you can change your business entity." ([Help Center, managing business entities, L20](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/business-entities.md?plain=1#L20)) "you need to deactivate all financial services before you can change your store's country in your Shopify admin." ([L31](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/your-account/business-entities.md?plain=1#L31))
- **F9. The seller's area within a country.** The entity's address "Represents the address of a merchant's Business Entity.", with a "province" field ([admin schema, L218](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L218)). A fee is taxed by the seller's province: "If your legal business address is in Canada, then GST, HST, QST, PST, or RST is added to the Managed Markets fee, depending on your province." ([Help Center, Managed Markets, L78](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/international/managed-markets/overview.md?plain=1#L78))
- **F10. Market kinds and their order.** The market types include "REGION", "LOCATION", "COMPANY_LOCATION" and "CHANNEL" ([admin schema, L2004](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2004)). "B2B markets are more specific than retail markets. Retail markets are more specific than country or region markets." ([Help Center, market types, L106](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L106)) "Catalogs from all applicable markets are combined" ([L108](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L108)).
- **F11. A market for part of a country.** "Sub-region markets are available as an early access feature." ([Help Center, market types, L27](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L27)) "On a sub-region market, you can customize only the shipping options." ([L32](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/market-types.md?plain=1#L32))
- **F12. The primary market.** It "represents the default customer experience for your store" ([Help Center, managing markets, L113](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/managing-markets.md?plain=1#L113)). "Your primary market is determined by your store currency" ([L118](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/getting-started/managing-markets.md?plain=1#L118)).
- **F13. Money in Shopify's API.** An amount "Combines a decimal amount with a three-letter currency code" ([admin schema, L2266](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2266)), drawn from "The currency codes that represent the world currencies throughout the Admin API." ([L985](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L985)) The pair "contains the equivalent in the shop's base currency" ([L2263](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/admin-graphql-schema/2026-10/items.jsonl?plain=1#L2263)).
- **F14. Money in Shopify's own library.** It "Provides a `Money::Currency` class which encapsulates all information about a monetary unit." ([money README, L11](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L11)) "Currencies are consistently represented as instances of `Money::Currency`." ([L92](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L92)) "To load custom currencies from a YAML file:" ([L186](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L186)), through a setting named "experimental_custom_currency_path" ([L189](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L189)). "Custom currencies are looked up after ISO and crypto currencies, so they cannot shadow built-in currencies." ([L205](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/open-source/money/main@4d9b0127e5a2/files/money-4d9b0127e5a242a3343d67285a70c328556158eb/README.md?plain=1#L205))
- **F15. Paying in a market's own currency.** "To process payments in multiple currencies, your store must use Shopify Payments or Adyen as its payment processor." and "If you use a different provider, then customers in all markets pay in your store" ([Help Center, local currencies, L3](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/customizations/local-currencies.md?plain=1#L3)).
- **F16. Gift cards.** "You can't create gift cards in a specific market's local currency." ([Help Center, discounts and gift cards, L51](https://github.com/Hamza-ye/observed-sh/blob/04de369da9ac84ae530ae80a55749167ff4139d4/structures/shopify/help-center/help.shopify.com@en-ar/md/en/manual/markets/discounts-and-gift-cards.md?plain=1#L51))

---

## Part A. Your 22 decisions the review keeps

### The 8 that stay as they are

#### Line 4 · Credentials in evidence
- **What it decides, and what it closes off:** evidence that holds credentials, cookies or tokens is read and cited like any other. It closes off skipping such a file: "never skip, withhold or mask a file because of them".
- **The genuine alternatives:**
  - (a) Keep it.
  - (b) Retire it, since `CLAUDE.md` line 37 says almost the same (Note 2).
- **The evidence:**
  - *For (a):* `CLAUDE.md` line 37 leaves out "never skip, withhold or mask", so it carries the rule only in part.
  - *For (b):* "Keep only what a decision needs now" (`CLAUDE.md` line 25).
  - Keeping it closes off nothing the platform needs, and no first decision rests on it.
- **Does keeping it leave one out?** Only (b), which would first need that clause added to `CLAUDE.md`.
- **Verdict: holds.**

#### Line 9 · Following the work
- **What it decides, and what it closes off:** you follow the work "Through a report at each milestone and planned pause". It closes off asking you to follow the work between those points.
- **The genuine alternatives:**
  - (a) Keep it.
  - (b) Retire it, since every step of `PLAN.md` ends in a decision for you (`PLAN.md` line 17).
- **The evidence:**
  - *Against (b):* `PLAN.md` names no milestones or pauses, and no reports to you, so it carries the rule only in part.
  - The go of 29 October also asks for an orientation page, and leaves its timing to engineering (that file, line 23). This fits with keeping line 9.
- **Does keeping it leave one out?** No.
- **Verdict: holds.**

#### Line 10 · Code
- **What it decides, and what it closes off:** spikes and exploratory code are allowed, and production code waits "until requirements, architecture and engineering documentation exist to validate it against". It closes off production code before then.
- **The genuine alternatives:**
  - (a) Keep it.
  - (b) Retire it, since the review says "`PLAN.md` carries it".
- **The evidence:** *against (b):* `PLAN.md` line 23 is narrower than line 10 in two ways.
  - It allows a spike only "where a decision raises a question only code can answer".
  - It makes production code wait for "the decisions and their documentation", without requirements.

  Retiring line 10 would take your wider allowance with it.
- **Does keeping it leave one out?** No. (b) is weaker.
- **Verdict: holds.** *Reading:* the review's "`PLAN.md` carries it" is true only in part.

#### Line 11 · No merchant interviews
- **What it decides, and what it closes off:** "None, ever". It closes off interviews as a source of requirements. It is your own choice and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No. The platform's shape comes from Shopify's evidence (line 35; `PLAN.md` line 8), not from interviews.
- **The genuine alternatives:** retiring it would only leave your choice unrecorded, and engineering can't make that choice for you.
- **Verdict: holds.**

#### Line 14 · No decision holds because it was accepted before
- **What it decides, and what it closes off:** a decision "is assessed on its merits before anything builds on it". It closes off keeping a decision only because it was once taken.
- **The genuine alternatives:**
  - (a) Keep it.
  - (b) Retire it, since `PLAN.md` says the same, but only for this review (`PLAN.md` lines 21 and 29).
- **The evidence:** *for (a):* line 14 applies always, and line 30's reopening rule rests on it.
- **Does keeping it leave one out?** No.
- **Verdict: holds.**

#### Line 20 · Default 2, while a market runs only C
- **What it decides, and what it closes off:** Sharrwah's fees are never taken from sellers' money at a provider while a market runs only C. Where A or B is switched on, how fees are collected there comes to you. It closes off netting Sharrwah's fees out of sellers' money under C. It is your choice on fees, which belong to "plans and prices" (line 26), and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No.
  - Shopify does the same thing where its own payment service is off: its fees go on its bill, and it deducts fees only from payouts it makes itself (F7).
  - Apps that bill merchants through the platform (`first-decisions.md`, '12. Charges to the merchant') are not Sharrwah's fee, and line 20 doesn't touch them.
- **The genuine alternatives:**
  - (a) Keep it.
  - (b) Fold it into default 2 and retire it. The review's Part 3 proposes this while also keeping line 20.
- **Within its own content:** S-01's register leaves one question open for the bill: "if the bill also collects partners' charges, such as apps or shipping labels, and pays them out, Sharrwah holds third parties' money" (S01-E3). That question belongs to first decision 12. Line 20 neither answers it nor closes it.
- **Does keeping it leave one out?** No. The review does place it twice, though: see Line 16.
- **Verdict: holds.** S-01's E3, which puts Sharrwah's fees in a billing part of their own, follows from it and also holds.

#### Line 28 · Which quality wins
- **What it decides, and what it closes off:** the order is trustworthiness; then coherence and user experience; then performance; then completeness, "read as what each release delivers, never what the model covers". Scale numbers come later. It closes off reading completeness as how much of the model is covered. It is your order and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No. The platform's extent comes from Shopify's model (line 26), not from any one release, and `PLAN.md` line 16 relies on this order.
- **The genuine alternatives:** the files support none beyond keeping it.
- **Verdict: holds.**

#### Line 34 · Up to four agents at once
- **What it decides, and what it closes off:** up to four agents may run at once, and fewer if agents start being stopped mid-run. It closes off running more than four.
- **The genuine alternatives:**
  - (a) Keep it.
  - (b) Retire it as engineering's own practice (Note 2), since line 13 makes the method engineering's.
- **The evidence:** *against retiring it before it is carried elsewhere:*
  - neither `PLAN.md` nor `CLAUDE.md` sets a limit;
  - the row's basis is your own usage under your plan (line 34, its basis), which is close to spending, and spending is yours (line 26).
- **Does keeping it leave one out?** Only (b), which would first need the limit written into `PLAN.md`.
- **Verdict: holds.**

### The 12 that stay with new words

#### Line 7 · How work comes to you
- **What it decides, and what it closes off:**
  - plain business words, with an unavoidable term defined in one line;
  - quotes and ids kept in the files;
  - several decisions in one message, each with its own answer line;
  - method rulings listed one plain line each, for your veto.

  It closes off technical pages, and decisions that come without an answer line.
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) The review's words.
  - (c) Retire it once `CLAUDE.md` carries it (Note 2).
- **The evidence:**
  - *For (b):* the old words list only "method rulings". But line 26 makes everything outside your list engineering's, for your veto, and the review's "engineering's rulings" matches that.
  - *Against (c):* `CLAUDE.md` line 23 only asks for a reading of your message.
- **Within its own content:** kept as it was, the row would shut out listing engineering's platform rulings for your veto. The new words don't.
- **Does keeping it leave one out?** Only (c), which is weaker until `CLAUDE.md` carries it.
- **Verdict: holds.**

#### Line 8 · The guard on sellers' money (first-page item 2)
- **What it decides, and what it closes off:** no arrangement that holds sellers' money through Sharrwah (A or B) "goes live anywhere" without your decision. "It limits only what goes live." Its last sentence left you to decide whether the design provides for A or B. The guard is your own choice and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No. It limits only what goes live, and line 19 keeps room for A and B.
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) Drop only the last sentence, as the first-page item 2 says.
  - (c) The review's words, which also narrow "anywhere" to "in any market" (the review, line 57) and add a sentence on keeping room.
- **The evidence:**
  - *For dropping the last sentence:* you answered it on 26 October ("Keep room, as recommended.", line 19). Line 26 also makes it engineering's: "How the platform keeps room for it is engineering's."
  - *Against (c):* S-02's E5 attaches the holding arrangement to the business, not to the market (S-02 `decisions.md`, 'Engineering constraints'). *Reading:* that makes "anywhere" the wider guard.
  - *Against (c):* the added sentence repeats lines 19 and 26.
  - *Against (c):* the handoff asks that the guard not be reopened (line 43).
- **Within its own content:** S-01's register leaves open whether partners' charges collected on Sharrwah's bill would hold third parties' money (S01-E3). *Reading:* the guard as worded covers sellers' money only, so that question is first decision 12's.
- **Does keeping it leave one out?** Yes: (b).
- **Verdict: holds, with a change.** Take (b): drop only the last sentence, keep "anywhere", and add nothing. Item 2 holds.

#### Line 12 · The reset of 25 October
- **What it decides, and what it closes off:** as it was written, it:
  - returned to the plan at G1;
  - reopened Decision 1;
  - made the decisions of 10 October bind nothing;
  - made history bind nothing.

  The review keeps only the rule on history and the line on the decisions of 10 October. It closes off using history except through its sources.
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) The review's words.
  - (c) Retire it.
- **The evidence:**
  - *Against (a):* line 35 replaced the plan it returned to, and line 16 answered Decision 1.
  - *For (c):* `CLAUDE.md` line 19 states the same rule more strictly: "Use it only through a link pinned to a commit in a working file".
  - *For (c):* O-01's open question, which company contracts with sellers, is on your list (line 26, "the company").
  - *For (c):* the decisions of 10 October sit outside the working files, so they bind nothing anyway.
  - *For (b):* the review's reason, "no other decision of yours states it", is true. Only `CLAUDE.md` does.
- **Does keeping it leave one out?** Yes: (c), an equal choice, which Note 2 favours.
- **Verdict: holds.** Retiring it loses nothing, unless you want the rule in your own file.

#### Line 13 · Who decides what
- **What it decides, and what it closes off:** engineering owns the method, you decide business questions only, and you aren't asked to audit lists. It closes off bringing you method questions or lists to audit.
- **The genuine alternatives:**
  - (a) Keep it as it was, with its pointer to a `PLAN.md` section that no longer exists.
  - (b) The review's words.
  - (c) Retire it, since line 26 and `PLAN.md` line 31 carry your list and your veto.
- **The evidence:**
  - *Against (c):* nothing else carries "is not asked to audit lists of practices or decisions".
  - *Reading:* the review's own first page asks you to approve twelve new wordings. Note 2 would shorten that list, which is what this row asks for.
- **Does keeping it leave one out?** Only (c), which is weaker until its last clause is carried elsewhere.
- **Verdict: holds.**

#### Line 17 · Decisions 2 to 12, settled by Decision 1
- **What it decides, and what it closes off:** under C, each provider or courier collects, settles, pays out and deducts its own fees. Sharrwah sends no payouts, has no agency role in receiving payments, takes no security interest in sellers' money, and bills its own fees apart. It closes off each of these while a market runs C. It follows from your Decision 1 and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No.
  - S-01's register reopens each answer wherever A or B is switched on (S01-D2 to S01-D12).
  - S-01's E4 keeps refunds working under C: a refund is carried out by whoever holds the money, and its result is recorded on the order. E4 holds.
- **The genuine alternatives:**
  - (a) Keep it as it was, with its pointers to subjects that no longer exist.
  - (b) The review's words.
  - (c) Retire it, since it was "Settled by the answer to Decision 1" and the register keeps each answer.
  - (d) The review's words with installments split: the platform's part goes to the payments area's design, and which providers, on what terms, goes to each market's setup.
- **The evidence:**
  - *For (d):* under C, "the question narrows to which providers, on what terms" (S-01's register, S01-D13). Partners and financing are both on your list (line 26).
  - *Against (c):* *reading:* the row records your acceptance of "no agency role" and "no security interest". Both touch the company's legal structure, which is also on your list.
- **Does keeping it leave one out?** Yes: (d).
- **Verdict: holds, with a change.** Take (d). Proposed words: *Installments (Decision 13): the platform's part with the payments area's design; which providers, and on what terms, at each market's setup.*

#### Line 19 · Keeping room for A and B
- **What it decides, and what it closes off:** it keeps room for A and B.
  - "Who holds sellers' money is a market's setting", and it is C everywhere at launch (S-01's E1).
  - An order's payment record is the same whoever holds the money, and a holder's ledger is a separate part, empty under C (S-01's E2).

  It closed off building for C alone.
- **The genuine alternatives:**
  - (a) Keep it as it was, with "market" read as you asked ("my words of 26 October were a working description", the handoff, line 39). S-02's E5 already reads it that way, and you didn't veto E5 (line 30).
  - (b) The review's words: "a setting of the business that takes the payment", justified "as Shopify's shape does".
  - (c) Narrower, and closer to Shopify: whether a holding service run through Sharrwah (A or B) may be switched on is a setting of the business that takes the payment. Each payment records who holds it.
- **The evidence:**
  - *For tying it to the business:* Shopify assigns markets to business entities "to determine payment processing" (F1), and keeps each order with the entity that was active when it was placed (F2).
  - *Against the review's reason:* Shopify's entities matter only on its Plus plan, and only for Shopify's own payment service. Third-party methods stay with the main business (F2, F3). So under C, which runs everywhere at launch, Shopify ties nothing to the business.
  - *For (c):* Shopify runs its own payment service beside a third-party provider within one entity (F3, L36). S-01's register already noted this: "as Shopify runs its own service beside third-party providers" (S01-E2).
  - *For (c):* each Shopify payment names its gateway (F4), and your Decision 1 says "Each payment method's provider holds the money" (line 16).
- **Within its own content:** read as one value per business, the review's "Who holds sellers' money is a setting …", with C as its value, would shut out a business that holds some money through a service run through Sharrwah and the rest through its own providers. Shopify's shape has exactly that (F3), and S-01's E2, with its single payment record, allows it.
- **Does keeping it leave one out?** Yes: (c). The review's reason also says more than Shopify shows.
- **Verdict: holds, with a change.** Replace the review's first sentence with (c)'s, and keep the rest of the review's words. S-01's E1 takes the same new words. S-01's E2 holds as it is: it matches Shopify's shape (F4).

#### Line 23 · A budget never costs evidence (first-page item 6)
- **What it decides, and what it closes off:** a budget must never cost evidence. You move to a higher plan first, and the coordinator says when one is needed. It closes off cutting evidence to stay within a budget. It is your choice on spending (line 26) and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No.
- **The genuine alternatives:**
  - (a) Keep it as it was, still naming S-02's budget and "every subject".
  - (b) The review's words: "evidence about Shopify's shape … for every step".
  - (c) Retire it (Note 2).
- **Within its own content:** the first decisions rest on two sources, Shopify's shape and published practice (`first-decisions.md`, its opening; `PLAN.md` line 20). The review's words cover only the first. *Reading:* published practice is cited, not captured, so the narrower words risk little.
- **The evidence:** *against (c):* spending is on your list (line 26), and nothing else carries this rule.
- **Does keeping it leave one out?** No.
- **Verdict: holds.** Item 6 holds.

#### Line 24 · Evidence not held is a request
- **What it decides, and what it closes off:** evidence that a run could capture, but that isn't held, goes out as a request.
  - The coordinator records the gap and leaves a handoff.
  - "the founder hands it on".
  - The local agent captures what it can, pushes, and notifies.

  It closes off treating a missing capture as a decision for you.
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) The review's two changes.
  - (c) Retire it once `PLAN.md` carries the procedure (Note 2).
- **The evidence:**
  - *For (b), and for going further:* under line 35, only observed-sh shapes the model. Yet the decision's text still says "the repositories' journey catalogs" and "into that repository".
  - *Against (c):* the row names a step of yours, and nothing else carries it.
- **Does keeping it leave one out?** No. But the review's changes miss those two phrases.
- **Verdict: holds, with a change.** Also change them, in these proposed words: *observed-sh's journey catalogs* and *into observed-sh*.

#### Line 25 · Sharrwah's markets (first-page item 3)
- **What it decides, and what it closes off:**
  - your markets: MENA, Yemen among them, not all at launch;
  - how Sharrwah competes;
  - that Yemen's present circumstances and today's capacity don't become permanent product or architecture constraints "without a genuine, justified reason".

  The markets are your choice and aren't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** Not as reworded. Kept as it was, the exception would let a market's limits shape the platform once someone finds a reason, and line 35 rules that out ("never define the platform").
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) Drop only the exception, as the first-page item 3 says.
  - (c) Drop the whole sentence, as the review's proposed words do ("The dropped sentence is replaced by line 35").
  - (d) Keep it as it was, and let lines 26 and 35 govern where they differ.
- **The evidence:** *for (b) over (c):*
  - line 35 covers a market's limits and the platform, but names neither "product" constraints nor today's capacity;
  - line 26 covers capacity ("Launch and today's resources decide when, never whether").

  So (b) keeps your protection in your own row.
- **Does keeping it leave one out?** The review offers (b) on its first page and (c) in its proposed words, so you would be approving two different things.
- **Verdict: holds, with a change.** Take (b). Proposed words: *Yemen's present circumstances and today's business capacity don't become permanent product or architectural constraints.* Item 3 holds.

#### Line 26 · Sharrwah's intent (first-page item 4)
- **What it decides, and what it closes off:**
  - the frame: the platform comes from the class, and a market's setup fills its slots;
  - your list of decisions;
  - engineering's share, under your veto;
  - the test for narrowing the platform;
  - the rule on product gaps.

  Your list isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No. Where it differs from line 35, line 35 holds (line 26, its review column).
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) The review's words.
  - (c) Only the smallest edits: change "the class" to Shopify's model, and drop "which shape is better where they differ".
- **The evidence:** *against (b) as written:* it drops "where an earlier decision differs, this one holds" (line 26).
  - Line 35's basis relies on that sentence: "as that row says of the decisions before it".
  - The review itself relies on it under Line 8.
- **Does keeping it leave one out?** What it leaves out is a sentence, not an alternative.
- **Verdict: holds, with a change.** Keep "Where an earlier decision differs, this one holds." in the new words. Item 4 holds.

#### Line 32 · The agents' effort floor
- **What it decides, and what it closes off:** no agent reads evidence, reviews or makes an engineering judgement at `medium` or `low`. A type of task that keeps missing things runs at a higher level. It closes off low effort for that work.
- **The genuine alternatives:**
  - (a) Keep it as it was, with its last sentence pointing to a table that is gone.
  - (b) The review's words.
  - (c) Retire it once `PLAN.md` carries it (Note 2).
- **The evidence:** *for (b), and against (c):* you set it because "Previous work has shown that lower effort can miss substantial evidence and leave important gaps." (line 32, its basis). Nothing else carries the floor.
- **Does keeping it leave one out?** Only (c), which is weaker until `PLAN.md` carries it.
- **Verdict: holds.**

#### Line 33 · Read the evidence through its guides
- **What it decides, and what it closes off:** before a capture request goes out, what the evidence repository holds is read through its guides and indexes, not by search alone. It closes off reading by search alone.
- **The genuine alternatives:**
  - (a) Keep it as it was. It names other-product-class and `method/held_index.py`, which line 35 and `CLAUDE.md` leave out.
  - (b) The review's words.
  - (c) Retire it once `CLAUDE.md` line 17 names all seven guides (Note 2).
- **The evidence:** all seven guides it names exist in observed-sh at this commit. `CLAUDE.md` line 17 names three of them.
- **Does keeping it leave one out?** Only (c), which is weaker until `CLAUDE.md` names them all.
- **Verdict: holds.**

### The 2 that split

#### Line 16 · Decision 1: who holds sellers' money
- **What it decides, and what it closes off:** C, with the three defaults, in every market at launch, and A and B off under the guard. It closes off at launch:
  - Sharrwah, or a payment company through Sharrwah, holding sellers' money;
  - Sharrwah's fees being netted out of sellers' money;
  - a balance that sellers pay into.

  It is your own choice and isn't second-guessed.
- **Does keeping it, as worded, close off something the platform needs?** No.
  - Line 19 keeps room for A and B.
  - The decision reopens wherever you switch on A or B in a market (S-01's register, S01-D1).
  - A payment taken outside any provider has its place (F5).
  - Providers plug in as apps (F6).
- **The genuine alternatives:**
  - (a) Keep it word for word. Line 19 then carries the platform's place, and the couriers, transfers and cash in line 16 read as your description of C, to be filled at each market's setup. The handoff asks not to "take my wording as the design" (line 43).
  - (b) The review's split into a platform part, your part and a market part.
  - (c) A different split: your part stays in line 16, with one added sentence sending the providers, couriers and payment channels to each market's setup. The platform part is stated once, in line 19.
- **The evidence:** *against (b):*
  - its platform part says what its words for line 19 and for S-01's E1 also say, so the same thing is written three times;
  - the wording jars between them: one calls it "a place in the platform", another says "it is not a property of the platform";
  - the review's Part 3 gives default 2 new words with line 20 folded in, while its own split of line 16 keeps "default 2 as line 20 narrows it".
- **Does keeping it leave one out?** Yes: (a) and (c).
- **Verdict: holds, with a change.** Take (c), and leave default 2 as written, beside line 20. Defaults 1 and 3 hold as they are, since neither names a market (S-01's register, S01-D1.1 and S01-D1.3).

#### Line 30 · No veto on S-02's rulings
- **What it decides, and what it closes off:**
  - no veto on S-02's rulings D1 to D9 and E1 to E5;
  - how many markets a plan allows, and of which kinds, comes to you with plans;
  - a conflict between a ruling and the model is reopened with its evidence.

  Kept as it was, it accepts D8's dated area on every business record and D9's condition on every money record. Both come from Yemen alone (S-02 `decisions.md`, 'Needs no reference meets').
- **The genuine alternatives:**
  - (a) Keep it as it was.
  - (b) The review's split.
  - (c) Retire it, because each of its parts already lives elsewhere:
    - the plan limits under "plans and prices" (line 26);
    - the reopening rule in line 14;
    - D8's and D9's waits in their own verdicts;
    - D1 to D7 in first decisions 5 and 7, each record for your veto (`PLAN.md` line 14).
  - (d) Leave the rulings to those records, re-read from Shopify's shape (`PLAN.md` line 22).
- **Within its own content:** the plan item is yours and stays yours either way. Shopify's own plans limit markets: on its lower plans, a store can have at most three active catalogs across its B2B markets (`first-decisions.md`, '11. Plans and the shop's state').
- **The evidence:** *for (c):*
  - S-02's rulings are "engineering's rulings, for your veto" (S-02 `decisions.md`, line 9);
  - only approved decisions go in your file (`CLAUDE.md` line 24);
  - line 26 says "Everything else is engineering's".
  - *Reading:* the split's platform part only routes rulings to the first decisions; it decides nothing.
- **Does keeping it leave one out?** Yes: (c), together with (d).
- **Verdict: holds, with a change.** Take (c).

**The rulings themselves, checked against Shopify's shape:**
- **D1, D2, D3** (the store's country, a seller who moves, what follows the country): hold (F1, F2, F8).
- **D4, D5, D6** (what a market is, how markets overlap, per-market settings): hold (F10, F11; `first-decisions.md`, '5. Markets').
- **D7** (currency and prices per market): holds, with a change. Add that buyers can pay in a market's own currency only where that market's providers can take it, set at the market's setup. Shopify takes payment in several currencies only through its own processor or Adyen (F15).
- **D8** (a seller's area within a country): holds. Taxing by area is part of Shopify's shape, and Shopify's entity address already holds a province (F9). *Reading:* waiting for the dated field therefore costs less than S-02 counted.
- **D9** (two currency areas under one code): holds, with a change, as under Note 1 below. The review calls one currency record per code an extension of Shopify's shape. In Shopify's own library it is Shopify's shape (F14). Only a second record under the same code goes beyond it.
- **E1, E2** (how per-market settings and country rules are read): hold (F1, F2).
- **E3** (one main market): holds (F12). First decision 5's record should say how the main market's place is set, since Shopify sets it from the store's currency (F12).
- **E4** (the store's own currency): holds, with a change. S-02's E4 also keeps a gift card in a market's currency open, which Shopify rules out (F16). Under line 35, either drop that clause or name it as an extension.
- **E5** (who holds sellers' money, by business): holds, with a change. Its reason, "Shopify's business entities carry payment processing", needs Shopify's conditions (F2, F3), as under Line 19.

---

## Part B. The 11 retirements

- **Line 2 · Go on the plan of 12 October.**
  - *Alternatives:* keep it, or retire it.
  - *Evidence:* line 12 and line 35 replaced it (`PLAN.md` line 3).
  - *Left out:* none.
  - **Holds.**
- **Line 3 · No standing business model.**
  - *Alternatives:* keep it, as a record that no business model is set; or retire it.
  - *Evidence:* the review's reason, "Replaced by line 35: the model is Shopify's", mixes two models. Line 35's model is the platform's shape (`PLAN.md` line 4). The business model is yours, under "plans and prices" (line 26).
  - **Holds, with a change:** give line 26 as the reason. The business model stays yours, and it is still open.
- **Line 5 · Q3's two sets of rows.**
  - *Alternatives:* keep its caution that an agent's list is not a requirement, or retire it.
  - *Evidence:* the rule that every claim is a fact, a reading or an assumption carries that caution (`PLAN.md` line 8).
  - **Holds.**
- **Line 6 · Agents' effort, delegated.**
  - *Alternatives:* keep it, or retire it.
  - *Evidence:* line 32 assumes the delegation ("where the coordinator sets it"), and line 13 makes the method engineering's.
  - **Holds.**
- **Line 15 · One Yemen row per decision.**
  - *Alternatives:* keep it, or retire it.
  - *Evidence:* under line 35, a market's providers, law and limits are its setup, and "never define the platform".
  - **Holds.**
- **Line 18 · The subjects S-02 to S-11.**
  - *Alternatives:* keep the scope it set, or retire it.
  - *Evidence:* line 26 carries that scope ("Sharrwah rules out nothing the class shows").
  - **Holds.**
- **Line 21 · No test of Decision 1 against Shopify alone.**
  - *Alternatives:* keep declining the test, retire it, or run the test.
  - *Evidence:* a test without Yemen's facts already reached C (`decision-1.md`, 'A test, not a source'). First decision 5 now reads the holding place from Shopify's shape (F2, F3).
  - **Holds.**
- **Line 22 · B1 to B8 left in history.**
  - *Alternatives:* delete the row; keep it, marked retired; or move its pinned link into the record that will need it.
  - *Evidence:* the review relies on "the pinned link in line 22", and history may be used only through such a link (`CLAUDE.md` line 19).
  - **Holds, with a change:** say that retired rows stay in the file, marked retired. The same applies to lines 12, 29 and 31.
- **Line 27 · The class's model before architecture.**
  - *Alternatives:* keep it, reword it for Shopify, or retire it.
  - *Evidence:* first decision 2 divides the platform into areas by Shopify's own components (`first-decisions.md`, '2. Areas and their borders').
  - **Holds.**
- **Line 29 · Architecture's own plan (first-page item 5).**
  - *Alternatives:*
    - your go on the first decisions' records, as the review proposes;
    - your go on `PLAN.md` and the list of fifteen first decisions, given with your answer to this page, before step 3;
    - a separate architecture plan.
  - *Evidence:*
    - line 29 says "architecture starts on my go on that plan";
    - the records are the first piece of architecture work (`PLAN.md` line 22), and each comes to you for veto anyway (`PLAN.md` line 14);
    - `PLAN.md` and `first-decisions.md` ('Their order') already state what line 29 asked an architecture plan to state.
    - *Reading:* the review's go would come after the very work it was meant to come before.
  - **Holds, with a change:** take the second. Item 5 holds with the same change.
- **Line 31 · What comes at GM.**
  - *Alternatives:* retire it; or keep its purpose, reworded for Shopify: your view of the platform's extent, "as my view of the extent: its areas and capabilities", with a check for what the platform misses.
  - *Evidence:* each step's page reports decisions, not the extent. First decision 2 will set out the areas.
  - **Holds, with a change:** say that this view isn't carried, or that it comes with first decision 2's record.

## Part C. The coordinator's two notes

### Note 1 · Money: start from Shopify's way
- **The recommendation:** start first decision 7 from an amount with a standard currency code. Keep the review's currency record only if it costs almost nothing now, or else let it wait for the market that needs it.
- **The genuine alternatives:**
  - (a) The review's: "Amounts refer to a currency record, one per currency code at launch", stated as an extension of Shopify's shape (the review, 'D9').
  - (b) The note's, as stated above.
  - (c) *Named by neither:* the form of Shopify's own money library (F14).
    - An amount carries its currency.
    - The currency is a record found by its code, and held as data.
    - A currency outside ISO's list is added under a code of its own.

    A second currency area under one ISO code then gets a new code and record of its own. Where a provider takes only ISO codes, the new code maps back to the ISO one.
  - (d) Wait entirely, under line 35's "case by case".
- **The evidence:**
  - Shopify's API names a currency by a three-letter code from Shopify's own list (F13).
  - Shopify's library holds each currency as a record found by that code, and loads new currencies from data, behind a setting it names experimental (F14).
  - *Against (a)'s second record under one code:* Shopify's library won't let a new currency reuse an ISO code (F14), and its API carries the code alone (F13). *Reading:* two records under one code couldn't be told apart through that API, so the API would change later either way.
  - *For (a):* S-02 counts a bare code in every amount as "a redesign" later (S-02 `decisions.md`, D9). *Reading:* that is only true if the code must stay ISO's. Under (c), the area travels in the code itself, and only the payments area's border maps it. That is one module.
  - *On where the room sits:* the go of 29 October (line 12) places the room S-02 recommends "in the core: how every amount names its currency". Line 29 calls D9 "the worked example". *Reading:* (c) keeps the room in the core. (d) moves it to a market's setup.
- **Left out, or not borne out:** (c) is left out. The note's own words, "an amount with a standard currency code", describe Shopify's API (F13), not its library (F14), so the note's choice between a code and a record is narrower than Shopify's actual shape.
- **Verdict: holds, with a change.**
  - Start first decision 7 from (c).
  - Its record then weighs (a)'s second record under one code against a new code, with the cost of each.
  - If it drops the room, it says so, for your veto.

  *Assumption:* a code of Sharrwah's own can fit Shopify's three-letter form. None is chosen here.

### Note 2 · Retire the rules that only govern how the work runs
- **The recommendation:** retire the kept rows that only govern how the work runs (effort levels, agents at once, capture requests, the evidence guides, budgets), since `PLAN.md` and `CLAUDE.md` carry them.
- **The genuine alternatives:**
  - (a) The review's: keep these rows.
  - (b) The note, as written.
  - (c) Retire each row only once `PLAN.md` or `CLAUDE.md` carries its substance, and say where.
  - (d) Keep spending, and your own choices, whatever happens to the rest.
- **The evidence:**
  - I searched both files. Neither mentions effort levels, agents at once, capture requests or budgets. The nearest is `PLAN.md` line 28: each decision reports its cost.
  - They carry some rows only in part:
    - credentials: `CLAUDE.md` line 37, without "never skip, withhold or mask";
    - code: `PLAN.md` line 23, which is narrower than line 10;
    - the evidence guides: `CLAUDE.md` line 17, which names three of the seven.
  - They carry in full only line 12's rule on history (`CLAUDE.md` line 19).
  - Budgets are spending, which is on your list (line 26), and the review itself files line 23 there. So the note's own test keeps line 23.
  - Line 32 is your floor on a choice you had delegated (line 6), and line 24 names a step of yours.
  - *For retiring:* "Keep only what a decision needs now" (`CLAUDE.md` line 25), and lines 13 and 26 make the method engineering's.
- **Left out, or not borne out:** the note's reason doesn't hold for four of its five examples.
- **Verdict: holds, with a change.**
  - Retire line 12 now.
  - Retire lines 4, 7, 9, 13, 14, 24, 32, 33 and 34 only once their substance is written into `PLAN.md` or `CLAUDE.md`.
  - Keep lines 11 and 23, and line 10 unless `PLAN.md` line 23 takes in its wider allowance.

## Part D. The review's first page, and what lies beneath the rows

- **Item 1 · Approve the new words as written.**
  - *Alternatives:*
    - as written;
    - with this page's changes;
    - fewer of them, once Note 2 retires the working-method rows;
    - none: leave the earlier rows as they are, with line 35 holding where they differ.
  - *Evidence:* line 13 says you are "not asked to audit lists of practices or decisions". The last option would leave dead pointers in your file, such as `PLAN.md` sections that no longer exist (lines 13 and 32).
  - **Holds, with a change:** approve with this page's changes, and fewer of them as Note 2 retires rows.
- **Items 2 to 6** are checked under lines 8, 25, 26, 29 and 23 above. Items 2, 3, 4 and 6 hold. Item 5 holds with a change.
- **Item 7 · A veto on the retirements, and on D9 going to first decision 7.**
  - *Alternatives:* your approval, rather than a veto, for the two retirements that touched your list: line 3, the business model, and line 18, business scope.
  - *Evidence:* line 26 already carries both of those ("plans and prices"; "Sharrwah rules out nothing the class shows"). *Reading:* so retiring them changes nothing on your list.
  - **Holds.**
- **What lies beneath the rows** is checked inside them:
  - S-01's E1 and E2, under line 19;
  - S-01's E3, under line 20;
  - S-01's E4, under line 17;
  - defaults 1, 2 and 3, under line 16;
  - S-02's D1 to D9 and E1 to E5, under line 30.

## What was read

- `decisions/review.md`;
- `founder-decisions.tsv`;
- S-01's `decision-1.md` and register, and S-02's `decisions.md` and register;
- `decisions/first-decisions.md`;
- `PLAN.md` and `CLAUDE.md`;
- the five founder messages that rows cite: the go of 29 October and the handoff (lines 26 to 29), and the three messages of 30 October on effort, agents at once and the evidence guides (lines 32 to 34);
- Shopify's evidence in observed-sh at `04de369`, through its own guides first.

Nothing else was read: no other platform's evidence, and no git history.
