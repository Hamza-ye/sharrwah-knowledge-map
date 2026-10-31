# Held pass, Shopify, batch SH-94: notes

25 entries of `plan-page-public` (effort high), the last of its 50, in `items.jsonl` lines 662 to 687: the same page, record and sources as SH-93 (its notes). This file says only what differs from SH-93's notes. Entry numbers below are the batch's order (`held_entries.py show --platform shopify --batch SH-94`).
- **1 to 15:** the FAQ, from the first question's answer to the eighth answer: seven questions (h3) and eight answers (div), lines 662 to 676.
- **16 to 20:** the closing banner: its heading 'Turn plans into progress', its trial and credits, its email field's label, its button and its disclaimer (lines 677 to 682).
- **21 to 25:** the page's disclaimer: Bill Pay's provider, the banking partners, and the footnotes of the table's finance rows ¹, ³ and ² (lines 683 to 687), the page's end.

**Placed:** 25 entries in 38 lines. 23 entries are on capabilities, one of them with a second line on the new thing (17), and 2 are `out` (18, 20). 8 entries take more than one line.
- Supports, by line: 14 `core`, 17 `shows`, 5 `outside`; no `own-service` or `extension-point`.
- 5 lines carry fillers (the disclaimer's providers and banks) and 10 carry qualities.
- The checker raises no `CHANGES`.

**Sources read beyond SH-93's:**
- **The twins' lines:** SH-72's lines 2 to 17 (the FAQ), SH-74's line 30 (Balance), SH-78's lines 179 to 185 (the disclaimer), and SH-92's lines 2, 3, 10, 11 and 37.
- **The twins' texts in `entries.tsv`,** compared by script with each entry's (the 31 October markup's `<br />`, links and logo taken out). Each answer and disclaimer is its twin's in the same words, but for the Balance date (below).
- **`source.html`:** the closing banner's markup (line 4): its subhead's two arrow images, with an empty `alt`, and its form, which posts to https://admin.shopify.com/signup, with two submit buttons; Melio's logo, its `alt` 'Melio'.
- **`held_index.py`** for the three pages the disclaimer links: Issuing Bank Terms, Program Terms and Reward Terms are all held (observed-sh's `20260930T050139Z-shopify-com-pages` and `20260930T003703Z-help-en-md`).

## Rules my lines follow, beyond SH-93's

- **P13, the FAQ:** each answer takes its twin's lines, and each question the twin's line on the capability it asks about.
- **P16. The closing banner** repeats the hero (SH-68's notes read the 31 October banner, which no entry holds, as the trial again):
  - Its heading takes CM-PLN-001 `core`, as the hero's heading “You've got plans. Us too.” does (SH-92's line 2).
  - Its subhead takes two lines:
    - the trial, CM-PLN-001 `core` with its qualities, as the hero's 'Try 3 days free, then $1/month for 3 months.';
    - the credits, SH-68's new thing, at the highest of the cards' maximums, the site alone its scope, since the banner names no plan.
  - Its button takes P3's two lines. CM-ACC-001 rests on the form's action, admin.shopify.com/signup, since the button has no link; it takes no term, since 'signup' isn't in the entry's text.
  - Its field's label is a UI string (P8), and its disclaimer the sign-up's consent to Shopify's own mail, which the 31 October hero's line gives no line (SH-70's line 96): both are `out`.
- **The disclaimer:** each paragraph takes its twin's lines, which SH-78 split from one item, with the twin's scope, `www.shopify.com and U.S.` for WebBank (the rulings after SH-69 and SA-53).

## New things

**`new:Earn 1% back on all sales as subscription credits`** (SH-68's), 1 line: the closing banner's credits, entry 17 (SH-E-03946376).
- **Its words:** 'Earn up to $10,000 in credits', the Advanced card's maximum (SH-92's line 37), with no plan named.
- SH-68's and SH-92's notes give the rest: its place of its own (the comparison table's row), domain, area, parent and the terms searched.

## Entries I couldn't tell, and what would settle each

- **The questions' supports** (2, 4, 6, 8, 10, 12, 14), P13.
  - The question takes its twin's line on the capability it asks about. Three are `core`: 10, PCI compliance; 12, the domain; 14, hosting.
  - The other reading is `shows` for every question, since a question states nothing by itself.
  - No cell changes either way.
- **4, 'Can I cancel or change my subscription anytime?', on CM-PLN-002 alone.**
  - Its answer's second line, the account's closure on CM-ONB-002, is the other line it could take, by its word cancel.
  - I left it to the answer, which names the account.
- **16, 'Turn plans into progress', CM-PLN-001 `core`.** The other reading is `out` by P9: a slogan over several things, the trial, the credits and the sign-up. No cell changes.
- **17's credits, the site alone as scope.** $10,000 is the Advanced card's maximum, so `Advanced;www.shopify.com` is the other scope. That reading rests on the cards, not on the banner's words.
- **18, the email field's label, `out`.** The other reading is CM-ACC-001 `shows`, as the sign-up form's field.
- **19, CM-ACC-001 `shows` with no term**, by the form's action. Without the ruling after SA-19's reading for a form, it keeps only its CM-PLN-001 line.

## A structure whose items and sources disagree

- **'Melio'** in entry 21's text is the logo's `alt`, not text on the page (source.html, line 4).
- **Items 680 and 681** are the form's two buttons (an inline one and a second one), one entry.
- **The answers' paragraphs** run together in the items ('pricing.Additionally', 'account.If'), where the source breaks them; the 31 October twins hold `<br />` there.
- **The Balance footnote** states 'accurate as of September 28, 2026' here and October 29, 2026 in its twin a month later (SH-74's line 30), the only difference between the two (P12).

## What the sources state that no entry holds (for the second stage)

- **The closing form's field** is named `pricing-signup-conversion`, with `autoComplete` email (source.html, line 4): the sign-up's own field, a lead for CM-ACC-001's sign-up only.

## Problems with the brief or the script

- **`earlier` finds no FAQ twin** (SH-93's notes).
- **No B-extent conflict.**

## The checker's lines, read again

- **No `CHANGES`.**
- **`NOTE`, line 13** (entry 8): its first lead, CM-MKS-009 (countries' reference data), holds nothing on Shopify. Its reading now says the lead is market data, not where the platform serves.
- **`NOTE`, line 24** (entry 15's checkout): `core` on a product named with the platform's brand, Shopify Checkout. Its reading now says it is `core` by the platform's own checkout, whose settings page the cell cites (SH-68's R9), not by the brand.
- **`NEW`:** Earn 1% back on all sales as subscription credits, 1 line.

## The coordinator's check (31 October 2026, after the batch)

- **The checker passes:** 25 of 25 entries, no problem and no `CHANGES`. The check is SH-93's, which covers both batches, their rules and their cost.
- **The new thing** takes one more line, the closing banner's credits, on the site alone.
