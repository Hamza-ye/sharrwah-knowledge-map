# Review of the areas list (step R1)

**18 October 2026.** This is an independent review of `areas.tsv`, `depth.tsv` and `areas.md` in this folder, at commit 7cc6c78, made from the brief `studies/proposals/briefs/R1-areas-review.md`. I made none of the list.

Ids lead to the evidence:
- concern ids (`SH-C-001`) and statement citation ids (`SH-S-0001`) point to the concern map in `studies/concern-map/platforms/<platform>/`;
- `S01-` ids point to the pilot's `statements.tsv`.

Arabic statements are given here in English paraphrase, and the id leads to the platform's own words. A statement marked **not reached** is carried by no concern in an area tied to the question named. I checked each such case by script.

By the time I finished, the branch had moved on to d54e414, and then to checkpoints that hold only this file. Between 7cc6c78 and d54e414, the areas files, the scripts and my brief are unchanged. `questions-for-agents.md` has only gained numbers for each question's sentences, and I cite those numbers in brackets, as in Q4 [3].

## Severity at a glance

- **Must fix (15):** findings 2, 3, 4, 5, 7, 11 to 19, and 22.
- **Optional (10):** findings 1, 6, 8, 9, 10, 20, 21, 23, 24 and 25.

**Verdict:** the list can't go to the founder yet. The reasons are at the end.

## What I ran and read

- **Scripts.** I ran `python3 -I method/check_areas.py` for each platform and for `merged`. I ran `method/render_areas.py` from a scratch copy of the script and its inputs, and compared the result with `areas.md`.
- **The files.** I read the questions as agents get them, `areas.tsv`, `depth.tsv`, `areas.md`, and each platform's areas file and notes.
- **The extracts.** I searched them only to settle three doubts: Salla's help-centre categories, Shopify's Help Center menus, and whether "International sales tools" and "Markets" are separate menus.
- **The recorded data.** I searched the concern map's concerns, statements and gaps for all five platforms by script, and read citations only for the ids named below. I sampled the pilot's statements. I read one held file from observed-sh's git objects, from outside the repository: Shopify's store features for store 2jiwxs-gr, at commit e49840729.
- **Sampling for each question and platform.** I read five statements at random from the areas tied to the question. From the areas not tied to it, I read the statements that match the question's key words, enough to see the pattern: from a few to about 60 per pair.
- **Sampling for each `depth.tsv` row.** I read three or four statements of each concern the row cites, ranked by the question's key words.

## Check 1. The checks by script

### 1. The scripts find nothing, and they don't check three things the findings below turn on

- **Where:** `method/check_areas.py` and `method/render_areas.py`.
- **What they report:** all six checks report 0 problems and 0 warnings:

  | Check | Areas | Concerns placed |
  |---|---|---|
  | shopify | 29 | 198 |
  | salla | 28 | 152 |
  | woocommerce | 28 | 118 |
  | zid | 29 | 96 |
  | bigcommerce | 30 | 88 |
  | merged | 29, over 144 platform areas | — |

  The scratch render of `areas.md` is identical to the repository's, byte for byte (md5 `ef46654527d562d5ff2013ff3b79d90e` for both).
- **What they don't check:**
  - whether each concern a `depth.tsv` row cites sits in an area tied to that row's question. Ten don't (finding 11);
  - whether an area's "kept anyway" text agrees with its `left_out` text. A-04's don't agree (finding 21);
  - what the renderer leaves out. It prints only the first three names of each platform area (`ns[:3]`), so `areas.md` never shows names that plain lines and notes rely on:
    - "BigCommerce Payments", the sixth name of BC-A-10 (see finding 2);
    - Zid's "الأسواق", the eighth name of ZD-A-10, which A-15's note cites;
    - Shopify's "Acceptable Use Policy", the fourth name of SH-A-28, on which A-17's note relies.
- **Fix:** add the first two checks to `check_areas.py merged`. Render every name, or at least the names that notes and plain lines rely on.
- **Severity:** optional.

## Check 2. Groupings

### 2. The platforms' own payment services are split between A-11 and A-12, and A-12 names only some of them

- **Where:** A-11 and A-12; the platform areas SA-A-17 and BC-A-10.
- **Problem:**
  - A-12's heading is "The platform's own payment service, the seller's balance and payouts". Its plain line lists "Shopify Payments, Salla's wallet, Zid Pay and Zid Wallet, WooPayments".
  - Salla's own service, Salla Payments (SA-C-110, 43 statements), sits in SA-A-17, so in A-11. BigCommerce's, BigCommerce Payments (BC-C-025), sits in BC-A-10, so in A-11 too.
  - `areas.md` shows "BigCommerce Payments" in no area (finding 1). A founder marking A-12 would read that BigCommerce has no payment service of its own, and that Salla's is a wallet.
  - A-12's "kept anyway" calls its statements "the main record of who holds sellers' money", but BigCommerce's balance isn't in it.
  - A-11 isn't tied to Q6 or Q7, so the place rules of these two services don't reach Q6.
- **Evidence:**
  - BC-S-0141: "Balance and payout reporting are handled natively inside your BigCommerce admin through the Money Dashboard."
  - BC-S-0147: "Add your bank account and set payment preferences."
  - From the pilot:
    - S01-BC-072: the BigCommerce Payments account balance;
    - S01-BC-073 to S01-BC-075: payouts from that balance, automatic and manual, and refunds issued from it;
    - S01-BC-086: BigCommerce Payments supports United Kingdom and United States-based stores.
  - BC-S-0143: "Initially, BigCommerce Payments is available only to US-based merchants with self-serve and retail plans." Not reached for Q6 or Q7.
  - Salla Payments is one service spread over four merged areas:
    - its methods, in SA-C-110, are in A-11;
    - its balance and payouts (SA-C-111) and settlement currency (SA-C-164) are in A-12;
    - the bank account its payouts go to (SA-C-112) is in A-18;
    - its payment services contract (SA-C-177) is in A-19.
- **Fix:**
  - Put SA-C-110 and BC-C-025 in platform areas merged into A-12, re-cutting SA-A-17 and BC-A-10. Name Salla Payments and BigCommerce Payments in A-12's plain line.
  - If they stay in A-11, say so in A-12's plain line and note, and tie A-11 to Q6 and Q7.
- **Severity:** must fix. The founder would mark A-12 on a wrong basis.

### 3. Financing is split: A-13 shows two platforms, while Salla's and WooCommerce's financing sit in A-12

