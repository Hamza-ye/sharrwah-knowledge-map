# S-01: the independent review of its outcome, and what was done with each finding

**What this file is:** the record of the second independent review of S-01, run on 26 October 2026 after Decision 1 was answered. It reviewed `reports/S-01-review.md` and `register.tsv` at [commit `2d014cf`](https://github.com/Hamza-ye/sharrwah-knowledge-map/tree/2d014cf9a7e0ee1f76214f166d8f83b8ff140de0). The reviewer wrote neither, and was asked to refute them against their sources ([`PLAN.md`, section 3](../../../PLAN.md#3-who-does-what)). It used 28 tool calls and 0.27 million tokens.

**The result:**
- **71 claims checked against their sources.**
  - 49 held as stated.
  - 6 held only once a dropped scope or date was put back.
  - 16 didn't hold.
- **40 findings.** I checked each against its source before applying it. All 40 held, and each is applied, in the pack, in the register, or in Decision 1's page.

| # | Finding | Severity | Held? | Done |
| --- | --- | --- | --- | --- |
| 1 | S01-SH-048 doesn't show sellers' own provider accounts | must | yes | Replaced by Shopify's configuring-providers page, L32 |
| 2 | S01-SH-022 is a verification hold, quoted without its condition | should | yes | Replaced by S01-SH-006 and S01-SH-010 |
| 3 | "Money Shopify holds" contradicts B: its processors hold | should | yes | "held through Shopify Payments, by its processors" |
| 4 | S01-ZD-080 is about Emkan's pay-later; "لديهم" is ambiguous | should | yes | Replaced by S01-ZD-109 and S01-ZD-077 |
| 5 | Not every reference runs its own service beside outside providers: Zid allows only Tabby and Tamara; Shopify not Stripe | should | yes | Narrowed |
| 6 | BigCommerce Payments is under beta terms (S01-BC-059) | should | yes | Marked as beta |
| 7 | S01-WC-109 is an interest clause | optional | yes | Replaced by S01-WC-120 |
| 8 | Scopes dropped (S01-SA-056, -101, -098, -041) | optional | yes | Scopes stated |
| 9 | Coexistence letters written beside option letters | should | yes | E1's evidence restated; the letters are no longer mixed |
| 10 | Shopify's fees quoted without "If you don't activate Shopify Payments" | must | yes | Corrected in the pack, the register (D1.2, E3) and Decision 1's page |
| 11 | E4 tied to Decision 11, which is about returning held funds | must | yes | E4 re-anchored to the refund concerns and the schemas |
| 12 | Salla's withholding is for dropshipping apps only | should | yes | Scope stated |
| 13 | Facts linked to live pages, not held copies | should | yes | Each now names its held copy at a commit, with its line |
| 14 | YA-26 says a ban was reversed, the opposite of what was cited; YA-217 is one wallet's licence, of 2022 | must | yes | YA-26 and YA-217 dropped; YK-124 (corrected) and Cash Pay's Sana'a address cited; the area point marked as a reading |
| 15 | The A row put both areas in one sentence | should | yes | Each area in its caution's words |
| 16 | "A licence in each area" and "out of reach today anyway" | should | yes | The first marked as the pilot's reading; the second replaced by an assumption |
| 17 | YK-515 without its date, or that the minimum can change | should | yes | Both added |
| 18 | "International processors: no" generalised from one | should | yes | "Not shown directly", with YA-62's full state |
| 19 | "What C needs exists there" against the rows' "in part" and "unknown" | should | yes | Stated per way to pay |
| 20 | Yemen facts not checked against their quotes | should | yes | Checked tonight, with dates: YK-203, YK-161, YA-131, YA-107 |
| 21 | A, B and C verdicts given as facts | should | yes | Marked as readings |
| 22 | "whichever provider took it" given as fact | should | yes | Restated from the schema's own fields |
| 23 | Readings and assumptions unmarked in the summary, E2 and section 4 | should | yes | Marked |
| 24 | "That one difference carries others" given as fact | should | yes | Marked as a reading |
| 25 | E4 as worded closed store credit and manual refunds | should | yes | E4: whoever holds the money, or store credit (RefundMethodInput, line 2820) |
| 26 | The cash-on-delivery and financing rows lacked default 2's caveat | should | yes | Caveat added |
| 27 | B may need the platform's own registration (S01-SH-105) | should | yes | Added to B's needs; I3 widened to B |
| 28 | Missing: dropshipping withholding, marketplace channels, a seller money account | should | yes | Rows added; I5 corrected |
| 29 | Where provider balances sit under C | optional | yes | E2: read from the provider; no ledger kept |
| 30 | Refund concerns not cited | should | yes | Cited for E4 |
| 31 | Buyer-side balances (store credit, customer wallets) | should | yes | Row added; I8 |
| 32 | Platform billing that collects and pays out partners' money | should | yes | E3's trade-off and I8 |
| 33 | Platform financial products (Balance, Credit, Capital) | optional | yes | Balance and Capital rows |
| 34 | Others: label costs, Salla's contract, a partner unavailable, Mahally, WooPayments' KYC | optional | yes | Partner-unavailable risk added; I4 and I5 cite them |
| 35 | E1 and E2 put to the founder as a veto, though building ahead is the founder's | must | yes | Now a decision for the founder, with options and a recommendation |
| 36 | Yemen named as a driver of Decision 1, against "nothing in the row shaped it" | must | yes | R4 removed from Decision 1's drivers; R4 is what the Yemen row tests |
| 37 | The defaults' scope framed inconsistently | should | yes | The recorded answer is at launch; only default 2's "never" is put to the founder |
| 38 | D12 cited the Yemen marks, a derived document | should | yes | D12 cites S01-SH-023, S01-WC-112 and S01-SH-135 |
| 39 | R3 marked as a decision in force; it is the plan's rule | should | yes | Status corrected |
| 40 | Minor wordings; "a script checked" with no script | optional | yes | Fixed; `method/check_register.py` added |

**Found by me while applying them:**
- **The courier behind cash on delivery** (YK-203). Its page doesn't state its area, and says connecting an online store is still to come. The pack now leads with a store in Sana'a that takes cash on delivery (YE-C536), and investigation I7 asks which couriers collect for online sellers, and where. *Corrected after the quote check, below:* I had first written that the page doesn't name its country. Its description says "في اليمن" [in Yemen].
- **Shopify Capital.** Shopify offers it to sellers on approved outside providers too, so financing repaid from sales may not need A or B. The pack's row was too strong, and is corrected.

**Found by the quote check, after:** a script, [`method/check_report.py`](../../../method/check_report.py), looked up every quote in the pack in the line its citation names. At first, 4 of 38 didn't match. Each is fixed, and all 47 quotes in the pack now match:
- **Shopify's provider page** (finding 1's replacement) was cited at line 30. The quote is on line 32. Decision 1's page and the register quote both lines 30 and 32, so they now cite both.
- **YK-203's quote** cited only the Yemen study's row, which doesn't hold it. It now also cites the held page, line 141. Tracing it showed my own finding above was half wrong, and it is corrected.
- **Shopify Capital's two quotes** cited the concern's row, SH-C-091. They now cite its statements, lines 1818 and 1820. Tracing them showed that [G2's page](../../../reports/G2.md) and [the subject list](../subjects.tsv) still put all financing with A or B. Zid's financing is repaid by deduction from sales through Zid Pay (ZD-C-023), so it stays there. Shopify Capital's concerns move to what's left to the build.
- **Four quotes had only a live link or a description.** Each now links its held line: Salla's wallet (record 1240), the pilot's currency recommendation, your recorded answer, and Shopify's fee condition.
