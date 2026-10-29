# S-02: the independent review (step 5)

The reviewer made none of S-02's register, Yemen row or scenario walk. This review read only what `briefs/G-review.md` names, and left out every `notes*.md` file and every `note` column. Each finding cites the file and id, and the evidence read for it. `must fix` means checked against the evidence; anything not verified is marked as a reading. Nothing here decides anything for the founder.

Baseline checks, run from the repository root on the working tree (HEAD 9665383f):
- `python3 -I method/register_items.py studies/subjects/S-02`: "142 founder items; 0 unanswered, 0 answered twice, 0 names unknown".
- `python3 -I method/check_register.py studies/subjects/S-02/register.tsv`: "770 citations checked, 0 problem(s)".

## Findings

### 1. Gap 3 is declared "met", but no reference meets it (`decisions.md`, "Gap 3"; `register.tsv` S02-D7, `alternatives` (e), `recommendation`, `evidence`)

**Problem.** `decisions.md` says gap 3 (one currency code over two currency areas) is met because "Shopify and Salla hold an exchange rate per market, and a market can be drawn for an area within a country, so two areas sharing one currency code can sell at two rates". D7 repeats "held per market rather than per currency, as Shopify and Salla hold it", and its `evidence` calls yemen-row line 35 "a need this decision and S02-D4 meet: a rate held per market, in a market drawn per area, S02-SH-103, S02-SA-051". Two of the three legs fail on the statements:
- **Salla's rate is the currency's, not the market's.** S02-SA-103 (stated, scope "each market"): "أم سيعتمد تحديد سعر المنتجات تلقائياً بناء على سعرها الأساسي وسعر الصرف للعملة" (prices set automatically from the base price and *the currency's* exchange rate). The only cited support, S02-SA-302 (shipped), is an order field: "scope_exchange_rate ... Scope-specific exchange rate information, if available"; it doesn't say what a scope is, and D7's own alternative (e) words it "Salla per store scope", not per market. S02-SA-079 says only that prices follow "سعر الصرف الحالي" (the current rate).
- **Shopify's market for an area can't hold its own currency.** S02-SH-104 (stated, marker "Early access"): "On a sub-region market, you can customize only the shipping options. Everything else, such as currency, catalogs, theme, and domain, is inherited from the parent market." S02-SH-103 and S02-SH-072 carry the same "Early access" marker. Shopify's rate per market (S02-SH-568) is real, but for markets that can hold a currency, which an area within a country can't.

So no reference sells two areas of one country, with one currency code, at two rates. The combination of a rate per market and a market for an area is the register's own design, not something a reference shows. By `PLAN.md` section 6, step 5, a need the Yemen row shows that no reference meets is "a product gap, written without Yemen's name ... and a design decision for the founder". Folding it into D7 as "met" keeps it from the founder as a question of its own. It also gives D7's "per market rather than per currency" a second driver that comes from one market. The generality argument for a rate per market still stands on Shopify alone (S02-SH-568), so D7's recommendation may hold, but the page should say which of its parts the references support.

**Evidence.** S02-SA-103, S02-SA-302, S02-SA-079, S02-SH-104, S02-SH-103, S02-SH-072, S02-SH-568, read through `method/point_view.py --records` and the RD2/RD3 slices.

**must fix**

### 2. D4 closes customer-group prices with a reason that doesn't reach them (`register.tsv` S02-D4, `closes`, `recommendation`, `answers_items` S02-VP-49|a group of customers; `decisions.md` D4, "What it rules out")

**Problem.** D4 answers the founder item "Does pricing take its value per group of customers in Sharrwah, outside its markets?" (c/RD3 answers, S02-VP-49|a group of customers: BigCommerce gives it, S02-V-822, S02-BC-020: "Populate different versions of catalog pricing and assign them to different customer groups"). The recommendation says "(d)'s dimensions become markets of those kinds", and `closes` rules out "(d) as mechanisms apart from markets ... where a market kind reaches them (S02-SH-117, S02-SH-604)". But the kinds D4 recommends are places, channel, point of sale, business customer and storefront, and none of them is a group of customers:
- phase C's S02-VP-26|a group of customers is a commonality that no platform gives (c/RD2 answers: `lacks` shopify, `not_stated` the other four, cause `no difference`). The register carries it as such in S02-F5, which by the C brief means "not carried: none of the references does it";
- Shopify's own list excludes it: S02-SH-N03 (shipped absence), "A market condition type for a group of customers other than a company location, such as a customer segment: the enumerated type MarketConditionType holds REGION, LOCATION, COMPANY_LOCATION and CHANNEL";
- S02-SH-117, which `closes` cites, lists Regions, Company locations, POS locations and Channels, and no customer group.

