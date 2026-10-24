# Step 2b, range 3: YG-166 to YG-331

## What was done

- 637 rows in 166 groups, each with one line in `states-3.tsv`. `holds`: 630 held, 2 ended, 5 proposed. `now` is empty on every row: no source in this range gives an earlier and a current state for one place at the same date.
- 74 groups have more than one label among their held and ended rows.
- No row is placed `across Yemen`. The sources that say "all governorates", "all regions of Yemen", "anywhere in Yemen" or "all Yemeni cities" are describing one party's own service: Procorners, Wagbat, Yes Media, Awsan, Perfume Garden, Taiseer, Floosak, Cash and Hasseb. Those rows take the party's service.
- 22 services were added in `places-3.tsv`, each grouped with itself:
  - 16 products, under the brief's product rule: M Floos, Hasseb, Kuraimi Jawal, E-Pay and Kuraimi Pluto Debit (Kuraimi); Mobile Money and Mobile Money Business (CAC Bank); Shamil Money; Yemen Wallet (Yemen Post); Cash Mughtarib and Cash Pay (Cash e-wallet); National Wallet, e-payment gateway and e-invoicing (MEPS Yemen); e-sadad (Yemen Telecom); OnTime (Quality Connect).
  - 6 parties not in `places.tsv`: Taiseer, WeNet, jeeey, Torod, Talqa and Market Yemen.
- Evidence opened: `runs/20261010T050304Z-cited-sources/items/154-sanaacenter.org/text.txt`, to find out who issued Circular No. 11 of 2014 and the context of YQ-E206. Line 516 says "the CBY issued Circular No. 11 of 2014" in late 2014, without a seat, so YQ-E191, YQ-E218, YQ-E219, YQ-E113, YQ-E175 and YQ-E203 take `Central Bank of Yemen's area`. YQ-E206 is a general description and stays at `place not stated`.

## Placement choices

