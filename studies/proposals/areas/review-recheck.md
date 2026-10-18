# Re-check of the areas list after its fixes (step R1)

**18 October 2026.** This re-checks the fixes the coordinator made after my review of the areas list (`review.md`: 25 findings, 15 must fix). The fixes are commit 2731962. I checked:
- `areas.tsv`, `depth.tsv` and `areas.md`;
- each platform's areas file and notes;
- `method/check_areas.py`, `method/render_areas.py` and `method/copy_statements.py`;
- the new dated entry in `PLAN.md` section 11.

By the time I finished, the branch had moved to 5fd5079. In between, the areas files, the two areas scripts and that entry are unchanged. `copy_statements.py` changed, and I note how below.

Ids lead to the evidence, as in `review.md`. Arabic statements are given in English paraphrase. A statement **not reached** for a question is carried by no concern in an area tied to that question. I checked each case by script, splitting cite ids on spaces as well as on ";".

## At a glance

- **The 25 findings:**
  - 21 are fixed, including all 15 must-fix findings;
  - 2 are partly fixed (9 and 25);
  - 2 are not fixed: 8 waits for the runs' starting messages, and 20 was kept, as it allowed.
- **New findings (7):**
  - **must fix (1):** finding 1, on A-15's texts and BigCommerce's Geography;
  - **optional (6):** findings 2 to 7.
- **Verdict:** not yet, but one edit away. Fix new finding 1, run the two scripts again, and the list can go to the founder.

## What I ran and read

- **Scripts.** I ran `check_areas.py` for each platform and for `merged`. I ran `render_areas.py` from a scratch copy of the script and its inputs, and compared the result with `areas.md`.
- **My earlier samples, again.**
  - The 92 question-and-statement pairs that findings 12 to 19 and 22 marked not reached.
  - Every cite in `depth.tsv`, by a check of my own as well as the script's.
  - A key-word scan of each question's untied areas, reading the hits for the platforms read in depth.
  - The five new merged areas, against the questions they aren't tied to.
  - The 17 concerns whose merged area lost a question in the re-cut.
- **Sizes.** Each run's candidate concerns and statements, before the fixes (c613452) and after them.
- **Beyond the changed files:**
  - the concern map's statements and gaps for the concerns named below;
  - one search of `extract-shopify.md`, for its International sales tools menu, to check SH-A-17's new note.

## The checks by script

| Check | Areas | Concerns placed | Problems | Warnings |
|---|---|---|---|---|
| shopify | 33 | 198 | 0 | 1 |
| salla | 34 | 152 | 0 | 1 |
| woocommerce | 30 | 118 | 0 | 0 |
| zid | 32 | 96 | 0 | 1 |
| bigcommerce | 34 | 88 | 0 | 1 |
| merged | 34, over 163 platform areas | — | 0 | 0 |

- **The four warnings.** Each says the platform has more areas than the brief's aim of 30. They follow from the re-cut the review asked for, so nothing needs to change.
- **The render.** The scratch render is identical to `areas.md`, byte for byte (md5 `7ffd91feed90d02dce3b1571b3176fe0` for both). It now says "34 areas" and shows every platform name.
- **`copy_statements.py`.**
  - The pilot's row, S-01, now ends every question's selection. It is `copy` for Q5 and `candidate` for the others, and `copy` copies the pilot only when the row is marked `copy`.
  - At 2731962, though, `show` refused S-01. So a run outside Q5 couldn't read the pilot's statements to judge the row.
  - Commit 5fd5079, from another re-check, made `show` print them. The script is sound now.
- **The new checks in `check_areas.py`.**
  - They pass on every current row. My own check agrees: every concern a `depth.tsv` reason cites, directly or through a citation, sits in an area tied to its question.
  - They have gaps that no current row falls into (new finding 4).

## The 25 findings, one by one

1. **Fixed.**
   - `check_areas.py merged` now checks that each concern a depth reason cites is reached by the row's question, and that no area with questions gives a `left_out`.
   - `areas.md` shows every name, among them "BigCommerce Payments" (A-12), Zid's "الأسواق" (A-15) and Shopify's "Acceptable Use Policy" (A-19).
   - The new check has gaps (new finding 4).
