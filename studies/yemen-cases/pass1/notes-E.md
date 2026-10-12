# Pass 1, part E: notes

**Part E** is the cited-sources run, `evidence/yemen/runs/20261010T050304Z-cited-sources/`, items whose `n` in its `manifest.tsv` is 132 to 262. Its `README.md` says it was fetched from a container outside Yemen on 10 October 2026, so every citation here has `fetched_from` = `outside Yemen`. Each item was read from the file named in its `text_file` column.

**Commit** in every `source`: `9d0de523f1852ebf7716f0da01b6b619edc5e8fc`.

**Resumed work.** An earlier agent wrote YQ-E001 to YQ-E009 and YE-E001 to YE-E014 (items 133 to 137) and was interrupted before writing these notes. Those rows were kept as written; the rows from item 138 on, and these notes, were written after the restart.

**Numbering of the manifest.** The `n` column has no rows 29, 30, 94 to 107, 186 or 244, and runs to 280. So part E holds 129 rows (`n` 132 to 262, without 186 and 244), and items 263 to 280 are in neither part D (1 to 131) nor part E. They were not read here.

## Identifications within the part

Rows given the same `condition` wording because they name the same act or availability for the same role:

- Mobile-wallet services available to buyers: YQ-E006, YQ-E010.
- Identity verification of mobile-wallet users: YQ-E016, YQ-E017.

## Place groupings within the part

Two place names counted as one place because a single source uses both for the same area:

## Not readable

## Reading log

One line per item: `n`, folder, what was read, and the rows it gave.

