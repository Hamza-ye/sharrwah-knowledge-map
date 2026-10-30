# Scope notes

Every row of `scope.tsv` is a reading. Sources read: `class_slice.py seed` and `class_slice.py concerns --platform P --all --where` for each platform, plus, for SH-C-112, SH-C-082 and eight Zid concerns whose names didn't settle them, `class_slice.py statements` (keys cited below).

Checker (`check_class_part.py studies/class-model/scope.tsv`): `concerns per domain: A 110, B 40, C 218, D 98, E 98, F 72, G 16; 1 matches split`, 0 problems, 1 flag (M-055, below).

## Rules I applied throughout

- **Extensions:** an extension surface that works inside one feature goes with that feature, and names F under `also`: checkout UI extensions (SH-C-049, WC-C-087, BC-C-017) go to C; POS UI extensions (SH-C-144) to E; customer account UI extensions (SH-C-165) to D; theme app extensions and app snippets (SH-C-166, SA-C-198) to E; single-purpose Shopify Functions (SH-C-052, 053, 083, 122, 123, 124, 128) go to their feature's domain. An extension mechanism that isn't tied to one feature goes to F: Shopify Functions as such (SH-C-163), Admin UI extensions and App Home (SH-C-164), Salla's Embedded SDK, App Functions and App settings (SA-C-196, 197, 199), WooCommerce's extension framework (WC-C-086), Zid's embedded and private apps (ZD-C-073, 074). This is my reading of "apps and extensions as such" together with "the channel doesn't set the domain".
- **App-store categories:** these go to the domain of what the apps do (for example SH-C-185 to SH-C-196, WC-C-104 to WC-C-110, SA-C-200, SA-C-207, ZD-C-061).
- **Platform fees and app billing:** the platform's own bill goes to A (PLN). That covers plans, bills, taxes on the platform's fees and third-party transaction fees (SH-C-018). App charges billed through the platform go to F (APP), with A under `also`, because they are part of M-010 with partner payouts: SH-C-019, SA-C-195, ZD-C-022, BC-C-029.
- **Payments-specific policies and KYC go to C:** Shopify Payments' prohibited businesses (SH-C-173, M-085), WooPayments' (WC-C-011), Zid Pay's (ZD-C-037), Salla's selling policy for e-payments (SA-C-172) and KYC for payments (M-003). The platform's general acceptable-use, sanctions and legal concerns go to A (TRU).
- **Card data security (PCI DSS)** goes to A (TRU), with C under `also`: M-062 (SH-C-184, WC-C-018, WC-C-019) and BC-C-028.
- **Storefront hosting and SSL** go to E (SFR): SH-C-036, BC-C-052, BC-C-078. WooCommerce's server recommendations (WC-C-034) go to G (OPS), because there the hosting is of the whole installation, not only a storefront.
- **The merchant's mobile admin app** goes to G (SRF), following the seed's lead "merchant mobile app": WC-C-090, BC-C-077. The store's own mobile app for buyers goes to E (CHN): SH-C-195, SA-C-094, SA-C-174, ZD-C-116.
- **The platform's support to merchants** goes to A (ONB): M-066 (SH-C-155, SA-C-014, WC-C-062) and ZD-C-114. Partner or expert services that merchants hire go to F (PTN).

## Split match

- **M-055** (SH-C-138, SH-C-146, SA-C-074, SA-C-092). SH-C-138 (product feeds and listings for channels) goes to E (CHN), with D under `also`. The other three go to D. SH-C-138's terms and `where` are `product_listings/add`, `read_product_listings`, `listings:root` and `mappings:root`: publishing products to sales channels, Shopify's own channel publishing. The rest of the match is pixels, ad-platform feeds and storefront tracking events, which are marketing and analytics. The reason in SH-C-138's row names M-055.

No other match is split. Several matches hold concerns whose subject leans toward a second domain. I kept these together and named that domain under `also`, without splitting:
- M-044: WC-C-051 is about the payout currency, and stays in E with C under `also`.
- M-009: WC-C-057 stays in A with SH-C-017.
- M-013: gift cards stay in D with Salla's customer wallet.
- M-074: subscriptions stay in B, since the recurring-payments API goes with what it charges for.
- M-077: accounting stays in C.
- M-003: KYC stays in C.

## Hard to place