2. **Fixed.**
   - Salla Payments (SA-C-110, now in SA-A-31) and BigCommerce Payments (BC-C-025, now in BC-A-32) are in A-12. A-12's plain line names both.
   - A-12's note says where Salla files the bank account its payouts go to (A-18), and its payment services contract (A-19).
   - A-11 is tied to all eight questions.
   - BC-S-0141, BC-S-0143 and BC-S-0147 are reached for every question.
3. **Fixed.** Salla's financing (SA-C-128, now in SA-A-32) and WooCommerce's (WC-C-016, now in WC-A-29) are in A-13. Its note names all four platforms' financing.
4. **Fixed.**
   - Languages (A-30) and currencies (A-31) are areas of their own, and A-15's "won't do" says that mark doesn't remove them.
   - Salla's languages (SA-C-008) are in A-30. Zid's countries and Zid Egypt (ZD-A-31) are in A-16.
   - Zid's languages stay with its currencies in A-31, since ZD-C-050 is one settings page. A-30's and A-31's notes say so. This doesn't change what either mark removes from Sharrwah.
   - The re-cut brought a new problem into A-15 (new finding 1).
5. **Fixed.**
   - A-32 holds Shopify's gift cards and store credit (SH-A-32), and Salla's and Zid's customer wallets (SA-A-34, ZD-A-32).
   - A-33 holds BigCommerce's price lists (BC-A-33), with Shopify's catalogs (SH-A-33).
   - BigCommerce's gift certificates stay in A-05, since BC-C-010 joins them with coupons and banners. A-05's "won't do" and note say so; on the wording of the "won't do", see new finding 2.
6. **Fixed.**
   - SH-A-17 is marked as an agent's grouping, with its reason. Its note says the International sales tools menu holds domains and geolocation, which stay in SH-A-17, its currency pages, now in SH-A-31, and its languages, now in SH-A-30. That matches the menu in `extract-shopify.md`.
   - The WordPress.com account (WC-A-30) is in A-01.
   - Shopify's catalogs are in A-33.
   - The notes of A-03, A-08, A-23 and A-28 say what the finding asked.
   - A-17's note is corrected for Zid and for Shopify's sanctions. It now leaves out Shopify's other such rules (new finding 3).
7. **Fixed.**
   - A-34, Charity stores, holds SA-A-33 (SA-C-127), under Salla's help-centre names "🤝 Charity stores" and "Payment methods for charities".
   - Its note points to Salla's donation options (A-04), Zid's charity business type (A-18) and Shopify's non-profit entity (A-01).
   - On how its heading is marked, see new finding 3.
8. **Not fixed.**
   - The coordinator intends to name these in the runs' starting messages, which is the finding's own fix:
     - SH-I-2418, in Q8's;
     - the per-place Shopify keys, in Q1's and Q7's.
   - Those messages aren't written yet, and no file records the intent (new finding 7).
9. **Partly fixed.**
   - Defined or replaced:
     - "access scopes" (A-25) and "subprocessors" (A-20);
     - all seven terms in the depth reasons:
       - "underwriting" is now "the checks on a business before it gets credit";
       - Nafath and the coming-soon mode are explained;
       - "block extensibility" is now "ways for extensions to change its blocks";
       - Mahally, Embedded Payment Providers and Unified Billing are marked as the platforms' own names.
   - A-11 now says "methods the seller records outside a provider such as bank transfer and cash on delivery".
   - A-16 shows Salla's phrase once: "مدعوم في, Available in, Countries".
   - A-26's note says Salla's names there are its Partners portal's menus.
   - Left as they were:
     - "APIs" and "webhooks" (A-25) are still undefined;
     - the scraped names "Merchant ServicesEssentials" (A-26) and "Salla PointFree Cashier" (A-22) are kept as extracted, by the coordinator's choice.
10. **Fixed.**
    - The founder's texts no longer use "parts", "availability" or "conditions".
    - "Manual payment methods" is marked as Shopify's ("what it calls").
    - "Market" is marked as the platforms' word in A-15 and in the depth reasons: Q1 and Q2 Salla, and Q7 Zid.
    - One new unmarked "market" is in A-33's plain line (new finding 3).
