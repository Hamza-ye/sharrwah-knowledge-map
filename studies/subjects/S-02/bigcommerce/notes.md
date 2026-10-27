# S-02, phase A: bigcommerce (BC)

BigCommerce is read "from what is recorded": statements come from `recorded.tsv` and the Q1 index; a page is read further only to close a gap instead of routing it to the founder (when `method/held_index.py` finds it held and readable), or, under rule 5, where a recorded excerpt is too short to show what bears on the subject.

## Documents read, in order

1. `studies/subjects/S-02/briefs/A-one-platform.md` (the brief), in full.
2. `studies/subjects/S-02/bullets.tsv`, in full.
3. `studies/subjects/S-02/bigcommerce/recorded.tsv` (R001 to R081), in full.
4. `studies/subjects/S-02/bigcommerce/recorded-citations.tsv`, in full.
5. `studies/concern-map/platforms/bigcommerce/concerns.tsv`: the concern ids, names and platform terms (columns 1 to 3), all 88 concerns.
6. `studies/concern-map/platforms/bigcommerce/statements.tsv`: by script, not loaded whole. Every statement of BC-C-005, 007, 008, 025, 026, 029, 030, 034, 040, 056, 066, 068, 069, 070, 072, 073, 077, 080 to 087; and, for every other concern, the statements whose identifier, statement or scope holds a word on countries, regions, locations, addresses, jurisdictions, markets, currencies, languages, channels or storefronts. The statements of BC-C-038, 039, 047, 048, 074, 075 and 079 are all in `recorded.tsv`.
7. `studies/concern-map/platforms/bigcommerce/citations.tsv`: by script, the citations of the index statements copied (source, locator, access path) and their notes in `statements.tsv`.
8. `evidence/product-class/runs/*/manifest.tsv`: the addresses on bigcommerce.com, bigcommerce.co.uk and commerce.com that the capture runs hold (an index of what is held, not a reading of the pages).
9. `method/check_subject.py`, `method/held_index.py`, `method/corpus_search.py`, `method/quote_check.py`: their usage notes, and the checker's rules on `from` and `conditions`.
10. https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/store-information/v2.md, held at sharrwah-knowledge-map@85d0ae478f5ad60d165bb3fbc1e2c8ccde6790a6:evidence/product-class/runs/20261012T0419Z-q1-bigcommerce-sources/items/043-docs.bigcommerce.com (read 2026-10-27, as `quote_check.py --text` prints it). The page holds only its introduction and a pointer to Store Settings for channel-specific overrides: no field of the store's address or country.
11. https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/store-information/v3.md (item 044 of the same run): its introduction is on store metafields only.
12. https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/settings.md (item 040): the table of Settings V3 resources; no field list.
13. https://docs.bigcommerce.com/developer/docs/admin/store-configuration/settings/store-configuration.md (item 075), in full, read again under rule 5 (R019's excerpt) and for the gaps of (a) and (b): S02-BC-097 to S02-BC-103.
14. https://docs.bigcommerce.com/developer/docs/integrations/webhooks/event-reference/events.md: the Stores section and its "Store information updated events" list (S02-BC-106).
15. https://www.bigcommerce.com/start-your-trial/, held in run 20261019T051155Z-proposals-Q6-bigcommerce (item 001), in full: S02-BC-107, S02-BC-108. The form has no field for a country.
16. `python3 -I method/corpus_search.py bigcommerce "store country" "store_country" "store location" "store address" "store's address" "store profile" "country of residence" "located in" "change your country" "store's country" --max 40` (2026-10-27): 24 documents. Read from them: store-configuration.md (above); the support articles Getting-Started-with-Localization-on-Multi-Storefronts, Fastlane-by-PayPal, Manual-Tax-Setup and Automatic-Tax-Setup (the passages on the store's location and shipping origin address), Store-API-Accounts and Date-and-Timezone-Settings (the lines naming the store profile). The other matches name the store profile's email address or phone number, or a payment method's own country requirement already recorded in S-01.
17. https://support.bigcommerce.com/s/article/Getting-Started-with-Localization-on-Multi-Storefronts, held in run 20261013T053949Z-s01-bigcommerce-help-founder-machine (item 029), in full, from its `text.txt`: S02-BC-109 to S02-BC-119.
18. https://docs.bigcommerce.com/developer/docs/admin/multi-storefront/msf-international-enhancements/overview.md, held in run 20261019T000455Z-proposals-Q1-bigcommerce (item 001), in full: S02-BC-120 to S02-BC-122.
19. https://support.bigcommerce.com/s/article/Fastlane-by-PayPal (run 20261013T053949Z-s01-bigcommerce-help-founder-machine, item 026), its Requirements, Setup and FAQ country list, from `text.txt`: S02-BC-123 to S02-BC-128.
20. https://support.bigcommerce.com/s/article/Manual-Tax-Setup (item 034), its tax-zones section, from `text.txt`: S02-BC-129, S02-BC-130. https://support.bigcommerce.com/s/article/Automatic-Tax-Setup (item 012): the line on the shipping origin address in a store's shipping settings (already stated by S02-BC-053; nothing new recorded).
21. https://support.bigcommerce.com/s/article/Store-API-Accounts (item 044) and https://support.bigcommerce.com/s/article/Date-and-Timezone-Settings (item 023): the lines naming the store profile and the Manage Settings permission for date and timezone settings; nothing recorded (neither names the store's country).
22. https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/channels.md (run 20261012T0419Z-q1-bigcommerce-sources), in full: S02-BC-136 to S02-BC-140 (channel statuses, deletion).
23. https://docs.bigcommerce.com/developer/docs/admin/multi-storefront/overview.md (same run), its Channels and Sites sections: S02-BC-131 to S02-BC-135.
24. https://support.bigcommerce.com/s/article/Multi-Storefront (item 035), chapter 1 in full, from `text.txt`: S02-BC-141 to S02-BC-147.
25. https://support.bigcommerce.com/s/article/Getting-Started-Channels (item 027), its Multiple Storefronts section: S02-BC-148.
26. https://support.bigcommerce.com/s/article/Platform-Limits (item 038), in full: S02-BC-149, S02-BC-150.
27. https://www.commerce.com/terms/ (run 20261012T0419Z-q1-bigcommerce-sources), as `quote_check.py --text` prints it: the Contracting Entity table and section, Governing Law, the Arbitration Agreement's applicability and the sanctions clause: S02-BC-151, S02-BC-152.
28. https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/geography.md (same run), in full: its introduction only (S02-BC-047); no country record or address format.
29. https://support.bigcommerce.com/s/article/Editing-Form-Fields (item 024), its Address Fields and Adding and Editing Fields sections, from `text.txt`: S02-BC-153 to S02-BC-157.
30. `python3 -I method/corpus_search.py bigcommerce "verify your" "verification" "verified" "KYC" "know your customer" "proof of address" "business verification" "identity" --with "country" "countries" "located" --max 40` (2026-10-27): 12 documents. Read the matching lines of Connecting-with-BigCommerce-Payments (KYC status of a BigCommerce Payments account), Fastlane-by-PayPal (a shopper's verification code), payments/overview.md (stored instruments); none checks the store's country.
31. `python3 -I method/corpus_search.py bigcommerce "store_country" "Localization settings" "hosting region" "data center" "hosted" "change the country" "change country" "change your country" "store's country" "migrate your store" --max 40` (2026-10-27): 40 documents and more past the cap. "store_country" matches only store-configuration.md; "change country" matches the bigcommerce.com site's own country selector ("Change country" in the page header); "hosted" matches pages on BigCommerce-hosted storefronts. None says who can change the store's country.
32. `python3 -I method/corpus_search.py bigcommerce "address format" "address formats" "postcode" "postal code" "zip code" "address validation" "address fields" --with "country" "countries" --max 40` (2026-10-27): 7 documents: Editing-Form-Fields, geography.md, Manual-Tax-Setup, Getting-Started-Payments, Connecting-with-Stripe-OCS, B2B-Edition-Settings, Connecting-with-Braintree. Their lines on address fields were read: none gives an address format per country.
33. Held status checked with `method/held_index.py` (2026-10-27): not held are https://support.bigcommerce.com/s/article/Localization-Settings, https://support.bigcommerce.com/s/article/Store-Profile-Settings, https://support.bigcommerce.com/s/article/International-Enhancements-for-Multi-Storefront, https://support.bigcommerce.com/s/article/Store-Settings, https://support.bigcommerce.com/s/article/Store-Profile, and the Settings V3 pages .../management/settings/store-profile.md, .../settings/store-profile/get-settings-store-profile.md, .../settings/store-profile/update-settings-store-profile.md, .../settings/store-locale.md, .../settings/store-locale/get-settings-store-locale.md and .../settings/store-locale/update-settings-store-locale.md.
34. https://support.bigcommerce.com/s/article/Checkout-Settings (item 016), the lines on the country drop-down, phone number validation, Google Address Autocomplete and the enhanced checkout's address sections, from `text.txt`: S02-BC-158 to S02-BC-161.

## Recorded statements left out (rule 5: they bear on no bullet)

R013, R014, R015, R017, R018, R020, R023 (Settings V3 and Store Information V2 resources, scopes and introductions whose excerpts name no country, address or market; the store-configuration page read in their place gives S02-BC-097 to S02-BC-103). R011, R012 (partners adapting to multi-storefront; the reason for no breaking changes), R022 and R026 (the Translations API's availability and scope: no statement read ties translations to a market), R033 (settlement currency), R035, R036 (conversion fee and bank rate), R041 (Stripe OCS narrowing the payment methods), R058 (cryptocurrency payments enabled for all merchants), R069 (PayPal Braintree approval), R071 (auto-migration to BigCommerce Payments), R078 (PayPal order sync).

## What couldn't be read

- Not held, so not read under "from what is recorded" (rule 9): the support articles Localization-Settings, Store-Profile-Settings, Store-Settings and International-Enhancements-for-Multi-Storefront (linked from the localization article), and the Settings V3 store-profile and store-locale endpoint pages; the Geography API's endpoint pages. They are the routes of S02-BC-G01 to S02-BC-G03.

## Problems with the brief or the tools

- `quote_check.py --text <url>` prints only the first file of a capture. For the support.bigcommerce.com pages of run 20261013T053949Z-s01-bigcommerce-help-founder-machine that file is `raw.html`, the Help Center's loading shell ("Loading … Sorry to interrupt … CSS Error"); the page's text is in the `text.txt` beside it, which the checker also searches. Those pages were read from their `text.txt` and are cited by their live URL.
- `corpus_search.py bigcommerce` searches captured pages whose host matches bigcommerce.com, commerce.com or bitpay.com: the held pages on bigcommerce.co.uk (https://www.bigcommerce.co.uk/pricing/ in run 20261019T000455Z-proposals-Q1-bigcommerce, https://www.bigcommerce.co.uk/payments/bigcommerce-payments/ in run 20261012T104936Z-s01-sources) are outside its searches.
- Rule 5 lets a recorded source be read again when its excerpt is too short; "from what is recorded" lets a page be read further only to close a gap. store-configuration.md was read again under both (R019's excerpt, and the gaps of (a) and (b)).

## Check

`python3 -I method/check_subject.py` on a copy (`bullets.tsv` and this folder) with every capture run, 2026-10-27: 161 statements, 3 gaps, 217 quotes found, no line of level error. One line of level review: the 2 claims of absence await the phase A3 audit.


## Absence audit (phase A3, 2026-10-27)

Brief: `studies/subjects/S-02/briefs/A3-absence-audit.md`, with `briefs/A-one-platform.md` for what is recorded. Audited: the absences S02-BC-N01 and S02-BC-N02. The gaps S02-BC-G01 to S02-BC-G03 are all of kind `page not read`, outside the audit. One row per claim in `absence-audit.tsv`. Added: statements S02-BC-162 to S02-BC-204, citations S02-BC-C218 to S02-BC-C263. Changed (step 5): S02-BC-009's `conditions` take S02-BC-164 to S02-BC-172, S02-BC-175, S02-BC-177 and S02-BC-179, the new statements that name multi-storefront or storefront channels.

### What was found

- S02-BC-N01 (a place among what defines a channel; a channel type for a place): confirmed. The Create Channel endpoint, read live, requires name, type and platform, and gives `type` as an enum of pos, marketplace, storefront and marketing (S02-BC-162), without the `custom` that the overview's list names; its channel object has no field for a country, region or place. The Catalyst Multi-Storefront Overview and Setup, read live, sell into countries through a storefront channel per country and that channel's locales, domain, products, price lists and currencies (S02-BC-163 to S02-BC-182). carts.md ties "selling in different markets" to a cart's locale (S02-BC-183, S02-BC-184). The Buy Online, Pick up in Store overview states that different warehouse locations and inventory can't serve different storefront channels (S02-BC-185).
- S02-BC-N02 (the store's country among the settings whose change triggers store/information/updated): confirmed. events.md holds no word "country"; it sends settings events to the Channel Webhooks guide, whose Settings table lists the channel settings events, none for the store's country (S02-BC-186 to S02-BC-204; the table's locale/added row is S02-BC-038).

### Documents read, in order

1. https://docs.bigcommerce.com/developer/docs/integrations/webhooks/event-reference/events.md, held (run 20261012T0419Z-q1-bigcommerce-sources, item 088): the Stores section in full; its pointers for Settings, Sites, Category trees and Channel events; its Info notes (the asterisk marks metafield scopes that support data filters). The page holds no word "country".
2. The webhook lines of the 7 documents, among the third N02 search's 25, that mention webhooks: msf-international-enhancements/overview.md, B2B-Edition-Settings, orders/overview.md, payments/overview.md, Connecting-with-Stripe-OCS, Connecting-with-Braintree, llms.txt. None is on store/information/updated.
3. In the 71 documents of the second N01 search: the passages where a channel word falls within 250 characters of a place word (15 documents hold one; they are listed in `absence-audit.tsv`).
4. In the 21 captured documents of the third N01 search: the sentences holding "market" or "markets".
5. https://docs.bigcommerce.com/developer/docs/integrations/webhooks/event-reference/channel-events.md, held (same run, item 087): the Settings section in full: S02-BC-186 to S02-BC-204. The page holds no word "country".
6. https://docs.bigcommerce.com/developer/api-reference/rest/admin/management/channels/create-channel.md, live, read 2026-10-27, in full: S02-BC-162.
7. https://docs.bigcommerce.com/developer/docs/storefront/catalyst/features/localization/multi-storefront/overview.md, live, read 2026-10-27, in full: S02-BC-163 to S02-BC-173.
8. https://docs.bigcommerce.com/developer/docs/storefront/catalyst/features/localization/multi-storefront/setup.md, live, read 2026-10-27, its text in full (not its code blocks): S02-BC-174 to S02-BC-182.
9. https://docs.bigcommerce.com/developer/docs/storefront/headless/cart-and-checkout/carts.md, held (run 20261012T0426Z-q1-bigcommerce-sources-2, item 019): its note on markets and its note on the locale format: S02-BC-183, S02-BC-184.
10. https://docs.bigcommerce.com/developer/docs/integrations/platform-solutions/buy-online-pick-up-in-store/overview.md, held (same run, item 014): its Multi-channel awareness section: S02-BC-185.
11. https://docs.bigcommerce.com/developer/docs/admin/multi-storefront/overview.md, held (run 20261012T0419Z-q1-bigcommerce-sources, item 072): the Channels section, again (the list of S02-BC-132).
12. https://support.bigcommerce.com/s/article/Getting-Started-Channels, held (run 20261013T053949Z-s01-bigcommerce-help-founder-machine, item 027): its lines on the kinds of channel (Point of Sale, Marketplaces, Ads & Social, multiple storefronts).

### Searches too many to read in full, and how they were narrowed

- `corpus_search.py bigcommerce "channel" "channels" --with "country" "countries" "region" "regions" "location" "locations"`: 71 documents, past the cap of 40; run again with `--max 80` (71 documents and one founder's save). Narrowed by printing, from each document's held text, the passages where a channel word falls within 250 characters of a place word: 15 documents hold one, and those passages were read. The two pages that define a channel, multi-storefront/overview.md and channels.md, are not among the 71: they hold no word for a country, region or location.
- `corpus_search.py bigcommerce "Store Name" … "store settings" --with "الدولة" "country"`: 25 documents, all listed, but most support articles match "Language" only through the Help Center's header ("Preferred Language EN"). Narrowed by checking each document's held text for webhooks or store/information/updated: 7 mention webhooks, and their lines were read.
- `corpus_search.py bigcommerce "name" "type" "platform" … --with "السوق" "market" "markets"`: 21 documents and 2 founder's saves (the same code of ethics PDF twice, read by its snippet). "name" and "type" match nearly every page, so the search reduces to the pages holding "market" or "markets": their sentences holding either word were read.

### Problems with the method or the tools

- `corpus_search.py` matches an identifier as written: "store_country" doesn't match the Markdown captures, which escape the underscore ("store\_country"). The escaped spelling had to be searched as its own term. Phase A's search 31 above reports "store_country" matching store-configuration.md; in this audit the same term didn't.
- `corpus_search.py` printed held copies at commit 063b00c2187231de9e593c2dc7ca5aebaf43b512, and `held_index.py` prints this repository's captures without a commit. The repository's HEAD when they were read was f72d361fc4eacb5dd29b3bce9e55d2fd346819a3, the commit `absence-audit.tsv` gives them.
- The brief's second search for (e) has the names of a channel's properties ("name", "type") as its terms, and they match nearly every page, so it finds no more than the general word alone.
- The pages that state most on channels and countries (the Create Channel endpoint, the Catalyst multi-storefront pages) are not held. They were read live and are cited by their `.md` URLs, pending capture.