So one of two things is wrong. If customer groups are not a market kind, D4 closes BigCommerce's variant on a reason ("where a market kind reaches them") that is false for it. If they become one (the recommendation's "(d)'s dimensions become markets"), D4 goes against the commonality S02-F5 records. "Business customer" is Shopify's company location (S02-VP-26|a company), which is a different thing from a group of customers. `decisions.md` puts the closure plainly: "separate systems for ... customer groups beside markets". The option the register missed is a customer group as its own dimension that a setting can key on beside markets, which is how BigCommerce holds it, with none of the references making it a market.

**Evidence.** c/RD2/answers.tsv S02-VP-26 (keys `a group of customers`, `a company`); c/RD3/answers.tsv S02-VP-49|a group of customers; S02-SH-N03, S02-SH-117, S02-BC-020.

**must fix**

### 3. D8's recommendation is said to rest on no one market, and the page says every recommendation comes from the references alone, but D8's own text shows otherwise (`decisions.md`, opening and D8 "Why"; `register.tsv` S02-D8, `recommendation`)

**Problem.** `decisions.md` opens "Every recommendation comes from the five references alone, with no market's facts", and D8 says "it ... rests on no one market: the platforms themselves tie rules to areas of one country". D8's own `alternatives` say "No reference keys payment services, the currency or the exchange rate on such an area, or runs a move's checks when it changes", and its `evidence` is yemen-row lines 13 and 14. What the references show is option (b): tax and one feature keyed on a province or state (S02-SH-513, S02-SH-515, S02-SH-931, S02-WC-118, S02-SH-485, S02-SH-486). The parts of (c) beyond (b), which are payment services, currency and the rate keyed on an area, and a change of area running a move's checks, come only from the Yemen row's need. Calling (a) and (b) "restricted forms of (c)" applies generality to a variant no reference shows. Section 6's generality rule is about the references' variants, and a design beyond them falls under "Options beyond the references", which D8 doesn't use.

Handling D8 as a product gap and a decision for the founder is what `PLAN.md` section 6, step 5 asks. The fault is the wording. `PLAN.md` section 1's guard asks that "each decision page says whether its recommendation comes out the same without Yemen". For D8 it would not: without the first market's need, the question wouldn't arise, and the references support (b) at most. The page should say that, and drop "rests on no one market" and the opening sentence's "every recommendation".

**Evidence.** `register.tsv` S02-D8 `alternatives`, `recommendation` and `evidence`; `decisions.md` lines "Nothing here is decided ..." and D8's "Why"; `PLAN.md` section 1 (the guard) and section 6, steps 4 and 5.

**must fix**

### 4. E4 and D7 close gift cards in a market's currency with none of the three reasons, and the founder's page doesn't say so (`register.tsv` S02-E4, S02-D7 `recommendation` and `closes`; `decisions.md` D7 and E4; `scenario-walk.tsv` line 43)

**Problem.** E4 says "a store keeps one currency of its own beside any market's, the one its gift cards and its own reports use", and D7 repeats "the store's currency stays the one for gift cards". That rules out gift cards in a market's currency. The walk flags it at line 43: `closes` "gift cards in a market's currency", `reason` "none of the three: E4's only evidence for it is Shopify's own limit (S02-SH-189), one vendor's choice", `flag` `premature`. The register doesn't take the flag up:
- E4 has no `closes` and no reason;
- D7's `closes` names only "Money records that keep one currency only";
- `decisions.md` presents E4 and D7's gift-card clause without saying they close anything.

The F brief says a premature closure reaches the founder "either it is changed, or it is kept with its reason on the record". Neither has happened. The evidence is S02-SH-189 alone ("You can't create gift cards in a specific market's local currency"). S02-VP-41|the whole store (a commonality) supports a store currency, but not a ban on gift cards in a market's currency.

**Evidence.** `register.tsv` S02-E4 (no `closes`), S02-D7 `closes`; `scenario-walk.tsv` line 43; S02-SH-189; c/RD3/answers.tsv S02-VP-41|the whole store.

**must fix**

### 5. The walk repeats D4's closure of customer groups without the `premature` flag (`scenario-walk.tsv` line 23, RD2 S02-D4, second market)