| Concern | Placed | Weighed | Why |
|---|---|---|---|
| SH-C-025 Gift cards | D (LOY) | B (SEL), C (PAY) | M-013 joins it with SA-C-063 (customer wallet, cashback, gift cards), and the seed lists gift cards under LOY too. |
| SH-C-045 Payment terms | C (PAY) | D (B2B) | `payment_terms/create` sets when an order is paid. It is used for B2B, so D is under `also`. BC-C-031 (B2B invoices and net terms) follows it. |
| SH-C-037 Catalogs; BC-C-007 Price lists | D (B2B) | B (CAT), E (MKS) | The seed puts Catalogs under B2B. BC-C-007 follows Shopify's catalogs as the same kind of thing: prices per customer group or channel. BC-C-008 (the storefront Pricing API) stays in B. |
| SH-C-082 Shop Cash | D (LOY) | C (PAY) | `SH-C-082/where/SH-S-0437`: "a Shopify-funded rewards program for Shop app customers". It is a reward, though the help page sits under payments. |
| SH-C-112 Rollouts | E (MKS) | G (EVO), C, D | `SH-C-112/decides/SH-S-0576`: "a scheduled set of changes to your online store's main theme, checkout and accounts pages, discounts, product catalogs". The help page is under markets. |
| SH-C-140 Agentic commerce | F (AIA) | E (CHN) | The seed lists it under both. AIA names agentic commerce, so CHN goes under `also`. |
| SH-C-141 Collective; SH-C-185 Product sourcing; SA-C-098 Wholesale market | E; B; D | B, D, E | These are all under U-016 (not a match). Shopify places Collective under online sales channels. Sourcing apps are about where products come from (B). The seed puts Souq Eljomla under B2B. |
| SH-C-188 Upsell, bundles, pre-orders | B (SEL) | D (MKT) | Bundles and pre-orders are ways of selling; upsell goes under `also`. ZD-C-089 (Bundle Offers, in Zid's Marketing API) goes to D. |
| SH-C-191 / SA-C-210 Accounting and ERP (M-077) | C (PAY) | G (MIG), D (ANL) | No seed area holds it. The store's finances are closest to "payments, payouts and money". G is under `also`. |
| SH-C-147 Network Intelligence | A (TRU) | D | Its `where` is settings/privacy. |
| SA-C-012 / WC-C-095 AI connector and MCP (M-079) | F (AIA) | B, E | Salla's concern also holds AI generation of descriptions and SEO. |
| SA-C-150 Quality gateway | C (SHP) | D (SUP) | The seed lists it under SUP, but its terms are all about shipping companies: `shipping-ticket-system`, `shipping-rating`. |
| SA-C-180 Policy /policies/nd96 | A (TRU) | any | Its content was not reached. It is placed as a Salla policy page. The coordinator may move it once it is read. |
| SA-C-206 Partner affiliate programmes | F (PTN) | D (MKT) | Its `where` is the Partners portal. It is the partner's side of affiliate marketing; the store's own affiliates (SA-C-072) are D. |
| SA-C-234 Platform security and status | G (OPS) | A (TRU) | `where`: status page component list; "استقرار المنصة وجاهزيتها للذروة". |
| SA-C-235 Partner unavailability | G (OPS) | C, F | Continuity when a partner fails. It has no `where`. |
| SA-C-304 Global selling programme | F (PTN) | E (MKS), C | It is a programme offered to partners (MoR). |
| WC-C-031 Checkout rate limiting | A (TRU) | C, F | It protects checkout from abuse, like bot protection (SH-C-051), and is not an API convention. |
| WC-C-033 HPOS | C (ORD) | G | How orders are stored. |
| WC-C-037 Store logs; BC-C-060 | G (OPS) | A (TRU) | These are technical logs, apart from the audit logs of M-005. |
| WC-C-049 WordPress.com / Jetpack connection | A (ACC) | F | It is the merchant's account for Woo services. |
| WC-C-091 Order withdrawal | C (RET) | A | The buyer's withdrawal from an order. |
| WC-C-102 Memberships | B (SEL) | D | It sits under Extensions > Merchandising. |
| WC-C-109 Store management extensions | G (SRF) | A, C, D | A mixed category covering insights, import and export, order management, policy and security, notifications and accounting. No single main subject. |
| ZD-C-017 Zid Wallet | C (PAY) | A (PLN) | It holds COD collections and deductions from Zid Pay. |
| ZD-C-025 Zid Agent | F (AIA) | D | `ZD-C-025/boundary/ZD-S-0717`: an AI agent for "product research, store optimization, campaign management, and conversational assistance". |
| ZD-C-026 VAS | A (PLN) | | Add-on features bought from Zid (`ZD-C-026/decides/ZD-S-0720`). |
| ZD-C-103 Google Maps | D (CUS) | C, E | Follows SA-C-065, where map services serve customer addresses. |
| ZD-C-104 Working hours | C (ORD) | E | Read like Salla's ordering hours (SA-C-047). This is a reading: its statements weren't printed. |
| ZD-C-111 Zid Assurance | D (SUP) | NTF, C | `ZD-C-111/responsible/ZD-S-0998`: Zid "handle[s] any complaints or inquiries"; `boundary/ZD-S-0999`: WhatsApp order updates. |
| ZD-C-112 Zid Voice | C (CHK) | F (AIA), D | `ZD-C-112/where/ZD-S-0452`: "Recover abandoned carts with a voice agent". It goes with the abandoned carts. |
| ZD-C-115 Zid Growth | F (PTN) | D | `ZD-C-115/responsible/ZD-S-1080`: "شركاء يقدمون الخدمة". |
| BC-C-066 Powered By | F (PTN) | A, E | Commerce-as-a-Service for other platforms. |
| BC-C-076 Staging environments | F (DVT) | G | Environments for testing store changes. |

## Problems with the brief or scripts

- `statements --concerns` takes a `;`-separated list in one argument. Space-separated ids are refused, though the brief writes `--concerns ...`.
- Domain C holds 218 concerns, a third of the class. The brief already expects C to be split by area before its parts run.
