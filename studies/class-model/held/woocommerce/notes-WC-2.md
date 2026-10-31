# Notes: held pass, WooCommerce, batch WC-2 (`core-profiler-free-extensions`, entries 76 to 151)

**What the batch holds:** 76 entries of `woocommerce/core-profiler-free-extensions`: items.jsonl lines 4 to 7 (other-product-class@0d79b794f:woocommerce/structures/core-profiler-free-extensions/items.jsonl), the free extensions the set-up offers for a store in SA (21 entries), OM (21) and YE (21), and the first 13 of the item labelled EG: its bundles obw/basics, obw/grow, task-list/reach and task-list/grow, with their plugins. WC-3 holds the rest of that item, from its bundle obw/core-profiler.

**WC-1 read first, as corrected.** I read WC-1's placements and its notes to the end, "The coordinator's corrections". Every entry of this batch but the PayPal card has the same text as WC-1's US:CA entry with the same bundle and plugin key. I compared every field but `within`, `image_url` and `learn_more_link`, `is_installed` and `is_activated` included (all `false` here). So each takes WC-1's US:CA lines, with its own entry id and scope, and the same readings. The corrections need no change here: this batch has no ShipStation, and Jetpack's CM-OPS-001 lines are dropped in WC-1 too.

**Count:** 76 entries, 156 lines.
- By entry: every entry has at least one `capability` line. No entry is `out`. Eleven entries have a `new` line beside their capability lines.
- By line: 145 `capability` and 11 `new`.
- By capability: CM-APP-011 39, CM-CHN-004 25, CM-ONB-004 19, CM-MKT-010 17, CM-MKT-007 11, CM-MKT-006 8, CM-TRU-019 7, and 4 each for CM-MKT-022, CM-MKT-009, CM-MKT-005 and CM-CUS-001. CM-PAY-013 takes 3.

## What differs from WC-1

- **PayPal Payments in full** (WC-E-86e399e0 SA, WC-E-df65cbbe OM, WC-E-7f863f6e YE).
  - Its key is `woocommerce-paypal-payments`, not WC-1's `woocommerce-paypal-payments:wallet-only`.
  - Its description is 'Offer more ways to pay with this all-in-one checkout solution', and its label 'Maximize conversions with PayPal Payments'.
  - It goes on CM-PAY-013 as `extension-point`, with PayPal as its filler. The cell already cites the same extension: PayPal Payments by PayPal, the official, all-in-one checkout solution (WC-S-0911), `extension-point`. That is rule 2: a cell's reading that cites the same term.
  - `is_built_by_wc: false` names no maker. `install_options` (`woocommerce_paypal_branded: profiler`) and `install_priority` go in `reading`.
  - `caps --terms "all-in-one; checkout solution; conversions; conversion; more ways to pay; paypal payments"` finds only CM-PAY-013 for the extension. 'Maximize conversions' names no capability: conversion here isn't CM-MKT-008's attribution or CM-MKT-012's paid conversions.
- **The bundles' plugin lists.**
  - obw/basics holds Jetpack only. US:CA's held WooPayments, WooCommerce Shipping and Jetpack.
  - obw/core-profiler holds PayPal Payments, Jetpack, Pinterest, Klaviyo, Google, Snapchat Ads and Reddit Ads. It has no WooPayments, WooCommerce Shipping or WooCommerce Tax.
  - The containers' readings name the plugins of each bundle.
- **Scope:** each entry's country, in the source's identifiers: `SA`, `OM`, `YE`. The EG entries are scoped `YE` (next section).

## A structure whose items and sources disagree: the item labelled EG

- **The item:** items.jsonl line 7 is labelled `store_country: EG`.
- **The run's script** (20261029T024814Z-free-extensions-en/commands.jsonl, line 2) sets each country in turn with `POST /wc-analytics/settings/general/woocommerce_default_country {value: c}`, then reads `/wc-admin/onboarding/free-extensions`. It doesn't check the POST's answer.
- **The POST of EG was refused.** Its answer, `answers/belfast-portal-fruit-sell.trycloudflare.com/index.php/ae3f76a93249675edacd86e2a4b9c6f20e084911736eed454da90605511e9daf.json`, is `{"code":"rest_setting_value_invalid","message":"An invalid setting value was passed.","data":{"status":400}}`.
  - The setting's own options (the YE POST's answer, `7d2f0fb2679f4956020c05c460bfefcfa4cb06e3cc5e502fa0c03d3bdc220f4b.json`, whose `value` is `YE`) hold Egypt only with a state, `EG:EGALX` to `EG:EGWAD` (27 keys). They hold no `EG`.
  - So the free extensions read next (02:48:58.731Z) are the store's at YE. This is a reading: a refused setting is left as it was.
  - The answer bears it out: SA, OM, YE and "EG" share one answer file, `b714f634...json`, whose four calls answers.jsonl line 20 lists.