- 132 `132-newdc.qtb-bank.com`: not readable. The run did not fetch it (manifest: "live payment endpoint, not a public page; not fetched"); the folder has no text file. 0 conditions.
- 133 `133-newhedge.io`: read (`text.txt`). Conditions YQ-E001 to YQ-E003; citations YE-E001 to YE-E004.
- 134 `134-obj.ca`: read (`text.txt`). Conditions YQ-E004 to YQ-E006; citations YE-E005 to YE-E008.
- 135 `135-ofac.treasury.gov` (recent actions, 5 March 2025): read (`text.txt`). Conditions YQ-E007, YQ-E008; citations YE-E009 to YE-E011.
- 136 `136-ofac.treasury.gov` (Counter Terrorism Sanctions programme page): read (`text.txt`). It lists advisories and recent actions and states nothing about selling or paying in Yemen. 0 conditions.
- 137 `137-packagist.org`: read (`text.txt`). Condition YQ-E009; citations YE-E012 to YE-E014.
- 138 `138-play.google.com` (Floosak wallet, Play Store page, Arabic): read (`text.txt`). The developer's description is a live page (capture date); reviews and replies carry their own dates. Conditions YQ-E010 to YQ-E017; citations YE-E015 to YE-E025.
- 139 `139-play.google.com` (Floosak wallet, Play Store page, English): read (`text.txt`). Live page; reviews carry their own dates. Conditions YQ-E018 to YQ-E024; citations YE-E026 to YE-E033.
- 140 `140-play.google.com` (Etlobni delivery app, Sana'a): read (`text.txt`). Live page; reviews carry their own dates. Conditions YQ-E025 to YQ-E030; citations YE-E034 to YE-E042.
- 141 `141-play.google.com` (jeeey shopping app): read (`text.txt`). Live page. Conditions YQ-E031 to YQ-E033; citations YE-E043 to YE-E045.
- 142 `142-play.google.com` (ONE Cash agent and merchant app): read (`text.txt`). Live page. Conditions YQ-E034 to YQ-E039; citations YE-E046 to YE-E055.
- 143 `143-play.google.com` (ONE Cash customer app, Arabic): read (`text.txt`). Live page; reviews carry their own dates. Conditions YQ-E040 to YQ-E057; citations YE-E056 to YE-E075.
- 144 `144-play.google.com` (ONE Cash customer app, English): read (`text.txt`). Live page. Conditions YQ-E058 to YQ-E073; citations YE-E076 to YE-E094.
- 145 `145-press.un.org`: not readable. The run's result is "blocked from here" (HTTP 406; the browser failed too); the folder has no text file. 0 conditions.
- 146 `146-radar2.net` (exchange rates in Aden and Sana'a, 26 December 2025): read (`text.txt`). It gives no figures. Conditions YQ-E074, YQ-E075; citations YE-E095, YE-E096.
- 147 `147-rbi.org.in` (Reserve Bank of India, Master Directions on Prepaid Payment Instruments): read (`text.txt`, headings and a search). It sets rules for India and does not mention Yemen. 0 conditions.
- 148 `148-remittanceprices.worldbank.org`: not readable. The run's result is "blocked from here" (HTTP 403); `text.txt` holds only Cloudflare's bot-check page. 0 conditions.
- 149 `149-root.packagist.org` (PHP package for Kuraimi Bank's E-Pay API): read (`text.txt`). Conditions YQ-E076 to YQ-E078; citations YE-E097 to YE-E101.
- 150 `150-s205.q4cdn.com` (Jumia's fourth-quarter 2025 results, PDF text): read (`text.txt`, opening and a search). It reports on Jumia's African markets and does not mention Yemen. 0 conditions.
- 151 `151-sahafah24.net` (exchange rates in Sana'a and Aden, 4 October 2026): read (`text.txt`). Conditions YQ-E079, YQ-E080; citations YE-E102 to YE-E104.
- 152 `152-sahafahonline.net` (women's e-commerce, Shein resellers): read (`text.txt`). The page shows only "منذ سنة"; its `raw.html` gives `date_added` 2025-05-14, used as the published date. Conditions YQ-E081 to YQ-E089; citations YE-E105 to YE-E124.
- 153 `153-sanaacenter.org` (Sana'a Center, "Fostering Opportunities for E-Commerce Growth in Yemen", 15 September 2025, PDF text): read in full (`text.txt`). Conditions YQ-E090 to YQ-E147; citations YE-E125 to YE-E191. Where `pdftotext -layout` broke a word across lines (e.g. "bank-" / "led"), the quote was split at the break.
- 154 `154-sanaacenter.org` (Sana'a Center, "Challenges and Prospects for Electronic Money and Payment Systems in Yemen", March 2022, PDF text): read in full (`text.txt`). Conditions YQ-E148 to YQ-E248; citations YE-E192 to YE-E306. The source gives two figures for account holders in 2019 (3 million, YQ-E155; almost 2.9 million at the end of 2019, YQ-E208), and says both that CAC Bank was permitted to collect customs revenue in e-rials in early 2021 (YQ-E196) and that public revenues are accepted only in cash in Houthi-held areas (YQ-E241); each is recorded.
- 155 `155-sanaacenter.org` (Sana'a Center, "Supporting Trade Finance in Yemen Amid Uncertainty", 17 February 2026, PDF text): read in full (`text.txt`). Conditions YQ-E249 to YQ-E301; citations YE-E307 to YE-E374. It dates the Houthi ban on new notes "starting in 2020" (YQ-E287), where item 154 gives 18 December 2019 for the extended ban (YQ-E184); both are recorded.
- 156 `156-sanaacenter.org` (Sana'a Center Economic Bulletin, 27 November 2020): read in full (`text.txt`). Conditions YQ-E302 to YQ-E313; citations YE-E375 to YE-E388.
- 157 `157-sanaacenter.org` (Sana'a Center, "Currency War Threatens to Deepen Yemen's Monetary Rift", 18 July 2025): read in full (`text.txt`). Conditions YQ-E314 to YQ-E321; citations YE-E389 to YE-E396.
- 158 `158-sanaacenter.org` (Sana'a Center Economic Bulletin, 9 September 2020): read in full (`text.txt`). Conditions YQ-E322 to YQ-E330; citations YE-E397 to YE-E404.
- 159 `159-sanaacenter.org` (The Yemen Review, April-June 2025, the economy section, 22 July 2025): read in full (`text.txt`). Conditions YQ-E331 to YQ-E360; citations YE-E405 to YE-E441.