- **Where:** A-12 and A-13; the platform areas SA-A-18 and WC-A-03.
- **Problem:**
  - A-13's plain line reads: "Money products the platform offers sellers beyond payments: ... loans and cash advances". Its note says: "Shopify files these under Finance and Zid under تمويل زد".
  - Salla's financing (SA-C-128, "Financing for merchants (Salla Capital; financial support)") is in SA-A-18. WooCommerce's (WC-C-016, Stripe Capital) is in WC-A-03. Both go to A-12, whose plain line doesn't mention financing.
  - So the founder sees two platforms offering financing where four do.
- **Evidence:**
  - Salla:
    - SA-S-0111, paraphrased: 25% of the net sales of each payment batch is collected and the rest goes to the merchant's bank account; the investment is run through صندوق سلة with Tanami;
    - SA-S-0112: a Sharia-compliant structure managed by Tanami;
    - SA-S-3487: the `financial-support` flag, on the Pro and Special plans.
  - WooCommerce:
    - WC-S-0559: "WooCommerce has partnered with Stripe to offer eligible businesses access to fast, flexible financing through the Stripe Capital program";
    - WC-S-0560: "Loans issued by Celtic Bank".
  - WC-A-03's note gives the list's length as its reason for joining financing with payouts: "to keep the list near thirty areas". SA-A-18's note says financing was added to Salla's own heading.
- **Fix:**
  - Put SA-C-128 and WC-C-016 in platform areas merged into A-13, re-cutting SA-A-18 and WC-A-03, and rewrite A-13's note.
  - At the least, name Salla's and WooCommerce's financing in A-13's plain line and note, and say where they sit.
- **Severity:** must fix. The founder would mark A-13 on a wrong basis.

### 4. A-15 joins per-country store versions with languages and currencies, which the platforms keep apart, and its "won't do" names only the first

- **Where:** A-15; the platform areas SH-A-17, SA-A-02, SA-A-21, ZD-A-10 and BC-A-19.
- **Problem:**
  - The heading is "Selling to several countries: per-country store versions, languages and currencies". What a "won't do" mark removes is given as only "Selling to several countries would be outside Sharrwah's extent".
  - A store in one country may still want two languages, or a second currency. By the heading and plain line, a "won't do" here drops those too. The text the founder reads as the mark's effect doesn't say so.
  - The platforms keep these apart:
    - Shopify has a Languages settings page beside Markets (SH-A-17's names);
    - Salla shows Markets, Currencies and Languages as separate settings pages. Its languages concern (SA-C-008) sits in SA-A-02, so in A-02, not in A-15;
    - BigCommerce names Currencies and Store Translations apart (BC-A-19's note);
    - Zid's الأسواق and لغة وعملات المتجر are separate settings (ZD-A-10's note).
  - ZD-A-10 also brings the countries Zid serves, and Zid Egypt's company, into A-15. A-15's note says so for the countries.
- **Evidence:**
  - A-15's row in `areas.tsv`;
  - the names and notes of SH-A-17, SA-A-21, BC-A-19 and ZD-A-10. SA-A-21's note says: "The help centre's Multi-market and the settings page Currencies are separate";
  - SA-C-008 in SA-A-02: SA-S-2973, the `languages` flag, on the Plus, Pro and Special plans.
- **Fix:**
  - Split A-15 into per-country store versions, languages and translation, and currencies, re-cutting SH-A-17, SA-A-21, ZD-A-10 and BC-A-19 as needed. Salla's SA-C-008 joins languages, and the countries Zid serves join A-16.
  - At the least, make the "won't do" text say that a store in more than one language or currency goes too.
- **Severity:** must fix.

### 5. A-05 "Marketing and promotions" also holds ways buyers pay and BigCommerce's price lists, but its "won't do" names only marketing tools

- **Where:** A-05; the platform areas SA-A-09, ZD-A-16 and BC-A-03, and Shopify's SH-A-05 and SH-A-08.
- **Problem:**
  - A-05's "kept anyway" says "customer wallets, store credit and gift cards are ways buyers pay". Its "won't do" says only "Marketing tools would be outside Sharrwah's extent".
  - A founder could well mark marketing "won't do" for a first build. Without knowing it, they would also drop:
    - customer wallets and store credit, which also carry refunds;
    - BigCommerce's price lists, which set prices per customer group and channel (BC-C-007).
  - The same kind of thing sits in three areas:
    - Salla's and Zid's customer wallets, and BigCommerce's gift certificates, are in A-05;
    - Shopify's store credit is in A-06 (SH-C-026);
    - Shopify's gift cards are in A-04 (SH-C-025).
  - So for Shopify, A-05's "kept anyway" claims store credit and gift cards it doesn't hold.
- **Evidence:**
  - SA-A-09's plain line: "the customer wallet with cashback and gift cards";
  - ZD-A-16's names: "Customer Wallets";
  - BC-A-03's names: "Price Lists", "Pricing", "Coupons, discounts, and gift cards";
  - BC-S-0050: a price list assigned to a sales channel or a customer group;
  - SH-C-025 sits in SH-A-05, and SH-C-026 in SH-A-08.
- **Fix:**
  - Put customer wallets, store credit and gift cards together, either next to how buyers pay (A-11) or in an area of their own. Put BigCommerce's price lists with pricing: in A-23, or in a pricing area together with Shopify's catalogs.
  - At the least, make A-05's "won't do" text say that customer wallets, store credit, gift cards and BigCommerce's price lists go too.
- **Severity:** must fix.

### 6. Other splits, a mislabelled grouping, and notes that misdescribe

- **Where:**
  - SH-A-17;
  - WC-A-10 and A-20;
  - SH-A-09 and A-23;
  - the notes of A-08, A-17 and A-28;
  - A-01, A-03 and A-24;
  - A-23.
- **Problem and evidence:**
  - **SH-A-17 is mislabelled.** It is marked "platform's own", but it joins two top-level Help Center menus with the Languages settings page. The menus are Markets (`/en/manual/markets`) and International sales tools (`/en/manual/international`), per extract-shopify.md, "The Help Center's menus". It is an agent's grouping.
  - **WooCommerce's account sits under privacy.** WC-A-10 joins the WordPress.com account and Jetpack connection, which Woo's services require at sign-up (WC-S-5335), with usage tracking and telemetry. The merge puts the account under "Privacy and security" (A-20), and A-01 shows no WooCommerce account.
  - **Shopify's catalogs sit under B2B only.** They (SH-C-037) serve Markets as well as B2B, but sit in A-23, B2B. SH-S-5101 lists the entitlements `markets.retail.catalogs`, `markets.regions.catalogs` and `markets.b2b.catalogs`.
  - **A-17's note is wrong for Zid and Shopify.** It says Shopify, Salla and Zid "keep them in their terms or verification areas". In fact:
    - Zid's prohibited activities are in Zid Pay's area (ZD-C-037 in ZD-A-01, so in A-12);
    - Shopify's sanctions are in A-16 (SH-C-174).
  - **A-28's note leaves out where AI sits on other platforms.** It says only Shopify and BigCommerce give AI an area. That's true, but other AI features sit elsewhere:
    - Salla's AI Connector and AI writing tools are in A-02 (SA-A-02);
    - WooCommerce MCP is in A-25 (WC-A-22);
    - WooCommerce's AI Guidelines are in A-19 (WC-A-08);
    - Shopify's agentic storefronts are in A-21 (SH-C-140), though they are what A-28's own plain line calls "AI agents that shop on a buyer's behalf".
  - **A-08's note doesn't give its reason.** It says where Salla's and Zid's checkout sit, but not why the heading is the coordinator's own.
  - **Support for sellers is in three areas:**
    - Shopify's in A-01 (SH-A-01);
    - Salla's and Zid's in A-03;
    - WooCommerce's support policy in A-24 (WC-A-23).

    Yet A-03's plain line claims "the platform's support".
  - **A-23 (B2B) shows only Shopify and BigCommerce.** Others also offer it:
    - Salla's plan list carries "البيع للشركات وبالجملة B2B" (SA-I-1200, out of the concern map's scope as "a marketing line"), and its help centre has a "Wholesale stores" subcategory under Special plan features;
    - WooCommerce lists B2B extensions (WC-A-24, in A-24) and "B2B payments" (WC-C-005, in A-11).
