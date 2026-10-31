# Review of the held pass's dry run, part R2: BC-1, lines 38 to 96 (payment-gateways)

**What this is.** Part R2 of the review the brief `studies/class-model/briefs/H-review.md` (at `2316f3ab`) sets: every line of BigCommerce's `payment-gateways` structure in batch BC-1, tested against its entry, its sources and the model's cells. The rows are in `review-H-R2.tsv`, one per verdict. This file holds:
- the counts;
- the case the brief names for R2, and the notes' other items that bear on these lines;
- the fixes to H-held.md;
- what the batch never placed;
- the notes' claims;
- the leads.

**What I read, pinned:**
- the placements and notes at `ff50bbee` (`studies/class-model/held/bigcommerce/placements-BC-1.tsv`, lines 38 to 96; `notes-BC-1.md`), which are the same in the working tree;
- `briefs/H-held.md` and `held/selection.tsv` at `dc1e6414`, also unchanged;
- `briefs/B-extent.md`, "Cells and evidence" and "Conventions from the dry run", as of `04aefe93`. That version is in force when the batch ran: it is an ancestor of `dc1e6414`;
- the model's cells through `land_points.py cell`, at `13205959` (`merged/` is unchanged since then);
- other-product-class at `0d79b794f`, in this order:
  - its `README.md`;
  - `bigcommerce/README.md`, `GAPS.md` and `structures/REGISTER.tsv`;
  - `index/runs.tsv` and `index/run-notes.tsv`;
  - the structure's `meta.json`, `items.jsonl` and `source.html`;
  - the text of the file `meta.json` names under `source` (`held_as`: `raw/runs/20261029T024758Z-help-center-en/steps/001.html`). I read it as `001.text.txt`, and checked quotes in `001.html` by script, without printing it;
- the entries and their leads, through `held_entries.py show --platform bigcommerce --batch BC-1 --from 25 --to 81 --candidates` and `--meta`, as the script prints them now;
- the checker's code (`method/held_entries.py`, `cmd_check`), to say which test would catch each miss.

**Citations below:**
- `[art]:N` is line N of `other-product-class@0d79b794f:bigcommerce/raw/runs/20261029T024758Z-help-center-en/steps/001.text.txt`;
- `[src]` is `other-product-class@0d79b794f:bigcommerce/structures/payment-gateways/source.html`;
- a cell is the model's, read with `land_points.py cell <cap_id> bigcommerce`.

Every claim not marked as a fact or an assumption is a reading.

**The entries against their sources (facts):**
- the 57 items equal the 57 rows of `[src]`'s four tables, field by field (0 mismatches, by script);
- each of the four tables occurs verbatim, once, in `001.html`;
- each entry's text is its item, with empty marks left out (0 mismatches);
- no line's terms are missing from the entry's text, no filler differs from the item's name, and every quality matches the item's marks.

So no row here is `entry differs from source`. What the items leave out is listed under "What the batch never placed".

## Counts

143 rows on 59 lines (entries 25 to 81, 57 entries; PayPal and Amazon Pay have two lines each). 9 lines stand whole (63 to 69, 93, 95); 50 carry at least one miss. Lines 92, 94 and 96 stand as placed but miss a line.

| Verdict | Rows | Lines |
| --- | --- | --- |
| `stands` | 12 | 63 to 69, 92 to 96 |
| `wrong supports: core` | 45 | 38 to 42, 44 to 52, 54 to 61 (table 1), 43, 70 to 91 (table 3) |
| `wrong supports: shows` | 1 | 62 |
| `can't tell` | 1 | 53 |
| `missing line: CM-SEL-001 shows` | 15 | 38, 39, 45, 46, 47, 52, 57, 62, 70, 71, 73, 75, 76, 81, 89 |
| `missing line: CM-PAY-016 core` | 2 | 92, 94 |
| `missing line: CM-B2B-001 shows` | 1 | 96 |
| `wrong reading` | 22 | 70 to 91 |
| `missing terms: Payment Gateway` | 44 | the table 1 and table 3 lines on CM-PAY-011 |

