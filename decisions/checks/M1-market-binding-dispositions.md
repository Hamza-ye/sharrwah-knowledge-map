# The check of D-001's revision, D-006 and part five: what was done with each finding

This is the coordinator's record of the independent level-3 check of commit `2274d2a` (`M1-market-binding-check.tsv`, 44 findings: 13 hold, 26 fix, 5 open). Each finding was tested against its evidence before it was applied (`METHOD.md` section 6). No finding was rejected.

**The evidence checked first:**
- **Shopify:** "If it's supported in the country where your business is located, then Stripe won't be available for you to activate." And: "If you can't activate Shopify Payments in a supported country … then standalone Stripe isn't available as an alternative" (`HC:payments/third-party-providers/payment-gateway-availability.md:17`, `:19`). Providers are selected "from the list" (`configuring-providers.md:30`).
- **Salla:** "Before you can activate Salla Payments, all three requirements must be met": "Salla Plus, Pro, or Special", completed verification, and "Payments have been enabled for your store by the Salla team." Also: "Online payment methods require an eligible paid plan" (`SA-en:651`, Kuwait; `SA-en:566`, the UAE).
- **The quoted titles:** `SA-en:1046` and `SA-en:1080` hold the activation titles only as links in other articles.
- **The test's record changed** after the coordinator first read it. The report had quoted the earlier draft.
- **"unsettled, not unmet"** is the pilot's (`studies/subjects/S-01/entry.md`:119).

**Applied:**

| Finding | What was done |
| --- | --- |
| MB-01, MB-06, MB-11, MB-12 | D-001's reasons give the sources' conditions: some countries, store by store, plan and verification. The pattern is marked as the coordinator's reading in the page, the drivers and the guard section |
| MB-02, MB-03 | The Shopify quote is in its two parts. Stripe's sentence is quoted in full, with "banking partner" marked as not saying who holds |
| MB-04, MB-05 | Salla's own activation articles (`SA-en:651`, `SA-en:566`) replace the link titles, with their three requirements |
| MB-07, MB-15 | Sellers' own providers come "from a list" each platform keeps; Salla's online methods need a paid plan. "Wherever a provider serves the seller" is removed |
| MB-08 | `SA-en:495` is marked as not saying whose account receives the transfer |
| MB-10, MB-19, MB-24 | The hedges are restored: "*On my reading*", the licensed holder, "no source read shows which", and "provide payment services" as the sources' words. D-006's A row says what each area licenses, marks Sharrwah's holding no licence as an assumption, and says no licensed holder is shown |
| MB-18 | D-006's B row carries the pilot's "unsettled, not unmet" |
| MB-21, MB-22 | D-006's Carried claims follow D-001's choice 1: C under the seller's own agreement, B where Sharrwah would be party, and a case between them to the founder |
| MB-23 | D-006's row uses the test's own conditions, word for word. "Integrated with Sharrwah" is kept, so the seller's own providers count in the first market once one is integrated (S-07) |
| MB-29 to MB-34 | Part five quotes the test's final record; "reached choices 2 and 3" becomes choice 2 for fees, among consequences it marks as interpretation; "Yemen shaped the wording, not the decision" is marked as the coordinator's reading; the references' pattern is marked as a reading |
| MB-36 | The glossary's market names include Shopify Capital's United States |
| MB-42 | D-002 has one first-market line, its Confirmation's blind derivation; D-003 has one, the change scenario |

**Open rows answered:**
- **MB-09:** the test's brief and its 24 tool calls are now held (`decisions/checks/M1-blind-decision-1-log.md`). None of them names the first market, Stage 1, a decision record, the glossary, `METHOD.md`, `STATE.md`, the founder's files, `studies/` or `reports/`.
- **MB-37:** 9 entries restated an outcome and were changed at `76ec8a7`. Part five lists them. The 5 entries changed at `2274d2a` gained D-006 in their "Used by" lines only. Two more carry a decision's words that the decision defines, and were kept: *held through Sharrwah* and *at launch*.
- **MB-38:** `method/inventory_quotes.py architecture/12-glossary.md` gives 168 quoted strings: 153 found on the same line, 1 within three lines, and 14 for a person. These match its count before the change. Each changed entry's *Here* keeps its definition; only the restated outcome left it.
- **MB-39:** the coordinator read Coplien, Hoffman and Weiss from a copy at `courses.cs.duke.edu` on 25 October 2026. The quotes and page 43 were matched there. It is not held here.
- **MB-41:** part five now gives its pattern, and the check's own counts beside its own.

**The founder's question that followed:** whether the pilot's variation points, variants and Yemen marks were safeguards a plan change dropped. Part five, section 6, answers it. D-001 now rests first on the pilot's analysis of S01-VP-01, and D-006 carries the pilot's six marks for it.