- **Fix:**
  - Mark SH-A-17 as the agent's own, with its reason.
  - Split WC-A-10 so that the account goes to A-01.
  - Correct the A-17 and A-28 notes, and give A-08's reason.
  - In A-03's and A-23's notes, say where the other platforms' support and B2B sit.
- **Severity:** optional.

## Check 3. Nothing lost

### 7. Salla's "Charity stores" falls in no area, and no area names charities or donations

- **Where:** Salla's help-centre categories; A-01, A-04, A-11 and A-18.
- **Problem:**
  - The brief asks that each of Salla's help-centre categories falls in some area, by name or by plain line. Two fall in none:
    - "🤝 Charity stores" (Salla 4.0);
    - "Charity store management" (older articles: getting started, payment methods for charities, and charity store design).
  - Charities and donations show on three platforms, but no area's plain line names them.
- **Evidence:**
  - extract-salla.md, the help centre's categories, in English and in Arabic (إدارة متاجر الجمعيات الخيرية).
  - SA-C-127, "Charity stores' payment gateways", in SA-A-17, so in A-11:
    - SA-S-0206;
    - SA-S-3300, the `e-payment-charity` flag;
    - SA-S-5056, the Moyasar gateway;
    - SA-S-5057: charities' difficulty in activating Apple Pay delays donations.
  - Salla's quick donation (SA-S-3118) and product donation options (SA-S-3481), under SA-C-020 in A-04.
  - Zid's charity business type (ZD-S-0753, under ZD-C-035 in A-18).
  - Shopify's Non-Profit business entity (SH-S-7191, under SH-C-004 in A-01, with the scope countryCode YE).
  - Salla's notes flag it: "No concern covers charity stores as such."
- **Fix:**
  - Better: an area of its own under Salla's own name, "Charity stores", gathering SA-C-127, the donation features and the charity business types.
  - At the least: name "Charity stores [help centre]" in SA-A-17, add "including payment methods for charities' stores" to A-11's plain line, and add donation options to A-04's.
- **Severity:** must fix. Something the platforms offer would be missing from the list.

### 8. The other "nothing lost" checks hold, but one out-of-scope entry and some out-of-scope keys need a pointer

- **Where:** the inventory entries out of the concern map's scope; Shopify's Help Center menus; legal, place and eligibility matters.
- **What holds:**
  - Every concern is under one area, and none is under none (the checker).
  - The entries the platforms' notes flag stay within one merged area, or fit its plain line:
    - Shopify's "Dropshipping" section is split between SH-A-05 and SH-A-28;
    - Salla's 240 Partners-portal countries are in SA-A-22;
    - Zid's App Market categories are in ZD-A-21;
    - WooCommerce's payment suggestions are in WC-A-06;
    - BigCommerce's inventory webhooks are in BC-A-01.
  - Every top-level Shopify Help Center menu falls in an area, by name or plain line. So does every Salla help-centre category except Charity stores (finding 7). "Industry tips" and "Salla tools" hold tips, not offerings.
  - Legal, place and eligibility matters each have an area wherever the extracts show them, though some sit away from their kind:
    - Zid Egypt's company is in A-15 (finding 4);
    - Feedonomics' and Makeswift's contracting companies are in A-21 and A-25.
- **Out of scope, sampled.** I sampled about 30 entries:
  - Shopify's "Unplaced" keys, read with their values from the held file;
  - Shopify's legal, admin and product-menu entries;
  - Salla's flags, bundles and plan lines;
  - all of Zid's, WooCommerce's and BigCommerce's.

  Each falls under some area's plain line, except one:
  - **The exception.** Shopify's terms section "9.10 Beta Services" (SH-I-2418, SH-S-3182) is out of scope as "pre-release features offered by invitation". No area's plain line covers a platform's pre-release programme. It bears on Q8's "by release stage".
  - **Keys that reach no question.** Several Unplaced Shopify keys bear on Q1 and Q7: `perMarketIncoterms`, `landedCostIncoterms`, `multiCurrencyGatewayEnabled`, `subCountryMarketsEnabled`, `marketDeliveryProfiles`, `managedMarkets`, `usingMarketsPro`, `catalogRolloutsEnabled` and `threeDSecureEligibilityForCountry`. They fall under A-14, A-15 and A-11 by plain line, but being out of scope they reach no question's candidates.
  - **Keys I couldn't read.** Shopify's `argusConnect` and `appliedSpellcastingEnabled`, and Salla's `virtual-iban` and `sweply`, can't be read from their names.
- **Fix:** name SH-I-2418 in the Q8 briefs, and the per-place keys in the Q1 and Q7 briefs, for the runs to add.
- **Severity:** optional.

## Check 4. Plain lines and plain words

### 9. `areas.md` uses terms it doesn't define, one platform's word for all, and scraped names

