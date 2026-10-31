# F-backfill-woocommerce: notes

## What this part did

F-woocommerce added three capabilities to domain F: CM-APP-011 (apps made by the platform's company, under CM-APP-002), CM-APP-012 (marketplace connection, under CM-APP-001) and CM-API-012 (API response caching, under CM-API-001). This part writes their six cells for Shopify and Salla. It adds no capabilities, lands no concerns, and writes no rulings, qualities or slot fillers.

For each platform I ran `candidates --domain F --platform P --areas APP,API`, which found no statement for any of the three: their terms are WooCommerce's own (Developed by Woo, WooCommerce.com, rest_api_caching). I then searched with `search` and read the leads with `key`: Salla in English and in Arabic, each Arabic term in its singular and its plural, with and without ال. The terms are in each cell's `searched`. One cell holds statements, five are `none-held`. `none-held` means only that the concern map holds nothing found by those terms; it never means the platform lacks the capability. Each placement is a reading unless it quotes a statement.

| Capability | Shopify | Salla |
|---|---|---|
| CM-APP-011 apps made by the platform's company | own-service: SH-C-156/responsible/SH-S-0738; shows: SH-I-2100 | none-held |
| CM-APP-012 marketplace connection | none-held | none-held |
| CM-API-012 API response caching | none-held | none-held |

## The readings

- **CM-APP-011, Shopify.** F-woocommerce's lead holds. "Apps that are made by Shopify are usually free and are supported by Shopify" (SH-S-0738) names Shopify as the maker and the supporter of these apps: `own-service`. The help center's section Apps made by Shopify (SH-I-2100, an inventory entry placed in SH-C-156) gives the term: `shows`. The anchor cites SH-S-0738 as `shows` in CM-APP-001; CM-APP-011 is in the same tree (under CM-APP-002, under CM-APP-001), so SH-C-156 isn't strained.
  - **Gap:** no statement shows Shopify's own apps as a category of their own in the Shopify App Store, which is the grain of WooCommerce's cell (Extensions > Developed by Woo, WC-S-0697). The help center's section isn't the App Store's.
  - **Not cited:** apps whose names carry Shopify's brand and that are installed from the Shopify App Store: Shopify Flow (SH-C-151/where/SH-S-0753), Shopify Audiences (SH-C-132/where/SH-S-7255), Shopify Fulfillment Network (SH-C-120/where/SH-S-0716). A brand in a name doesn't name the maker, and no statement held names Shopify as theirs (a gap). Shopify Inbox's Google Play listing names "publisher Shopify Inc." (SH-C-153/where/SH-S-2758), but it is a mobile app's store listing, not an app or extension in the platform's marketplace, so I left it uncited (a reading).
- **CM-APP-011, Salla.** No statement names Salla as the maker of an app or extension for stores. The hits:
  - the App Store's policy and its owner (SA-C-175, SA-C-195);
  - Salla's hosting of partners' apps "دون أن يُعد ذلك بمثابة توصية أو تزكية رسمية" (SA-C-194/responsible/SA-S-0037);
  - the Salla CLI, "developed by Salla team" for building apps and themes (SA-C-203/reason/SA-S-5096), a tool for developers, not an app for stores (a reading);
  - Salla's merchant mobile app (SA-C-004), App Functions managed by Salla (SA-C-145, SA-C-196);
  - services Salla provides: electronic payments (SA-C-110), the wholesale market (SA-C-098), an MCP server (SA-C-012).
- **CM-APP-012, both.** No statement links the store to an account of the platform's app marketplace. Shopify's hits are the Shopify Account of the Terms (SH-C-001 and others) and the staff permission to install apps (SH-I-1007), which belongs to CM-APP-001. Salla's are plan lines that link the store to advertising, shipping and accounting services, and installing the ZATCA app (SA-S-0151). A reading: on both, apps install from the App Store into the store with no connection the statements name.
- **CM-API-012, both.** Shopify: no statement or placed entry holds the terms. Salla: the plan line تفريغ الكاش (clear the cache), an advanced feature of سلة بلس (SA-C-002/decides/SA-S-2092, SA-I-1092). It names no API and no cache of API responses, and what it clears isn't stated, so I left it uncited (a reading). If the reviewer reads it as the platform's own cache setting, it could be `shows` here, but it is not a setting of the API.

## Homonyms

- **Marketplace:** Shopify Marketplace Connect (SH-C-137) connects a store to other companies' marketplaces, not to the platform's app marketplace. It isn't CM-APP-012's.
- **Salla Apps** (SA-C-203, Salla Apps Playbook) means apps built on Salla, not by it.
- **الكاش** matches cashback (الكاش باك, SA-C-063) and كاشير (SA-C-095).

## Rulings of F-woocommerce that these cells change

- **(WC-C-050, SH-C-156), U-052:** `nested:CM-APP-011` becomes `joined:CM-APP-011`, since SH-C-156's statement SH-S-0738 is now cited in CM-APP-011. The coordinator corrects the row in F-woocommerce's `rulings.tsv`.
- **(WC-C-050, SH-C-157) and (WC-C-050, SA-C-194):** they stay `nested:CM-APP-011`. No statement shows a category of Shopify's or Salla's own apps in its App Store, and Salla's cell is `none-held`.

## What the checker flagged

1. **own-service on SH-S-0738:** the statement says "Apps that are made by Shopify", which names Shopify as the maker. It also says they "are supported by Shopify". Its scope is Shopify's apps in general; "usually free" bears on their price, not their maker.
2. **CM-APP-011 Salla, 27 matches:** read above. They name Salla as the App Store's owner, a host, the maker of a developer tool, or the provider of services and of its mobile app, never as the maker of an app for stores. "رسمي" also matches official rates and channels (SA-C-160, SA-C-204, SA-C-206).
3. **CM-APP-012 Shopify, 8 matches:** the Shopify Account (SH-C-001, SH-C-006, SH-C-008, SH-C-174), a domain's renewal (SH-C-033), and two app entries (SH-I-1007, the install permission; SH-I-2106, Uninstalling apps), which are CM-APP-001's.
4. **CM-APP-012 Salla, 5 matches:** plan lines for links to advertising, shipping and accounting services, and installing the ZATCA app. None is a connection to the App Store.
5. **CM-API-012 Salla, 11 matches:** تفريغ الكاش (read above), cashback and its permissions (SA-C-063), كاشير (SA-C-095), and the plan line أرشيف الرسائل النصية (SA-C-011/decides/SA-S-2091), which matches only because the raw plan entry it sits in holds a neighbouring line.

## Gaps

- Shopify: whether its own apps form a category of the App Store; and who makes the apps that carry its brand.
- Salla: any app or extension that Salla makes, and what تفريغ الكاش clears.
- Both: any connection between the store and the marketplace's account, and any cache of API responses.

## Problems

None with the brief or the evidence.