| Cause / effect | Rows | What |
| --- | --- | --- |
| `brief` / `column` | 46 | the supports of the gateway rows (45) and of BigCommerce Payments (1) |
| `brief` / `capability` | 18 | the missing lines |
| `care` / `column` | 66 | the misquote (22) and the missing term (44) |
| `evidence` / `count` | 1 | PayPal's second line |

**By the structure's four tables:**
- table 1, Embedded Payment Providers (lines 38 to 62): 55 rows;
- table 2, app payment processors (63 to 69): 7 rows, all `stands`;
- table 3, Open Payment Providers (70 to 91): 73 rows;
- table 4, offline methods (92 to 96): 8 rows, 5 of them `stands`.

**By third of BC-1's 175 lines:**
- lines 38 to 59 fall in the first third, and all 22 of them have a miss;
- lines 60 to 96 fall in the second third, and 28 of their 37 do.

The misses follow the tables' kinds, not their place in the batch. Each is one choice applied to a whole table: the supports on tables 1 and 3, the misquote on table 3, the missing term on both. A reading.

**How I used `effect`.** The brief's five values don't cover two of the cases here. I name them so R6 can weigh them:
- **A row's `supports` changes, but its cell keeps its placement: `column`.** This covers all 46 supports rows. CM-PAY-011's BigCommerce cell already holds `core` from BC-S-0150, and CM-PAY-002's and CM-PAY-012's hold `core` from other statements. On a platform whose cell lacked that statement, the same 44 gateway rows would be `count`.
- **A missing line adds evidence to another capability: `capability`.** For the 15 CM-SEL-001 rows, this turns a `none-held` cell into a held one, placed `not-stated`. The effect list has no value for that. I take it as an important detail: the cell no longer reads `none-held`, which says the concern map holds nothing on it by the terms searched.

## The case: which supports the payment-gateways rows take (R2)

**The brief's premise:**
- **Fact:** the brief says the model's CM-PAY-011 cell reads "the article's 'more than 65 pre-integrated online payment solutions'" as `core`. That phrase isn't in this article: there are 0 matches in `001.text.txt` and in `001.html`. It is BC-S-0150, a statement of the concern map's concern BC-C-026 (`class_slice.py search --terms "pre-integrated"`).
- **The article's own words for the same thing:**
  - for table 1, "Processing payments through BigCommerce gateway integrations on the Embedded Payment Provider list do not incur Open Payment Provider fees", set against "custom integrations to processors on the Embedded Payment Provider list, including those connected via third-party apps" (`[art]:77`);
  - for the whole article, "BigCommerce supports a broad range of payment gateway integrations, serving numerous countries and currencies." (`[art]:73`);
  - for table 3, "the above payment gateway integrations" (`[art]:151`).

**The cell's two readings, the precedents:**
- CM-PAY-011's BigCommerce cell reads BC-S-0150 as `core`: "providers the platform has integrated".
- It reads the bare list BC-S-0142, "Embedded Payment Provider List* BigCommerce Payments Adyen Affirm", as `shows`.

A row of table 1 alone is like BC-S-0142. Read with its article, it is like BC-S-0150. B-extent's convention "A statement's title against its description: its words as a whole decide" makes it the second.

**Does H-held.md's rule for a help page's title apply to a row of a table in one?**
- No. The clause covers "a help page's title, a changelog post, or a FAQ": an entry that is only a title, whose words are all that is held. A row of a table inside an article isn't one of those. It is a statement of the article, and takes B-extent's values read with the article's words, as H-held.md's rule 4 says ("`supports` takes `B-extent.md`'s values exactly").
- Even under the clause, a table 1 row read with its article names more than "only ... a third party". It names the platform's own integration with that third party, which is the clause's own `core` ("built-in feature").

**The ruling, table by table:**