- **Provider terms that cite the central bank.** YQ-C101, YQ-C005, YQ-C055 and YQ-C099 say what the provider's own account offers, or what it operates under, so they take the provider's service. Pass 1 had placed them at `Central Bank of Yemen's area`. YQ-C108 and YQ-C112 state the central bank's rule (ceilings, three accounts under decision No. 1 of 2020), so they stay at that area.
- **Resolutions of the Aden central bank** that pass 1 placed at the IRG's areas (YQ-E808, YQ-E809) take the authority's area. YQ-E115, YQ-E116, YQ-E381 and YQ-E799 keep their area, because each describes a model or a project in an area rather than a rule. YQ-E186 is a CBY-Sana'a circular, so it takes `Houthis' area`.
- **Kuraimi.** The rows name M Floos, Hasseb, Kuraimi Jawal, E-Pay and Pluto Debit separately, and each takes its product's place. YQ-C341, YQ-C343, YQ-C344 and YQ-D620 describe the bank's "API linking service" without naming E-Pay, so they stay at the bank's service. Step 2c may find them to be one service with E-Pay; no row says so.
- **WeNet.** YQ-E227 (pass 1: Houthi-controlled areas) describes WeNet's own scheme, so it takes WeNet's service.

## Rows hard to label

- **Compatible statements from one party on one date.** The build will show these as disputed. Each pair or set comes from different pages of the same party, and they describe different parts of one requirement, or one is less specific than the other. I kept the labels apart because the rows don't state the same thing:
  - YG-166: Jawali (YQ-D586, the KYC form, against YQ-C034 and YQ-D593, ID and phone number); Floosak; ONE Cash; M Floos.
  - YG-167 and YG-169: ONE Cash.
  - YG-179: Cash (its terms, its currency list, and "more than one currency"); Jawali.
  - YG-240: Jawali (YQ-D133 gives no method).
  - YG-243: Hasseb (two Kuraimi pages list different requirements).
  - YG-278 and YG-280: CAC Bank (two pages name different cards and requirements).
  - YG-237: E-Pay ("available" against "community code exists").
- **One label for one source's partial statements.** Where one source gave a rule in two rows, both rows take one label:
  - YQ-D116 and YQ-D117: the Aden regulation of 21 September 2022, on banks and payment companies, and on exchange companies.
  - YQ-A051 and YQ-A052: one Sana'a resolution, whose law one report names and the other only describes.
  - YQ-D298 and YQ-D300: one Dakhm payment page.
  - YQ-D316 and YQ-D344: one World Bank report.
  - YQ-E135 and YQ-E145: one Sana'a Center report.
  - YQ-C084 and YQ-C095: two Cash pages; only one says where cash is withdrawn.
- **YG-307 (delivery apps).** All rows that say an app delivers take `available`, and what each delivers is in `note`. Only the 2019 Wagbat review (Sana'a only) and the list of apps (YQ-E030) differ. This gives up part of `what_varies` ("what it delivers") to avoid false disputes within one app's rows.
- **YG-222 (who may provide e-money).** Four labels:
  - banks only;
  - banks and non-bank institutions (the Sana'a side);
  - banks and licensed non-bank institutions (the Aden side, 2023);
  - banks and licensed non-bank payment service providers, not exchange companies unless they convert (the Aden side, 2022).

  The 2014 bank-led circular, the CBY's 2014 regulations, and "the prewar framework CBY-Aden holds to" all take "banks only".
- **YG-291 (instant payments).** Each row is labelled by what it says of the system: absent; absent, planned; under discussion; under development; or operating. YQ-E836 (World Bank, June 2025, "to be developed") is labelled "under development". I changed it to "absent, planned" under the coordinator's first ruling on forecasts, then put it back when the ruling was narrowed.
- **Lists of offers that change** (YG-212, Hasseb's discounts; YG-331, Procorners' stores) take one label per post. The axis's "today" at that service will be the latest post. The latest post is one offer, or one set of stores, not the whole range.

## `holds`

- **proposed:**
  - YQ-C040 (Cash: international card as a possible future addition);
  - YQ-C043 (Cash: NFC to be provided);
  - YQ-A017 and YQ-A018 (2014 UnionPay agreement: cards to be issued and acceptance coverage given as an expected effect; the coverage is a projection of a future value, so it stays proposed under the narrowed ruling);
  - YQ-E659 (WeNet's Instant Transfer Scheme in the future tense, July 2022).
- **Forecasts.** Under the coordinator's narrowed ruling, only a forecast or projection of a future value is `proposed`, and an estimate of a present value is `held`. Besides YQ-A018 there is no forecast in the range, and no row was made `proposed` for being an estimate. The counts in YG-279, YG-286 and YG-290 are reported figures for past dates. YQ-E799's "expected within three years" is a forecast date that the label leaves out: its state is that the system is being implemented, which the source says holds.
- **ended:**
  - YQ-E118 (the "previous regulations" that the 2020 decree overrides; no authority named);
  - YQ-D089 (banks only, "before 2020"; this date is never today).
- **YQ-E380.** The Yemen Payments and Clearing Company is licensed but "months from operating". I made the licence `held` and say in the label that it is not yet operating.

## Disagreements between sources

- YG-227: minimum capital for a payment system operator. 700 million rials in a news report of the 21 September 2022 regulation (YQ-D119); 750 million in the OCR of the instructions dated 13 September 2022 (YQ-F080).
- YG-291:
  - WeNet's instant transfer scheme started in mid-September 2020, per Sana'a Center (YQ-E227, March 2022). BPC's July 2022 case study gives it in the future tense (YQ-E659).
  - The Houthi authorities run their own fast payment system (YQ-E383, YQ-E560). Other sources say Yemen has no fast payment system at all (YQ-E107, YQ-E797).
- YG-284: whether a national switch operates. No, per YQ-E798, February 2026. Yes, run by WeNet (YQ-E656, YQ-E658), by MEPS Yemen (YQ-E712) and by SabaCard (YQ-A013).
- YG-224: Jawali and Floosak say they are licensed by the Central Bank of Yemen (YQ-C152, YQ-C248). The Aden circular, which is in YG-223, lists them as unlicensed.
- YG-202: within the Aden instructions of 8 August 2023, YQ-F101 makes the customer responsible for all transactions, and YQ-F102 makes the issuer bear failures by its partners. They are labelled apart. The later consumer protection instructions (YQ-F110) are the latest at that place.
- YG-244 and YG-247: one community client of Kuraimi's E-Pay says payments start from the bank's apps (YQ-F048) while its code has the supplier send them (YQ-F049). Another client sets currency by zone (YQ-F063) in one file and the rial on each request (YQ-F067) in an unrouted one.
- YG-187: Yemen Wallet is free outright (YQ-C272) and free during a campaign (YQ-C275). The dates differ.

## Problems with the method

- **Live pages tie on the capture date.** Every live page is dated 10 October 2026. So any two pages of one party that describe a service differently, even where they agree, tie as "disputed". The brief has no way to mark one row as a less specific form of another.
- **Product places split one party's axis.** Kuraimi now has six service places in this range: the bank, M Floos, Hasseb, Kuraimi Jawal, E-Pay and Pluto Debit. Rows that name the bank only, such as the "API linking service", may describe one of the products, but no row says so.
- **Other agents' names may differ.** Other step 2b agents may add the same products under other names. Step 2c will need to group them.
- **Group size.** Several groups join a provider's terms with the Aden central bank's instructions: YG-191, YG-194, YG-202 and YG-229. The instructions hold at the IRG's area and the terms at the provider's service, so they never compete. That is consistent with the overlap rule, but each such axis mixes a rule with a service's practice.

## Problems with the brief

- The product rule makes `<product> (<party>)'s service` places. It doesn't say which party name to use when `places.tsv` names the party by a brand, such as "Cash e-wallet" for Tamkeen. I used the name `places.tsv` uses.
- The brief gives no rule for a state that is held in part and announced in part. Quality Connect's On Time delivers food and has announced "anything at any time" as coming soon. I recorded it as `held` for what is offered.
