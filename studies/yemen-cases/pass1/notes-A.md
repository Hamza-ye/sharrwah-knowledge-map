# Pass 1, part A: notes

Part A covers the founder's pages from inside Yemen, `evidence/yemen/blocked-evidence-founder/`, and any attestation in `evidence/yemen/attestations/` besides `TEMPLATE.md`.

## Commit

Every `source` cites `sharrwah-knowledge-map@9d0de523f1852ebf7716f0da01b6b619edc5e8fc`, as the coordinator's message instructed. At the start of this run `git rev-parse HEAD` gave `95679091004737adae316fff6a38222d7bda5bc2`. `git diff` between the two commits shows no change under `evidence/`, `method/` or `studies/yemen-cases/brief.md`.

## What was read

- `evidence/yemen/blocked-evidence-founder/`: `README.md`, `manifest.tsv` and all 15 pages, F01 to F15. All 15 were readable. Every quote is taken from the page's HTML file and checked against it.
- As a reading aid, the visible-text file the manifest names for each page, `evidence/yemen/derived/blocked-evidence-founder/F01/text.txt` to `F15/text.txt`. Each page's HTML was also compared with its text file. Beyond the text file, it holds nothing bearing on Yemen except image alt text, which sits inside tags and so cannot be quoted: F15's alt text names the ون كاش app on Google Play and the Apple store. F06's icon cells have no text at all.
- `evidence/yemen/attestations/` holds only `TEMPLATE.md`, so there was no attestation to read.
- Nothing else was opened. `method/check_yemen_cases.py` was run, not read.

Counts: 15 pages read, none unreadable; 54 condition rows (YQ-A001 to YQ-A054) on 35 distinct conditions; 112 citations (YE-A001 to YE-A112).

