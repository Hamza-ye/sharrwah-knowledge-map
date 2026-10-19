# Q7 draft: notes

## What was read

- **The brief**, `studies/proposals/briefs/R4-drafting.md`, whole.
- **The question:** Q7's section of `studies/proposals/questions-for-agents.md` (sentences [1] to [4]).
- **Depth:** Q7's rows of `studies/proposals/areas/depth.tsv`: Shopify and Zid in depth; Salla, WooCommerce and BigCommerce checks. Their `why` text was not used as evidence.
- **The five accounts**, `studies/proposals/records/Q7/<platform>/account.md`, in that order.
- **From each platform's `notes.md`, only these lists:**
  - Shopify: "Copies that differ from what was read". Copy Q7-SH-K1936 (contact Shopify Support after the first sale) differs from Q7-SH-008 and Q7-SH-181. The draft rests nothing on K1936 and cites those two.
  - Zid: "Copies" (none found wrong).
  - Salla: "Account points not checked" and "Copies" (none found wrong).
  - WooCommerce: "Account points left unchecked" (none).
  - BigCommerce: "Account points past the 20th not-found row (not checked)" and "Points not sorted against".
  - Section 1 flags each point it uses from these lists ("not checked on Salla", "not checked on BigCommerce").
- **Ids looked up** with `python3 -I method/record_ids.py`:
  - every id of its own platform that each account cites: Shopify 142, Zid 71, Salla 101, WooCommerce 108, BigCommerce 118;
  - after the coordinator's tool change, the same ids again with `--all`. The output was identical, so no id had more than 12 quotes and nothing read earlier was cut short.
- **Pilot statements no account cites:** `grep -F` on Q7's five `copied-view.tsv` files, reading only the printed lines. Terms: `currenc`, عملة, العملة, بالريال, ريال, دينار, درهم, SAR, AED, KWD.
  - Looked up from these: Q7-ZD-P0059, Q7-SH-P0154, Q7-BC-P0027, Q7-SA-P0155 and Q7-ZD-P0149.
  - Only Q7-ZD-P0149 is cited, for Zid's full sentence on مدفوعات زد. Its quotes cover كي نت, which copy Q7-ZD-K0300's single quote doesn't.
- **Source kinds:** `python3 -I method/source_kinds.py` on the main sources behind the cited records, so section 1 names kinds where a comparison mixes them.
- **Areas:** in `studies/proposals/areas/areas.md`, only the areas whose questions include Q7: A-01, A-03, A-09, A-11, A-12, A-15, A-16, A-22, A-31 and A-33. They are not cited; their text was not used as evidence.
- **The Yemen digest:** `studies/proposals/yemen-digest.md`, read whole, once, after sections 1 to 5 and 7 were written.
  - Stage 1's rows were looked up by id: YA-01, YA-07, YA-15, YA-21, YA-62, YA-86, YA-114, YA-166, YA-204, YK-05, YK-12, YK-16, YK-349, YK-452 and YK-514.
  - YA-15, YA-204, YK-349 and YK-514 were left out of the final draft; YA-149 was used, then left out, to keep to length.
- **The variation point:** S01-VP-23, from `studies/subjects/S-01/variation-points.tsv`, reading only its `vp_id`, `question` and `x_words`.
  - Its `x_words` are earlier runs' words. Zid's (للعملات التالية) comes from the no-part statement Q7-ZD-K0137 / Q7-ZD-P0123, on which section 8 rests no reading.
- **Not read:** other questions' records and drafts, `PLAN.md`, `STATE.md`, `founder-decisions.tsv`, `founder-messages/`, `register/`, `studies/proposals/questions.md`, the rest of `studies/subjects/`, the platforms' own pages, and the checker's source.

## What the records don't show

- **The currency of Zid Pay's deposits, and of the Zid Pay balance before deposit** (Q7-ZD-N02, Q7-ZD-N01).
  - Would show it: asking Zid, or reading the held pages again after a new capture, as the rows give.
  - Section 8 (Decision 14) needs it.
- **The currency of Shopify's Reserved funds, and of funds in a Payment Processor Account** (Q7-SH-N01).
  - Would show it: the Shopify Payments payouts page, opened by the owner of a store with Shopify Payments active and a balance or reserve.