**Problem.** Line 23 closes "(d): channels, points of sale and customer groups as mechanisms apart from markets", with the reason "two mechanisms would answer which values a buyer sees (S02-SH-117, S02-SH-604)". For customer groups no market kind exists to be the second mechanism: S02-SH-117 lists Regions, Company locations, POS locations and Channels; S02-SH-N03 (shipped absence) shows Shopify's MarketConditionType holds no customer group; and phase C's S02-VP-26|a group of customers is given by no platform (finding 2). For that part of (d), the stated reason doesn't hold, so by the F brief the line should carry `premature`, or the closure should be narrowed to channels and points of sale, for which the reason holds (S02-SH-604).

**Evidence.** `scenario-walk.tsv` line 23; S02-SH-117, S02-SH-604, S02-SH-N03; c/RD2/answers.tsv S02-VP-26|a group of customers; c/RD3/answers.tsv S02-VP-49|a group of customers (BigCommerce, S02-BC-020).

**must fix**

### 6. The same claim about Salla's per-market rate recurs in the Yemen row and the walk (`yemen-row.tsv` lines 35 and 40; `scenario-walk.tsv` lines 36, 37 and 39)

**Problem.** These lines carry finding 1's claim further:
- **Yemen row line 35** (`product_gap`): "Half met by option (e): a rate held per market, which register.tsv shows Shopify and Salla holding, prices each of two currency areas sharing one code at its own rate."
- **Yemen row line 40** labels option (e) "(Shopify; Salla per store scope)".
- **Walk line 36** cites "(Shopify: S02-SH-568; Salla: S02-SA-302)" for "a rate per market".
- **Walk line 37** says "two markets are drawn per area (a sub-region market, S02-SH-103; ...), each with its own rate (S02-SH-568)". Shopify's sub-region market inherits its currency from the parent market (S02-SH-104, "Early access"), so no reference shows it.
- **Walk line 39** says "a rate per market still rests on the references (Shopify: S02-SH-568; Salla: S02-SA-302)".

S02-SA-103 gives Salla's rate as the currency's ("سعر الصرف للعملة"). Line 37's cost under the recommendation (`a setting`) can stand, since it tests Sharrwah's own design, but its evidence must not suggest a reference does it. Line 39's conclusion (D7 unchanged without the first market) stands on Shopify alone (S02-SH-568). The `half met` in the Yemen row's line 35 needs the same correction as `decisions.md`'s "met". By the Yemen row's own facts the need stands (line 41: one rate per currency code is `no` in the first market, YA-01: YE-D721 "1,562.00 1,567.00" at Aden on 2026-10-10; YE-E1304 "OLD NOTES - SANA'A USD / YER 533" on 2026-10-08), so it is a product gap for the founder.

**Evidence.** As finding 1; `yemen-row.tsv` lines 35, 40 and 41; `scenario-walk.tsv` lines 36, 37 and 39; Stage 1 citations YE-D721, YE-E1304, YE-E1308.

**must fix**

### 7. D5 closes overlap within one kind of market as unorderable, but D4 and D7 rely on such overlaps, and Shopify orders them by nesting (`register.tsv` S02-D5 `recommendation` and `closes`; `decisions.md` D5; `scenario-walk.tsv` lines 26 and 27)

**Problem.** D5 recommends that a country fall "in one market only within a kind, so a buyer matches at most one market of each kind". It closes "Overlap within one kind" because "a buyer would match two markets with nothing to order them". That conflicts with:
- **D4's own recommendation:** "a market may sit within another and inherit from it". A market for one country inside a market for a region are both of the places kind, so a buyer in that country matches two markets of one kind.
- **D7's recommendation:** prices are set "for the market or for a country within it", "(d) as a market within a market (S02-D4)". The same overlap.
- **`decisions.md` D5's own "Why":** "a seller can sell to a region as one market and still treat one country apart". Doing that by a market within the region market is again an overlap within one kind.
- **Shopify's statements.** S02-SH-125: "A country or region can be included in more than one market." S02-SH-131: "If a new market is determined to be within an existing market, then it's considered a submarket." S02-SH-080: "Submarkets inherit the customizations of their parent market". Nesting is the order that the closing reason says doesn't exist.

The case the evidence leaves open is two markets of one kind that partly overlap, with neither inside the other. No statement read shows what a reference does there, so "nothing to order them" is a reading for that case only. As worded, the closure rules out what D4 and D7 recommend. The walk's lines 26 and 27 repeat it ("nothing orders two markets of one kind") without testing a market within a market.