- **Where:** A-11, A-16, A-20, A-25 and A-26 in `areas.md`, and the depth reasons.
- **Problem and evidence:**
  - **Terms not defined.**
    - In the areas:
      - "APIs, webhooks, access scopes and app authorization" (A-25). "Access scopes" is Shopify's term;
      - "subprocessors" (A-20).
    - In the depth reasons:
      - "underwriting" (Q3 Shopify);
      - "Nafath" (Q3 and Q6 Zid);
      - "Mahally" (Q8 Salla);
      - "block extensibility" (Q8 WooCommerce);
      - "embedded payment providers" (Q5 BigCommerce);
      - "unified billing" (Q8 BigCommerce);
      - "coming soon" (Q3 WooCommerce).
  - **One platform's word for all.** A-11's plain line says "offline methods", as if everyone used it. It is WooCommerce's and BigCommerce's name for them ("Payments > offline [settings]"; S01-BC-113). Shopify calls them manual payment methods.
  - **Names shown to the founder.**
    - Some are scraped strings with a badge's text joined on: "Merchant ServicesEssentials", "Salla PointFree Cashier".
    - A-26 shows "Salla: Affiliates, Influencer, Payments". These are Partners-portal menus, for partner programmes and partner billing, and they read as the seller's own affiliates and payments.
    - A-16 shows one Salla phrase three times: "مدعوم في:, Available in, مدعوم في".
- **Fix:**
  - Replace each term, or define it in one line.
  - In A-11, say "methods the seller records outside a provider, such as bank transfer and cash on delivery", as SH-A-13 does.
  - Show cleaned names, and in A-26 put "Salla's Partners portal" before Salla's names.
- **Severity:** optional.

### 10. Working words outside the headings and plain lines

- **Where:** the "kept anyway" texts of A-03, A-21, A-22 and A-28, and the depth reasons.
- **Problem:** the headings and plain lines are clean of the working words. A-15's "markets" is marked as some platforms' word, and A-11's "offline" is finding 9. But the texts the founder reads beside them use these:
  - **"parts":**
    - A-03: "plans as a way the platform adds parts";
    - A-21, A-22 and A-28;
    - the Q8 reasons for Shopify ("parts a store adds") and WooCommerce ("a platform built in parts").

    Q8 [2] asks for "the units it names, whatever it calls them", so "parts" presupposes the answer.
  - **"market":**
    - as our word: Q3 Zid ("in a market near Yemen's");
    - as Salla's and Zid's own word, but unmarked: Q1 and Q2 Salla ("per market") and Q7 Zid ("for each market").
  - **"availability":** Q2 WooCommerce ("WooPayments' availability by country").
  - **"manual payment methods":** Q4 Shopify. It is Shopify's own term, unmarked.
- **Fix:**
  - For Q8, use "units", or the platforms' own names.
  - Mark Salla's and Zid's word as theirs.
  - In Q2 WooCommerce, say "where WooPayments is offered".
- **Severity:** optional.

## Check 5. What each question draws on

### 11. Ten of `depth.tsv`'s own citations point to concerns their question won't start with

- **Where:** `depth.tsv`, ten rows, and the `questions` column of `areas.tsv`.
- **Problem:** each row's reason rests on concerns it cites, but these nine concerns (ten citations) sit in areas not tied to that row's question:

  | Row | Depth | Cited concern | Its area | Questions its area is tied to |
  |---|---|---|---|---|
  | Q1 Shopify | in depth | SH-C-037, catalogs | A-23 | Q4 |
  | Q7 Shopify | in depth | SH-C-037, catalogs | A-23 | Q4 |
  | Q3 Shopify | in depth | SH-C-174, sanctions and unsupported regions | A-16 | Q1, Q2, Q5, Q6 |
  | Q2 WooCommerce | in depth | WC-C-112, business services | A-24 | Q5, Q8 |
  | Q8 WooCommerce | in depth | WC-C-005, payment extensions | A-11 | Q1 to Q5 |
  | Q5 Zid | check | ZD-C-024, Mazeed's collections and dues | A-21 | Q1, Q8 |
  | Q8 Zid | check | ZD-C-060, Zid Logistics | A-10 | Q1, Q4, Q5 |
  | Q6 WooCommerce | check | WC-C-049, WordPress.com account | A-20 | Q2 |
  | Q7 BigCommerce | check | BC-C-007, price lists | A-05 | Q5 |
  | Q8 BigCommerce | check | BC-C-065, B2B Edition | A-23 | Q4 |

- **Evidence:** the cited concerns' statements bear on their questions:
  - SH-S-0304: "Individuals and businesses within unsupported countries and regions are prohibited from creating a Shopify account."
  - ZD-S-0704, paraphrased: Zid transfers Mazeed's dues to the merchant's bank account on the 30th of each month, once seven days have passed and the sum is at least 500 riyals.
  - WC-S-5335: "you'll have to create a WordPress.com account".
  - WC-S-0627: "Payment gateways should be created as additional plugins that hook into WooCommerce."
  - BC-S-0354: "BigCommerce's add-on for business-to-business commerce".

  Two cites are exceptions:
  - WC-C-112's statements are only category names: WC-S-0766 "Compliance", WC-S-0769 "Law".
  - BC-C-007's statements say nothing about currency.
- **Fix:**
  - Tie A-23 to Q1, Q7 and Q8; A-16 to Q3; A-21 to Q5; A-20 to Q3 and Q6; and A-10 and A-11 to Q8.
  - Drop WC-C-112 from Q2 WooCommerce and BC-C-007 from Q7 BigCommerce, with their words in the reasons.
  - Add the check described in finding 1.
- **Severity:** must fix. The questions would start without what their own depth reasons rest on.

### 12. Q1 misses what is set up differently by the seller's place in A-03, A-13, A-18, A-20, A-22 and A-23

- **Where:** Q1's ties (A-01, A-10, A-11, A-12, A-14, A-15, A-16, A-19, A-21).
- **Problem:** Q1 [3] asks, "What does the platform set up differently for sellers based in different places?" Offers that differ by the seller's place are recorded across most areas. Six areas Q1 doesn't draw on hold them.
- **Evidence (all not reached for Q1):**
  - **A-13, Shopify (in depth):**
    - SH-S-0472: "Eligible businesses based in Australia, Canada, France, Germany, Ireland, the Netherlands, Spain, the United Kingdom, and the United States can apply for Shopify Capital";
    - SH-S-0479: "your principal place of business must be within the country, and your bank account must be located in the country";
    - SH-S-0498: "Shopify Bill Pay is available only to merchants in the United States".
  - **A-13, Zid (check):** ZD-S-0693, paraphrased: Zid's financing is for merchants in Saudi Arabia only.
  - **A-22, Shopify (in depth):**
    - SH-S-7285: "German merchants can meet TSE Compliance ... to comply with KassenSichV regulation";
    - SH-S-7274: "POS Equipment Agreement ... applicable to your country".
  - **A-22, WooCommerce (check):** WC-S-0869, In-Person Payments for merchants in ten listed countries.
  - **A-03, Shopify:** SH-S-0268: "The billing currencies that are available to you are determined by the country of your billing address".
  - **A-20, Shopify:** SH-S-0662: the "Customer privacy settings lets you customize your privacy settings for each country and region where you sell to".
  - **A-18, Salla (in depth):** SA-S-0140, paraphrased: in Kuwait, only commercial bank accounts are accepted.
  - **A-23:** Shopify's catalogs by market (finding 11).