- **What I did:** the source governs (rule 1). The 13 EG entries (WC-E-2d492894 to WC-E-dc8f468f) take YE's lines with scope `YE`, and each reading says why.
  - WC-3 holds the rest of the same item (its obw/core-profiler bundle), and the same applies to it.
  - The repository's own run note says otherwise: `index/runs.tsv`, line 7, and `run-notes.tsv`, line 7, say 'SA, OM, YE and EG PayPal Payments in full'. That is the capture's note, not the platform's.
- **What would settle it:** a capture with an Egyptian state, such as `EG:EGC`. This pass sends no capture request, so this is for the coordinator.
  - If the coordinator would rather drop these entries than scope them YE, they repeat YE's lines in full, so YE's cells lose nothing.

## New things

These are the same as WC-1's, with the same names, each `shows` with no place of its own (rule 2). Each is decided with WC-1's.

| new | entries | place of its own | proposed domain / area / parent (a reading) | name (English; WooCommerce is held in English only) | terms searched |
| --- | --- | --- | --- | --- | --- |
| `new:speed` | WC-E-30d67b11 (SA), WC-E-a7de4125 (OM), WC-E-00a7b08d (YE), WC-E-d88e68a3 (EG, scope YE). Jetpack: 'Enhance speed and security' | none: a line of a card | G OPS; parent CM-OPS-003 | speed | WC-1's: speed; site speed; page speed; performance; CDN; image optimization |
| `new:backups` | WC-E-3ff0b1b3 (SA), WC-E-97972f57 (OM), WC-E-edc29269 (YE). Jetpack: 'Keep your store online with full security and backups' | none: a line of a card | G OPS; parent CM-OPS-001 | backups | WC-1's: backup; backups; restore; downtime |
| `new:schedule posts` | WC-E-67b1b409 (SA), WC-E-7bd4b394 (OM), WC-E-04be69fc (YE), WC-E-dc8f468f (EG, scope YE). Kliken: 'schedule a month of posts' | none: a line of a card | D MKT; parent CM-MKT-005 or CM-MKT-010 | schedule a month of posts | WC-1's: social media post; social post; schedule posts; scheduling; posts; Facebook; Instagram |

These entries' leads are the same as WC-1's (CM-ACC-010, CM-TRU-001, CM-TRU-010, CM-MKT-005, CM-PLN-001, CM-DVT-004). I read their cells again and kept to WC-1's reasons:
- CM-ACC-010 is the Jetpack connection, not the plugin.
- CM-TRU-001 is sign-in security.
- CM-PLN-001 matches on Kliken's own plans.
- CM-DVT-004 matches only on free and launch.

## CHANGES lines, and what I decided on each

Each is WC-1's CHANGES again, on the same texts, for SA, OM and YE (EG scoped YE). I kept each, for WC-1's reasons:

- **CM-APP-011 gains own-service** (39 lines). Kept.
  - For the extensions with `is_built_by_wc: true`, the maker is WooCommerce, by the ruling (3799.js; DefaultFreeExtensions.php, line 123). These are Google for WooCommerce, Pinterest for WooCommerce, MailPoet, Snapchat Ads and Reddit Ads.
  - For Jetpack, the maker is Automattic: WC-S-0594 names it, and WC-S-0461 places it in the group (M-1).