**Evidence.** `register.tsv` S02-D4, S02-D5 and S02-D7 `recommendation`; S02-SH-125, S02-SH-131, S02-SH-080, S02-SH-109; c/RD2/answers.tsv S02-VP-27|a country in more than one market (Shopify, S02-V-422) and S02-VP-26|a market within a market (Shopify, S02-V-406).

**must fix**

### 8. D2's named rule, and the walk's "confirmed fact", say more than S02-SH-596 does (`register.tsv` S02-D2 `recommendation` and `closes`; `decisions.md` D2 "Why"; `scenario-walk.tsv` line 6)

**Problem.** D2's rule is "the references that tie money or a contract to the country lock it (S02-SH-596, S02-WC-182)", and the walk's line 6 gives as its reason "a confirmed fact (Shopify and WooPayments lock it)". The two statements are narrower than that:
- S02-SH-596 locks the country of "individual or sole proprietor entities" only ("You can't change the business type, country, or the person associated with individual or sole proprietor entities").
- S02-WC-182 locks a WooPayments account's country, not a store's.
- Shopify lets a store's country change in place once its financial services are off (S02-SH-250, "you need to deactivate all financial services before you can change your store's country"), which is D2's own option (b).

So what the references show is a lock while money is attached, plus a fixed country for an individual's entity and for a payment account. The rule named is also not one of `PLAN.md` section 6's rules. The closure of (a) for the legal country still stands on its other reason (an engineering cost), so this is a matter of precision.

**Evidence.** S02-SH-596, S02-SH-250, S02-WC-182; c/RD1/answers.tsv S02-VP-06, S02-VP-07.

**optional**

### 9. The RD1 summary reads as if one contracting company for all were settled by rule (`decisions.md`, RD1 "What follows by rule"; `register.tsv` S02-F2)

**Problem.** The page says "Set per seller's country by rule: the store's taxes, the privacy law, one contracting company for all." Phase C's key is S02-VP-08|every store (Salla and Zid give it; cause `market, pattern`), which follows as "a variation point bound per market". What is bound per seller's country by rule is *whether* one company contracts with every store there. That Sharrwah has one company for all is not settled: which company contracts with sellers is a company question for the founder (`PLAN.md` section 6, step 0) and S-03's (S02-M1). Suggested wording: "bound per seller's country: whether one contracting company serves every store there (S-03 fills it)".

**Evidence.** c/RD1/answers.tsv S02-VP-08|every store; `register.tsv` S02-F2 and S02-M1.

**optional**

### 10. D6 says four platforms hold many of these settings per market, but Zid holds 3 of 18 (`decisions.md` D6, "What the platforms do"; `register.tsv` S02-D6 `alternatives` (a))

**Problem.** Across D6's 18 points, c/RD3/answers.tsv has `a market the store sells into` given by BigCommerce on 16, Salla on 15, Shopify on 12, Zid on 3 (S02-VP-47, S02-VP-51, S02-VP-53) and WooCommerce on 1 (S02-VP-89). The register's "by setting" is accurate. The page's "Four platforms hold many of these per market" isn't accurate for Zid.

**Evidence.** c/RD3/answers.tsv, the `gives` column for the two keys on S02-VP-43 to S02-VP-89, tallied.

**optional**

### 11. "A set may combine across markets, as Shopify combines catalogs" stretches S02-SH-109 to payment methods and shipping (`register.tsv` S02-E1, S02-D6, S02-D5 `recommendation`; `decisions.md` D5, D6, E1)

**Problem.** S02-SH-109 says "the more specific market type takes priority for how your market customizations take effect" and "Catalogs from all applicable markets are combined". Only catalogs combine there. E1 names "the payment methods, the shipping options" among sets that may combine. On Shopify, shipping on a market for part of a country is a customization of the more specific market (S02-SH-104: "On a sub-region market, you can customize only the shipping options"). Combining payment methods and shipping options is engineering's own choice. It may be sound, but it should be marked as a reading, not as Shopify's practice. The walk's line 40 shows its risk: a limit such as cash on delivery shown "only in Saudi Arabia" (S02-SA-283) must still hold after combining.

**Evidence.** S02-SH-109, S02-SH-104, S02-SA-283; `scenario-walk.tsv` line 40.

**optional (a reading)**

### 12. D8's "a redesign without it" is a reading that the register's other recommendations weaken (`register.tsv` S02-D8 `cost_later`; `decisions.md` D8)

