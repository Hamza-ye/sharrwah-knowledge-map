# Shopify: lines resting on a maker not held, aligned before the amendment

**What this is.** The coordinator's alignment, on 31 October 2026, of Shopify's checked placement lines whose `reading` rested on no maker held while their `supports` was `core` or `extension-point`. The rules applied:
- the ruling after SH-43, with the corrections after SH-45 (`held/review-H-rulings.md`, its last section);
- the amendment notes' items 'Apps and separate products with no maker statement held' and 'Shopify Capital' (`shopify/amendment-notes.md`);
- the digests' first-party tables (`held/rules/editions-page-data.md`, `merchant-changelog.md`, `admin-router.md`).

The candidates were the 46 lines the coordinator listed. The Editions batches' Capital lines were found by searching `placements-SH-50.tsv` to `placements-SH-67.tsv` for 'Capital'.

**What changed.** On each changed line, only `supports` changed, and its `reading` gained '; aligned by the coordinator before Shopify's amendment: …'. No `filler` needed to change: every filler left on a `shows` line is a venue, an ERP or a law. The Editions digest's rule 54 makes a venue a filler, and SH-62:28, SH-66:76 and SH-48:118 keep venue fillers on `shows` lines. No line moved, so the line numbers are the files' own, with the header as line 1.

**How the makers were looked up.**
- `python3 -I method/held_entries.py makers --platform shopify`, for the 34 names below, in one run.
- The concern map: `class_slice.py search` for the same apps, which found no maker statement.
- The digests' tables.

The entries cited are held at observed-sh e38dc17e3 (`entries.tsv`, `source`), and the quotes from SH-E-136aca69, SH-E-ee2ee993, SH-E-0678ff26 and SH-E-4c0f3472 were checked against those bytes. What `makers` printed and what the entries say are facts. **Each support is a reading, the coordinator's, by the rule cited.**

**Counts:**
- Candidates: 46 lines.
  - 32 changed: 28 to `shows` (23 from `core`, 5 from `extension-point`), 3 to `own-service` and 1 to `core;own-service`.
  - 14 kept.
- Shopify Capital in the Editions: 10 lines from `shows` to `own-service`; 2 kept `core`.
- `held_entries.py check` printed 0 problems on each of the 20 batches changed (section 4).

## 1. The candidates

'Maker held' means a statement naming Shopify, or a third party, as the app's maker or provider.