| Rows | Supports | Why (a reading) |
| --- | --- | --- |
| Table 1, the 22 third-party gateways on CM-PAY-011 | `core`, each gateway its filler | "BigCommerce gateway integrations" (`[art]:77`): the platform itself provides the connection, which is B-extent's `core` ("the platform itself does it for the merchant"), as the cell reads BC-S-0150. Not `outside`: the platform's integration is named. Not `extension-point`: no app, extension target, provider interface or API is named for these rows. |
| Table 1, BigCommerce Payments on CM-PAY-002 (line 62) | `shows` | The row names a gateway with the platform's brand. B-extent: "A product's name that carries the platform's brand doesn't name its maker", and "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap". CM-PAY-002's cell reads the same kind of statement (BC-S-0148, its row in the compatible gateways table; BC-S-0142) as `shows`. The capability stands. |
| Table 1, Amazon Pay on CM-PAY-012 (line 43) | `core` | The article puts the wallets' setup "under the Digital Wallets section of Settings › Payments" (`[art]:166`), the platform's own admin section. |
| Table 1, PayPal on CM-PAY-013 (line 53) | can't tell | Which PayPal the row is isn't stated; see the row. |
| Table 2, the 7 app payment processors | `extension-point` (stands) | "the following app payment processors are also Embedded Payment Providers" (`[art]:111`), and `[src]` links each to its App Marketplace page (`www.bigcommerce.com/apps/<slug>/`): an app on the platform's marketplace. |
| Table 3, the 22 Open Payment Providers | `core`, each gateway its filler | "payment gateway integrations" that "BigCommerce supports" (`[art]:73`, `:151`). The article sets them apart from table 1 by fee only (`[art]:117`), and `[src]` links each to the platform's own "Connecting with <gateway>" article. This is weaker than table 1, which says "BigCommerce gateway integrations"; see method ruling M1. |
| Table 4, the 5 offline methods | `core` (stands) | The platform's own methods, with no third party named, as the cells read S01-BC-115 to S01-BC-119. |

**Where B-extent's three clauses that H-held.md leaves out bear here:**
- core's "the platform itself does it for the merchant" decides the 44 gateway rows and line 43;
- extension-point's "the statement shows third parties doing it through something the platform provides" gives table 2 the same answer as H-held.md's clause;
- own-service's "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap" decides line 62. The line's reading notes "its name names no maker", but its `core` rests on CM-PAY-002's cell, not on the entry.

## The notes' other items that bear on these lines

- **"Couldn't tell" 1 (the gateway rows):** ruled above. The notes' "the same rule applied" gives two answers:
  - for the offline methods and the app payment processors, the same answers as mine;
  - for BigCommerce Payments, `core`, which B-extent's own-service clause and CM-PAY-002's cell refute.
- **"Couldn't tell" 2 (gateways not given a second capability):**
  - **BNPL and crypto:** the refusal stands. Neither the entries nor the article state instalments or buy now, pay later for Affirm, Afterpay, Clearpay, Klarna Payments, Sezzle or Zip, nor cryptocurrency for BitPay. The article names BNPL only as a type of APM (`[art]:160`), and Klarna only as an APM (`[art]:74`). CM-PAY-015's cell reads four of them as `shows` "by the providers' names, which WooCommerce's and Shopify's cells hold", but H-held.md allows a placement only from the entry and its source. This is method ruling M2.
  - **Amazon Pay's second line:** the right capability, with the wrong supports (above).
  - **PayPal's second line:** can't tell (above).
  - **Not in the notes:** the `Recurring Payments: ✔` marks, which are CM-SEL-001's (below).