11. **Fixed.**
    - Eight of the ten cites are now reached: SH-C-037 for Q1 and Q7 Shopify, SH-C-174, WC-C-005, ZD-C-024, ZD-C-060, WC-C-049 and BC-C-065.
    - WC-C-112 and BC-C-007 are dropped, with the words that rested on them.
    - The script now checks this. So does my own check, and no cite is unreached.
12. **Fixed.**
    - All 11 statements are reached for Q1.
    - A-03, A-13, A-18, A-20 and A-22 are tied to Q1, and so is A-33, where the catalogs now are.
13. **Fixed.** All 12 statements are reached for Q2. A-01, A-02, A-05, A-10 and A-22 are tied to Q2.
14. **Fixed.**
    - All 13 statements are reached for Q3.
    - A-04, A-14, A-15, A-16, A-20, A-21 and A-22 are tied to Q3.
    - SH-S-0366, which moved to A-31, is reached there.
15. **Fixed.**
    - All 5 statements are reached for Q4, among them finding 22's two from A-27.
    - A-12, A-18 and A-27 are tied to Q4.
16. **Fixed.**
    - All 11 statements are reached for Q5.
    - Shopify's gift-card and store-credit statements (SH-S-0676 to SH-S-0678) are now in A-32, which is tied to Q5.
    - SH-S-0545 is now in A-31, which is tied to Q5.
17. **Fixed.**
    - All 15 statements are reached for Q6.
    - A-10, A-11, A-13, A-14, A-20, A-21 and A-22 are tied to Q6.
    - WC-S-5335 is now in A-01, which is tied to Q6.
18. **Fixed.**
    - All 8 statements are reached for Q7.
    - A-01, A-09, A-11, A-16 and A-22 are tied to Q7, and so is A-33, where the catalogs now are.
19. **Fixed.**
    - All 17 statements are reached for Q8.
    - Q8 now draws on every area, so the 399 placements of Salla's flags that the finding counted outside Q8 are in it.
20. **Not fixed, as the finding allowed.**
    - A-02→Q6, A-03→Q7, A-15→Q6 and A-05→Q5 are kept.
    - The re-cut leaves two more ties of this kind (new finding 5):
      - A-06→Q5, made for Shopify's store credit, which is now in A-32;
      - A-20→Q6, made for the WordPress.com account, which is now in A-01.
    - They only add candidates for runs to set aside.
21. **Fixed.**
    - Each "kept anyway" now names exactly its area's questions (34 of 34). A-04's contradiction is gone.
    - A-05 no longer claims store credit and gift cards it doesn't hold. A-06's text matches its ties.
    - "Your guard" (A-12) and "section B" (A-11, A-24) still rest on files my brief doesn't name.
22. **Fixed.**
    - A-27 is tied to Q4, and A-04 to Q3, Q5 and Q8.
    - Every `left_out` is empty, and the checker now refuses one on an area with questions.
    - SA-S-2553 and SA-S-3281 are reached for Q4, SH-S-0593 for Q3 and Q5, and SH-S-0677 and SH-S-0678 for Q5.
23. **Fixed.** All ten reasons now say what their cites show:
    - Q4 Shopify: "that it charges no transaction fee on these methods";
    - Q2 and Q6 Salla: "its Saudi companies". Which company contracts in each country is "not yet recorded", and the reasons say where it is to be read;
    - Q6 Salla: no sanctions claim;
    - Q1 Salla: no languages;
    - Q5 WooCommerce: "Its core software holds no balance, while WooPayments keeps one, with reserves";
    - Q2 and Q8 WooCommerce: no business services;
    - Q7 BigCommerce and Q7 Shopify: no price lists, and no billing currency;
    - Q8 Salla: released "by plan", not by country.

    One small gap remains in Q5 WooCommerce's cites (new finding 6).
