# S-02, the Yemen row (YR-1): notes

**What this is:** the notes to `yemen-row.tsv`, S-02's Yemen row (`PLAN.md` section 6, step 6), made from the brief `briefs/E-yemen-row.md`. For each option of S02-D1 to S02-D7, the row says what the option needs in Yemen today and whether that exists. It decides nothing, and it is no reason for a recommendation: Yemen is one of the founder's markets, and its circumstances may change (`founder-decisions.tsv`, 28 October).

## How to read the row

- **`needs`** is a reading of what the option itself requires. "Nothing particular in any market" marks an option that only chooses how the platform is modelled.
- **`exists`, `evidence` and `as_of`** come from Stage 1's records. Each fact was checked against its quote in `citations.tsv`, read with its date and with `corrections.md`. Six sources were also opened at the cited lines: exrye.com (Aden's rates), wise.com, ACAPS's YETI page, Arab News, the World Bank's report (lines 6655-6690) and the IGC report (lines 1525-1550).
- **Cases (`YC`)** are cited only where an option depends on a condition that changes (the split's rules for S02-D3, the notes and rates for S02-D7), and only cases whose quotes were checked.
- **`note`** holds facts, each cited in `evidence`, and readings, each marked "a reading".
- **Split rows.** An option has two or three rows where its needs have different answers: S02-D4 (a), S02-D6 (d) and S02-D7 (c). S02-D2's gap applies to every option, so it has a row of its own.

**What the row finds.** 39 rows: 28 `yes`, 6 `no`, 5 `unknown`.
- **`no`:**
  - S02-D3 (a) to (d), the rules keyed on the seller's country;
  - S02-D2's moves;
  - S02-D7 (c) with one rate per currency pair.
- **`unknown`:**
  - the bounds of an area whose conditions differ (S02-D4 (a) and (c), S02-D5 (b));
  - the address form (S02-D6 (d));
  - a rate feed a platform can read (S02-D7 (c)).

**The product gaps,** written without the market's name. There are three, from two roots:
1. **The seller's area within a country** (S02-D3 (a), and as (a) for (b) to (d)). Where one country's areas answer to different authorities for payment services, the currency and the exchange rate, a rule keyed on the seller's country gives one answer for areas whose answers differ.
2. **A move between such areas** (S02-D2, every option). The move changes what a seller answers to, though its country stays the same. Its root is the same as gap 1's.
3. **One currency code covering two currency areas** (S02-D7 (a) and (c); as (a) for S02-D1 (e) and S02-D3 (f)). The two areas have notes one of them doesn't accept, and rates about three to one apart. A currency held by its code, a rate held per currency pair, and an amount stored with its code can't tell the areas apart. A rate quoted for the code (an international provider's) matches neither area.

## Facts that were hard to read

1. **YA-44.**
   - The axis's own state map puts YE-D435 and YE-D436 at the government's area. `corrections.md` moves them to place not stated, so the row cites them there.
   - It uses only these: the Sana'a bank's licence in the Houthis' area (YE-A005, YE-A088), and nationwide institutions answering to both banks (YE-D423).
2. **YA-102.**
   - Following `corrections.md`'s caution, the row states the rule per area: the Aden bank's rules for payment-service providers (YE-D113), and non-banks made eligible for e-rial services on the Sana'a side (YE-E193).
   - The `today` part "banks only @ Central Bank of Yemen's area" doesn't say which bank, and is not used.
3. **YK-124, as corrected.**
   - The quote (YE-D521) gives one direction only: Sana'a providers "are not authorized to operate in Aden without investing in separate infrastructures located in the South".
   - Read as two facts: without that infrastructure they may not operate; that they may with it is not stated.
   - The same page finds the two regions' frameworks "similar" (YE-D520). The row carries both.
4. **YA-195 beside YK-124.** Jawali and Yemen Wallet state on their own pages that they reach all governorates or all districts. The records don't settle whether a given wallet reaches buyers in both currency areas, so the row doesn't claim it either way.
5. **YK-452, as corrected.** Its source is a community-written client of Kuraimi's E-Pay, not the provider's documentation. The row uses it only to show an integration that tells currency zones apart, never as the provider's terms.
6. **YE-D423.** "Two currencies are in circulation, though only one is accepted across the country."
   - Read as two facts: one is accepted everywhere; the other is not.
   - The quote doesn't say which. YE-E1307 and YE-E1308 give the new notes barred in the north.
7. **YA-21's places.**
   - The records place the rial-only rule at "Council of Ministers' area" and "Ministry of Justice's area" without saying whose council or ministry. YE-A056's quote says "داخل الجمهورية اليمنية".
   - The row uses the rule as placed, with the government's enforcement (YE-E410). It doesn't say which authority made it.
8. **YA-15.**
   - The government's area's state (all notes legal tender) dates from 2020-02-26.
   - YC-101, "provided for" in 2024, withdraws notes printed before 2016 there. The records don't say whether that took effect, so the row gives both, dated.
9. **YA-01.**
   - exrye.com's Aden page shows two figures under the dollar (lines 44-47) without labels in the lines read. The record reads them as buying and selling, and the row follows it.
   - ACAPS's Sana'a rate is "Unofficial exchange rates sourced from YemenSul, Telegram" (YE-E1306).
10. **YA-07.**
    - Wise's mid-market quote (236.197 rials to the dollar, 2026-10-10) and another provider's all-time high (251, September 2017: YE-E802) match neither area's market rate.
    - The records don't say what such quotes track, and the row doesn't guess.
11. **YK-209 (YE-B102).** "No trading in a shop except by one entered in the register of the shop's district."
    - Read as two facts: one entered may trade in a shop; one not entered may not.
    - Trading with no shop, such as online only, is not addressed.
12. **YA-150.**
    - The 30-day rule is on a page the records place in the Houthis' area (YE-B253, captured 2026-10-10).
    - For the government's area, the records hold only the 1991 law.
13. **YE-F356.** A registered seller invoicing in a foreign currency must show the rial value at "the prevailing exchange rate". The decision took effect in 2002, before the split, and names no currency area.
14. **The Sana'a central bank's pages.** That the capture could not read them from outside Yemen ("connection reset") comes from `unknowns.tsv`, YA-88's read. It has no `YE` id, so the row cites it by that file and axis. The pages were the bank's decisions and circulars, not its rate statement.
15. **YA-169.**
    - Al-Mahra's local authority keeps local sales taxes and 70 percent of customs (2025-11). Areas below the two currency areas may therefore differ too.
    - The row doesn't use this: it bears on who collects revenue, not on a store's settings.
    - The sales tax rate is one for the country in the records: 5 percent, by a law effective 2005-07-18.

## Problems with the brief or the records

1. **The areas have no bounds in the records.**
   - Stage 1's records name the areas by authority or direction: "Houthis' area", "the internationally recognized government's area", "the north", "the south and east". They never list them as governorates or districts, and hold no axis for who holds which place.
   - So the options that need an area's bounds can't be tested (S02-D4 (a) and (c), S02-D5 (b)), and Q2 has no case of the bounds moving.
   - Stage 1's `places.tsv` may say how the records' places nest. The brief doesn't name it, so it wasn't read.
2. **No case varies YK-12,** one currency and one central bank for the whole country. It is a constant, so Q2 holds no case of the split ending. That scenario is outside the row's cases.
3. **Gaps against the references.** Whether a reference meets a product gap couldn't be checked from what the brief names: `register.tsv`'s options alone. These would show it:
   - for gaps 1 and 2, a seller's key below the country: S02-VP-17 and S02-VP-18;
   - for gap 3, a currency or rate held per area or per market: S02-VP-41 and S02-VP-50;

   each in `variation-points.tsv` and `variants.tsv`.
4. **A commonality, not an option.** `register.tsv`'s S02-D2 alternatives end with "the seller changes it in the admin on all five", so it has no row. S02-D4 (b) bundles six variants in one row, since none needs anything particular.
5. **Only checked cases are cited.** YA-01 has 80 cases and YA-03 has 24. The row cites the ones whose quotes were checked; the others were not needed to show that the rate moves.
6. **Cases have no column of their own.** The brief's columns don't include one, so cases are cited in `evidence` and described in `note`.

## After the register's second pass

The register's second pass (`register.tsv` at f4d3d4c6) added two things and reworded two decisions. The row now has 44 rows: 31 `yes`, 7 `no`, 6 `unknown`. The counts above are the first pass's. `method/check_yemen_row.py` passes, with 0 problems and 0 warnings.
- **S02-D8, new.** Four rows:
  - (a) is `no`, as S02-D3 (a);
  - (b) is `yes`, and leaves payment services and the currency keyed on the country;
  - (c) is `yes` for the area read from the address, and `unknown` for the bounds of an authority's area, as S02-D4 (a).
- **S02-D7.**
  - The row that tested one rate per currency pair moved from (c) to (e), the per-currency form, as the options are now worded. It stays `no`. It was given no gap then; that is withdrawn after the third pass (below).
  - A new (e) row holds the rate per market, kept on each order: `yes`.
  - Gap 3 was then read as half met by (e). That reading is withdrawn after the third pass (below).
- **S02-D3.** Its options are unchanged, and its rows still match. Gaps 1 and 2 now say the register takes them up as S02-D8.
- **Problem 3 above is answered in part:** S02-D8 (b) shows references keying tax and a feature on an area, but not payment services or the currency. The reading that option (e)'s rate per market meets gap 3 is withdrawn after the third pass (below).

## After the register's third pass

The independent review (`review.md`, findings 6 and 19) and the register's third pass (`register.tsv` at 47847720) changed the row. It now has 48 rows: 33 `yes`, 8 `no`, 7 `unknown`. `method/check_yemen_row.py` passes, with 0 problems and 0 warnings.
- **Finding 6: gap 3 is not met.** No reference sells two areas of one country under one currency code at two rates. A sub-region market inherits its parent's currency (S02-SH-104), and Salla converts at the currency's rate (S02-SA-103). The register drafts the gap as S02-D9, and the row now points to it:
  - S02-D7 (a)'s gap (line 35) is S02-D9's, in full;
  - S02-D7 (e)'s per-market row (line 40) names Shopify only, and its note says why two areas of one country can't sell at two rates under it;
  - the per-currency row (line 41) adds Salla, and its gap is S02-D9;
  - S02-D1 (e) and S02-D3 (f) point to S02-D9.
- **S02-D9, new.** Four rows:
  - (a) is `no`, as S02-D7 (e)'s per-currency row;
  - (b) is `yes`, and leaves the gap;
  - (c) is `yes` for the currency areas, their notes and rates, and `unknown` for which buyers are in which area, as S02-D4 (a).
- **Finding 19.** S02-D1 (c)'s "from abroad" (line 4) is now marked as an assumption: where the company is based is S-03's, and open.
- **S02-D4 and S02-D5.** S02-D4's options changed only in (d)'s evidence, so its rows still match. S02-D5 (b) now reads as the register words it: "the most specific settings".
