# Notes: Q1, BigCommerce

## What was read
- Capture run 20261012T0419Z-q1-bigcommerce-sources: multi-storefront/overview.md, settings/store-configuration.md, currencies/overview.md, settings/locales-configuration.md, the management/shipping.md reference, www.bigcommerce.com/llms.txt, commerce.com/terms/jurisdiction-specific-terms/, and the line on www.bigcommerce.com/payments/bigcommerce-payments/ about where it is available.
- Capture run 20261012T0426Z-q1-bigcommerce-sources-2: store-configuration/shipping/overview.md.
- Capture run 20261013T053949Z-s01-bigcommerce-help-founder-machine, Help Center articles: Multi-Storefront, Getting-Started-with-Localization-on-Multi-Storefronts, Using-Multiple-Currencies, Managing-Currencies, Tax-Overview, Manual-Tax-Setup, Automatic-Tax-Setup (lines on regions), Available-Payment-Gateways, Getting-Started-Channels, Getting-Started-Payments, Connecting-with-Braintree (lines on storefronts and China).
- Capture run 20261013T003518Z-s01-a2-sources: one line of the commerce.com press release on BigCommerce Payments.
- No founder's saves were read: the corpus search pointed to none that bear on Q1.

## Live pages (read 2026-10-18, all served in English)
- https://docs.bigcommerce.com/developer/docs/admin/multi-storefront/msf-international-enhancements/overview.md (md endpoint): read; cited.
- https://www.bigcommerce.co.uk/pricing/ (rendered through page_text.mjs): read; one footnote cited.
- https://support.bigcommerce.com/s/article/Multi-Storefront-Payment-Methods?language=en_US: couldn't be read. curl returns the Salesforce shell, and page_text.mjs renders it with no text. Recorded as Q1-BC-N02.

## What couldn't be read
- Help Center chapters "Enabling Multi-Storefront", "Configuring Storefronts", "Create Storefronts" and "Creating an International Storefront" (Q1-BC-N01), and the shipping-zones article (Q1-BC-N03): not held, and support.bigcommerce.com can't be read from here.

## Copies
- None found wrong.
- Q1-BC-071 ("over 60 online payment integrations; serving 230 countries") gives different figures from copy Q1-BC-K0139 ("more than 65 … 150+ countries"). Both are recorded as their pages state them.

## Problems with the method and tools
- **Same URL captured twice.** Two capture runs hold https://support.bigcommerce.com/s/article/Available-Payment-Gateways?language=en_US, and the same holds for Connecting-with-Braintree.
  - The checker resolves a URL to the earliest run, 20261013T003518Z-s01-a2-sources, whose text.txt is empty (0 bytes), so every quote cited by URL failed.
  - Those citations now cite the readable capture as a local path: sharrwah-knowledge-map@53c7c948…:evidence/…/20261013T053949Z-s01-bigcommerce-help-founder-machine/items/002 and 005.
- **Over the length guide.** There are 149 new statements, past the 120 in rule 12. 48 of them are the rows of the two gateway tables in Available-Payment-Gateways, which rule 5 records one row per statement. Reading had already stopped when the count passed 120.
- **List statements without markers.** Help Center lists hold no item markers in the captured text, so list statements join the items with spaces, verbatim to the capture.
- **Table rows.** Gateway table rows are written with " | " between cells, so that empty cells stay visible.