24. **Fixed.**
    - Zid is read in depth for Q6, and the reason gives what the finding found:
      - Syria is among Zid's countries;
      - Zid Pay is offered only in Saudi Arabia and Kuwait, and bars dealings with sanctioned countries;
      - one answer says Zid serves merchants "of all nationalities".
    - ZD-C-032 carries ZD-S-0741 to ZD-S-0743, and ZD-C-037 the sanctions ban.
    - Q1 is unchanged. The finding asked only that it be weighed.
25. **Partly fixed.**
    - Done:
      - the pilot is cited: S01-BC-113 to S01-BC-120 for Q4, and S01-BC-029, S01-BC-086 and S01-BC-091 for Q6;
      - Q7 BigCommerce's reason says the settlement currency is set through the payment provider, and the conversion rate is outside BigCommerce's scope;
      - Q7 Salla's reason says most of the gaps are pages held but not read.
    - Left:
      - BigCommerce stays a check for Q3 and Q7. The finding asked only that this be weighed.
      - The holes in the record (BigCommerce's Help Center, and salla.com's held pages) are to be named in starting messages not yet written.
      - Q3 BigCommerce's reason still says it "records little here" (new finding 6).

## New findings

### 1. A-15's heading and "won't do" now speak of all selling abroad, and its plain line takes in BigCommerce's address lists

- **Where:** A-15 and A-16 in `areas.tsv`; the platform area BC-A-34.
- **Problem:**
  - **The heading and "won't do" say more than the area holds.**
    - With languages and currencies split out, A-15 holds only per-country versions of a store, with Shopify's tools for them. Its plain line begins "Per-country versions of one store, each with its own settings, which Shopify, Salla and Zid call markets; Shopify's Managed Markets, international domains and geolocation". Its note says "WooCommerce and BigCommerce have no such setting".
    - But the heading is "Selling to several countries from one store", and the "won't do" reads "Selling to several countries from one store would be outside Sharrwah's extent". The old heading named "per-country store versions"; the new one doesn't.
    - So a founder who wants stores to sell abroad without per-country versions, as WooCommerce does, would read the mark as ruling that out, and leave A-15 in.
    - A founder who marks A-15 would think selling abroad is gone, while the mark removes only the per-country versions.
    - WooCommerce's own setting for the countries a store sells and ships to (WC-C-030) sits in A-16, whose plain line doesn't mention it.
  - **The plain line now takes in something every store needs.**
    - The re-cut split BigCommerce's Geography from BC-A-19 into BC-A-34, "The countries, states and provinces a store's addresses, shipping and tax use", and left it in A-15.
    - A-15's plain line now ends "and the countries and regions a store's addresses use", and its note says "BigCommerce's Geography ... is here".
    - By that plain line, a "won't do" on A-15 would also remove the lists a store's addresses use. The "won't do" text doesn't say so.
  - **The same lists on the other platforms are in A-16.** So one kind of thing is split between A-15 and A-16:
    - Salla's countries, cities and districts (SA-C-166);
    - Zid's store countries and cities (ZD-C-033);
    - WooCommerce's country and continent data (WC-C-099).
- **Evidence:**
  - A-15's and A-16's rows in `areas.tsv`, and BC-A-34's row in `areas-bigcommerce.tsv`.
  - BC-S-0412, BC-C-075's one statement: "Use these endpoints to retrieve geographic data for use in shipping, tax, and address validation workflows."
  - WC-S-0600 (WC-C-030): "This option lets you limit which countries you are willing to sell to."
  - WC-S-5459 (WC-C-099): "Returns an array of countries and codes".
  - ZD-S-0744 (ZD-C-033): "Retrieve a list of countries where the store operates."
  - Before the re-cut, BC-C-075 sat in BC-A-19, so in A-15 too. But A-15's plain line didn't name it, and its heading named per-country store versions.