**Problem.** With E2 (every rule read through one entry point) and D1 (the business record holds the address, and S02-VP-01|the store's address is a commonality), a rule re-keyed from country to area later changes inside the resolver. Turning an area change into a checked move changes D2's move procedure, which D2 costs at `one module`. What a later retrofit can't recover is a dated area on past records, and whether past records need it isn't shown. So "a redesign" may hold only where E2 or D1 is declined. This is a reading. It is worth saying because the founder weighs D8 on this cost.

**Evidence.** `register.tsv` S02-D8 `cost_later`; S02-D2 `cost_later`; S02-E2 `recommendation`; c/RD1/answers.tsv S02-VP-01|the store's address.

**optional (a reading)**

### 13. The walk's line 15 says D8's extension has no reference and no need without the first market, yet it carries no flag (`scenario-walk.tsv` line 15, RD1 S02-D8, first market dropped)

**Problem.** The line's own text: "keying payment services, the currency or the rate on an area, and running checks when an area changes, has no reference (D8's alternatives say so) and no need left". The F brief flags "a constraint that traces only to one market today". D8 provides a capability rather than imposing a constraint, so the flag may be arguable. But the line should either carry `one market` or say why not, so that the founder sees, next to D8, which of its parts trace only to the first market (finding 3).

**Evidence.** `scenario-walk.tsv` line 15; `register.tsv` S02-D8 `alternatives`.

**optional**

### 14. D1 answers the Salla seat item without answering its question, and the page calls WooCommerce's location a map location (`register.tsv` S02-D1 `answers_items` S02-VP-01|مقر المتجر; `decisions.md` D1)

**Problem.**
- **The seat.** The founder item is "Does Sharrwah hold a store's seat (مقر المتجر), where it is based, as a setting of its own beside its country?" D1 only closes the seat as a source of the country ("Filling the country from ... a seat setting"). It doesn't say whether a seat is held beside the country. S02-SA-177 lists مقر المتجر beside موقع المتجر (the store's location) among basic settings.
- **The map location.** `decisions.md` says "Four platforms hold a map location". WooCommerce's key is the onboarding question "Where is your store located?" (S02-V-274: S02-WC-294, S02-WC-322), not a map. The register's own words, "a location set on a map or by hand", are accurate.

**Evidence.** c/RD1/answers.tsv S02-VP-01|مقر المتجر (founder item) and |the store's location; S02-SA-177; variants.tsv S02-V-014, S02-V-274.

**optional**

### 15. D5's "confirmed fact" for opening several countries per market includes a reading (`register.tsv` S02-D5 `closes`; `decisions.md` D5 "Why"; `scenario-walk.tsv` line 26)

**Problem.** The fact holds: c/RD3/answers.tsv S02-VP-57|the buyer's country is `no difference` across all five. The step from it to "a market need not be one country for tax" is a reading:
- Salla gives its one-country rule on tax grounds: "Taxes are calculated based on the country assigned to each market. Each market supports one country only." (S02-SA-077).
- D6 holds tax settings per market (S02-VP-57|a market the store sells into is in its `answers_items`).

So a market of several countries needs its tax values keyed on the buyer's country inside the market, and D6 doesn't name that key. Since one country per market stays a configuration, little is closed, but the reason should be marked as fact plus reading.

**Evidence.** c/RD3/answers.tsv S02-VP-57; S02-SA-077; `register.tsv` S02-D6 `answers_items`.

**optional**

### 16. D7 joins parts of different cost under one answer, and the page drops the condition on its cost (`register.tsv` S02-D7; `decisions.md` D7)

**Problem.**
- **Different costs.** D7 asks one question that holds a currency per market (S02-VP-41), prices per market and per buyer's country (S02-VP-49), the platform converting prices (S02-VP-50) and two amounts on every money record. Their costs differ in kind. A rate per market rather than per currency is a rate table, `one module`. Two amounts on every money record is what makes `a redesign`. The D brief lets a setting stand apart when its later change costs more in kind. Here the cheap part (the rate's level, whose second driver is gap 3, finding 1) rides with the expensive one. A founder could want the second amount and no per-market rate, or the reverse.
- **The dropped condition.** `decisions.md` writes "Changing course later: a redesign." with no condition. The register's `cost_later` says it is the cost "if orders, refunds and reports keep one currency and markets later sell in their own". Read alone, the page suggests that departing from the recommendation later costs a redesign.

**Evidence.** `register.tsv` S02-D7 `question`, `answers_items`, `cost_later`; c/RD3/answers.tsv S02-VP-41, S02-VP-49, S02-VP-50.

**optional**

