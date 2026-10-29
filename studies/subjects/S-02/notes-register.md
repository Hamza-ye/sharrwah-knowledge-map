# S-02, the register's draft: notes (REG-1)

**What this file is:** the drafting agent's notes on `register.tsv` and `decisions.md`, under `briefs/D-register.md`: the calls I made, and the problems I found with the brief or the evidence. Each call is mine, for the coordinator's check and the review.

## The register's shape

The register has 43 rows. There were 41 at the first draft; the second pass added S02-D8 and the third added S02-D9:
- 11 drivers (S02-R1 to S02-R11);
- 9 founder decisions, all within the brief's four per root decision:
  - RD1 has 4: D1 to D3, and D8 from a product gap;
  - RD2 has 2: D4 and D5;
  - RD3 has 3: D6, D7, and D9 from a product gap;
- 8 moved rows (S02-M1 to S02-M8), one for each of S-03, S-04, S-05, S-07, S-08, S-09, S-10 and S-11;
- 10 follows-by-rule rows (S02-F1 to S02-F10). RD2 has no key bound per market and none kept open, so it has two such rows;
- 5 engineering constraints (S02-E1 to S02-E5).

Of the 142 founder items:
- 85 go to the seven decisions;
- 57 go to the moved rows.

Some items sit in a decision of another root decision: see call 1.

Read per row: D1 has 6, D2 7, D3 10, D4 16, D5 8, D6 34 and D7 4; M1 has 9, M2 17, M3 5, M4 19, M5 1, M6 1, M7 2 and M8 3.

## Calls I made