- **Fix:**
  - Move BC-A-34 to A-16. A-15 and A-16 are tied to the same seven questions, so no question loses a candidate.
  - Drop "and the countries and regions a store's addresses use" from A-15's plain line, and the sentence on Geography from its note.
  - Name A-15 for what it holds, for example "Per-country versions of one store".
  - Make A-15's "won't do" say what stays, for example: "Per-country versions of one store would be outside Sharrwah's extent: ... Selling and shipping to buyers in other countries, languages and currencies are in other areas (A-16, A-10, A-30 and A-31), so this mark doesn't remove them."
  - Add to A-16's plain line what it holds for a store: the countries it sells and ships to, how it locates a buyer, and the lists of countries, states and cities its addresses use.
  - Correct A-16's note. It gives WooCommerce's "Selling locations" as a list of the places WooCommerce serves, but that is a store's own setting. Woo's list of the places it serves is WooPayments' "supported countries" (WC-C-010).
  - Run `check_areas.py merged` and `render_areas.py` again.
- **Severity:** must fix. The founder would mark A-15 on a wrong basis. A first build for one country would most likely mark this area.

### 2. Two other "won't do" texts: A-31 can't mark a store in one currency, and A-05 speaks of the record

- **Where:** the `wont_do_removes` of A-31 and A-05.
- **Problem and evidence:**
  - **A-31.**
    - Its "won't do" removes "Setting a store's currencies" and adds "Every store needs at least one currency, so this mark is unlikely".
    - A-30's removes only "A store in more than one language".
    - So the founder can mark a store in one language, but not a store in one currency: marking A-31 would take the store's own currency too.
    - Currencies are one of the founder's eight items (Q7), so this choice may matter to them.
  - **A-05.**
    - Its "won't do" ends "BigCommerce's gift certificates, which it files with its coupons, would go with them".
    - But a mark removes things from Sharrwah's extent, and the area's evidence still serves its questions. Gift cards stay in Sharrwah's extent through A-32 unless that is marked too.
    - The sentence reads as if a kind of gift card left with marketing.
- **Fix:**
  - Word A-31's "won't do" as A-30's is worded, for example: "A store that shows or takes prices in more than one currency would be outside Sharrwah's extent". Or, if the mark is meant to be whole, say so.
  - In A-05's, say instead: "Gift cards, store credit and customer wallets are an area of their own (A-32), so this mark doesn't remove them." The note already says where BigCommerce files its gift certificates.
- **Severity:** optional.

### 3. Headings, plain lines and notes the fixes left inexact

- **Where:**
  - A-34, A-33, A-17 and A-30 in `areas.tsv`;
  - the opening of `areas.md`, written by `render_areas.py`;
  - the Salla, WooCommerce, Shopify and BigCommerce notes.
- **Problem and evidence:**
  - **A-34's heading is Salla's, marked as the coordinator's.**
    - It is marked "coordinator's own", and its note begins "The heading is ours".
    - But "Charity stores" is Salla's own help-centre category: SA-A-33 is named "🤝 Charity stores [help centre]".
    - `areas.md` tells the founder that the heading is the coordinator's "where no one name covers all the platforms". Here one name covers the one platform.
  - **A-33's plain line uses "market" unmarked:** "catalogs for a market or a business customer". The heading is the coordinator's, and the word is Shopify's.
  - **A-17's note leaves out two of Shopify's rules.**
    - Of Shopify, it names only "Shopify's sanctions with where it operates (A-16)".
    - Shopify's Acceptable Use Policy (SH-C-172) is in A-19.
    - Shopify Payments' prohibited and restricted businesses (SH-C-173) are in A-12.
    - My finding 6 named only the sanctions, and the rewrite followed it.
  - **A-30's note says nothing of WooCommerce.**
    - WooCommerce has no languages setting of its own.
    - Its translation and localization extensions are a Marketplace category, "International and localization" (WC-C-108), in A-07.
  - **The opening of `areas.md` still says the platform areas were "named in its own words by one short run per platform".**
    - After the review, 19 of the 163 platform areas are new, made by the coordinator, and 16 more were changed.
    - The names are still the platforms' own, but some of the cuts aren't the runs'.
  - **Stale figures in the platforms' notes:**
    - Salla's notes say "28 areas" (now 34), and WooCommerce's say "one of the 28 areas" (now 30);
    - the entries split across areas are now 1,059 for Shopify (the notes say 1054), 90 for Salla (84) and 62 for BigCommerce (61).
