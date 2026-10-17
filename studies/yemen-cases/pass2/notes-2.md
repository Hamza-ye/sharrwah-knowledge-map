# Step 2b, range 2: groups YG-077 to YG-165

## What was done

- **Inputs:** `brief.md`, `conditions.tsv`, `citations.tsv`, `groups.tsv`, `places.tsv` and `notes.md`. The quotes in `citations.tsv` were read where a row left its place, party or date open.
- **Evidence opened:** one source, `runs/20261010T050304Z-cited-sources/items/154-sanaacenter.org/text.txt`, lines 1190-1212. I opened it to see whether YQ-E207's "the bank" is a named party. It isn't: the passage describes bank e-wallets in general, so the row keeps `place not stated`.
- **`states-2.tsv`:** 650 rows over 89 groups. 646 are `held`, 2 `ended` (YQ-D626, YQ-A036) and 2 `proposed`, both plans (YQ-C435, YQ-E006). No row is `provided for`, and no row has `now`.
- **Estimates.** Under the coordinator's corrected ruling, a source's estimate of a present value is `held`. That covers:
  - YQ-A039 and YQ-E895 ("يُقدر عددها بالآلاف");
  - YQ-D356 and YQ-E770 ("an estimated 800 unlicensed");
  - YQ-C445 and YQ-C462 ("may exceed 15").

  No row in this range forecasts or projects a future value.
- **Labels:** 49 groups have more than one label and 40 have one. A trial build of this range alone, run in the scratchpad, gives 49 axes and 40 constants.
- **Places:**
  - 370 rows are at a party's or a product's service.
  - 41 rows moved to an authority's area (listed below).
  - No row is `across Yemen`.
- **`places-2.tsv`:** 23 services added, each grouped with itself:
  - 14 products, named `<product> (<party>)'s service`: Aden Cash, BYES, Cash Pay, Hasseb, Ki Bank, Kuraimi Express, Kuraimi Jawal, M Floos, Mahfathati, Mobile Money, National Wallet (MEPS Yemen), OnTime, Shamil Money, Tadhamon Pay and Yemen Wallet;
  - 9 parties that `places.tsv` lacks: CoinGate, Stripe, WooPayments, Rho, Zid Pay, the Yemeni Store for E-Payment, MB wallet and the National Wallet Company.

## How rows were labelled and placed

- **Services.** A row about one wallet, bank or platform's own service takes that service's place, whoever the source is. This includes:
  - reviews (YQ-C165, YQ-C425, YQ-D149, YQ-E024, YQ-E056);
  - third-party guides (YQ-D305 on Western Union, YQ-E579 on PayPal).
- **Products.** A row that names one product of a party with several products goes to that product's place. A row that names two or more products of one party goes to the party's service. Examples: M Floos with Hasseb, or Kuraimi Jawal with M Floos, go to `Kuraimi Islamic Microfinance Bank's service`. Rows that name only Hasseb, M Floos, Kuraimi Jawal or Kuraimi Express go to that product.
- **Availability labels.** On the per-service availability groups (YG-120, YG-144, YG-147 to YG-159, YG-165), a service's rows are labelled `Available`, or the opposite. The detail goes in `note`: which bills, which networks or banks, which link (WeNet, Wasel), and the agents' locations. Those details are compatible across rows from one service on one date. Labelling them apart would have shown false disputes at that service.
- **Rules.** A rule an authority sets moved to that authority's area, whatever area pass 1 gave it:
  - to `the internationally recognized government's area`: YQ-D331, YQ-E272, YQ-D455, YQ-A031, YQ-D276, YQ-D474, YQ-D486, YQ-D284, YQ-D031, YQ-D032, YQ-D033, YQ-D487, YQ-F092, YQ-F104, YQ-F082, YQ-F094 (all from `place not stated`), and YQ-A029, YQ-E524, YQ-E795, YQ-E890, YQ-E810, YQ-E787 (from `government-controlled areas`);
  - to `Houthis' area`: YQ-E309, YQ-C370, YQ-D027, YQ-D029, YQ-E442, YQ-E796, YQ-C435, YQ-C393, YQ-D034, YQ-E791, YQ-E612 (from `Houthi-controlled areas`), YQ-C382 (from `Sana'a`), and YQ-F151, YQ-F152 (from `place not stated`). The Sana'a central bank's circulars name the Republic.