1. **Grouping by the question the founder answers.** Most items are grouped within their own root decision. A few went to the decision whose question they ask:
   - **RD3's "store's own country" keys** go to D3, since they ask what the seller's country decides: S02-VP-41, S02-VP-55 and S02-VP-57.
   - **RD3's keys for channels, points of sale and customer groups "outside its markets"** go to D4, since whether those are kinds of market is D4's question: S02-VP-47|a channel, S02-VP-47|a location, S02-VP-49|a group of customers, S02-VP-67|a channel and S02-VP-68|a location.
   - **S02-VP-73** (placing a buyer in a market; which customers may enter one) goes to D5.
   - **S02-VP-85** (a country per market, shown as the store's) goes to D1. D1 answers it as a display value only, held under D6.
   - **S02-VP-49|the buyer's country** (a price per country within a market) goes to D7.
   - **S02-VP-55|the buyer's country** (checkout fields) goes to D6, as a narrower key of the same interface.
2. **What stands apart:**
   - **D1 stands apart from D3.** Changing D1 later is a redesign, since the data model changes; changing D3 is one module once the interface exists.
   - **D7 stands apart from D6.** Its later change reaches every money record, and S-09's decision follows from it.
   - **Payment methods, tax and shipping per market stay in D6.** S-04, S-05 and S-10 decide their values. Their holding is D6's mechanism, and changing that later costs a setting once D6's interface exists.
3. **Moved rows.**
   - I kept phase C's own subject label for every item whose wording carries one.
   - I assigned the unlabelled items by the brief's list:
     - S02-VP-11, S02-VP-12 and S02-VP-13 go to S-04;
     - S02-VP-14 goes to S-11;
     - S02-VP-15 goes to S-05;
     - S02-VP-19 goes to S-08;
     - S02-VP-05's assessors and government bodies, S02-VP-10, and S02-VP-07's two verification keys go to S-07.
   - **S02-VP-81** (the platform setting a store's status, by default for a new store or by closing a store under its terms) goes to S-03. My reading is that closing a store is a term of the merchant's contract, while the status itself is held under D6. A reviewer may prefer to keep it in S-02.
4. **S02-VP-07|a billing currency supported for the billing address's country** stays with S-09, phase C's label, though S-11 meets it through S02-VP-14 (the currency of Sharrwah's fees). The two subjects should read both rows.
5. **Columns.**
   - For moved rows, what S-02 settles is in `recommendation`, not `answer`, because it rests on D1 and D3, which are the founder's to accept.
   - `answer` is empty on every decision and moved row. It holds text only on drivers (the founder's decisions in force) and on follows-by-rule rows, as S-01's register does.
6. **Follows-by-rule rows list their keys in `vp_id`,** as `vp_id|key`. The brief names no column for them, and `method/register_items.py` counts any name in `answers_items` that isn't a founder item as an error.
7. **S02-E5 is a reading.** It says which market carries S-01's holding arrangement: the seller's own country, through the business entity that takes the payment.
   - The frame asks S-02 to say this, but no founder item covers it.
   - So it was drafted as an engineering constraint. Since the second pass (the coordinator's ruling), its status is "for the founder: a reading of their decision of 26 October, to confirm", and it names the other reading.
8. **No market in a recommendation.** Recommendations name platforms, never a market or a market's facts. Market names appear only as phase C's keys, in `answers_items` and in the follows rows' `vp_id`, as data.
9. **Kinds and causes.** The kinds in `alternatives` come from `variants.tsv`, for the variants each option cites. The causes come from `c/<RD>/answers.tsv`.

## Problems with the brief or the evidence

1. **Section name.** The brief cites the frame's "How S-02 relates to other subjects"; the frame calls that section "Where it meets other subjects".
2. **Subjects the frame doesn't name.** The frame's section names S-01, S-03, S-04, S-05, S-07, S-09 and S-10, but not S-08 (data) or S-11 (what Sharrwah charges). The brief adds both, and I followed the brief.
3. **A commonality with no platform.** S02-VP-26|a group of customers is recorded as a commonality with an empty `gives` (`c/RD2/answers.tsv`). S02-F5 lists it as phase C has it. A reviewer should check whether it is a common absence.
4. **One key, two things.** S02-VP-06|the platform joins two different things:
   - Shopify's support changing a store's billing address or default entity on request (S02-V-064, S02-V-269);
   - WooCommerce's code migrating a stored location's state code (S02-V-276).

   My first draft of D2 read both as staff acting under a contract; I corrected it, and D2 now cites them apart.
5. **D6's size.** D6 answers 34 items, which ask one question of 18 settings. Apart from currency (D7), I found no setting among them whose later change costs more in kind once the interface exists.
6. **Inconsistent labels.** Phase C labelled some moved items with their subject and not others, so call 3 is mine. The review should check it.
7. **Length.** After the third pass, `decisions.md` is 3,450 words over 176 lines, written as prose to stay within six pages. Longer drafts of the third pass, at 3,800, 3,700 and 3,500 words, were rewritten.

## Second pass, 29 October

The second pass applied the coordinator's rulings on the draft, the product gaps from the Yemen row, and four fixes from the scenario walk. I first checked that `register.tsv`, `decisions.md` and this file were unchanged since 3275770b; they were.

### The rulings

1. **Payouts.** Sharrwah sets no payout currency: each provider pays out on its own terms (S02-R4).
   - S02-D7 and S02-E4, and `decisions.md`'s D7 and E4, now give the store's own currency to gift cards and the store's own reports only.
   - S02-E2 names which payment providers a seller may connect (S-04's), each paying out on its own terms. S02-M2 says Sharrwah holds no payout term.
   - S02-BC-224 is now labelled as a provider's own term where it is cited (S02-D7, S02-M2). I dropped it from S02-E4, which it no longer supports.
   - S02-SH-183 and S02-SH-035 are cited in S02-D7 as providers' own terms.
2. **S02-E5.** The reading stays, and it now names the other reading: the markets a store sells into, as Shopify assigns entities to markets (S02-SH-280). Its status is "for the founder: a reading of their decision of 26 October, to confirm". `decisions.md` says the same.

### The product gaps, checked against the references

**Where I read them:**
- `yemen-row.tsv`, the `product_gap` column: gap 1 at line 14, gap 2 at line 13, gap 3 at line 35.
- In `notes-yemen-row.md`, I read only lines 23 to 26 and 77 to 80. The file has no section headed "The product gaps". The gaps are a bold paragraph under "How to read the row" (lines 23 to 26), and its third problem (lines 77 to 80) says where the references would show them.

**Gaps 1 and 2: a seller's area within a country, and a move between such areas.**
- **For payment services, the coordinator's finding holds.** Payment rules key below the country only on places with country codes of their own: S02-SH-027, S02-SH-583, S02-SH-642, S02-WC-008, S02-WC-009, S02-WC-010, S02-WC-042, S02-WC-051 and S02-WC-052. The same holds for two features (S02-SH-026, S02-SH-484).
- **For a seller's rules in general, it does not.** Some rules key on areas that have no country code of their own:
  - Shopify keys the tax on its own fee on the seller's province (S02-SH-513, S02-VP-15).
  - Shopify keys the store's own taxes on its province or state (S02-SH-515, S02-SH-931, S02-VP-16), and WooCommerce Tax on the store address's state-level location (S02-WC-118).
  - Shopify keys a feature's eligibility on whether the seller's fulfilment locations sit in one province, or in one part of a country and not both (S02-SH-485, S02-SH-486, S02-VP-17).
- Phase C keyed these statements by country, so the area doesn't show in its keys.
- **So the references meet the key itself,** an area within a country, for tax and one feature. None keys payment services, the currency or the exchange rate on such an area, and none runs a move's checks when it changes.
- **The result:** one founder decision, S02-D8, which is RD1's fourth. Its options include not providing for the need. Its recommendation rests on the references' own area keys, not on the market the need came from.

**Gap 3: one currency code over two currency areas. I read the references as meeting it, which was wrong (see the third pass).**
- Shopify holds an exchange rate per market, set manually or automatically (S02-SH-568, S02-SH-531). Salla holds a scope-specific exchange rate (S02-SA-302, shipped).
- Both draw markets for an area within a country (S02-SH-103, S02-SA-051).
- Zid and WooCommerce hold a rate per currency instead (S02-ZD-020, S02-WC-027).
- **Where it follows:** into S02-D7, which adds option (e) and holds the rate per market, kept on each order, and into S02-D4.
- **What moved:** whether an amount's currency names its area beyond its code, in money records. That went to S-09, in S02-M6, which says what S-02 holds for it. There is no new decision.

### The scenario walk's four fixes

1. **S02-E2 against S02-D1.** S02-E2 now takes the order or market it answers for, keyed on the business serving it, and each order records the business that served it (S02-SH-280, S02-SH-147). Each rule says whether it reads the store's main business or the order's.
   - S02-D1's cost (a second business is a setting) holds only with that order record. Its `cost_later` now says so.
   - S02-D3's cost (one module) holds with that record, and its `cost_later` says so too.
2. **S02-D3's closes** is narrowed to a second copy of the seller's own country. It now names what it does not close:
   - where stock is held (S02-ZD-120, S-10);
   - each owner's residence for documents (S02-SA-134, S-07);
   - a provider account's country (S02-BC-128, S-04);
   - an area within the country (S02-D8).
3. **S02-D6 and S02-E1** now state the rule per kind of setting:
   - a one-value setting takes the most specific value;
   - a set may combine across the markets a buyer matches (S02-SH-109);
   - a product narrows a set.

   Under that rule, "nothing a reference shows is closed" holds. I changed S02-D5 to match: a buyer matches at most one market of each kind, not one market. The walk didn't name S02-D5, but without the change it would contradict S02-E1.
4. **Payouts in S02-E4 and S02-D7:** as ruling 1.

I also aligned the questions of S02-D3 and S02-D7 with the changed recommendations.

### Rows changed, for the walk's re-run

| Row | What changed |
| --- | --- |
| S02-D1 | cost_later |
| S02-D3 | question, recommendation, closes, cost_later, evidence |
| S02-D5 | question, recommendation |
| S02-D6 | recommendation, closes, evidence |
| S02-D7 | question, alternatives, recommendation, trade_off, evidence |
| S02-D8 | new |
| S02-M2 | recommendation, evidence |
| S02-M6 | vp_id, question, recommendation, depends_on, evidence |
| S02-E1 | recommendation, evidence |
| S02-E2 | recommendation, evidence |
| S02-E4 | recommendation, evidence |
| S02-E5 | recommendation, status |

No other row changed.

### Checks after the second pass

- `register_items.py`: 142 founder items; 0 unanswered, 0 answered twice, 0 names unknown.
- `check_register.py`: 770 citations checked, 0 problems.
- A scan of every row's question, recommendation, closes, trade-off and cost found no market's name.

## Third pass, 29 October

The third pass answered the independent review (`review.md`, at 60cfa1e4). I first checked that the three files were unchanged since f4d3d4c6; they were. Then I read findings 1 to 19 and fixed:
- the five must-fix findings that are mine: #1, #2, #3, #4 and #7;
- every optional finding that was plainly right: #8, #9, #10, #11, #12, #14, #15, #16, #17 and #18;
- the six conditions from the walk's re-run.

#5, #6, #13 and #19 are the walk's and the Yemen row's.

### The must-fix findings

1. **#1, gap 3 isn't met.** My second pass was wrong.
   - I put Shopify's rate per market (S02-SH-568) together with its markets for an area within a country, without S02-SH-104: such a market inherits its currency from its parent (early access).
   - I read Salla's order field S02-SA-302 as a rate per market. S02-SA-103 says Salla converts at the currency's rate.
   - **The fix:** S02-D9 is a new founder decision in "Needs no reference meets", with option (a) not providing for the need. S02-D7 (option (e), its recommendation and evidence) and S02-M6 now agree with it.
   - S-09 still decides what identifies a currency in money records. The condition is stated in S02-D9, S02-M6 and the page: amounts that refer to a currency record keep a later currency area under one code to one module, and a bare code in every amount makes it a redesign.
2. **#2, S02-D4.** Its closes now covers only channels and points of sale, which a market kind reaches. A group of customers isn't closed. No market kind defines one (S02-SH-N03; S02-VP-26|a group of customers, S02-F5), so it stays a dimension beside markets that a setting such as a price may key on (S02-BC-020). S02-E1 names it as a key beside the market.
3. **#3, S02-D8.**
   - Only (b), tax by area, rests on the references.
   - The extension to payment services, the currency, the rate and a move's checks comes only from the product gap.
   - The generality rule over (a) to (c) is gone: (c) is a design beyond the references, with no outside source read.
   - The page's opening now limits "from the five references alone" to D1 to D7. Its "Needs no reference meets" section says each need comes from the Yemen row alone, and that providing for it is room kept for the founder to weigh.
4. **#4, S02-E4 and S02-D7.** The store's currency is the default for gift cards, and a gift card in a market's currency is left open. S02-SH-189 is one vendor's limit, not a reason.
5. **#7, S02-D5.** Within one kind, nesting orders the overlap (S02-SH-080, S02-SH-131, S02-SH-125). S02-D5 closes only two markets of one kind that partly overlap, neither inside the other, and marks that as a reading.

### The optional findings I applied

- **#8:** S02-D2's rule and closes are narrowed to what S02-SH-596, S02-SH-250 and S02-WC-182 say.
- **#9:** S02-F2 and the page now say "whether one contracting company serves every store there", which S-03 decides.
- **#10:** S02-D6's counts, checked against `c/RD3/answers.tsv`: BigCommerce 16, Salla 15, Shopify 12, Zid 3, WooCommerce 1.
- **#11:** in S02-E1 and S02-D6, combining payment methods and shipping options is marked as engineering's own choice, a reading. Only catalogs are Shopify's.
- **#12:** S02-D8's cost_later is now one module, given S02-E2 and a dated address. What can't be recovered later is a past record's area. It is a redesign only where S02-E2 or S02-D1 is declined.
- **#14:** S02-D1 answers the seat item: the seat is the business record's address, not a setting of its own. The page now says "a location set on a map or by hand".
- **#15:** S02-D5's closes separates the fact from the reading.
- **#16:** S02-D7's cost is split by part, with its conditions shown on the page.
- **#17:** S02-D7's option (c) no longer counts Shopify. S02-SH-179 is cited as a reading, under S02-VP-42.
- **#18:** the opening count now says 85 asked here and 57 moved.

### The walk's conditions

- **S02-E1:** a limit the platform or a law sets applies after values resolve and sets combine (S02-SA-283).
- **S02-D4:** matching takes the buyer's context, not only the country.
- **S02-E3:** the main market's places may change (S02-SH-128).
- **S02-D8:** the area is held at two levels from the start, the business record's address and the fulfilment locations (S-10's), because S02-SH-485 and S02-SH-486 key on fulfilment locations.
- **S02-E2:** if S02-D8 is taken, it takes an area beside the country. A rule about the business itself, before any order, reads the store's main business or the business named.
- **S02-D5:** precedence between kinds is stated only for business-customer, retail and region markets (S02-SH-109). For the other kinds it is unknown and kept open.

### Rows changed in the third pass, for the walk's and the Yemen row's re-run

These are the changes against f4d3d4c6.

| Row | What changed |
| --- | --- |
| S02-D1 | recommendation |
| S02-D2 | recommendation, closes |
| S02-D4 | alternatives, recommendation, closes |
| S02-D5 | question, recommendation, closes, evidence |
| S02-D6 | alternatives, recommendation |
| S02-D7 | alternatives, recommendation, cost_later, evidence |
| S02-D8 | recommendation, closes, cost_later, evidence |
| S02-D9 | new |
| S02-M6 | question, recommendation, depends_on, evidence |
| S02-F2 | answer |
| S02-E1 | recommendation, depends_on, evidence |
| S02-E2 | recommendation |
| S02-E3 | recommendation |
| S02-E4 | recommendation, evidence |

No other row changed.

### Checks after the third pass

- `register_items.py`: 142 founder items; 0 unanswered, 0 answered twice, 0 names unknown.
- `check_register.py`: 790 citations checked, 0 problems.
- A scan of every row's question, recommendation, closes, trade-off and cost found no market's name. S02-D8 and S02-D9 say where their need comes from without naming it: "the product gap this row's evidence cites". The page names the Yemen row as their source, as the coordinator asked.

## Fourth pass, 29 October

This pass answered the review's re-check (`review.md`, "Re-check after the fixes", at 54f2d448), and read the designs in `designs.tsv` (at 99d8e60b) without their note column. I first checked that the three files were unchanged since 47847720; they were.

### The changes

1. **#20, S02-D9.** Under S02-D7, S02-E1, S02-D4 and S02-D5, two markets for areas of one country already sell at two rates under one code. What S02-D9 adds is the area in the currency itself, so that prices, stored amounts and reports can tell the areas apart by currency. I rewrote its question, options, recommendation and cost to say that:
   - (a) is one rate per code;
   - (b) is what S02-D7 gives;
   - (c) names the area.

   S02-M6 stays reconciled: S-09 decides how money records identify a currency.
2. **#21, S02-D8 and S02-D9 weighed against `designs.tsv`.** Each row I used is cited in the row's `evidence` by source and locator, and the claim that no outside source was read is gone. The sources change both recommendations, from (c) as room kept to "(b) now, with room kept for (c)".
   - **S02-D8.**
     - Stripe keys a dated tax registration on a state (003:255-259), which supports (b).
     - Subdivision codes are added, deprecated, aliased and reused (Unicode TR35, 001:1362, 1364). So the area is held as a stable identifier mapped to the published code.
     - Levels below the country differ by country (OpenStreetMap, 004:46). So the level is named per country.
     - A postal address's area is optional and at the postal level (Google's PostalAddress, 002:83-89). So the area isn't only read from the address.
     - Fowler's Temporal Property supports the dated area (005:21).
     - **Where they cut against (c):** no design keys payment services or currency on an area. Unicode keys a currency default on one only rarely (001:1091). Fowler finds dating a property later not hard in code (005:37), so keeping the dated area now rests on past records alone.
   - **S02-D9.**
     - The standards and platforms read identify a currency by its code alone: Unicode TR35 (001:1559), Java's Currency (008:36), Stripe's PaymentIntent (009:249) and ISO 4217's lists (006:86, 122). That cuts against building (c) now, and means any area would map back to a bare code at a provider's boundary.
     - TigerBeetle holds each amount's currency as an application-defined number, and makes a changed unit a new record (010:30, 113). That supports the room: amounts that refer to a currency record, which is S-09's decision.
     - Fowler's Money (007:11) supports a currency on every amount, which all the options share.
3. **#22, S02-D7 on the page:** only Salla, Zid and WooCommerce are named as working from the currency's rate. BigCommerce shows none.
4. **#16, S02-D7:** the page's answer line now takes its three parts apart, each with its cost: two amounts on every record (a redesign), where the rate is held (one module), and which markets carry their own currency (a setting). The register's question names the three parts.
5. **#19, S02-E4:** the store's own currency may change, as the seller's setting. Records made before a change keep their amounts in the currency of their day, with the market and rate used, and aren't converted.

### Rows changed in the fourth pass, against 47847720

| Row | What changed |
| --- | --- |
| S02-D7 | question |
| S02-D8 | recommendation, trade_off, cost_later, evidence |
| S02-D9 | question, alternatives, recommendation, trade_off, closes, depends_on, evidence |
| S02-M6 | recommendation |
| S02-E4 | recommendation |

No other row changed. S02-D9's options keep their letters, but (b) now means what S02-D7 gives. The Yemen row's and the walk's lines for S02-D9 need re-reading against it.

### Checks after the fourth pass

- `register_items.py`: 142 founder items; 0 unanswered, 0 answered twice, 0 names unknown.
- `check_register.py`: 803 citations checked, 0 problems, including every `designs.tsv` locator cited.
- A scan of every row's question, recommendation, closes, trade-off and cost found no market's name.
- `decisions.md` is 3,688 words over 180 lines, with eleven answer lines: one per decision, and three for S02-D7's parts. That is about six pages: the sources weighed in S02-D8 and S02-D9, and S02-D7's three answer lines, added about 300 words, and further cuts would drop options, sources or costs.

## Fifth pass, 29 October

This pass made the review's two optional wording fixes, from "Last check". I first checked that the three files were unchanged since fe86177f; they were.

- **#23, S02-D9:** "ISO 4217's lists, one code per currency" is now marked as a reading of the maintenance agency's page, in the register and on the page, since the quoted SIX page doesn't say it. The fourth pass's notes above list it among what the sources show; this corrects that. What the sources do show is that Unicode, Java and Stripe identify a currency by its code alone.
- **#24, S02-D8:** the question now holds the area "as a dated field of the business record", not "read from the business record's address". The page's question says the same, matching the recommendation.

Rows changed: S02-D8 (question) and S02-D9 (recommendation). No other row changed.