- **Problem 1 ("The brief's two rules give different answers"):** the conflict is real in H-held.md's words. B-extent settles it toward neither rule. The `outside` rule fails because the platform's integration is named. The help-page rule doesn't reach a table row. The answer is `core`.
- **Problem 3 (the leads dropping a word's first letter, "ayPal", "igCommerce"):**
  - **Fact:** none of the current leads for these 57 entries shows such a fragment.
  - **Fact:** the batch's own commit `ff50bbee` records the fix: "the leads' identifier pattern fixed to match whole words only".
  - I didn't rerun the old script, so what the agent saw is not checked.

## Fixes to H-held.md

Each fix comes with:
- the words to paste;
- the lines of this part it touches;
- whether it stays within B-extent;
- the checker test that would catch the miss.

1. **Rule 4, rows of a table in an article.**
   - Paste: "A row of a table or an item of a list inside an article (a help page, a plan page, a guide) is read with the words the article gives it: its table's heading, the paragraph before the table, its columns' definitions, and the footnotes its marks point to. The help-page clause covers an entry that is only a page's title."
   - Touches the 44 gateway lines (38 to 61 but 43 and 53, and 70 to 91) and line 43.
   - Within B-extent: "its words as a whole decide".
   - **Checker:** no test can decide supports. One would have put these 44 lines in front of the agent: a NOTE for each `shows` line whose term is one of the target cell's terms on the platform, where that cell holds `core`. Here the terms are "Embedded Payment Providers" and "Open Payment Providers", and CM-PAY-011 holds `core`.
2. **Rule 4, B-extent's three clauses, and lists of providers.**
   - Paste, in B-extent's words:
     - for `core`, "the platform itself does it for the merchant";
     - for `extension-point`, "the statement shows third parties doing it through something the platform provides";
     - for `own-service`, "Without a statement naming the company, place the cell by what its statements show, and note the missing maker statement as a gap".
   - Then add: "A list of third-party providers that the platform's own words call its integrations is `core`, with each provider as its filler. One the words call an app, or link to the app store, is `extension-point`. A bare list of names is `shows`."
   - Touches lines 38 to 96.
   - Within B-extent: the last sentence is the model's own reading of BC-S-0150 and BC-S-0142.
3. **Rule 4, a product with the platform's brand.**
   - Paste: "A product whose name carries the platform's brand is placed by what its entry shows. The brand makes it neither `own-service` nor `core`. Note the missing maker statement as a gap."
   - Touches line 62.
   - Within B-extent.
   - **Checker:** a NOTE for each `core` line whose entry's text holds the platform's own name inside a product's name (here BigCommerce Payments; Salla Payments is another, in CM-PAY-002's own name), beside the NOTE `check` already prints for each `own-service`.
4. **Rules 2 and 5, a feature a table marks for each row.**
   - Paste: "A feature a table marks for each row (a ✔ under a column such as Recurring Payments) is also a statement of the feature's own capability. Where that capability's cell on the platform holds nothing, write a line there: `shows`, unless the row says who does it. Elsewhere the mark may stay a quality of the row's line."
   - Touches lines 38, 39, 45, 46, 47, 52, 57, 62, 70, 71, 73, 75, 76, 81 and 89.
   - Within B-extent: a quality is "a limit, a certification, an uptime or a data location ... on the capability it bears on". Whether a feature mark is a quality at all is method ruling M3.
   - **Checker:** a NOTE for each entry whose leads include a capability whose cell on the platform holds nothing, where no line of the entry places it there. The leads now print "[cell: holds nothing]" (`99d429ad`), and CM-SEL-001 is among the leads of all 15 entries.
5. **Rule 7, quotes in `reading`.**
   - Paste: "A quote in `reading`, in single quotes, is copied exactly from the entry's text or its source."
   - Touches lines 70 to 91, which quote 'outside the Embedded Payment Provider list' for the source's 'methods outside of the Embedded Payment Provider list' (`[art]:117`). `held_amend.py` writes the reading into the model's evidence as written.
   - Within B-extent: "No claim goes beyond what a cited statement says".
   - **Checker:** each single-quoted piece of `reading` must be found, with whitespace folded, in the entry's text, its item, its structure's `source.*`, or the text of the file its `meta.json` names under `source`.
6. **Rule 1, footnotes.**
   - Paste: "A footnote an entry's mark points to (an asterisk on a value or a name) is part of the entry's text: place what it states."
   - Touches line 96 (Check's footnote, B2B Edition's Purchase Order method) and line 91 (Windcave's '*See article for details.', which the reading already holds).
   - Within B-extent.
   - **Checker:** a NOTE for each entry whose text ends a value or a name with `*` (here `3D Secure: ✔*` and `Check*`).
7. **Rule 2, a child capability and its parent.**
   - Paste: "Where an entry's own words name a parent capability's thing (its section is the parent's term) and the entry is placed on a child, write the parent's line too."
   - Touches lines 92 and 94: Bank deposit and Cash on delivery are under "OFFLINE PAYMENT METHODS", CM-PAY-016's term. Their siblings are on CM-PAY-016, and the cells cite S01-BC-115 and S01-BC-116 on both parent and child.
   - **A method ruling (M4):** B-extent's `parent` convention is about grouping, not citation.
   - **Checker:** a NOTE for each line term that is another capability's cell term on the platform, where no line of the entry places it there.

**Not a fix:** the missing term "Payment Gateway" (44 rows, cause `care`). Rule 5 already asks for "the platform's own words for the thing, found in the entry's text", and every row's text holds "Payment Gateway: <name>". The cell's terms hold "connected payment gateways" and "compatible payment gateways", so little changes. No reliable checker test.

**For the review brief, not H-held.md:**
- the R2 case's premise (the 65 phrase is BC-S-0150, not the article's);
- the effect list's two gaps (above).