- **Fix:** tie A-03, A-13, A-18, A-20, A-22 and A-23 to Q1.
- **Severity:** must fix.

### 13. Q2 misses a place's laws and the platform's own partners in A-01, A-02, A-05, A-10 and A-22

- **Where:** Q2's ties (A-06, A-11 to A-20).
- **Problem:** Q2 [1] and [2] ask what changes "because of a place's laws, sanctions or licensing, or because of its own choice of partners and providers", recorded "wherever it shows". Two kinds of evidence sit outside its ties:
  - a place's law changing the product;
  - the platform's own choice of carriers and providers.
- **Evidence (all not reached for Q2):**
  - **A-22, Shopify (in depth):** SH-S-7285, Germany's KassenSichV at Shopify POS.
  - **A-22, Salla (in depth):**
    - SA-S-5038, paraphrased: freelance licences carry annual fees from Geidea under the merchant's contract with Geidea;
    - SA-S-5039: Salla Point's card payments go through a provider such as Geidea.
  - **A-10, Salla (in depth):**
    - SA-S-5059: Salla's labels need no contract with a carrier or payment gateway;
    - SA-S-5065 and SA-S-5066: Salla holds label amounts from the wallet and settles with the carrier after its commission.
  - **A-10, Zid (check):**
    - ZD-S-0839, paraphrased: Zid is a technical intermediary for shipping, not a carrier, and compensation follows the carriers' terms;
    - ZD-S-0848: merchants in Saudi Arabia or the Gulf can ship through licensed logistics companies.
  - **A-02, Zid:** ZD-S-1046 and ZD-S-0959, sender names and promotional messages under the Communications and IT Commission's rules.
  - **A-05, Salla:** SA-S-5017, from Salla's FAQ on abandoned carts, paraphrased: a rule given as being in line with the terms the Saudi Communications and IT Commission approved for the service.
  - **A-01, Shopify:** SH-S-0262, identity verification "helps Shopify comply with financial regulations".
- **Fix:** tie A-01, A-02, A-05, A-10 and A-22 to Q2.
- **Severity:** must fix.

### 14. Q3 misses requirements on the seller in A-04, A-14, A-15, A-16, A-20, A-21 and A-22

- **Where:** Q3's ties (A-01, A-02, A-03, A-11, A-12, A-13, A-17, A-18, A-19).
- **Problem:** Q3 [1] and [2] ask what a seller must do or meet before doing particular things, such as "opening the store to buyers, taking payments, receiving payouts, or selling particular products". Such requirements sit in seven areas it doesn't draw on.
- **Evidence (all not reached for Q3):**
  - **A-22, Shopify (in depth):** SH-S-0047 and SH-S-7262: "If you use our POS Services, you must use the same payment processor that you use for the Online Services".
  - **A-22, WooCommerce (check):** WC-S-0893 and WC-S-0894: the store address must be in a supported country, and "You must be using that country's native currency as the store currency".
  - **A-14, Shopify:** SH-S-0507: "you must register your business with your local or federal tax authority".
  - **A-15, Shopify:** SH-S-0366: "To sell in multiple currencies, you need to use Shopify Payments".
  - **A-16, Shopify:** SH-S-0038: "You must maintain an accurate location in the administrative console". Also SH-C-174 (finding 11).
  - **A-16, WooCommerce:** WC-S-5291: "A business must be located in the 50 states, Washington D.C., or Puerto Rico to sign up with WooPayments as a U.S. business".
  - **A-04, Shopify:** SH-S-0593: "POS stores that don't use Shopify Payments can't sell subscriptions".
  - **A-21, Zid (in depth):** ZD-S-0986 and ZD-S-0987, paraphrased: to sell on Mazeed, a store must be on a plan, and its activity must be allowed under Saudi rules.
  - **A-20, WooCommerce:** WC-S-5336: WooPayments "will be unable to take payments until reconnected to WordPress.com".
- **Fix:** tie A-04, A-14, A-15, A-16, A-20, A-21 and A-22 to Q3.
- **Severity:** must fix.

### 15. Q4 misses Zid Pay's payment links, a Salla limit on cash on delivery, and reports

- **Where:** Q4's ties (A-03, A-09, A-10, A-11, A-22, A-23).
- **Problem:** Q4 [4] asks what limits apply to orders paid outside the platform. Q4 [5] also asks for "any way of paying outside the checkout ... where the platform or a service it provides collects the money". Three areas it doesn't draw on hold such evidence.
- **Evidence (all not reached for Q4):**
  - **A-12, Zid (check):** ZD-S-0586 and ZD-S-0587, paraphrased: Zid Pay's payment links are made as manual orders (Orders > Manual orders > New).
  - **A-18, Salla (in depth):** SA-S-0110, paraphrased: cash on delivery is hidden from customers blocked in other Salla stores.
  - **A-27:** Q4 asks about reports. See finding 22.
- **Fix:** tie A-12, A-18 and A-27 to Q4.
- **Severity:** must fix.

### 16. Q5 misses where the money goes and who decides, in A-01, A-04, A-06, A-15, A-17, A-18, A-21 and A-23

- **Where:** Q5's ties (A-03, A-05, A-08 to A-13, A-16, A-22, A-24).
- **Problem:** Q5 [1] asks who decides which methods a seller can offer, and on what basis. Q5 [5] asks, "Where does the money from each method go on its way to the seller". Eight areas it doesn't draw on hold the answers, several for in-depth platforms.
- **Evidence (all not reached for Q5):**
  - **A-18, Salla (in depth):** SA-S-0094 and SA-S-0098, paraphrased: Salla transfers the store's dues to the bank account tied to store verification, whose holder's name must match the verification.
  - **A-04 and A-06, Shopify (in depth):**
    - SH-S-0676 to SH-S-0678: the seller is "legally responsible for all gift card or store credit issuance", handles the amounts "in compliance with Applicable Laws, including ... escrow", and supervises "all daily funds flow associated with Gift Cards and Store Credit";
    - SH-S-0593: subscriptions at POS require Shopify Payments.
  - **A-01, Shopify:** SH-S-0258: "Each entity has its own Shopify Payments account, payout currency, and bank account".
  - **A-15, Shopify:** SH-S-0545: "Only stores with Shopify Payments or Adyen as the primary gateway can process payments in a customer's local currency".
  - **A-23, BigCommerce (in depth):** BC-S-0195: "Every payment method you have enabled on the store-level can be enabled or disabled as needed on the Company level".
  - **A-17, WooCommerce:** WC-S-0525: "Merchants selling CBD must use Square or Viva Wallet".
  - **A-21, Zid:** ZD-S-0704, Mazeed's dues (finding 11).