| Line | Entry | App or product | Maker held | Support | Why (a reading) |
| --- | --- | --- | --- | --- | --- |
| SH-10:29 | SH-E-05146ff8 | Shopify Capital, its route capital:main | yes: SH-S-0484, SH-S-0491, SH-S-0493 (the router digest's table) | `core`, kept | the admin's own Capital route: routes stay `core` (the router digest's table; the ruling after SH-43, 'the admin's own sections, such as Shopify Capital's, stay `core`'); the brand in its title needs no maker (router rule 18) |
| SH-10:31 | SH-E-0608c698 | Shopify Capital, its route capital:amendment-terms | yes, as above | `core`, kept | the admin's own Capital route, as above |
| SH-34:70 | SH-E-b05648e0 | Shopify Forms | none: `makers` finds only SH-E-ee2ee993's 'our help docs', which names none (changelog rule 10) | `core` → `shows` | the ruling after SH-43, which names Forms; changelog rule 13 and its table |
| SH-34:183 | SH-E-9ef229ac | Shopify Flow | yes: SH-E-0678ff26 ('Today we’re introducing test runs in Shopify Flow'), SH-E-aca9896c | `core` → `own-service` | the ruling after SH-55; as SH-34:198 was aligned |
| SH-34:212 | SH-E-4517a726 | Shopify Flow | yes, as above | `core` → `own-service` | as above |
| SH-35:54 | SH-E-eda9f84c | SimGym | none: `makers` finds only 'our help documentation' (SH-E-eda9f84c, SH-E-a8864b63) and 'our help doc' (SH-E-08e97b75) | `core` → `shows` | the ruling after SH-43, which names SimGym; as SH-63:86 and SH-65:113 |
| SH-35:96 | SH-E-a8864b63 | SimGym | none | `core` → `shows` | as above; the AI Research Preview stays in `reading` |
| SH-35:195 | SH-E-c801d763 | Shopify Product Network app | none (`makers`: none) | `core` → `shows` | the ruling after SH-43, which names Product Network; as SH-64:2 |
| SH-36:36 | SH-E-e46f8f5a | Shopify POS, its quick count extension | not a separate product | `core`, kept | POS is the platform's own client (Editions rule 9; the ruling after SH-55). No held words call the extension an app, so it is POS's own, as the Pixel Helper is the admin's (changelog rule 13). The gap its reading names is only for a CM-POS-004 line, which it doesn't take |
| SH-36:93 | SH-E-08e97b75 | SimGym | none | `core` → `shows` | as SH-35:54 |
| SH-36:175 | SH-E-25748df9 | Shopify Launch Check app | none (`makers`: none) | `core` → `shows` | the ruling after SH-43, which names Launch Check |
| SH-36:176 | SH-E-25748df9 | Shopify Launch Check app, its AI analysis | none | `core` → `shows` | as above |
| SH-36:216 | SH-E-062d5c52 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-37:43 | SH-E-b94bb020 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-37:89 | SH-E-ea456de2 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-37:225 | SH-E-fc2c7dd6 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-38:73 | SH-E-2675a00b | Shopify Subscriptions app | yes: SH-E-4c0f3472 ('our new, free subscriptions app'); the digests' tables | `core` → `core;own-service` | the app's subscriptions are `own-service` (the ruling after SH-55), edited from the admin's own product page, `core`, as the Editions twin SH-59:38 reads the same feature |
| SH-38:100 | SH-E-26f1b52b | Shopify Subscriptions app | yes, as above | `core` → `own-service` | as its Editions twin SH-59:39 |
| SH-38:148 | SH-E-f333c0fd | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-38:164 | SH-E-4551569c | ShipSurance, named only in the title | none; its role isn't stated | `core`, kept | not a separate product shown: the insurance comes with labels 'purchased in Shopify admin', by plan, and is claimed 'in Shopify Admin' as Shopify Shipping insurance is (CM-SHP-003's `core`). ShipSurance's role stays a gap |
| SH-39:5 | SH-E-0bbdd469 | the Google & YouTube app; YouTube's affiliate programme | yes: 'Shopify's Google channel' (SH-E-5eb470e8), 'Shopify's Google Shopping app' (SH-E-5835be14) | `extension-point`, kept | Google's own services reached through Shopify's app stay `extension-point` (the corrections after SH-45 name this programme). Its reading's maker gap is superseded, not edited (section 3) |
| SH-39:29 | SH-E-c1cdec64 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-39:160 | SH-E-57a820c1 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-39:178 | SH-E-cf78b4cd | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-40:86 | SH-E-1a76361c | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-40:187 | SH-E-ee2ee993 | Shopify Forms | none: its own 'our help docs' names none | `core` → `shows` | as SH-34:70 |
| SH-41:171 | SH-E-4a13b1e1 | Shopify Privacy & Compliance app (apps.shopify.com/customer-privacy-banner) | none: `makers` finds none for it. For 'Customer Privacy' it finds only the Customer Privacy API (SH-E-9fb7f4c4) and the admin's Customer privacy section (SH-E-2a28fcaa) | `core` → `shows` | the ruling after SH-43, which names Privacy & Compliance; C43.5. The filler 'US privacy laws' stays: a law setting its terms |
| SH-42:11 | SH-E-51e7df71 | the Google channel app; Google Analytics 4 | yes, as SH-39:5 | `extension-point`, kept | Google Analytics through Shopify's app is Google's own service (the corrections after SH-45) |
| SH-42:112 | SH-E-986a6e04 | Shopify Forms | none | `core` → `shows` | as SH-34:70 |
| SH-45:75 | SH-E-6a94e28f | Shop Pay, renamed from Shopify Pay | not a separate product here | `core`, kept | Shop Pay in Shopify stores' checkout is the platform's own (the corrections after SH-45; C45.3; changelog rule 17). 'our ongoing effort' names no separate product |
| SH-50:168 | SH-E-a961b8d5 | the Google & YouTube app, its admin page | yes, as SH-39:5 | `core`, kept | the admin's page for an app, CM-APP-007 `core` (M-10; the corrections after SH-45) |
| SH-54:2 | SH-E-7bb3b9b0 | Shopify Forms, in the card 'Shopify Marketing Tools' | none | `core` → `shows` | this is Forms' line on CM-MKT-005. The card's other tools take lines 3 to 6, and SH-54:7 places 'Shopify Marketing Tools' `shows`. As SH-50:212 and SH-58:57 place Forms |
| SH-54:14 | SH-E-f787042c | the Google & YouTube app, its admin page | yes | `core`, kept | as SH-50:168 |
| SH-54:26 | SH-E-6bff85f5 | the Google & YouTube app; Google Analytics 4 | yes | `extension-point`, kept | as SH-42:11 |
| SH-54:48 | SH-E-8c9b0e16 | Shopify Forms | none | `core` → `shows` | as SH-34:70; E89 and the Editions digest's table |
| SH-55:66 | SH-E-c2dd20bc | Faire: Sell Wholesale app | none: `makers` finds only “We've partnered with Faire”, which names the marketplace Shopify partners with, not the app's maker | `extension-point` → `shows` | on CM-CHN-003 Faire is the marketplace the app connects, its venue (M-3), so the line is the app's own work (E89). Faire stays its filler (rule 54). As SH-62:28 and SH-66:76. Faire's own wholesale selling keeps its `extension-point` line, SH-55:67 |
| SH-55:110 | SH-E-320d69a9 | the TikTok app (admin.shopify.com/apps/tiktok-ads-2) | none: `makers` finds only SH-E-49553d41, on Shopify's checkout on TikTok | `extension-point` → `shows` | TikTok is the venue, and TikTok Shop is read as the venue, as SH-54:36 and SH-48:118 read it (M-3). Selling there is the channel's own work, as selling on YouTube is the Google app's (SH-42:205). TikTok stays its filler. Open (section 3) |
| SH-55:118 | SH-E-a5bde01e | Shop Minis, with Tolstoy, Videowise, Showday and Shop Quiz | third parties named as the work's source: 'from' each, each linked to install | `extension-point`, kept | others' Shop Minis are `extension-point` (Editions rule 11). The card's CTA opens the App Store's guide to apps in Shop (rule 19), and the named apps are the work's source (E124) |
| SH-55:119 | SH-E-a5bde01e | Tolstoy, Videowise, Showday | named as the work's source | `extension-point`, kept | E124: apps at App Store addresses named as the work's source ('shoppable videos on the home feed from' Tolstoy). The fillers stay |
| SH-55:120 | SH-E-a5bde01e | Shop Quiz | named as the work's source; no maker of its own held | `extension-point`, kept | as SH-55:119, by the card's words (E124). Open (section 3) |
| SH-57:133 | SH-E-f2a67d70 | Shopify Connector app, for Microsoft Business Central | none (`makers`: none for either name) | `extension-point` → `shows` | none is shown making it, as SH-62:28 reads the same Plus card for the NetSuite ERP connector. Microsoft Business Central stays as its other party (rule 54) |
| SH-59:119 | SH-E-1993ae93 | the Roku app (apps.shopify.com/roku-ads), Actions Ads | none (`makers`: none for Roku or Actions Ads) | `extension-point` → `shows` | Roku is named as the ad platform the ads run on, a venue (M-3). The ads are the app's own work, as the Google app's campaigns are its own (the corrections after SH-45). Roku stays its filler. Open (section 3) |
| SH-59:122 | SH-E-db678fdd | Shopify Forms | none | `core` → `shows` | as SH-54:48 |
| SH-60:108 | SH-E-7122f3c5 | Shopify Bill Pay | not Shopify. CM-PAY-027's cell holds a provider: 'Shopify Bill Pay is provided by Melio' (SH-C-098/responsible/SH-S-7200, `outside`) | `core`, kept | the card links the admin's own route finances/billpay (finance:billpay, SH-S-5166, CM-PAY-027's place). The ruling after SH-43 keeps that route `core`, as both digests' tables read Bill Pay there and SH-67:78 keeps Capital's section. Open (section 3) |
| SH-61:64 | SH-E-20e44959 | the Roblox app (apps.shopify.com/roblox) | none (`makers`: none) | `extension-point` → `shows` | Roblox is named only as the venue (M-3; E89), as SH-66:76 reads a channel. Roblox stays its filler (rule 54). The checkout in Roblox keeps its own `core` line, SH-61:65 |
| SH-61:126 | SH-E-c71a7f07 | Shopify Forms | none | `core` → `shows` | as SH-54:48 |

The names `makers` was run on: Shopify Capital, Capital, Shopify Forms, Forms app, Shopify Flow, Flow, SimGym, Product Network, Launch Check, Shopify Subscriptions, Subscriptions app, ShipSurance, shipping insurance, Google & YouTube, Google channel, Privacy and Compliance, Privacy & Compliance, Customer Privacy, Shop Pay, Shopify Pay, Faire, TikTok, Shop Minis, Tolstoy, Videowise, Showday, Shop Quiz, Shopify Connector, Business Central, Roku, Actions Ads, Bill Pay, Roblox and quick count.

## 2. Shopify Capital in the Editions batches

**Capital's maker is held.** The router digest's table names three statements, which CM-PAY-026's cell holds as `own-service`:
- SH-C-092/responsible/SH-S-0484: 'Shopify provides merchant cash advances in the United Kingdom through our partner YouLend under the receivables purchase agreement.';
- SH-C-095/responsible/SH-S-0491: 'This application is provided by Shopify Commerce France SAS';
- SH-C-096/responsible/SH-S-0493: 'Applications for merchant financing are made available to you by Shopify Commerce Germany GmbH, which is a registered Credit Broker in Germany.'

The changelog's SH-E-136aca69 also states “We've just released Shopify Capital for merchants in France.”, a 'we' statement (changelog rule 10).

So, as a reading, Capital's own features are `own-service`, and its admin section and application stay `core` (the amendment notes; the ruling after SH-41). The lines below had Capital `shows` by the Editions digest's rule 21, 'named by its brand alone'.

| Line | Entry | The card's thing | Support |
| --- | --- | --- | --- |
| SH-50:92 | SH-E-56d61216 | 'Shopify Capital has increased funding for first-time borrowers' | `shows` → `own-service` |
| SH-51:55 | SH-E-2fc55a7c | 'Shopify Capital extends to Australia' (Australia) | `shows` → `own-service` |
| SH-52:74 | SH-E-c57999c8 | the product list heading of SH-E-2fc55a7c (Australia), placed by script | `shows` → `own-service`, following SH-51:55 |
| SH-62:78 | SH-E-3a01bbfe | monthly-fee loans | `shows` → `own-service` |
| SH-62:79 | SH-E-99955ac8 | Capital in Germany | `shows` → `own-service` |
| SH-62:80 | SH-E-561fac29 | customizable offers | `shows` → `own-service` |
| SH-64:95 | SH-E-56aefaa6 | the Capital flex account (US only) | `shows` → `own-service` |
| SH-64:98 | SH-E-eee389d8 | Capital in the Netherlands, Spain and Ireland | `shows` → `own-service` |
| SH-67:76 | SH-E-9a01503e | funding repaid from the Shopify Payments balance | `shows` → `own-service` |
| SH-67:79 | SH-E-1e0dab76 | Capital in France | `shows` → `own-service` |
| SH-60:115 | SH-E-df474732 | 'submit required application documents directly within the admin' | `core`, kept: Capital's application in the admin |
| SH-67:78 | SH-E-02b5a11a | repayment control, linked to admin.shopify.com/capital/account/repayment | `core`, kept: the admin's own Capital section |

SH-55:150 to SH-55:152 (Shopify Lending's products, `core;own-service`) already hold `own-service` on their own maker statement, SH-E-797024ee's 'Our new lending portfolio', and are kept.

## 3. Cases not settled here

1. **SH-55:120, Shop Quiz:** kept `extension-point`, since the card names it as the quizzes' source, as it names Tolstoy, Videowise and Showday. Its name carries Shop's brand, which names no maker either way, so the card doesn't show whether it is a third party's. Its listing, apps.shopify.com/product-recommendation-quiz-revenuehunt, isn't held, and an App Store address names no maker (Editions rule 53). The listing's developer would settle it. SH-55's case 7 also asks whether CM-MKT-023, the platform's own recommendations on the storefront, holds a quiz in a Shop Mini. The case decides a cell: the checker prints, for SH-55, that line 120 alone makes CM-MKT-023 on Shopify held and gives it `extension-point`.
2. **TikTok and Roku, venue or the third party's own feature.** I followed the Editions batches' reading of TikTok Shop as the venue (SH-54:36, SH-48:118). C46.3, the changelog digest's rule after SH-46, gives a channel named for a third party one line `shows;extension-point` where the post names the third party's own feature (Pinterest's Product Pins; Instagram's shopping stickers and product tags). Read so:
   - 'TikTok Shop' would make SH-55:110 `shows;extension-point`;
   - 'Actions Ads on Roku', if read as Roku's own ad product, would do the same for SH-59:119.
3. **Lines outside the candidates that rest on the same apps with no maker held.** They are left as they are, since only the candidates and the Capital lines were to change:
   - Shopify Forms, `core`: SH-36:217 (SH-E-062d5c52) and SH-37:44 (SH-E-b94bb020), both on CM-MKT-005. Their readings name Forms without a maker wording, which the candidates' search missed. By the same ruling they would be `shows`.
   - Order Printer, `core`: SH-37:126 (SH-E-824336c3, CM-ORD-009), 'a branded app with no maker stated, core by what the post shows'. The ruling after SH-43 names Order Printer. It would be `shows`, unless printing from 'the Orders page within your Shopify Admin' is read as the admin's own.
   - Roku, `extension-point`: SH-50:210 (SH-E-7ae13922) and SH-52:33 (SH-E-2a23aea3, placed by script from it) say 'TV streaming advertising campaigns directly on the Roku streaming platform'. Read as SH-59:119 now is, they would be `shows`. SH-42:209 (SH-E-37405913) names 'Roku Ad Manager', Roku's own service the app connects to, which may keep `extension-point`, as Google's own services through the Google app do.
   - TikTok, `extension-point`: SH-55:111 (SH-E-320d69a9, CM-CHN-004) is the same card's 'Sync your products to' TikTok, read as done through the app. It would follow SH-55:110.
   - Faire: SH-55:67 (CM-B2B-001, `extension-point`) is Faire's own wholesale selling, the third party's own feature, by C46.3's split. If Faire is read as only a venue there too, it would be `shows`.
4. **Bill Pay's maker.** CM-PAY-027's cell holds Melio as Bill Pay's provider, `outside`: SH-S-7200, 'Shopify Bill Pay is provided by Melio', and 'powered by Melio' (SH-S-0499, SH-S-7201). The digests' tables say 'none held', and SH-60:108's reading says 'its maker a gap'. The amendment would decide whether Bill Pay's own features are a third party's service in the admin, and with them its lines at `apps/bill-pay` (such as SH-54:69's CM-APP-007 `core`).
5. **Capital outside the Editions batches** (not read for this alignment):
   - The changelog's Capital posts are `core`: SH-35:43, SH-35:57, SH-35:141, SH-35:177, SH-36:13, SH-36:187, SH-37:76, SH-37:157 and SH-46:108. Most are on applying 'directly through their Shopify admin', the application. SH-35:57's post is the 'we' statement above. Whether any of them is Capital's own feature (`own-service`) rather than its admin application is for the amendment.
   - The pricing pages' footnote lines on Capital are `shows`: SH-69:41, SH-72:25, SH-73:96, SH-74:32, SH-76:27, SH-78:185, SH-79:195 and SH-94:39.
   - SH-30:76 is a help page's 'Shopify Capital flex accounts are in early access'. It bears on SH-64:95 and SH-67:78, whose cards state no early access.
6. **Shopify Product Network.** The concern map's SH-C-133/where/SH-S-7252, 'Your ads can run across the Shop app, Shop website, Shopify Product Network, and optional third-party placements.', sets it beside the Shop app, apart from third parties' placements. It names no maker: a lead, not a maker statement.
7. **The Google app's kept lines** (SH-39:5, SH-42:11, SH-50:168, SH-54:14, SH-54:26) still say the app's maker isn't stated or named. Their supports stand. Their readings predate the corrections after SH-45, and weren't edited, since no column of a kept line was to change.
8. **CM-ONB-004.** SH-36:175 was the line giving CM-ONB-004 `core` in SH-36. It is now `shows`, so the checker prints 'CM-ONB-004@shopify holds nothing: becomes held, by line 175' for SH-36. SH-38:4 ('AI Store Setup Tool', `core`) still gives the cell `core`.

## 4. The checks

`python3 -I method/held_entries.py check --platform shopify --batch <b>` after the edits:

| Batch | The checker's last line |
| --- | --- |
| SH-34 | 130 of 130 entries placed; 0 problems |
| SH-35 | 130 of 130 entries placed; 0 problems |
| SH-36 | 130 of 130 entries placed; 0 problems |
| SH-37 | 130 of 130 entries placed; 0 problems |
| SH-38 | 130 of 130 entries placed; 0 problems |
| SH-39 | 130 of 130 entries placed; 0 problems |
| SH-40 | 130 of 130 entries placed; 0 problems |
| SH-41 | 130 of 130 entries placed; 0 problems |
| SH-42 | 130 of 130 entries placed; 0 problems |
| SH-50 | 130 of 130 entries placed; 0 problems |
| SH-51 | 92 of 92 entries placed; 0 problems |
| SH-52 | 98 of 98 entries placed; 0 problems |
| SH-54 | 82 of 82 entries placed; 0 problems |
| SH-55 | 81 of 81 entries placed; 0 problems |
| SH-57 | 86 of 86 entries placed; 0 problems |
| SH-59 | 80 of 80 entries placed; 0 problems |
| SH-61 | 82 of 82 entries placed; 0 problems |
| SH-62 | 84 of 84 entries placed; 0 problems |
| SH-64 | 82 of 82 entries placed; 0 problems |
| SH-67 | 99 of 99 entries placed; 0 problems |

The checker printed nothing new about the edited lines but two NOTEs. SH-38:73's NOTE, 'core on a product named with the platform's brand', is answered in section 1: its `core` is the admin's own product page. SH-61:64's NOTE, on its first lead CM-APP-010, is about its capability, which didn't change. The CHANGES lines on CM-ONB-004 (SH-36) and CM-MKT-023 (SH-55) are in section 3.

## The coordinator's check

Measured: 17.0 million tokens over 69 requests. Every changed batch's checker prints no problem.
- **Read against the commit before the edits (94dddff1):** 48 lines changed in all, only in their `supports`, `filler` and `reading` columns, no line moved: `core` to `shows` 26, `extension-point` to `shows` 8, `shows` to `own-service` 10 (Capital), `core` to `own-service` 3, `core` to `core;own-service` 1.
- **Kept:** the 42 lines this record changes and the 14 it keeps, each by the ruling after SH-43, the corrections after SH-45 and the digests' first-party tables.
- **The lines the candidates missed, aligned by the coordinator (open case 3):** Shopify Forms' SH-36:217 and SH-37:44 and Order Printer's SH-37:126 to `shows`, no maker statement held; Roku's SH-50:210 and SH-52:33 and TikTok's SH-55:111 to `shows`, the venue their filler, as SH-59:119 and SH-55:110. SH-42:209 keeps `extension-point`, since it names Roku Ad Manager, Roku's own service; Faire's SH-55:67 keeps Faire's own wholesale selling.
- **The other open cases** stand as the record leaves them: Shop Quiz (SH-55:120) stays `extension-point`, a third party's work through Shop Minis by E124; Bill Pay's provider, Melio, is held in CM-PAY-027's cell (SH-S-7200, `outside`), so the digests' 'none held' is read as no maker statement naming Shopify; Product Network is a lead.
