# Notes on batch P-5: S-02's points S02-VP-41 to S02-VP-54

Fourteen points, seven pairs. Each pair asks what a setting takes its value per (currency, languages, domains, product availability, pricing, discounts and gift cards, theme content), and who sets it. The model is read at a11d4727, as merged. `show` printed no warning that a domain's files had changed after the last merge.

Outcome of the draft: **10 landed, 4 with conflicts** (S02-VP-43, S02-VP-44, S02-VP-47, S02-VP-49). The conflicts are 2 `count` on languages and products, 2 `count` on product lists and prices, and 2 `placement` on PayPal. None rests on a founder's own decision. The register rows they name are engineering's rulings (S02-D6, S02-D7, S02-E1), a row that follows by rule (S02-F10), and `model`. Every placement, landing and reading below is a reading unless a key is given for it.

## Points that were hard to land, and why

- **S02-VP-41 and S02-VP-42 (currency).** The question covers two capabilities' things. A market's or a buyer's currency belongs to CM-MKS-006, and the store's own currency to CM-MKS-005. I gave S02-VP-41 `cross-cutting: money records and currency`, because every amount names a currency. That is the brief's own example. I gave S02-VP-42 ("who sets") `capability`. A setter is held through the configuration, not in every area. S02-VP-42 also names CM-MKS-007, because the third parties it names (Zid's gateway and partners, and Stripe on BigCommerce) convert amounts. Converting is CM-MKS-007's thing alone.
- **S02-VP-45 and S02-VP-46 (domains).** The store's own domains belong to CM-SFR-008, and a market's own domain to CM-MKS-004 (local domains, Shopify's MarketWebPresence). No lead offered CM-MKS-004 for S02-VP-46, so I found it with `caps`. It is cited by the key SH-C-111/boundary/SH-S-7458.
- **S02-VP-47 and S02-VP-48 (product availability).** These were the hardest. The model has no single capability for "the products a market offers":
  - Shopify's catalogs sit in **CM-B2B-003**, "Catalogs: product and price lists assigned to B2B buyers or markets". Its note says Shopify's catalogs also serve region markets (SH-S-5101). I landed the main thing there, because the brief says to land on X, not on Markets.
  - The platforms also answer in capabilities of their own, so each is named for its platform:
    - BigCommerce's products per storefront are channel assignment: CM-CHN-001, BC-C-038/where/BC-S-0219.
    - WooCommerce's Google channel visibility: CM-CHN-004, WC-C-110/boundary/WC-S-5494.
    - Shopify's products hidden by country under Managed Markets: CM-MKS-003.
    - Zid's products shown by the customer's city: CM-INV-010, ZD-I-0257.
    - WooCommerce's POS visibility: CM-POS-001.
    - Salla's order of products in a category per market: CM-CAT-003.
  - WooCommerce's catalog visibility (S02-V-1083, S02-WC-346) is a field on each product, so it isn't landed apart.
  - A rename for the coordinator to weigh: CM-B2B-003's name and note read as B2B-first, while the subject shows market product lists on four platforms. The note could say outright that a market's product and price list sits there, or the market lists could move to CM-MKS-001. The count conflicts below hinge on this.
- **S02-VP-49 and S02-VP-50 (pricing).**
  - Prices per market, storefront or customer group belong to CM-B2B-003. BigCommerce's Price Lists are assigned to a channel or a customer group (BC-C-007/decides/BC-S-0050).
  - Automatic conversion belongs to CM-MKS-007, and WooCommerce's prices in the buyer's currency to CM-MKS-006.
  - BigCommerce's "localize storefront prices for shoppers from different regions" is its Tax Settings API (S02-BC-058), so it lands in CM-TAX-001 (BC-C-072/reason/BC-S-0387).
  - Global-e on S02-VP-50 lands in CM-MKS-003. See its own item below.
- **S02-VP-51 to S02-VP-54.**
  - Discounts, coupons and gift cards land in CM-MKT-001, CM-MKT-002 and CM-LOY-002.
  - Salla's gifting, offered in the store's country (S02-SA-276), is CM-LOY-006's thing, found with `caps`.
  - Theme content lands in CM-SFR-001 and CM-SFR-002.
  - Shopify's automatic hreflang tags (S02-SH-174) land in CM-CNT-007, SEO, whose Shopify cell cites MarketWebPresence.

## Each conflict, with both sides' evidence

1. **S02-VP-43: `count` (rows: S02-E1, model). WooCommerce, CM-MKS-008.**
   - The subject's side:
     - S02-WC-423 is WooCommerce 11.2.1's own code. Its citation S02-WC-C524 is `includes/emails/class-wc-email.php`, line 427, `WC_Email::setup_locale()`: "Set the locale to the store locale for customer emails to make sure emails are in the store language."
     - S02-WC-325: "the shop displays in your locale if the language file exists".
     - Both show built-in behaviour, which the model's rules place `core`.
   - The model's side: the WooCommerce cell is none-held. Its reading says the site's language is WordPress's, "no statement held says so".
   - My reading: core on WooCommerce's use of the store's language. The setting itself is WP Admin > Settings > General > Site Language (S02-WC-324). The model's practice reads a WordPress admin setting as `shows`: CM-STF-002 cites WC-C-080/decides/WC-S-0884 that way. WordPress fetching the translation (S02-WC-326) is `outside` at most.
   - What settles it: an amendment citing S02-WC-423, and S02-WC-324 and S02-WC-326 as `shows`.
2. **S02-VP-43: `placement` (rows: S02-F10, model). BigCommerce, CM-MKS-008.**
   - The subject's side: S02-BC-287 says "In addition to the payment methods automatically translated by BigCommerce, PayPal automatically translates many of its payment methods based on the shopper's location, rather than the selected language."
   - The model's side: the cell is `core` (BC-C-048/decides/BC-S-0271, BC-C-048/decides/BC-S-0272) and places no one `outside`.
   - My reading: the statement shows BigCommerce translating payment methods itself, which is core. PayPal translates only its own methods' labels, which is a provider's own content.
   - What settles it: whether a provider's labels in the checkout are part of "the store's content" in CM-MKS-008. If they are, an `outside` row for PayPal is owed. If not, the conflict is dismissed.
3. **S02-VP-44: `placement` (rows: S02-F10, model).** The same statement and cell as conflict 2, under the "who sets" answer `PayPal` (S02-V-987). I recorded it on both points because each point stands alone. One settlement answers both.
4. **S02-VP-47: `count` (rows: S02-D6, S02-E1, model). Salla and Zid, CM-B2B-003.**
   - The subject's side, Salla: the product page's Product Display in Markets (S02-SA-155, S02-SA-281), the products table's column (S02-SA-165), and the setting `markets#auto_show_products_in_scope` (S02-SA-082).
   - The subject's side, Zid: its markets feature sets each market's products (S02-ZD-010, S02-ZD-019, S02-ZD-493).
   - These are built-in features, `core`.
   - The model's side: CM-B2B-003's Salla cell is not-stated, on SA-S-5047 (wholesale prices only). Its Zid cell is none-held.
   - My reading: core on both platforms.
   - What settles where the amendment goes: whether a market's product list belongs in CM-B2B-003 or in the platforms' CM-MKS-001 cells. Those cells already cite Salla's setting Market selection (`markets/browse_product_method`, SA-C-165/where/SA-S-1730) and Zid's الاعدادات > الأسواق (ZD-C-034/where/ZD-S-0748). If the coordinator chooses CM-MKS-001, those cells gain statements and CM-B2B-003's note says so.
5. **S02-VP-49: `count` (rows: S02-D7, S02-E1, model). Salla and Zid, CM-B2B-003.**
   - The subject's side, Salla: the option `markets/product_prices#option.fixed`, "Set product prices manually for each market from the product page" (S02-SA-078; also S02-SA-024).
   - The subject's side, Zid:
     - "سعر مخصص لكل سوق وقناة", a price per market and channel (S02-ZD-011);
     - the market setup's pricing steps (S02-ZD-020, S02-ZD-021);
     - Settings > Markets, "Set different product prices for each market and customer type, including B2B pricing" (S02-ZD-489).
   - The model's side: as in conflict 4.
   - My reading: core on both. The same Salla setting's automatic option is already cited in CM-MKS-007 (SA-C-163/decides/SA-S-0117), so the setting is in the model, but its manual per-market prices aren't.
   - What settles it: the same choice as conflict 4.

No `premise` conflict was found. I checked these rows' claims about the references against the cells:
- S02-F7: "as all five carry it", the currency shown following the buyer's country, and one currency for the store. CM-MKS-004 and CM-MKS-005 are `core` on all five.
- S02-E4: a store currency on all five. CM-MKS-005 is `core` on all five.
- S02-D7: a rate held per market, as Shopify holds it. Consistent with CM-MKS-007's Shopify reading.
- S02-D4: a price keyed on customer groups, as BigCommerce's are. Consistent with CM-B2B-003's BigCommerce cell.
- S02-D6: catalogs combined, as Shopify combines them. Consistent with CM-B2B-003's Shopify cell.
- S02-M1: a merchant of record setting prices in its markets. Consistent with Global-e in CM-MKS-003.

S02-M2 (moved to S-04) says each provider "converts" buyers' currencies. The cells show the platforms themselves converting prices: CM-MKS-007 is `core` on Shopify, Salla, Zid and BigCommerce. My reading is that M2 means the payment's own currency conversion, which the providers' terms hold (Stripe, BC-C-074/boundary/BC-S-0409). Price display conversion is a different thing, so I didn't record it as a conflict. If the coordinator reads M2 as covering price conversion too, it is a `premise` to carry to S-04.

## Findings the four types don't cover (for an amendment, not conflicts)

- **CM-MKS-004, Salla.** The cell's reading says "No Salla statement gives a market its own domain". The subject holds S02-SA-052 ("You can assign a subdomain to a market, but it is optional. A market without its own subdomain opens on your store's main domain.") and S02-SA-024 (دومين المتجر among what a market customizes). The cell is already `core`, on SA-S-0154, so no `count` arises. Its reading, though, is contradicted on markets, which the brief's grain rule doesn't excuse. I suggest the coordinator's amendment cite S02-SA-052.
- **CM-MKS-004, BigCommerce.** The cell's reading says no statement names local domains. The subject holds S02-V-818 and S02-V-819 ("Each of these storefronts can have its own unique domain"; and S02-BC-116, Channel Manager › Domains: "You can connect a localized domain (such as “cats.fr”) or subdomain (such as “fr.cats.com”) to a storefront"). The cell is already `core`, so the same applies.
- **CM-MKS-007, Zid.** The cell reads ZD-S-0809 (the gateway's exchange rate) as `shows`, because the gateway isn't named. The subject's S02-ZD-050 doesn't name it either, so no third party is named and nothing is owed.

## The checker's leads, and what I made of them

- `lead: P-5 S02-VP-43: the subject holds woocommerce's statements; no cell of CM-MKS-008 holds any on woocommerce`. This is conflict 1 (`count`): S02-WC-423 and S02-WC-325 support core. The capability is not missed: CM-MKS-008 is the languages capability, and no other capability holds WooCommerce's language.
- `lead: P-5 S02-VP-44: the subject holds woocommerce's statements; no cell of CM-MKS-008 holds any on woocommerce`. On a "who sets" point the brief compares only a named third party, as `placement` defines it. The WooCommerce cell is none-held, not `core`, so WordPress fetching translations (S02-WC-326) makes no `placement`. The seller setting the Site Language (S02-WC-324) is the platform's setting. The same amendment as conflict 1 would answer this lead.

## Slot fillers and third parties the subject names that `cell` doesn't list

All the landing capabilities are of the kind `class` (merged/kinds.tsv). The ones with `outside` cells are CM-MKS-003 (Shopify), CM-MKS-004 (WooCommerce), CM-MKS-006 (Shopify) and CM-MKS-007 (BigCommerce). Each item below is a lead, not a conflict:
- **CM-MKS-003, Shopify.** Global-e is listed as the merchant of record and tax registrant. The subject adds a role: Global-e's pricing configurations "can only be edited by Global-e" (S02-SH-290, `GLOBAL_E_PRICING_STRATEGY_NOT_PERMITTED`). The subject's S02-SH-498, S02-SH-526, S02-SH-537 and S02-SH-538 show Managed Markets restricting and hiding products by destination country, which the cell doesn't hold.
- **CM-MKS-007.** Stripe (Adaptive Pricing) is listed for BigCommerce. The subject names no other converter. Zid's "partners" are placed `extension-point` (ZD-C-050/boundary/ZD-S-0812), and its gateway is unnamed.
- **CM-MKS-008, BigCommerce.** PayPal (S02-BC-287), not listed. See conflicts 2 and 3.
- **CM-MKS-008, WooCommerce.** WordPress (S02-WC-326), which fetches the translation. A lead for a `shows` or `outside` row, depending on how the coordinator reads WordPress: as the software WooCommerce runs in, or as a third party.
- **CM-CHN-004, WooCommerce.** Google Merchant Center is listed. The subject adds Google as the channel that products and coupons are shown on (S02-WC-356, S02-WC-371, scope Google for WooCommerce). No statement names the extension's maker, so it supports no placement.

## Problems with the brief or the script

- `reach` for "who sets" points. The brief defines reach by the point's thing. I read a setter as held through the configuration, so every "who sets" point here is `capability`, including S02-VP-42, whose pair S02-VP-41 is cross-cutting. The coordinator may prefer to give a pair one reach.
- I added a capability for each platform whose answer sits in one of its own. The brief allows this ("Add another only where the platforms answer the question in different capabilities"), but it leaves S02-VP-47 with seven capabilities. If the coordinator prefers the main one alone, CM-B2B-003 is the main one, and the conflicts don't change.
- To match the file format, I read the header and first row of `P-4.tsv`, which the brief doesn't name. I read nothing else of it, and I wrote nothing to batch P-4's files.
- No script problem. `check --batch P-5` ends: `# 14 points in P-5, 0 problems`.