- **Fix:** tie A-01, A-04, A-06, A-15, A-17, A-18, A-21 and A-23 to Q5.
- **Severity:** must fix.

### 17. Q6 misses what isn't offered in a seller's place, in A-10, A-11, A-13, A-14, A-20, A-21 and A-22

- **Where:** Q6's ties (A-01, A-02, A-12, A-15 to A-19).
- **Problem:** Q6 [2] asks "What can a seller do when they are based in, or sell from, a place where the platform, or part of what it offers, isn't available, and how does the platform say so?" Q6 draws on only one area for this: A-12, the platform's own payment service. Most of what isn't offered in a place sits elsewhere.
- **Evidence (all not reached for Q6):**
  - **A-11:**
    - SH-S-0414: "Shop Pay Installments is available to eligible stores in the United States, Canada, and the United Kingdom";
    - ZD-S-0605: Paymob is for merchants in the UAE, Saudi Arabia and Oman;
    - BC-S-0143 and BC-S-0157: BigCommerce Payments and Braintree, for US-based businesses only;
    - SA-S-0084 (also in A-10), paraphrased: tracking cash on delivery in the wallet isn't available to stores in the UAE for now, so track the amounts through the carrier or your own courier. This is Q6's exact case.
  - **A-13:**
    - SH-S-0472, SH-S-0479 and SH-S-0498: Capital and Bill Pay, by country;
    - ZD-S-0693: Zid's financing, Saudi Arabia only.
  - **A-14:**
    - SH-S-0522: "Automated filing is available only for stores in the United States";
    - WC-S-0635: WooCommerce's automated taxes, for stores in listed countries.
  - **A-10:** WC-S-0905: "WooCommerce Shipping is currently available to stores based in the United States".
  - **A-22:** WC-S-0869: In-Person Payments, ten countries.
  - **A-21:** SH-S-0724: "Shop is available in countries where Shopify Payments is supported".
  - **A-20:** WC-S-5335, the WordPress.com account (finding 11).
- **Fix:** tie A-10, A-11, A-13, A-14, A-20, A-21 and A-22 to Q6.
- **Severity:** must fix.

### 18. Q7 misses currency rules in A-01, A-09, A-11, A-16, A-22 and A-23

- **Where:** Q7's ties (A-03, A-12, A-15).
- **Problem:** Q7 [1] and [2] ask, among other things, in what currencies buyers pay and sellers are paid out, and "what decides it". Q7 draws on three areas, and currency rules sit in six others.
- **Evidence (all not reached for Q7):**
  - **A-11, Shopify (in depth):**
    - SH-S-0388: "To accept manual payments in multiple currencies, you need to use Shopify Payments and activate the international sales tools";
    - SH-S-0582: "Each method is available only when a customer is in a supported country and selects an eligible currency".
  - **A-01, Shopify:** SH-S-0258, each entity's own payout currency.
  - **A-22, WooCommerce (check):**
    - WC-S-0870: card readers "can only collect payments in the default currency for each country";
    - WC-S-0894: the store currency must be the country's native currency.
  - **A-16, WooCommerce:** WC-S-0880: the store currency is chosen on the general settings page.
  - **A-09, BigCommerce (check):** BC-S-0112: "The payment provider must be enabled and configured with the same channel and currency that the order is placed against".
  - **A-23:** Shopify's catalogs (finding 11).
- **Fix:** tie A-01, A-09, A-11, A-16, A-22 and A-23 to Q7.
- **Severity:** must fix.

### 19. Q8 misses most of what the record says about how units are added and introduced

- **Where:** Q8's ties (A-03, A-07, A-21, A-22, A-24, A-25, A-26, A-28, A-29).
- **Problem:** Q8 [3] asks, for each unit, "how new ones are added or existing ones extended, and how the platform introduces them, for example by plan, by place or by release stage". Such statements sit in nearly every area, and most of them fall outside Q8's nine. This includes the material named in the Q8 reasons themselves.
- **Evidence (all not reached for Q8):**
  - **Salla's dashboard feature flags (Salla is a check).** Each flag records whether it is released, and the plans and countries it is scoped to. Counted once per merged area, they appear 520 times. 399 of those fall in areas not tied to Q8: 262 scoped by plan and 133 not yet released. They sit mostly in A-04, A-05, A-09, A-10 and A-11. Examples:
    - SA-S-3110, Google Pay: unreleased, on the Plus, Pro and Special plans (A-11);
    - SA-S-3341, multiple warehouses (A-04);
    - SA-S-3497, the wallet gift card (A-05);
    - SA-S-3265, order settings (A-09).

    Salla's Q8 reason names "features released by plan and country".
  - **WooCommerce's statements on how it is extended (in depth):**
    - WC-S-0627, gateways "created as additional plugins that hook into WooCommerce" (A-11);
    - WC-S-0628, "a Shipping Method API which plugins can use" (A-10);
    - WC-S-5433, the features class and plugins' declared compatibility (A-02);
    - WC-S-0875, multi-currency needs "a multi-currency extension/plugin" (A-15);
    - WC-S-0585 and WC-S-0463, "open-source" (A-19).
  - **Zid (check):** ZD-S-0837 and ZD-S-0838, Zid Logistics and shipping prices by plan (A-10).
  - **BigCommerce (check):** BC-S-0354, BC-S-0356 and BC-S-0357, B2B Edition as an add-on that extends native B2B (A-23).
  - **Shopify (in depth):** SH-S-5256 and SH-S-5257, scheduled rollouts (A-15). Also Shopify's Beta Services clause, out of scope (finding 8).
- **Fix:**
  - Simplest: let Q8 draw on every area, since every unit of every platform can be introduced by plan, place or release stage.
  - At the least, tie A-02, A-04, A-05, A-09, A-10, A-11, A-15, A-19 and A-23 to Q8.
- **Severity:** must fix.

### 20. Ties that would mostly add candidates for runs to set aside