- **CM-CHN-004 gains own-service** (25 lines: Google, Pinterest and Reddit). Kept, as WC-1's. `is_built_by_wc: true` is the maker statement the cell lacked, and the venue is the filler.
- **CM-MKT-010 gains own-service** (13 lines: Google, Snapchat Ads, Reddit Ads). Kept. Kliken's 4 CM-MKT-010 lines are `extension-point`.
- **CM-MKT-009 becomes held, extension-point** (Kliken's 'Meta Ads & Pixel by Kliken'; lines 26, 69, 112, 155). Kept, as WC-1's.
- **CM-TRU-019 gains own-service** (Jetpack, 7 lines). Kept, as WC-1's.

The checker's other NOTEs repeat WC-1's, and I read each:
- **CM-CHK-007, the first lead of Mailchimp's card, holds nothing.** The card names recovery, which CM-CHK-007's note sends to CM-MKT-022, not the carts' records.
- **CM-MKT-011, the first lead of Snapchat's card, holds nothing.** The card builds no audiences.
- **The containers' counts join bundles by title.** "Grow your store" counts obw/grow, task-list/grow and obw/core-profiler together, as in WC-1.

## Entries I couldn't tell, and what would settle each

- **PayPal Payments in full on CM-PAY-011 as well?** 'Offer more ways to pay with this all-in-one checkout solution' may describe a gateway the merchant connects, which is CM-PAY-011's thing (Stripe by Stripe, WC-S-0910, is cited there), more than PayPal as a method. I kept to the model's own placement of the same extension (WC-S-0911, on CM-PAY-013) and gave no CM-PAY-011 line. What would settle it: the coordinator's reading of the model's split between WC-S-0910 and WC-S-0911, or the extension's product page (`learn_more_link`, not held).
- **WC-1's doubts carry over unchanged.** They are Klaviyo on CM-CUS-001, Kliken on CM-MKT-006, Mailchimp on CM-MKT-005, MailPoet's follow-ups, Snapchat on CM-MKT-010, and Jetpack's `requires_jpc`.

## For the second stage, and gaps

- **No maker is stated for the third parties' extensions:** Klaviyo, Mailchimp, Kliken and PayPal Payments (`is_built_by_wc: false`), as in WC-1. Their `learn_more_link` pages on woocommerce.com aren't held.
- **WooPayments, WooCommerce Shipping and WooCommerce Tax are not offered for SA, OM or YE** in these answers, where US:CA has all three (and AE WooPayments).
  - An absence isn't a statement, so it is placed nowhere.
  - It is a lead to compare with CM-PAY-002's supported countries and CM-TAX-002's list (WC-S-0635).
  - The set-up's own warning for a store located in Yemen names 'Payment issues' (`index/runs.tsv`, line 2, run 20261029T020454Z-store-setup-en, steps 60 and 64). That is a run step, not an entry here, so it is a lead.
- **Egypt's free extensions aren't held** (above). A capture with `EG:<state>` would hold them.
- **The run's step pages** (steps/001 and 002) are the WooCommerce home, as WC-1 noted. Nothing in them is new to this batch.

## Problems with the brief or the script

- **The checker doesn't read a structure's sources against its items.** The EG item's refused write could be seen only in answers.jsonl and the POST's answer. The brief's rule 1 ("the source governs") caught it; the checker couldn't.
- **The checker's NOTE list is cut at "... and 5 more".** The hidden five are the EG lines of the same kinds as those shown: its containers, Mailchimp's CM-CHK-007 lead and Kliken's new thing with leads.
- **B-extent and this brief read the same on every case here**, as far as I found.

## The coordinator's rulings (30 October 2026, after the batch)

- **The item labelled EG is the YE store's answer: confirmed, and the entries stay YE's.** The run (`raw/runs/20261029T024814Z-free-extensions-en`, `answers.jsonl`) set the store's country in turn: US:CA, GB, AE, SA, OM and YE each answered 200, and `{"value":"EG"}` answered 400, `rest_setting_value_invalid` (`answers/.../ae3f76a9….json`). The free-extensions answers after SA, OM, YE and EG are one file, `b714f634….json`, so SA, OM and YE are offered the same list, and the EG item is YE's again. Egypt's list isn't held. A capture that sets a state, such as `EG:C`, would hold it. That is a gap for the market subjects, since it can only add Egypt's scope to cells the other lists already place, so no request is made now (`evidence-map.md`). WC-3 places the rest of the item the same way.
- **PayPal Payments in full takes a CM-PAY-011 line** beside its CM-PAY-013 line: 'Offer more ways to pay with this all-in-one checkout solution' is a third party's payment solution the merchant connects (rule 2). The cell already places it `extension-point`, so no cell changes.
