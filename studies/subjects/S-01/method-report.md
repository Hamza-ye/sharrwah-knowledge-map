# S-01 method report: what broke and what changed

**Draft, 17 October 2026.** Written by the coordinator through phase C. It is completed after phase D, the register entry and the independent review (F).

## Where the pilot stands

| Measure | Value |
| --- | --- |
| Statements | 808 |
| Gaps | 68 |
| Variation points | 23 |
| Variants | 653: 616 answers, 35 `gap`, 2 `absent` |
| Quotes | 1,528, all found verbatim |
| Cited web pages | 146, all captured |
| Founder items from phase C | 12 |

## What broke, and what changed

### 1. Claims that something isn't there (phases A and A2)

- **What broke.** Salla's phase A, and its A2 at `medium`, recorded settlement in Kuwait and the UAE as not stated. Help articles held since 10 October state both. The founder found it.
- **Why.** A "searched, not found" named no search, and nothing checked it. A2's brief also limited recording to what fitted the gap, so other findings were dropped.
- **What changed:**
  - **A3,** a new step: an agent that made none of the claims audits every gap and absence (`briefs/A3-absence-audit.md`).
  - **`method/corpus_search.py`** searches every held corpus in every language the platform uses. A "searched, not found" must show it, and the checker enforces that.
  - **A2 and A3** record everything they find on the subject, with the scope its source gives.
  - Salla's A2 was re-run at `high`, under the effort policy's re-run rule.
- **Result.** Over all five platforms, A2 and A3 added 220 statements to phase A's 588, BigCommerce's re-run included. The audits settled 60 claims of absence: 50 confirmed, 7 partly contradicted and 3 contradicted.

### 2. The tools that say what is held

Each of these faults made an agent think something was missing, or readable, when it wasn't. Each is fixed:
- **`method/held_index.py`** counted an empty capture as readable. That gave 42 false "read it instead of routing it to the founder" errors.
- **`corpus_search.py`:**
  - its host rule let `commerce.com` match `woocommerce.com`;
  - English terms matched inside words ("lien" in "client");
  - it didn't read zid.sa's raw pages, where Zid keeps its content;
  - it didn't search the fetch archives (WARC);
  - for an address held twice, it showed the first copy, so an empty capture hid the founder's full one;
  - it didn't search the founder's own saves.
- **The subject checker** made a gap's route an error for as long as the page was held, even once a later phase had read it. A page now counts as read once A2 or A3 names its held copy. An address alone doesn't count, because BigCommerce's first A2 listed the addresses it had been refused.

### 3. Pages behind bot checks

- **What broke.** BigCommerce's Help Center answers automated browsers with HTTP 400, and the briefs forbid getting around a bot check.
- **What changed.** The founder ran the repository's own capture tool on their machine (51 of 52 addresses) and saved the Trust Center by hand.
- **Result.** BigCommerce's A2 was re-run on them. It added 59 statements, and closed 5 gaps in full and 8 in part. One of the new statements contradicts an earlier one: BigCommerce Payments is offered in the UK as well as the US.
- **Still with the founder:** Salla's payment services contract, and Zid's two dashboard pages.

### 4. An audit that missed what a later audit found

- **What broke.** The first audit of BigCommerce's G08 (agency) confirmed it. The second audit, on a gap asking the same question of other pages, found the Master Services Agreement's no-agency clause.
- **What changed.** The coordinator corrected G08's row and said so in its note.
- **Lesson.** Gaps that ask one question of different sources should be audited together.

### 5. Phase B: placing statements under variation points

- **Comparisons.** The second pass compared each answer with another platform's statement where one exists, and 106 rows changed basis.
- **Problems it recorded, still open:**
  - different English words for one thing ("custody" for "holds");
  - a term one platform lists with an empty definition;
  - comparisons that depend on the order statements are placed;
  - partly contradicted gaps;
  - A2 listing statements under variation points whose bullet they don't carry;
  - a scope separator that clashes with scopes containing it.
- **Gaps closed by a general statement.** A2 closed BigCommerce gaps with a general Help Center statement: "You will control and direct funds in your merchant account with your merchant service provider". The coordinator accepted this, because its scope is general and phase C compares by scope.

### 6. Phase C: what counts as the same answer

- **What broke.** The rule for "same" treated the merchant as one party everywhere, but each platform's own name as a different party. So two platforms that each name themselves "differed".
- **What changed.** The merchant, the buyer and the platform itself (its name, payment product or company) are one party on every platform. "Names a law" means a particular law or regulator. Both are marked as the coordinator's own, in the brief and in `PLAN.md` section 11.
- **Result.** The second run changed no cause, letter, rule or founder item. The differences come from third parties only some platforms name (Global-e, BitPay, Tamara, Trendyol), or from gaps.
- **Problems still open:**
  - strict set equality hides shared answers. On VP-16, Salla and Zid share minimums for Saudi Arabia and Kuwait;
  - one coexistence letter per platform can't hold mixed binding;
  - `general_variant` takes one id;
  - "product" in letter C is ambiguous;
  - scopes without a country aren't covered;
  - a single `beta` marker decides VP-13's cause;
  - a gap on either side blocks agreement, which gives three `unknown` causes.

### 7. Running the work

- **The weekly usage limit** stopped every agent from 13 to 17 October. Each one resumed from its own transcript. The two-hourly check-in couldn't act before the reset.
- **A coordinator's ruling worded too broadly.** In Stage 1, a ruling that forecasts are `proposed` took in estimates too, and had to be narrowed.

## To complete

- Phase D, on Stage 1's cases, and what it shows about the method.
- The register entry, and whether the founder can decide from it (G1).
- The independent review's findings.
