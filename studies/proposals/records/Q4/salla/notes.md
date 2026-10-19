# Notes: Q4 on salla

## What was read

All held, at observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3. No live page was read.

- Help centre (through `method/help_map.py salla`): category lists for 💳 طرق الدفع والمحفظة, 📦 الطلبات, - الطلبات (old), 🏪 كاشير سلة بوينت; articles dcrwxldslve7spa8eqdgii8g, xwboef9bg8yax7dpsmuq0aq3, dsw3leig1h4jocdmnengiw8s, n53zyxfv29z0pujrwswnqxqm, lwd3jzhb0qs7v51b50rcc50a, ho3182vb4jj8qmhar6ll3uor, bx4sc8a84fxh1c0spsp5rrsx, mdke7ybzpze7jnsiiloylga2 (ar and en), vw91ng2oejceja6cvdaw0uch, vb93lvz57832o1hr4ocjez6a, mp51njqskddr8cbo4pit91y7, v5jrh4oz46bfkh8u0dnnlk8v, i31g2awy4qa2ifu6bp352zoy, d9me3k8vqi09hdiun8r2ngfr, f0ik50tqs9hgdbf8xna21oqh (from texts.jsonl line 146). Searched with grep only: brcrs6n595b0v7ijuagfj1m7, nysbqdb4hj4sqpniinmrwmkh, bkg4fsbz4b2yfq4q9rqua722, a5dilpk2huccim5z65e0b9wr.
- Dashboard translations (ar): orders.json, payments.json, sallapoint.json, shipping.json, reports.json, reportsv2.json, checkout.json (its bank transfer strings concern paying Salla for a plan, so none was recorded).
- structures/salla/com-policies/shipping/text.txt (for gap Q4-SA-G0117) and com-policies/terms/text.txt (article 8 is already in the copies, Q4-SA-P0080, Q4-SA-P0081).
- Fetch archives: raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@545582 (salla.com/ar-ae/sallapoint); raw/runs/20261005T234928Z-docs-md/fetch.warc.gz@1577680 (orders/update.md), @1184382 (app-fuctions/events-order.md), @2228049 (coupon/create.md, read, nothing recorded).
- Corpus searches: bank transfer terms (ar, en); fees with bank transfer and cash on delivery; receipts with under-review terms; limits with bank transfer.

## Selection

SA-C-004 was first set aside and then copied (its plan line بدون عمولة منصة على مبيعاتك bears on fees); the second copy run kept the ids already copied.

## Gaps

- Q4-SA-G0117 (who collects and holds cash-on-delivery amounts through Salla shipping labels): the held salla.com/shipping page was read; it says only "استلم مبالغ الدفع عند الاستلام بشكل دوري، وساعد تدفقك النقدي يظل مستمر." (already copied as Q4-SA-P0097). The gap stays open.
- Q4-SA-G0119 (the payment services contract for bank transfer) was not read for: no held copy of the contract was found in what was read.

## Copies

- Two copies give different lists of carriers supporting cash on delivery through Salla shipping labels: Q4-SA-P0095 names six; the article إدارة بوليصات الشحن (Q4-SA-014) names three (أي مكان، أرامكس، J&T).
- The permission key salla_point_cod_orders is named طلبات الدفع عند الاستلام in Q4-SA-K1426 and الطلبات النقدية in sallapoint.json (Q4-SA-041).

## Method

- Statements from dashboard translation files are single values: the checker finds a statement verbatim only within one value, so a label and its description are recorded as the description, with the label in the identifier and cited second.
- The checker reads a bare host name (help.salla.sa, s.salla.sa) in a not-found route as an address, and refuses the route when the host's root is held; routes were reworded without bare hosts.
- The help map limit of 10 pages was passed across sentences: about 15 articles were opened in all, most of them for [1] and [3].