### 17. D7 puts Shopify among the platforms that convert a market's prices, where phase C's row has it as not stated (`register.tsv` S02-D7 `alternatives` (c); `decisions.md` D7)

**Problem.** c/RD3/answers.tsv S02-VP-50|the platform has `gives` salla;zid;woocommerce and `not_stated` shopify;bigcommerce, and its scopes note "shopify general (S02-SH-179, under S02-VP-42)". D7 adds "and Shopify states it", and the page says "all four convert prices when the seller chooses". S02-SH-179 ("Select Dynamic to automatically convert prices") supports the reading, but the register departs from phase C's row without marking the change as its own reading.

**Evidence.** c/RD3/answers.tsv S02-VP-50|the platform; S02-SH-179.

**optional**

### 18. The page says 142 items are asked as seven questions; 57 of them moved (`decisions.md`, "What this page is")

**Problem.** Counting `answers_items`: D1 to D7 answer 85 items, and S02-M1 to S02-M8 move 57 (S-03 9, S-04 17, S-05 5, S-07 19, S-08 1, S-09 1, S-10 2, S-11 3), for 142. The opening "Phase C's 142 items for you ... are asked here as seven questions" should say that 85 are asked here and 57 go to other subjects.

**Evidence.** `register.tsv` `answers_items`, counted per row; `method/register_items.py` (142, each once).

**optional**

### 19. Two unmarked assumptions in the Yemen row and the walk (`yemen-row.tsv` line 4; `scenario-walk.tsv` line 45)

**Problem.**
- **Yemen row line 4** (S02-D1 (c)) needs "A way to pay the platform's fees from abroad". "From abroad" assumes Sharrwah's company bills from outside the seller's country. Where the company is based is S-03's and open (the walk's own "company elsewhere" rows), so this should be marked as an assumption. The fact itself, that a card or wallet that pays foreign sites exists (YA-144: YE-D162, 2026-10-10; YE-D103, 2025-06-15, "limited to one or two wallets only, and not spread in all governorates"), holds against its quotes.
- **Walk line 45** (S02-E4, first market dropped) rates `a setting` while noting "E4 keeps one store currency but doesn't say whether it may change". If a moving seller's store currency changes, E4's gift cards and D7's second amount on past records are in the old currency. That cost is unknown from what E4 says, not a setting.

**Evidence.** `yemen-row.tsv` line 4; Stage 1 citations YE-D162, YE-D103; `scenario-walk.tsv` line 45; `register.tsv` S02-E4, S02-D7.

**optional (a reading)**

## What was checked and held

These were checked and found sound, so the coordinator need not recheck them:
- **D1 to D3's option lists** match phase C's keys and platforms (c/RD1/answers.tsv S02-VP-01, S02-VP-06, S02-VP-07, S02-VP-09 to S02-VP-18; c/RD3 S02-VP-41, S02-VP-55, S02-VP-57).
- **D1's and D3's "confirmed fact"** holds: S02-SH-247 says "The store address must be in the same country as your business entity address", and S02-SH-253 says "The country of your billing address must match the country of one of your active business entities".
- **D4's places and channels** match S02-VP-26's keys, and its general variant (S02-V-400, S02-V-453) is phase C's.
- **D6's inherit-and-override examples** show that pattern (S02-SA-042, S02-SH-095, S02-BC-320, S02-V-865).
- **E3's default market and E4's store currency** are commonalities of all five (c/RD2 S02-VP-26|a default market; c/RD3 S02-VP-41|the whole store).
- **E5's merchant's country** is a commonality for S02-VP-11 and S02-VP-12.
- **E5 is put to the founder as a reading to confirm,** not as decided.
- **No market's name** appears in any founder decision's or constraint's `question`, `recommendation`, `trade_off`, `closes`, `cost_later` or `reopens_when`.
- **The Yemen row's sampled facts** hold against their quotes and dates. It respects `corrections.md` for YA-44 (YE-D435 and YE-D436 at place not stated), YK-124 (one direction only) and YA-102 (per area). Its product gaps are written without the market's name.
- **The walk's sampled citations** hold (S02-SA-113, S02-SA-490, S02-ZD-114, S02-SA-283, S02-SA-280, S02-SA-211, S02-SH-287, S02-ZD-129, S02-SH-541, S02-SH-147, S02-SH-280, S02-ZD-055).

## Counts, under the brief's seven headings