- **Fix:**
  - Mark A-34's heading as Salla's own name, or say in its note that it is Salla's category name without its emoji.
  - Mark "market" in A-33 as Shopify's word, or say "a country's version of the store".
  - Add to A-17's note Shopify's acceptable use (A-19) and Shopify Payments' prohibited businesses (A-12).
  - Add to A-30's note WooCommerce's localization extensions (A-07).
  - Add a clause on the re-cut to the opening of `areas.md`, in `render_areas.py`.
  - Correct the figures in the notes.
- **Severity:** optional.

### 4. The new checks in `check_areas.py` have gaps

- **Where:** `check_merged` in `method/check_areas.py`.
- **Problem and evidence:**
  - **Citations it can't trace pass unchecked.**
    - The check maps a cited citation to its concerns by splitting each statement's `cite_ids` on ";" only.
    - 27 WooCommerce citation ids, WC-S-5471 to WC-S-5497, under eight concerns from WC-C-103 to WC-C-112, are written with spaces between them ("WC-S-5471 WC-S-5472"). So the script maps them to no concern.
    - Nor does it map the 3,643 citation ids in the five `citations.tsv` files that no statement carries.
    - A reason citing any of these passes, since the test is `if concerns and not any(...)`. No current row cites one.
    - Since 5fd5079, `copy_statements.py` splits cite ids on commas, spaces and ";", "as the checker reads them". `check_areas.py` doesn't.
  - **Nothing checks "kept anyway" against the ties.**
    - All 34 texts name exactly their area's questions now, but they were written from the ties, and nothing keeps them so.
    - The next change of ties could leave them stale again, which is the risk finding 21 named.
  - **The docstring.** The sentence 'A depth of "none" is allowed only under the founder's cuts ...' now follows the `left_out` bullet. It belongs with the `depth.tsv` bullet.
- **Fix:**
  - Split cite ids as `copy_statements.py` does, and report a cited citation that maps to no concern.
  - Check that `kept_anyway` names the area's questions, or have `render_areas.py` write that sentence from `questions`.
  - Move the sentence.
- **Severity:** optional.

### 5. A few statements still sit outside their question's ties, and two ties now bring little

- **Where:** A-05, A-06, A-07, A-09, A-20, A-21 and A-32.
- **Problem and evidence:**
  - I scanned each question's untied areas again by key words, and read the hits for the platforms read in depth. What remains are single statements, not the patterns of findings 12 to 19:
    - **SH-S-0733** (SH-C-132, Shopify Audiences, in A-05): "Shopify Audiences is available to eligible stores on the Shopify Plus plan that use Shopify Payments and are based in the United States or Canada." Not reached for Q1, Q3 or Q6.
    - **SH-S-7215** (SH-C-026, store credit, in A-32): "Before you can issue and accept store credit, you'll need to enable the new customer accounts login experience." Not reached for Q3.
    - **SH-S-7475** (SH-C-141, Shopify Collective, in A-21): "It's your responsibility to then agree with each retailer what manual payment method they should use to pay you, and on what terms." Not reached for Q4.
    - **SA-S-5020 and SA-S-5021** (SA-C-065, customer addresses, in A-06). Paraphrased: the Transport General Authority requires the national address for delivering shipments, and when the setting is on, customers in Saudi Arabia must give it to complete an order. Reached for Q2, but not for Q1.
    - **SA-S-5034** (SA-C-093, information pages, in A-07). Paraphrased: the barcode on the invoice lets the customer open the store's exchange and returns policy, so that the store meets one of the main invoice requirements of the e-commerce law. Not reached for Q2.
    - **WC-S-5441 and WC-S-5442** (WC-C-091, order withdrawal requests, in A-09): WooCommerce "does not determine whether the customer has a legal right to withdraw", and "For advice specific to your business and customers' locations, consult a qualified legal professional." Not reached for Q2.
  - **Two ties left with little.**
    - A-06→Q5 was made for Shopify's store credit, which is now in A-32.
    - A-20→Q6 was made for the WordPress.com account, which is now in A-01.
    - My samples of both find nothing else that bears.