| Page | What it is | Date used | Condition rows | Citations |
| --- | --- | --- | --- | --- |
| F01 | Saba (Sana'a): text of the Central Bank of Yemen governor's Resolution No. (4) of 1445 AH | 31 May 2024 | YQ-A001, A002, A051 | 6 |
| F02 | Central Bank of Yemen (centralbank.gov.ye): "Electronic payment services companies" | live page, captured 10 Oct 2026; two undated headlines | YQ-A003 to A005 | 20 |
| F03 | CNBC: U.S. sanctions on Houthi funding networks | 16 Jan 2026 | YQ-A006 | 2 |
| F04 | UNCTAD: cyberlaw reforms in least developed countries | 24 Feb 2022 | YQ-A007 | 1 |
| F05 | Trilegal: RBI guidelines on payment aggregators (India) | none | none | 0 |
| F06 | World Bank Remittance Prices Worldwide: Saudi Arabia to Yemen | data 21 Aug to 2 Sep 2025 | YQ-A008, A009 | 9 |
| F07 | SabaCard (Yemen Payments and Cards Co.) | live page, 10 Oct 2026 | YQ-A010 to A013 | 6 |
| F08 | UN press release SC/16222: resolution 2801 (2025) | 14 Nov 2025 | YQ-A014 | 3 |
| F09 | U.S. Treasury release on Yemen Kuwait Bank, via GlobalSecurity.org | 17 Jan 2025 | YQ-A015, A016, A054 | 10 |
| F10 | Electronic Payments International: UnionPay and CAC | 29 Dec 2014 | YQ-A017, A018 | 3 |
| F11 | Al-Masdar Online: Council of Ministers Decision No. (13) of 2025 | 12 Aug 2025 | YQ-A019, A020 | 4 |
| F12 | Al Arabiya: the central bank tagged Aden stops dealing with 6 banks | 30 May 2024 | YQ-A021 to A028 | 10 |
| F13 | Al-Masdar Online: the unified transfer network (UNMONEY) | 8 Jul 2024 | YQ-A029 to A042, A053 | 17 |
| F14 | Al-Masdar Online: the central bank in Sana'a bans 13 banks | 31 May 2024 | YQ-A043 to A047, A052 | 7 |
| F15 | Yemen Kuwait Bank: ون كاش page | live page, 10 Oct 2026 | YQ-A048 to A050 | 14 |

F05 states no condition for Yemen: its text concerns India, and Yemen appears only as an option in the country list of the page's subscription form.

## Dates

- Live pages, where a party describes its own current service or rule, take the capture date, 10 October 2026: F02's list, F07 and F15.
- F02's two "Most read" headlines (YQ-A004, YQ-A005) carry no date and link to announcements; they are not the page's own current rule. They are recorded with `held_at` set to `no date`, since the checker requires a value.
- F04: the manifest gives no date; the page's date element reads "Published on February 24, 2022", which is used.
- F06 is not a party describing its own service, so it is dated by the end of its data-collection range, 2 September 2025.
- F08 (YQ-A014): the assets freeze is renewed until 14 November 2026. `held_at` is the range's end, which falls after the capture date.
- F09: the manifest's date hint is 2025-01, from the address; the page shows January 17, 2025, which is used.
- Month precision where the source gives only a month: YQ-A029 (mid-February 2024), YQ-A032 and YQ-A033 (March 2024), YQ-A047 (early April 2024).
- `date_basis` values in conditions: `stated`, `still holds: source date`, `range end`, `source date: published`, `live page: capture date`, `no date`. In citations: `published`, `shown` (F06), `capture` (live pages).

## Identifications within the part

Rows given the same `condition` wording:

- **Banks a party may deal with:** YQ-A001 (F01), YQ-A015 (F09), YQ-A021 (F12), YQ-A033 (F13), YQ-A043 and YQ-A045 (F14). The act is dealing with a named bank. The party barred differs, and each state names it: local and foreign financial and non-financial institutions and individuals (F01); U.S. persons, and transactions within or transiting the United States (F09); banks, exchange companies and establishments and remittance agents (F12); exchange companies and establishments and local money transfer networks (F13); not stated (F14).
- **Licence needed to conduct banking business:** YQ-A002 (F01), YQ-A044 (F14).
- **Law on payment systems and electronic financial and banking operations:** YQ-A051 (F01), YQ-A052 (F14).
- **E-wallets available:** YQ-A003 (F02), YQ-A048 (F15).
- **International card brands issued to cardholders in Yemen:** YQ-A010 (F07), YQ-A017 (F10).
- **Card acceptance by merchants:** YQ-A011 (F07), YQ-A018 (F10).
- **Currency for domestic sales, services and financial contracts:** YQ-A019 and YQ-A020 (both F11).
- **Service to the public by banks the central bank has stopped dealing with:** YQ-A022 (F12), YQ-A046 (F14).
- **Where banks must base their operations centres:** YQ-A023 (F12), YQ-A047 (F14).
- **Circulation of a 100-rial coin:** YQ-A026 and YQ-A027 (both F12).
- **Domestic transfer network exchange companies may or must use:** YQ-A029, YQ-A030, YQ-A031, YQ-A032 and YQ-A034 (all F13).
- **Central bank monitoring of transfers through exchange companies:** YQ-A035 and YQ-A036 (both F13).

F14's list of 13 banks (note of YQ-A043) gives in Arabic, in the same order, the 13 names F01 gives in English (note of YQ-A001).

## Places

Each place is the area the source names for the statement. Where the source names only the authority, the place is `<authority>'s area`. Labels are in English, with the source's words in parentheses for Arabic sources.

Groupings within the part, where one source uses two names for the same authority or area:

- **Central Bank of Yemen (Sana'a)'s area.** F01 names the authority "the Central Bank of Yemen (CBY)" and "the Central Bank of Yemen, headquartered in Sana'a" (YE-A001, YE-A005). F13 writes "البنك المركزي الخاضع للحوثيين في صنعاء" and, in the same paragraph, "بنك صنعاء" (YE-A074, YE-A075); it also writes "البنك المركزي اليمني بصنعاء" (YE-A078) and "البنك المركزي بصنعاء" (YE-A081). F14 writes "البنك المركزي التابع لسلطات الحوثيين في صنعاء (غير معترف به)" (YE-A086) and "البنك المركزي في صنعاء" (YE-A088) for the bank issuing its decision. The label joins these because F13's "البنك المركزي اليمني بصنعاء" is F01's name in Arabic, and F14's "البنك المركزي في صنعاء" is F13's "البنك المركزي بصنعاء" with another preposition. Rows: YQ-A001, A002, A051 (F01); YQ-A034, A035 (F13); YQ-A043, A044, A052 (F14).
- **Central Bank of Yemen (Aden)'s area.** F12 calls the bank "البنك المركزي اليمني" and tags the page "المركزي اليمني - عدن" (YE-A060). F13 writes "البنك المركزي في عدن" (YE-A070, YE-A079) and "البنك المركزي اليمني في عدن" (YE-A077). F14 writes "البنك المركزي اليمني في عدن" (YE-A089) and "البنك المركزي المعترف به". Rows: YQ-A022 to A024, A027, A028 (F12); YQ-A030, A040, A053 (F13); YQ-A045 to A047 (F14).
- **United States.** F09 gives the area of OFAC's sanctions as the United States: U.S. persons, or within or transiting the United States (YE-A046, YE-A047). F03 names the same office, the U.S. Department of Treasury's Office of Foreign Assets Control, and calls its measures U.S. sanctions (YE-A026, YE-A027). Rows: YQ-A006 (F03); YQ-A015, A016, A054 (F09).
- **The Republic (في الجمهورية).** The same words in F12, for the addressees of the decision (YE-A063), and in F13, for the networks its 26 June 2024 decision covers ("العاملة في الجمهورية", YE-A079). Rows: YQ-A021, YQ-A031.

Places kept apart:

- F11 names the Council of Ministers decision's area "داخل الجمهورية اليمنية" for the ban (YQ-A019) and "جميع المناطق والمحافظات المحررة" for the rial-only obligation (YQ-A020). It does not say they are the same area, so they are two places.
- "Republic of Yemen (داخل الجمهورية اليمنية)" (F11) and "The Republic (في الجمهورية)" (F12, F13): no one source uses both.
- F13 names the area of the Aden central bank's February 2024 circular "المناطق الخاضعة لسيطرة الحكومة" (YQ-A029) and the networks covered by its 26 June 2024 decision "العاملة في الجمهورية" (YQ-A031), and it contrasts areas under Houthi militia control with areas under the Aden government's control. Neither name is joined to "Central Bank of Yemen (Aden)'s area", which is used for F13 rows whose statement names no area. Likewise F12 names the addressees of its decision as in the Republic (YQ-A021), while its other rows from that bank name no area.
- "Houthi group's area (جماعة الحوثي)" (F12, the issuing authority in YQ-A025 and YQ-A026) and "Areas under Houthi militia control (مناطق سيطرة ميليشيا الحوثي)" (F13, YQ-A042).
- "Central Bank of Yemen's area (centralbank.gov.ye)" (F02): the page names the bank only as "Central Bank of Yemen" and gives no city for it, so it is joined to neither central bank label. The folder README's description of F02 was not used for its place.
- "Yemeni Exchangers Association in Sana'a's area" (F13, YQ-A032, YQ-A033), the authority issuing the March 2024 circular. YQ-A034 names both the association and the central bank in Sana'a and takes the central bank's label.
- Others, each as named: "Yemen" (F04, F07, F10); "Saudi Arabia to Yemen (corridor)" (F06); "UN Security Council's area" (F08); "In Aden or in other areas" (F13, YQ-A036); "Hodeidah port" (F13, YQ-A041); "place not stated" (F13: YQ-A037 to A039; F15: YQ-A048 to A050).

## Disagreements and differences between sources

- When the Aden central bank's decision on the six banks took effect: F12 says the bank stopped them on Thursday, in a report dated 30 May 2024 (YE-A061); F14 says the decision is implemented from 2 June (YE-A090). Recorded as YQ-A021 (2024-05-30) and YQ-A045 (2024-06-02).
- The six banks' names differ in form: F12 has "اليمن الكويت", "اليمن والبحرين الشامل" and "الكريمي للتمويل الأصغر الإسلامي" (YE-A063); F14 has "بنك اليمن والكويت", "مصرف اليمن والبحرين الشامل" and "بنك الكريمي للتمويل الأصغر" (YE-A089).
- The parties named for ون كاش and كاش: F02 lists ون كاش under شركة المحفظة الوطنية الإلكترونية (YE-A016) and كاش under الشركة المالية تمكين (YE-A015). F15 is a Yemen Kuwait Bank page (YE-A104) for ون كاش that also shows كاش and فلوسك among the bank's solutions (YE-A101 to YE-A103). F02 lists فلوسك under بنك اليمن والكويت بالشراكة مع شركة كواليتي كونكت (YE-A012). Neither source says how these parties relate.
- F07's Visa section ends with the MasterCard sentence ("providing MasterCard cards in the Yemeni market"). YQ-A010 rests on the Visa section's first sentence (YE-A042) and the MasterCard section (YE-A041).

## Statements read but not recorded as conditions

- F08: the request for a Panel of Experts report on dual-use components and precursor chemicals sold or transferred to Yemen, and the mention of vessels carrying arms "in violation of paragraph 14 of resolution 2216 (2015)": neither states a rule for a merchant, a buyer or a party serving them. The travel ban renewed with the assets freeze.
- F09: the designation of Ansarallah as a Specially Designated Global Terrorist, effective 16 February 2024, and the sanctioned governor of the Houthi-aligned central bank in Sana'a. The release states its rules for designated persons in general; applying them to these by name would be inference.
- F12 and F14: the risk, given as the Aden decision's reason, that Houthi measures expose banks to account freezes and the suspension of foreign dealings.
- F13: banks stopping deposits with the Houthi-affiliated central bank after 2016; the unified network's ownership, capital and supervision; the effects projected if the Sana'a ban continues.
- F07: the company's history (founded in the second quarter of 2005) and the equipment it sells (ATM machines, thermal rolls).
- F06: payment instrument, transfer speed and, for five of the eight products, receiving method are shown only as images, and the legend's three groups carry no labels.

## Problems with the method

- The brief takes `source`'s commit from `git rev-parse HEAD` at the start; the coordinator gave commit 9d0de523, which was used (see Commit).
- The checker requires a non-empty `held_at`, so undated states carry `no date`.
- Several pages embed `data:` SVG images whose attributes contain `>`, so removing tags with a simple pattern leaves attribute text in the page text (F06, F15). Quotes were chosen not to span such images, and each was checked to match whether tags are removed with or without a space.
- The brief joins rows only for the same act and the same role, while its abstract model puts "who may do A" in the condition and the parties in its states. "Banks a party may deal with" follows the model, naming the barred parties in each state; pass 2 may split it by role.