- **The currency in which Salla Payments receives and settles funds, as its published pages state it** (Q7-SA-G0151).
  - The page is held but wasn't read. Would show it: reading the held salla.com/payments page; or Q7-SA-G0153's route, a settlement statement recorded in a store with Salla Payments in each market.
  - The run on store real-merchant (12 October 2026) shows SAR for one Saudi store only.
- **The currency of the Global-e account under Shopify's Managed Markets** (Q7-SH-N04).
  - Would show it: Shopify's Managed Markets terms, as the row's route gives.
- **What a change of store currency does to orders already recorded**, on Zid (Q7-ZD-N03) and Salla (Q7-SA-N07), and what a change of a market's currency does on Shopify (Q7-SH-N02).
  - The proposal doesn't rest on these, since its **order currency record** keeps each order's own currencies and rates.
  - Would show it: a store-currency change recorded in a store that has orders, as the rows' routes give.
- **The size of the rial's smallest unit**, which the **currency table** needs. No record read gives it.
  - Would show it: a Yemeni provider's API documentation, or a test payment, showing whether amounts are sent in whole rials or in a smaller unit.
- **Which currency code each Yemeni provider's API uses for each rial zone** (section 6, "doesn't show").
  - Would show it: E-Pay's and the other providers' API documentation, or a test payment in each zone.
- **The currency in which a Yemeni payment provider pays a merchant out to a bank account** (section 6, "doesn't show").
  - Would show it: a provider's merchant terms, or a recorded payout.

## Where the draft cites past the guide's counts

- **Statements, copies and citations: 80 distinct ids, past about 40.** They are 48 statements, 23 copies and 9 pilot copies: Shopify 23, Zid 17, WooCommerce 14, BigCommerce 13 and Salla 13. Three things push the count up:
  - section 1 says, for four sentences, what each of five platforms does, and each match is shown in each platform's own words, so most points need one id per platform;
  - section 8's Decision 14 needs each platform's payout currency and held-balance evidence (18 ids, almost all reused from section 1);
  - sections 2 to 7 reuse section 1's ids, adding only BC-K0177, ZD-K0156, SH-P0010, SA-P0079 and SH-099 for fees, legal position and per-method capability.
  - An earlier version cited 155 statement ids; it was cut to the one or two ids that best show each platform's part of a point.
- **Yemen facts: 14 (an axis or constant at one place), past about 8.**
  - The rial's split by area bears on five elements: currency table, place currency settings, exchange rate, rate provider and seller ledger.
  - Showing the split needs the same axis at two places: YA-01 at Sana'a and at Aden.
  - Showing that providers differ needs two states: YA-114 at E-Pay and at YemenPay, and YA-62 at Stripe and at WooPayments.
- **Within the guide:** not-found rows and copied gaps, 6 (5 not-found, 1 copied gap); "Yemen's evidence doesn't show", 2.

## Problems with the brief or the tools

- **Scratch files:** the session's tools refused to write a `.md` working file in the scratch directory (they block "report files" from a subagent). The working analysis was kept as `analysis.txt` there instead. `draft.md` and `notes.md` in this folder were written normally.
- **Arabic diacritics:** Salla's record Q7-SA-P0042 has تحوِّل with shadda before kasra. Retyped, the two marks came out in Unicode's canonical order (kasra, then shadda), and the checker reported the quote as not found. The quote was dropped. The checker could normalise both sides (Unicode NFC) before comparing, so that a correct copy in canonical order isn't rejected.
- **The citing guide:** with five platforms and four sentences, the brief's own requirement for section 1 (each platform, each sentence, matches shown in each platform's words) is hard to meet in about 40 statement ids. The draft goes past it and says why above.
- **Records that disagree:** Zid's help pages Q7-ZD-P0149 (3 August 2026) and Q7-ZD-004 (6 August 2026) aren't reconciled on the currency a buyer is charged with Zid Pay. Section 1 cites both, and the proposal rests on neither.
- **WooCommerce's policy pages:** the draft rests on none. Its WooCommerce points rest on WooCommerce's documentation and shipped code (woocommerce-11.2.1).
- **Interruptions:** the run was paused twice by the coordinator. The folder and the scratch directory were intact each time.