- **Where:** A-02 to Q6, A-03 to Q7, A-15 to Q6, and A-05 to Q5.
- **Problem and evidence:**
  - **A-02 to Q6.** My sample of A-02's statements tied to Q6 found nothing on who can register, or from where. It held:
    - permission names, and domain and language flags (SA-C-002, SA-C-007, SA-C-008);
    - team and security settings (ZD-C-094, ZD-C-095);
    - email templates (BC-C-046).

    The "kept anyway" phrase "what a store must give when it is set up" isn't shown.
  - **A-03 to Q7.** The currency the platform bills the seller in isn't one of Q7's four currencies. Examples:
    - SH-C-016;
    - BC-C-030: "Fees are payable in U.S. Dollars";
    - ZD-C-020, paraphrased: all fees are in Saudi riyals or the merchant's local currency.
  - **A-15 to Q6.** For every platform but Zid, A-15 holds selling to buyers in other countries, not where sellers are based.
  - **A-05 to Q5.** Most of Salla's A-05 is campaign, SEO and blog flags. Only customer wallets, cashback and gift cards bear on Q5.
- **Fix:** keep these ties or drop them; a run can set candidates aside. They matter less than the missing ties.
- **Severity:** optional.

## Check 6. What a "won't do" mark removes, and what is kept

A-05's and A-15's "won't do" texts are findings 4 and 5. A-12's "kept anyway" is finding 2. The rest follows.

### 21. "Kept anyway" texts that contradict their area or will go stale

- **Where:** A-04, A-05, A-06 and A-12, and every area whose ties change under findings 11 to 19.
- **Problem and evidence:**
  - **A-04 contradicts itself.** Its "kept anyway" is "Nothing: no question draws on it", while its `left_out` says that "Q5's runs add them from here", meaning gift cards.
  - **A-05 claims what it doesn't hold.** It claims "store credit and gift cards" for Q5, but Shopify's are in A-06 and A-04 (finding 5).
  - **A-06 names too little.** It names only Q2, yet it holds Shopify's store credit, which bears on Q5 (finding 16).
  - **Ties will change.** Once the ties change, each "kept anyway" that lists questions has to be rewritten to match.
  - **Texts I couldn't check:**
    - A-12's "won't do" cites "Your guard";
    - A-11's cites "section B's items 4 and 5", and A-24's "section B's item 5".

    These rest on the plan and the founder's decisions, which the brief doesn't name.
- **Fix:** rewrite these texts with the ties, and re-render.
- **Severity:** optional.

## Check 7. What the work doesn't read, and why

### 22. A-27's and A-04's reasons for leaving them out don't hold

- **Where:** the `left_out` and "kept anyway" fields of A-27 and A-04.
- **Problem:**
  - **A-27.** Its reason is "None of the eight items asks about reports." But Q4 [3] asks: "what does the platform do and not do: recording the payment, the order's status, refunds, fees and reports?" The founder would read a wrong reason, and the Q4 runs would start without the reports.
  - **A-04.** Its reason is "None of the eight items asks about products or stock as such." But Q3 [2] names "selling particular products", and A-04 holds:
    - statements that bear on Q3 and Q5;
    - the plan and release flags Q8 asks about.

    The reason also leans on Q5's runs adding gift cards, which no tie arranges.
- **Evidence:**
  - **For A-27.** Salla records a report of payment methods (تقارير طرق الدفع, SA-S-2553), and a setting for which order statuses reports include (SA-S-3281, on the Plus, Pro and Special plans). Both are not reached for Q4.
  - **For A-04, Shopify:**
    - SH-S-0593: "Subscriptions on POS require Shopify Payments. POS stores that don't use Shopify Payments can't sell subscriptions";
    - SH-S-0677 and SH-S-0678: the gift-card funds;
    - none of these is carried by any concern tied to Q3 or Q5.
  - **For A-04, plan and release flags:**
    - 68 Salla flags in A-04: 54 scoped by plan, 16 not yet released;
    - ZD-S-1021: Zid's warehouses, by plan.
- **Fix:**
  - Tie A-27 to Q4, and A-04 to Q3, Q5 and Q8.
  - Rewrite their `left_out` and "kept anyway" texts. With ties, `left_out` empties.
- **Severity:** must fix.

## Check 8. Depth by question

### 23. Reasons in `depth.tsv` that misstate what they cite

- **Where:** these `depth.tsv` rows: Q4 Shopify, Q2 Salla, Q6 Salla, Q1 Salla, Q5 WooCommerce, Q2 WooCommerce, Q8 WooCommerce, Q7 BigCommerce, Q7 Shopify and Q8 Salla.
- **Problem and evidence:**
  - **Q4 Shopify.** The reason says "its transaction fee on them". The cited concerns say the opposite:
    - "you aren't charged transaction fees on manual payment methods such as cash, cash on delivery (COD), and bank transfers" (SH-S-0322, SH-C-079);
    - "Transaction fees don't apply for POS orders or for manual payment methods" (SH-S-0276, SH-C-018).
  - **Q2 and Q6 Salla, contracting company.** The reasons say "its legal entities and contracting company per country". But:
    - SA-C-230's statements name only Saudi companies (SA-S-0015 to SA-S-0020, SA-S-5001);
    - its four gaps say that the clauses naming the company for each country are in pages held but not read;
    - Salla's own areas notes say, "Nothing says which company contracts in each country".
  - **Q6 Salla, sanctions.** The reason says "sanctions and screening". SA-C-232's statements show violations, customers blocked from cash on delivery, and beneficial owners in Kuwait. None of them names a sanctions rule.
  - **Q1 Salla, languages.** The reason says "languages ... set per market". No statement of SA-C-165 or SA-C-163 shows languages, and Salla's languages concern (SA-C-008) is in A-02.
  - **Q6 Zid.** The reason says "Zid serves sellers in Saudi Arabia and the Gulf". See finding 24.
  - **Q5 WooCommerce, balance.** The reason says "holds no balance itself". That is true of the core software (WC-C-001), but not of Woo's own WooPayments, which keeps an account balance and reserves (WC-C-007, WC-C-008).
  - **Q2 and Q8 WooCommerce, business services.** The Q2 reason says "business services for compliance", and the Q8 reason counts business services among what WooCommerce grows through. WC-C-112's statements are category names (WC-S-0766 "Compliance", WC-S-0769 "Law") and an agency-partner line. Nothing in them says what a place's law requires, or how the services extend the store.
  - **Q7 BigCommerce and Q7 Shopify.** Both lean on things Q7 doesn't establish:
    - BigCommerce: "price lists", though BC-C-007 says nothing about currency;
    - both: the billing currency (SH-C-016, BC-C-030), which Q7 doesn't ask about (finding 20).
  - **Q8 Salla, by country.** The reason says "features released by plan and country". Only 3 of Salla's 520 flag placements carry countries:
    - `shipping-tier-pricing-system`, for SA and AE;
    - `kyc_new_workflow`, for the six Gulf countries, which appears in two areas.