- **Fix:**
  - Name these concerns in the starting messages of the runs concerned, with finding 8's.
  - A run may add concerns from other areas, so naming them is enough. Tying their areas would add many candidates for one statement each.
  - The two ties can stay.
- **Severity:** optional.

### 6. Two depth reasons

- **Where:** `depth.tsv`, the rows Q3 BigCommerce and Q5 WooCommerce.
- **Problem and evidence:**
  - **Q3 BigCommerce.**
    - The reason says "BigCommerce records little here beyond BigCommerce Payments, fees and the store's profile".
    - It cites BC-C-080, whose BC-S-0438 binds the merchant to "an effective, risk-based compliance program and necessary internal controls (including, but not limited to, conducting sanctions screenings of your Relevant Parties and customers)".
    - No in-depth reason for Q3 shows such a requirement on the seller (finding 25). The founder reads the reason as saying BigCommerce has little to add.
  - **Q5 WooCommerce.** The reason says WooPayments keeps a balance "with reserves". But it cites WC-C-007 (balance and payouts) and not WC-C-008 (reserves). WC-C-008 is reached all the same, in A-12.
- **Fix:** name the screening duty in Q3 BigCommerce's reason, and add WC-C-008 to Q5 WooCommerce's cites.
- **Severity:** optional.

### 7. The PLAN entry: the copies will grow, Q8's most, and the deferred items aren't recorded

- **Where:** the entry of 18 October 2026 in `PLAN.md` section 11.
- **What holds:**
  - 34 areas;
  - the re-cuts it lists;
  - Q8 on every area;
  - the pilot offered to every question;
  - Zid in depth for Q6;
  - the new checks, and every name shown in `areas.md`;
  - the sample. 21 runs are in depth, and the median of their candidate statements in the concern map is 875. Q3 on Salla holds exactly 875. With each platform's pilot statements counted too (from 128 to 202, by platform), the median is 1,077, and it is still Q3 on Salla.
- **Problem and evidence:**
  - **The cost sentence.**
    - The entry says "A run sets aside what doesn't bear, so wider ties cost a longer selection, not longer copies".
    - But the new ties were made because their concerns bear, so runs will copy more.
    - Candidate statements before and after the fixes:
      - the in-depth runs: 12,428 over 20 runs before, 22,968 over 21 now;
      - all 40 runs: 18,336 before, 34,282 now.
  - **Q8 grows most:**
    - Shopify's run, from 48 concerns and 1,009 statements to 198 and 3,005;
    - WooCommerce's run, from 26 concerns and 295 statements to 118 and 1,499.
  - **A Q8 run may copy most of its platform's map.**
    - Q8 [2] asks the run to record every unit, and [3] how each is added, extended and introduced.
    - Drawing Q8 on every area was my proposal (finding 19), so this cost is mine to name.
  - **The deferred items aren't recorded.** No file records what the coordinator intends to put in the starting messages:
    - finding 8's SH-I-2418 and per-place keys;
    - finding 25's holes in the record;
    - the statements in new finding 5.
- **Fix:**
  - Say in the entry that copies will grow, and by up to how much. If step R3's cost was estimated on the earlier ties, estimate it again.
  - Record the deferred items where the starting messages are drafted, or in the entry.
- **Severity:** optional.

## What I couldn't check

- "Your guard" (A-12) and "section B" (A-11, A-24), which rest on files my brief doesn't name.
- The starting messages that findings 8 and 25 now depend on. They aren't written yet.
- Whether step R3's cost estimate assumed the earlier ties. The cost and sizing files are outside my brief.

## Verdict

**Not yet, but one edit away.** All fifteen must-fix findings of the review are fixed, and the scripts pass.

One new problem is must fix (new finding 1). A-15's heading and "won't do" speak of all selling abroad, though A-15 holds only per-country versions of a store. Its plain line now also takes in BigCommerce's address lists. The fix:
- edit the A-15 and A-16 rows, and move BC-A-34 from A-15 to A-16;
- run `check_areas.py merged` and `render_areas.py` again.

After that, the list can go to the founder. The six optional findings would improve it. None of them changes what a mark removes.