## Method rulings for the coordinator

- **M1:** table 3. B-extent's `core`, "the platform itself does it", reads two ways for "payment gateway integrations" that the platform "supports" with no builder named. I rule `core`, as the cell reads BC-S-0150. `shows` is the other reading. An Open provider's "Connecting with <gateway>" article, which `[src]` links from each row, would settle it.
- **M2:** may a held entry take a provider's role (instalments, cryptocurrency) from other platforms' cells, when the entry's own sources don't state it? CM-PAY-015's BigCommerce cell does, "by the providers' names". H-held.md says no; B-extent says nothing. Touches lines 40, 41, 49, 51, 54, 61 and 72.
- **M3:** is a provider's feature mark a quality? H-held.md's rule 5 says "a limit or value". B-extent says "a limit, a certification, an uptime or a data location", "on the capability it bears on". Touches the 45 lines with marks. I judged qualities by rule 5, as the review brief says, so the qualities stand.
- **M4:** is an entry placed on a child capability cited on its parent too (fix 7)?

## What the batch never placed

The structure's items hold the four tables' names and marks only, as its `meta.json` says ("four HTML tables"). The selection reads the structure through its items. H-held.md places entries only. So everything below was left out by the build. The agent noted five of these things (marked "noted") and placed none, as it couldn't.