- **Fix:** rewrite these reasons to say what the cites show. For Salla's contracting company, say that it is not recorded, and where to read it.
- **Severity:** optional. They don't change a scope mark, but the founder reads them, and two of them are wrong on facts.

### 24. Zid, read only as a check for Q6 (and Q1 and Q2), records an answer the in-depth platforms don't show

- **Where:** the Q6 Zid row, and the Q1 and Q2 rows.
- **Problem:** Q6 is read in depth on Shopify and Salla only:
  - Shopify bars sanctioned regions, Syria among them, outright (SH-C-174);
  - Salla serves Saudi Arabia and the Gulf (SA-C-167).

  Zid's record shows something neither of them shows. Zid lists Syria among its countries, while Zid Pay bars dealings with Syria. Zid Pay is offered only in Saudi Arabia and Kuwait. And one answer says Zid serves merchants of all nationalities (من جميع الجنسيات). The Q6 reason doesn't mention any of this.
- **Evidence:**
  - ZD-S-0741: zid.sa/llms.txt, "Other countries": Egypt, UAE, Kuwait, Oman, Syria (2026-10-12).
  - ZD-C-037 (Zid Pay, Saudi Arabia), paraphrased: the prohibited activities include dealing, directly or indirectly, with countries under international sanctions, among them Iran and Syria.
  - ZD-S-0743: Zid Payments, "Currently in Saudi Arabia and Kuwait".
  - ZD-S-0742, dated 2023, paraphrased: Zid currently serves merchants located in Saudi Arabia and the Gulf only, of all nationalities.
  - ZD-S-0737: Zid Egypt has its own commercial registration, yet zid.eg serves the Saudi terms (gap on ZD-C-031).
  - ZD-C-030: Kuwaiti merchants' Zid Pay contract is under Saudi law, with Riyadh courts.
  - ZD-S-0746: the wallet must be emptied before the store's country changes.

  For Q1, by contrast, BigCommerce is read in depth, though its notes say it records no list of countries where it operates or where a store may sell.
- **Fix:** read Zid in depth for Q6, and rewrite its reason. For Q1, weigh reading Zid in depth beside BigCommerce, or in its place.
- **Severity:** optional.

### 25. BigCommerce's checks (Q3, Q4, Q6, Q7) and Salla's Q7 check rest on thin or unread records, and BigCommerce shows answers the in-depth platforms may not

- **Where:** the rows Q3, Q4, Q6 and Q7 BigCommerce, and Q7 Salla.
- **Problem and evidence:** the candidates under the present ties are few, and gaps are many. The table counts candidate concerns, statements, statements matching the question's key words (a rough screen), and gaps, with in brackets the gaps whose page was not read:

  | Row | Concerns | Statements | Key-word statements | Gaps (unread) |
  |---|---|---|---|---|
  | Q3 BigCommerce | 20 | 122 | 10 | 34 (9) |
  | Q4 BigCommerce | 18 | 111 | 2 | 36 (16) |
  | Q6 BigCommerce | 15 | 79 | 1 | 28 (4) |
  | Q7 BigCommerce | 5 | 41 | 11 | 8 (1) |
  | Q7 Salla | 12 | 130 | 20 | 21 (20) |

  - **What lies behind the gaps:**
    - 31 of BigCommerce's gaps say that its Help Center could not be read;
    - 206 of Salla's 230 gaps, over 121 concerns, are pages held but not read because of a bot challenge. SA-C-164, the currency Salla Payments settles in, has 3 statements and 4 gaps.
  - **What the pilot adds.** The pilot fills part of BigCommerce's record, but no `depth.tsv` row cites it:
    - S01-BC-113 to S01-BC-120: the offline methods, with orders left in "Awaiting Payment" (S01-BC-114). These bear on Q4;
    - S01-BC-029, S01-BC-086 and S01-BC-091: where BigCommerce Payments and PayPal are offered. These bear on Q6.
  - **BigCommerce answers that differ.** BigCommerce's record shows answers the in-depth platforms may not:
    - **Q3:** the merchant must screen its own customers for sanctions: "conducting sanctions screenings of your Relevant Parties and customers" (BC-S-0438, with BC-S-0437). The gap notes that BigCommerce states no screening of its own;
    - **Q7:** the settlement currency is set through the payment provider (BC-S-0403), and the conversion rate is "outside of BigCommerce's scope" (BC-S-0405, BC-S-0406). On the platforms read in depth, the platform's own service decides:
      - Shopify sets payout currencies through Shopify Payments (SH-C-069);
      - Zid Pay charges buyers in the store's base currency, Saudi riyals or Kuwaiti dinars, whatever currency prices are shown in (ZD-S-0808, paraphrased).
- **Fix:**
  - Cite the pilot's statements in these rows.
  - Tell these check runs where the record's holes are (BigCommerce's Help Center, and salla.com's held pages), and how to find the held captures (`method/held_index.py`).
  - Weigh reading BigCommerce in depth for Q3 or Q7.
- **Severity:** optional.

## Verdict

**The list can't go to the founder yet.** Fifteen findings are must-fix, for three reasons:

- **Wrong basis for marks.** The founder would mark four areas on a wrong or partial basis:
  - A-12 hides two platforms' own payment services (finding 2);
  - A-13 hides two platforms' financing (finding 3);
  - A-15 and A-05 bundle things a first build may want apart, and their "won't do" texts don't say what goes (findings 4 and 5).
- **Something missing.** Charity stores, a category of Salla's own, appear nowhere (finding 7).
- **Questions starting without what bears on them.** Every one of the eight questions would start without evidence that bears on it, often for in-depth platforms. This includes concerns that `depth.tsv`'s own reasons cite, and reports, which A-27's reason wrongly says no question asks about (findings 11 to 19 and 22).

Most of the fixes are edits:
- to `areas.tsv`: its `questions` column, and its "won't do", "kept anyway", `left_out` and note texts;
- to `depth.tsv`: two cites, with the words of the reasons that rest on them.

A few need platform areas re-cut: SA-A-17, SA-A-18, BC-A-10 and WC-A-03, and, for the better fix to A-15, SH-A-17, SA-A-21, ZD-A-10 and BC-A-19. After that, run `method/check_areas.py`, ideally with the two checks from finding 1, and `method/render_areas.py`.

Once the must-fix findings are done and the scripts pass, the list can go to the founder. The optional findings would improve it, but none of them would change a mark.