| Heading | Checked | Findings |
| --- | --- | --- |
| 1. The grouping | `register_items.py` (142 items, none unanswered or twice); the 8 founder decisions' groupings; the 8 moved rows' item counts; the page's opening count | 2, 16, 18 |
| 2. The options and the evidence | 31 options of D1 to D7 against phase C's rows (D1 7, D2 4, D3 6, D4 4, D5 2, D6 3, D7 5), and the page's "What the platforms do" lines for D1 to D7 (21 sentences) | 1, 2, 10, 14, 17 |
| 3. The recommendations | 13 (D1 to D8, E1 to E5): each marked as engineering's (E5 as a reading for the founder); each rule named; market names (none); anything presented as decided | 3, 8, 9, 11 |
| 4. What each closes, and its cost | the `closes` of D1 to D8 and the missing one of E4 (9); the `cost_later` of D1 to D8 (8) | 2, 4, 7, 8, 12, 15, 16 |
| 5. The Yemen row | all 44 lines read; facts on 9 lines (3, 4, 13, 14, 35, 37, 40, 41 and, through its records, 19) checked against 18 Stage 1 quotes and `corrections.md`; 3 product gaps checked for the market's name | 6, 19 |
| 6. The scenario walk | all 44 rows read; each cost and flag weighed; 12 of its citations read | 4, 5, 6, 7, 8, 13, 19 |
| 7. Citations | `check_register.py` (770 citations, 0 problems); by hand, 39 statements and 8 variants the register cites, 12 the walk cites, and 18 Stage 1 citations the Yemen row cites. Every id resolves and every quote read matches. The problems are claims that say more than their statement: S02-SA-302 (finding 1), S02-SH-103 (finding 1), S02-SH-596 (finding 8) and S02-SH-109 (finding 11) | 1, 6, 8, 11 |

**Totals:** 19 findings: 7 `must fix` (1 to 7) and 12 `optional` (8 to 19), of which 3 are marked as readings (11, 12 and 19).

## Re-check after the fixes

Read on the working tree at 4a08c8dd: `register.tsv` and `decisions.md` at 47847720, `yemen-row.tsv` at d9828b5b, `scenario-walk.tsv` at 4a08c8dd. Notes files and `note` columns were left out. `register_items.py`: 142 items, 0 unanswered, 0 answered twice. `check_register.py`: 790 citations, 0 problems.