| # | What the source states | Where | Would it change a cell? |
| --- | --- | --- | --- |
| 1 | Each row's link: 45 to the platform's own "Connecting with <gateway>" articles (tables 1 and 3), and 7 to App Marketplace pages, `https://www.bigcommerce.com/apps/<slug>/` (table 2) | `[src]`, 52 links | No placement. The App Marketplace links show table 2 as apps. The help links are where each integration's builder (M1) and each gateway's countries would be read. |
| 2 | The six features' definitions, among them "Recurring Payments — Recurring or subscription payments are supported." | `[art]:80` to `:85`, `:120` to `:125` | **Yes:** with the marks, CM-SEL-001's none-held BigCommerce cell becomes held (`shows`). The others bear on CM-PAY-020, CM-PAY-022, CM-MKS-006 and CM-CHN-007, all `core` already. "3D Secure" has no capability, and a column is no place of its own. |
| 3 | "BigCommerce supports a broad range of payment gateway integrations, serving numerous countries and currencies." | `[art]:73` | No (CM-PAY-011 is `core`). It is the article's own word for what BC-S-0150 says. |
| 4 | The fee rules: Embedded integrations pay no Open Payment Provider fee; custom integrations and third-party apps do; the fee falls on self-serve plans; Performance plans under contract are exempt; offline methods pay it too (noted) | `[art]:77`, `:117`, `:151`, `:155` | No (CM-PLN-003 is `core`). It adds two things BC-S-0154 doesn't say: the fee on offline methods and the Performance exemption. |
| 5 | "See each gateway's documentation for details such as requirements, limitations, setup instructions, supported countries and currencies, and additional features." | `[art]:78`, `:118` | No. It says each gateway's countries are in its own article, so the fillers carry no market: a gap. |
| 6 | "Powered By" stores "may not have access to all listed payment gateways" (noted) | `[art]:79`, `:119` | No (CM-PTN-010 gains `shows`). |
| 7 | B2B Edition's Purchase Order method, in Check's footnote (noted, and quoted in line 96's reading) | `[art]:155` | No placement; a row on line 96. |
| 8 | Alternative payment methods: their types ("bank transfers", BNPL, "cash payments", "digital wallets", "direct debit", "mobile payments"), "Offered through a supporting payment gateway"; Alipay, Klarna, SEPA | `[art]:74`, `:156` to `:165` | No. CM-PAY-015 and CM-PAY-017 gain `shows`; CM-PAY-017 stays not-stated, since a gateway isn't the platform's service. |
| 9 | The wallets' setup "under the Digital Wallets section of Settings › Payments" (noted) | `[art]:166` | **The reading only.** CM-PAY-001's reading says no control panel page for payment methods is held; this names Settings › Payments, as R3's settings-list entry 104 does. CM-PAY-012 gains a `core` statement (row on line 43). |
| 10 | "For a full list of available APMs, digital wallets, and their supported gateways, see Introduction to Alternative Payment Methods." | `[art]:167` | No; an article not read. |
| 11 | Accelerated Checkout: "Fastlane by PayPal" and "Stripe Link — Supported by the Stripe payment gateways" | `[art]:75`, `:168` to `:174` | **Fillers:** PayPal and Stripe on CM-CHK-008 (`core` already). |
| 12 | "You will control and direct funds in your merchant account with your merchant service provider", with refunds "external to BigCommerce" | `[art]:176`, `:177` | **The reading only.** It answers CM-PAY-011's Q1 gap, "who holds the funds, searched, not found". The cell already holds `outside`. |
| 13 | The hosted gateways (Afterpay, Amazon Pay, BitPay, Klarna, Mercado Pago, Opayo, Optty, Serve First, Sezzle), "not compatible with Embedded Checkout on headless storefronts"; Google Pay and PayPal Pay Later support it (noted) | `[art]:178` to `:193` | No. CM-SFR-011 and CM-CHK-001 are held. It is an attribute per gateway that no item holds. |
| 14 | Level 2 and Level 3 data | `[art]:194`, `:195` | No capability holds it. |
| 15 | Regulated products: Bankful, NMI, Sezzle, USA ePay, Worldpay; "*You must use Paysafe as your Merchant Services Provider (MSP)." | `[art]:196` to `:203` | **A filler:** Paysafe, a third party setting the terms for USA ePay. CM-TRU-010 gains `shows` and stays not-stated. |
| 16 | "Yes, you can find additional payment processors on our App Marketplace." | `[art]:205` | No (CM-PAY-011 holds `extension-point`, BC-I-0490). |
| 17 | A notification in the control panel dashboard when a payment method changes, and records "in the Staff Action Logs" | `[art]:206` to `:208` | No (CM-NTF-002 and CM-TRU-003 are `core`). It bears on CM-PAY-001's reading, like item 9. |
| 18 | Additional Resources: 3D Secure, Enabling Stored Payment Methods, Introduction to Alternative Payment Methods, Manually Capturing Transactions (Authorize Only), Multi-Storefront Payment Methods, Optimized One-Page Checkout, Recurring Billing, Using Multiple Currencies, and two bigcommerce.com pages | `[art]:209` to `:219` | "Recurring Billing", a help page's title (`shows`), bears on CM-SEL-001 with item 2. The rest bear on held cells. |
| 19 | The Help Center's navigation (Checkout and Payments: Recurring Billing, Stored Credit Cards, Gift Certificates, Gift Wrapping, Order-level Fees, Persistent Cart and others) | `[art]:23` to `:64` | Outside this structure: it is the page's frame, not the article. No BigCommerce structure holds the help tree (`structures/REGISTER.tsv` lists eight structures, none of them it). |

## The notes' claims for payment-gateways

| Claim | Verdict | Why |
| --- | --- | --- |
| "payment-gateways (25 to 81)" | true | **Fact:** entries 25 to 81 of `show --batch BC-1` are the structure's 57 items. |
| "Couldn't tell" 1: three readings (`shows`, `outside`, `core`), to be settled by a ruling | ruled: `core` for tables 1 and 3 | B-extent's `core` applies: the article calls the rows the platform's integrations. The notes' "`core`: the article calls them 'BigCommerce gateway integrations'" was the right reading. |
| "Each gateway is its slot filler and each feature mark is a quality" | fillers: true; qualities: true by rule 5 | The `Recurring Payments` mark is also CM-SEL-001's: 15 missing lines. |
| "The same rule applied gives: the offline methods ... and the BigCommerce Payments row (32): core" | offline methods: true; BigCommerce Payments: refuted | The brand names neither maker nor built-in feature, and CM-PAY-002's cell reads its like (BC-S-0148) as `shows`. |
| "the 'app payment processors' (48 to 54): extension-point, as apps" | true | `[art]:111`, and `[src]`'s App Marketplace links. |
| "One difference with the existing cell: CM-PAY-002's cell reads a similar row, BC-S-0148, as shows." | true | **Fact:** the cell's evidence row BC-S-0148 is `shows`. The line should have followed it. |
| "Couldn't tell" 2: the entries don't say BNPL or cryptocurrency; "CM-PAY-015's cell reads them that way by their names" | true | True for Affirm, Afterpay, Clearpay and Klarna. The cell names neither Sezzle nor Zip. M2. |
| "Amazon Pay ... the article itself calls it one of the 'leading digital wallets'" | true; supports wrong | `[art]:74`. `[art]:166` names its admin section, so `core`. |
| "PayPal (39) has a second line on CM-PAY-013" | can't tell | Which PayPal the row is isn't stated. |
| payment-gateways listed among "Structures whose items and source disagree": "The items hold the tables only", with five kinds of prose left out | partly true | **Facts:** the items don't disagree with the source. All 57 equal `[src]`, and each table is verbatim in `001.html`; they leave things out. The list misses the feature definitions (item 2, a cell change), the funds FAQ (12), Paysafe (15), Accelerated Checkout (11), the notifications and Staff Action Logs (17), the APMs (8) and the links (1). |
| "That prose is CM-PLN-003's, CM-PAY-012's and CM-PAY-008's to read." | partly | The Check footnote names B2B Edition: CM-B2B-001's, and CM-PAY-008's only if a PO method is read as payment terms. |
| Problem 1: "The brief's two rules give different answers ... I followed the help-page rule" | the conflict is true; the answer is neither rule | B-extent's `core`. |
| Problem 3: the leads drop a word's first letter ("ayPal", "igCommerce") | fixed since | **Facts:** fixed at `ff50bbee`; no such fragment in the current leads. Not checked against the old output. |
| "Where the entries differ from what the model's cells say": nothing from payment-gateways; "Cells that were none-held and gain a placement": five, none from here | incomplete | **CM-SEL-001's BigCommerce cell is none-held**, and these entries hold its statement 15 times. Line 62's `core` differs from CM-PAY-002's reading of BC-S-0148, which the notes say only under "couldn't tell". |

**No new thing comes from this structure,** so there are no searched terms to check.

## Readings resting on a file beyond the item and its source

None in lines 38 to 96. Every quote in their readings is from the text of `001.html` (the file `meta.json` names under `source`), and `001.html` holds it. Line 62's reading rests on the model's CM-PAY-002 cell ("the platform's own payment service as its cell reads it"). H-held.md lets the agent read the cell, but another statement's reading can't give this entry its supports; fix 3 covers that. No file outside H-held.md's rule 1 is cited, so no fix is needed on that ground.

## The leads

`show --candidates` now prints at most three leads. Whether the right capability is among them, by line (`in_leads`):

| Rows | Right cap among the leads |
| --- | --- |
| Table 1, the 22 lines on CM-PAY-011 | 12 |
| Lines 43, 53 and 62 (CM-PAY-012, CM-PAY-013, CM-PAY-002) | 0 of 3 |
| Table 2, the 7 lines | 0 |
| Table 3, the 22 lines | 16 |
| Table 4, the 5 lines | 4 (not CM-PAY-029 for Cash on delivery) |
| **All 59 lines** | **32** |
| The 18 missing lines | 17: CM-SEL-001 15 of 15, CM-PAY-016 2 of 2, CM-B2B-001 0 of 1 |

**Why the leads miss CM-PAY-011 (a reading):**
- On the rows that mark Stored Payment Methods or Recurring Payments, "payment methods" and "recurring payments" fill the three places with CM-PAY-001, CM-SEL-001 and CM-PAY-022.
- A gateway's name sometimes takes a place: "Access" in Access Worldpay leads to CM-API-003, access scopes; "Amazon" leads to CM-CHN-003, marketplaces.
- On table 2, "payment processor" and "processor" lead to CM-PAY-004, CM-TRU-013 (data protection) and CM-TRU-015 (subprocessors), never to CM-PAY-011.