- **Laws of the Republic** whose seat no source gives go to `the unified Republic's area`: YQ-E303, YQ-E192, YQ-E170 ("by law"), YQ-D322 (the list of banking laws), and YQ-D353, YQ-D433 (Law No. 19 of 1995).
- **Kept at `place not stated`:**
  - YQ-F120, YQ-F121 and YQ-F122, from the 2026 list on cby-ye.com, because the document names no issuer (pass 1's note);
  - YQ-E220 and YQ-E202, which rest on Circular No. 11 of 2014, because their quotes name no issuer.
- **`across Yemen`.** None was given. The rows whose places or quotes say "throughout", "all regions" and the like are parties' own services (YQ-C337, YQ-C353, YQ-C252, YQ-C014 and others), or rules of the Aden central bank (YQ-D031 to YQ-D033, "all Yemen, including Houthi-controlled areas"). No other row's quote says that its state holds in all of Yemen.

## Rows that were hard to label

- **YQ-C041 and YQ-C169 (Cash, YG-120).** The quote "with the possibility of International Transfers" can mean available now or later. Pass 1 read it as a future addition. I kept it as `held` with the label "Named as a possibility", so Cash shows as disputed against its app listing's "Available".
- **YQ-C039 and YQ-E682 (Cash, YG-148)** say online shopping is a possible future addition and "SOON". Both are labelled "Not yet available, coming later", while Cash Pay's own row (YQ-C082) says available, at the product's place.
- **YQ-C384, YQ-C385, YQ-C386 and YQ-C387 (YG-092).**
  - YQ-C384 and YQ-C386 describe the same outage of Kuraimi's apps and both cite the technical-fault sentence (YE-C389). They share the label "Stopped by a technical fault", at Kuraimi's service.
  - The blocking report (YQ-C385) is at `Houthis' area`.
  - YQ-C387 names only Kuraimi Jawal, so it is at that product's place.
- **YG-106.**
  - The Aden central bank's network rules come in steps: UNMONEY required of exchange companies (February 2024); banks barred from using exchange companies' networks (18 February 2024); exchange companies' own networks closed (March 2024); all banks' and exchange companies' own networks closed (Decision 23, 26 June 2024); pending balances to be settled (February 2025). Each step has its own label.
  - YQ-E795 dates UNMONEY's launch to July 2024 and says only that it centralises transfers, so it has a label of its own.
- **YG-108 and YG-109.** Many reports of the same practice (exchange and hawala networks rather than banks) word it differently. They share one label per channel, so that one source's several rows (YQ-E165, YQ-E209, YQ-E210 and YQ-E232, all 2022-03) don't show as a dispute.
- **YG-118.** YQ-D031, YQ-D032 and YQ-E810 report the same 2024 decision of the Aden central bank: who may pay out, and through whom. They share one label.
- **YG-126.** YQ-B041, YQ-B042 and YQ-F152 rest on the Sana'a central bank's one announcement. They share one label, so the group is a constant.
- **YG-135.** YQ-D353 and YQ-D433 cite different articles of Law No. 19 of 1995. Both state what a money exchanger may and may not do, and they share one label.
- **YG-157.** Cash's four rows give about 1,500 agents, thousands of sub-points, or a network across Yemen. All four are labelled "Wide network across Yemen", with the numbers in `note`. Rows that give only a count keep that count as their label.
- **YG-160 and YG-163 (lists).**
  - Where one source gives two compatible rows on one date at one place, they share one label: YQ-D093 and YQ-D094; YQ-D091 and YQ-D092; YQ-E733 and YQ-E734 (Shamil Money's English and Arabic pages).
  - Wallets' service lists that name transfers, purchases and bills are labelled "Transfers, purchases and bills, among others". The full list is in `note`.
- **Status changes.**
  - YQ-D626 (a normal commission before the ban on new notes) is `ended`, since its source says the fee then rose to about 20% (YQ-D621).
  - YQ-A036 (the Aden central bank's oversight of exchange companies, "كانت معطّلة") is `ended`, set against the network's launch.
  - YQ-C435 (the Sana'a side's planned unified network) and YQ-E006 (the National Wallet Company's wallet, "well on our way towards launching") are `proposed`.

## Disagreements between sources

The build will show these as disputed:
- **Kuraimi Jawal apps (YG-092):** see YQ-C384 to YQ-C387 above.
- **Cash e-wallet and transfers from abroad (YG-120):** YQ-C041 against YQ-C169.
- **Wise (YG-125):** YQ-E580 (listed as an option) against YQ-E581 (not offered), both 2026-10-10.
- **Remittance payout currency on the Sana'a side (YG-119), item of 2026-02:**
  - YQ-E790: the association's rule of February 2024, in the currency sent;
  - YQ-E791: the Sana'a central bank's rule of March 2024, all in Saudi riyals.

  The source says both "have persisted". It doesn't present one as replacing the other, so neither has `now`.
- **Exchange companies in 2023 (YG-131):**
  - Aden: 91 (YQ-D352, YQ-D432) against 332 outlets, 96 companies and 86 agents (YQ-D429);
  - Sana'a: 415 (YQ-D351, YQ-D431) against over 170 (YQ-D430).
- **ONE Cash's uncollected transfers (YG-154):** 30 days (YQ-C233) against 14 days (YQ-E045, YQ-E064).
- **Cash's cash-out hours (YG-155):** official working hours (YQ-C127) against around the clock (YQ-C178).
- **The number of wallets on 11 July 2026 (YG-160):** "8 to 10" (YQ-C444, YQ-C461), "about 9, possibly over 15" (YQ-C445) and "possibly over 15" (YQ-C462).
- **Precision tie (YG-123):** YQ-D229 (2026, up to 50% at times) ties YQ-E596 (2026-04-29) at `place not stated`.
- **Same-day rows on the Sana'a side (YG-106):** YQ-D027 (the Sana'a branch stopped dealing with major exchange firms and networks) and YQ-D029 (dealing with the unified network banned), both at `Houthis' area` on 2025-12-15. These two can hold together, so the dispute comes from the group's size (see below), not from the sources.

## Problems with the method

- **Group size.**
  - Several groups hold states that can hold together, so the build will show a dispute or a needless axis:
    - YG-106: barring UNMONEY, and barring other networks;
    - YG-080: SWIFT Scope, and proof of relocation to Aden. The latter was required later, but the former was not repealed;
    - YG-122: the share of inflows, and banks' cash for payouts;
    - YG-083: what data banks report, and to which central bank.
  - Under rule 2, these may need splitting at step 2a.
- **Lists of services.** YG-160 and YG-163 compare lists whose length depends on the page. Two pages of one service give two labels unless their wording is coarsened. I coarsened only where both rows state the coarser label.
- **Proposed states make "unknown" parts.** A place whose only row is `proposed` takes `unknown`: `Houthis' area` on YG-107, and `National Wallet Company's service` on YG-163. So does a place whose only row has `ended`: the Aden-or-other-areas place on YG-138.
- **Third-party statements about a service.** The service rule puts a third party's statement about a provider at that provider's service. Examples are Wise's guide on PayPal (YQ-E579), Digibank on Western Union (YQ-D305), and user reviews. They then compete with the provider's own pages there. Undated ones lose to dated ones, but dated reviews from before the capture date are shown as earlier states. An example is Jawali's refused payment of September 2026 (YQ-C165).

## Problems with the brief

- **Products named twice.** The product rule covers a row that names one product. It doesn't say where a row naming two products of one party goes. I put such rows at the party's service, which leaves Kuraimi's rows split between the bank and four products. Step 2c may group them.
- **Issuers that are named only by a website.** Documents on cby-ye.com that name no issuer (pass 1's YQ-F120 to YQ-F122) are rules, but their authority isn't named. The brief's "a state with no place, and no authority setting it" keeps them at `place not stated`, beside reports.