1. **resolved.** D7 now says "as Shopify holds it for markets that hold a currency (S02-SH-568)". Its option (e) puts Salla per currency ("S02-SA-103; S02-SA-302 is an order field"), and its evidence calls yemen-row line 35 "a need no reference meets: S02-D9". The page drops "met" and asks D9: "No platform sells two areas of one country under one code at two rates" (S02-SH-104). No rate-per-market claim for Salla is left in the four files.
2. **resolved.** D4 now closes "(d) for channels and points of sale" only, with "Not closed: a group of customers, which no market kind reaches (S02-SH-N03), kept as a dimension beside markets". E1 holds a customer group as a key beside the market.
3. **partly resolved.** The page says "The recommendations for D1 to D7 come from the five references alone ... D8 and D9 go beyond the references, and say where". D8 says "Only (b), tax keyed on an area, rests on the references ... without that need the references support (b) at most", and the generality claim is gone. The part left is the rule D8 now names, which it says it didn't follow (finding 21).
4. **resolved.** E4 now makes the store's currency "the default for its gift cards. A gift card in a market's currency is left open: Shopify's limit (S02-SH-189) is one vendor's choice, not a reason". D7 and the page say the same, and the walk's E4 second-market row closes nothing.
5. **resolved.** The walk's D4 second-market row closes "(d) for channels and points of sale" only.
6. **resolved.** Yemen row: D7 (a)'s gap points to "S02-D9, two currency areas under one currency code, which no reference meets", and D7 (e) reads "(Shopify, for markets that hold a currency)". Walk: the D7 rows cite Shopify alone ("Without the first market, a rate per market rests on Shopify alone"), and D9's rows replace the gap-3 row.
7. **resolved.** D5: "within one kind they nest, a market within another inheriting from it and ranking above it, as Shopify's submarkets do (S02-SH-080, S02-SH-131, S02-SH-125)". It closes only two markets of one kind "that partly overlap, neither inside the other", marked as a reading. The walk adds a GCC row that tests nesting.
8. **resolved.** D2's rule now rests on "a lock while money is attached (S02-SH-250 ...), and a fixed country for an individual's entity (S02-SH-596) and for a payment account (S02-WC-182)". Its `closes` and the walk's D2 row say "The confirmed facts are narrower".
9. **resolved.** The page now says "whether one contracting company serves every store there (S-03 decides)".
10. **resolved.** D6 (a) and the page give the counts (BigCommerce 16, Salla 15, Shopify 12, Zid 3, WooCommerce 1).
11. **resolved.** E1 now reads "the payment methods and shipping options by engineering's own choice, a reading, since on Shopify a sub-region market customizes its own shipping (S02-SH-104)", with a platform's or a law's limit applied after combining (S02-SA-283). D6 and the page match.
12. **resolved.** D8's `cost_later` now reads "one module, given S02-E2's entry point and the business's address kept with its dates ... whether past records need it isn't shown, a reading. A redesign only where S02-E2 or S02-D1 is declined."
13. **resolved.** The walk's D8 first-market row (now line 16) says the extension "comes only from the first market's need" and that keeping the room "is the founder's to weigh". Its flag stays empty, which holds, since D8 keeps room rather than imposing a constraint.
14. **resolved.** D1 now says "A seat, where the store is based (Salla's مقر المتجر, S02-SA-177), is held as the business record's address, not as a setting of its own beside the country". The page says "a location set on a map or by hand".
15. **resolved.** D5's `closes` now separates the fact (tax follows the buyer's country on all five, a commonality) from the reading (a market of several countries keys its tax values on the buyer's country within it). RD3's follows by rule carries that key ("tax ... follow the buyer's country").
16. **partly resolved.** D7's `cost_later` and the page now cost it by part: the two amounts a redesign, the rate's level one module, which markets carry a currency a setting. It is still one question with one answer line, over parts whose costs differ in kind.
17. **resolved.** D7 (c) now says "Shopify isn't stated under that key, though its dynamic conversion (S02-SH-179, under S02-VP-42) reads the same, a reading", and the page marks it "(engineering's reading)".
18. **resolved.** The page now says "85 are asked here as seven questions (D1 to D7), and 57 go to the subjects that decide them".
19. **partly resolved.** The Yemen row's D1 (c) marks "from abroad" as "An assumption, marked as one". The walk's E4 first-market row (now line 50) adds "past records keep the store's amount in the old one (S02-D7)", but still rates `a setting` while saying E4 "doesn't say whether it may change".

### New findings

20. **D9's question credits it with something D7 already gives** (`register.tsv` S02-D9 `question` and `alternatives` (b); `decisions.md` D9). D9 asks whether a market's currency should name a currency area "so that two markets of one country sharing a code sell at two rates". Its option (b) says a rate per market "doesn't reach an area within a country". That is Shopify's limit (S02-SH-104), not D7's as recommended:
    - D7: "each market may carry its own currency and exchange rate".
    - E1: a one-value setting such as a currency takes "the most specific value set: the buyer's market (and a market within it)".
    - D4: places include "a region, a city", and D5 nests them.

    So under D7, E1, D4 and D5, two markets for areas of one country that share a code already sell at two rates, and each order keeps its market and rate (D7, E2). What D9 (c) adds is the area in the currency's identity, so that prices, amounts and reports can tell the two areas apart by currency and not only by market. D9's own `trade_off` says so ("a second currency area under one code is a new record, not a change across prices, orders and reports"). The question also asks for "that area's own exchange rate", while the recommendation keeps "its rate per market". As worded, the founder would weigh D9 on a benefit D7 already gives. **must fix**
21. **D8 and D9 name a rule they say they didn't follow** (`register.tsv` S02-D8 and S02-D9 `recommendation`). Both give as their rule "a design beyond the references (PLAN.md section 6, 'Options beyond the references'), with no outside source read". That section says: "Where a recommendation needs more than the references show, established designs and engineering writing are read for that decision. Each is weighed by its kind of source." There are two ways to fix this. Either such sources are read for D8's areas within a country and D9's currency areas. Or the two recommendations drop that rule and rest, marked as such, on engineering's cost reading under "hide what is likely to change". **must fix**
22. **The page says "the others work from the currency's rate", which takes in BigCommerce without evidence** (`decisions.md` D7, "What the platforms do"). The register's own list of per-currency rates names Salla, Zid and WooCommerce (S02-D7 (e): S02-SA-103, S02-ZD-020, S02-WC-027). BigCommerce's RD3 slice has no statement containing "exchange rate". Name the three, or cite BigCommerce. **optional**

**Re-check counts:** of the 19 findings, 16 resolved, 3 partly resolved (3, 16 and 19) and 0 not resolved. Three new findings: 20 and 21 `must fix`, 22 `optional`.
