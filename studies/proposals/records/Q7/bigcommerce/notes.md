# Notes: Q7, BigCommerce (checking run)

## Selection

Copied: BC-C-074, BC-C-025, BC-C-026, BC-C-020, BC-C-007, BC-C-030, S-01. Added and copied: BC-C-039. Set aside: the other 15 rows. BC-C-030 was first set aside and then copied in a second copy run, after an account point (Zid's fees currency) needed it. The ids copied earlier didn't change.

## What was read

No map of BigCommerce's help is held. Every page was read from this repository's capture runs, at commit 8d4e787a826d283fd28735114b60e0a2932a5092, through their text files.

- **Topic search** (`corpus_search.py bigcommerce "default currency" "default currencies" "transactional currency" "transactional currencies" "display currency" "display currencies" "settlement currency" "currency" "currencies" "multi-currency" --max 10`), 10 read:
  - docs.bigcommerce.com: currencies/overview.md, management/currencies.md, management/orders.md;
  - support.bigcommerce.com: Using-Multiple-Currencies, Managing-Currencies, Available-Payment-Gateways, Getting-Started-Payments, Price-Lists, Getting-Started-with-Localization-on-Multi-Storefronts, Multi-Storefront.
- **Per-sentence searches** (commands in `not-found.tsv`):
  - [1]: Getting-Started-Channels, Offline-Payment-Methods, multi-storefront/overview.md;
  - [2]: Creating-a-Manual-Order, Connecting-with-BigCommerce-Payments, Processing-Refunds;
  - [3]: bigcommerce.com/payments/embedded-payment-providers/, B2B-Edition-User-Roles-and-Permissions;
  - [4]: bigcommerce.com/product/.
- **Not read:** documents already read for another sentence, or whose statements were among the copies, were not opened again.
- **Live pages:** none read. Nothing needed fell outside what is held.

## Tables and lists recorded in part

- Available-Payment-Gateways, Embedded and Open Payment Providers tables (more than 20 rows in all). Recorded: the column definition, the header row with the Access Worldpay and Adyen rows, and the BigCommerce Payments and PayPal rows (Q7-BC-009 to Q7-BC-012). The other rows were left out. Rows with blank cells collapse to ambiguous text once whitespace is collapsed, so only rows whose ticks can be read against the header were recorded.
- Using-Multiple-Currencies, "Some BigCommerce features do not support multiple transactional currencies": only its store credit footnote was recorded (Q7-BC-007).
- Managing-Currencies, "Additional display settings" (symbol, decimal places), and Using-Multiple-Currencies FAQ items on cart currency changes, rounding and tax filing: not recorded.

## Account points past the 20th not-found row (not checked)

These account points weren't matched by what was read, and got no row because the cap of 20 was reached:
- Shopify [2] Q7-SH-186 to Q7-SH-190;
- Zid [2] Q7-ZD-K0229;
- Shopify [3] Q7-SH-007, Q7-SH-101/Q7-SH-102 (draft order exchange rate), Q7-SH-073, Q7-SH-119, Q7-SH-106 to Q7-SH-108, Q7-SH-109/Q7-SH-112/Q7-SH-113 and Q7-SH-110;
- Zid [3] Q7-ZD-K0157.

## Points not sorted against

Account points that rest only on not-found rows or gaps were not sorted against: Shopify Q7-SH-N01 to N04 (in part); Zid Q7-ZD-N01 to N05, Q7-ZD-G0004, G0027 and G0023.

## Problems with the method

- Two statements on the default currency disagree in what was read, and both were recorded as found:
  - the developer docs' Supported/Not Supported table lists "Stripe Payment Gateway" as supported and "Other Payment Gateways" as not (Q7-BC-008);
  - the Help Center's gateway tables tick Multicurrency for many gateways (Q7-BC-010 to Q7-BC-012).
- The first copy command in this run hung on a shell command waiting for input, and the run was interrupted by a usage limit. Nothing had been written. Step 1 was then redone from the start.
- The searches for sentences [2], [3] and [4] used `--with "currency" "currencies"` to keep the lists to currency matters. The checking brief's item 8 doesn't name `--with` for these searches.
- No copied gap covers a currency matter, so none is cited.
