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

## Re-check against the observed runs, 19 October 2026

### What was read

All at observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3, read with `git show` from outside the repository.

- Guides: `README.md`, `docs/READING.md`; `index/rest-endpoints.tsv` (lines for onboarding and qna).
- Searches (`python3 -I method/corpus_search.py salla …`, each `--max 10`):
  - N01: "رسوم" "عمولة" "fees" "commission" --with "التحويل البنكي" "bank transfer" "الدفع عند الاستلام" "cash on delivery";
  - N02: "إيصال" "الإيصال البنكي" "receipt" "under_review" --with "التحويل البنكي" "bank transfer" "بانتظار المراجعة" "under review";
  - N03: "الحد الأقصى" "حد أعلى" "maximum" "limit" "limits" --with "التحويل البنكي" "bank transfer" "bank";
  - G0117: "تحصيل" "collected" "collection" "unbilled-cod" --with "الدفع عند الاستلام" "cash on delivery" "salla_cod" "بوليصات سلة";
  - [1] and [2]: "التحويل البنكي" "الدفع عند الاستلام" "bank_transfers" "other_payment_methods" "bank transfer" "cash on delivery";
  - [3]: "استرجاع" "refund" "refund_action" "can_refund_to_wallet" --with "حوالة بنكية" "التحويل البنكي" "bank transfer" "الدفع عند الاستلام" "cash on delivery";
  - [4]: "شروط الدفع عند الاستلام" "cash on delivery terms" "cod_settings" "الحد الأدنى" "minimum order" --with "الدفع عند الاستلام" "cash on delivery";
  - [5]: "بوليصات سلة" "Salla shipping labels" "salla_cod" "unbilled-cod" --with "الدفع عند الاستلام" "cash on delivery";
  - pointer: "qna" "persona" "onboarding" --with "الدفع" "payment" "التحويل البنكي" "bank". It listed no `/persona/qna` page or answer; `index/rest-endpoints.tsv` lists no qna endpoint.
- Files, run 20261012T010906Z-sweep-real-merchant-full-en (store real-merchant): `run.json`, `actions.jsonl` (steps 17, 42, 56, 58, 61, 334, 345), `responses.jsonl`; `responses/1488.json` (gateways/payment, step 42), `responses/2008.json` (orders/24438069, step 56), `responses/2038.json` (its histories), `responses/2294.json` (orders/1202316591, step 61), `responses/0614.json` and `0617.json` (wallet summary and unbilled-cod-transactions, step 17), and the payment_method and cod fields of `responses/2229.json`, `2175.json`, `1955.json`, `1512.json`, `2120.json`; `steps/017.text.txt`, `042.text.txt`, `056.text.txt`, `058.text.txt` (lines with payment terms), `334.text.txt`, `345.text.txt`.
- Run 20261009T112238Z-journey-storefront-account-order-en: `run.json`, `actions.jsonl` (steps 37 to 80), `steps/039.text.txt`, `steps/072.text.txt`.
- Run 20261009T055452Z-journey-order-lifecycle-demo (store demo): `run.json`, `responses/0259.json` (shipping/company/989286562, its faqs), `steps/072.text.txt`, `steps/074.text.txt`.
- Run 20261008T125139Z-sweep-merchant-routes-ar: `responses/0535.json` (onboarding/persona-country): its question is the store's country, so nothing was recorded from it.
- Run 20261008T122729Z-sweep-merchant-menus-ar: `steps/002.text.txt` and `actions.jsonl` step 2 (the orders list), because the checker reported the N02 route's address held there; it shows the status بإنتظار المراجعة and no receipt.

### Open items

- Q4-SA-N01 (Salla fees on bank transfer or own-carrier cash on delivery): unchanged. The real store's gateways answer gives `fees` for its quick methods only; nothing read states a fee or its absence for bank transfer or cash on delivery. Search and reads added to the row.
- Q4-SA-N02 (reviewing a bank transfer receipt): unchanged in wording; partly bears: Q4-SA-070, Q4-SA-072, Q4-SA-073, Q4-SA-074. Search and reads added; the route was reworded without the address `https://s.salla.sa/orders`, which a sweep step holds and which shows no receipt.
- Q4-SA-N03 (limit on a bank transfer order's amount): unchanged. Search and reads added.
- Q4-SA-G0117 and Q4-SA-H0008 (who collects and holds cash on delivery through Salla shipping labels): stay open. Q4-SA-078 and Q4-SA-077 bear on G0117 and do not close it.
- No row closed, so `not-found-closed.tsv` was not written.

### Wording check

The three rows that stay were checked against what they read and this folder's records (التحويل البنكي, إيصال, بانتظار المراجعة, قيود الدفع); no change was needed.

### Stores and scope

- Run 20261009T112238Z-journey-storefront-account-order-en names its store `alshifahoney` in `run.json`; step 39's page is at store.rasasi.com.sa and its title names مرحبا بكم في متجر الرصاصي للعطور الرسمي, so Q4-SA-074 is scoped to that store, as the page states it. That checkout was not completed (steps 70 to 72 stay on the checkout).
- Order 24438069 of the real-merchant store has `"source": "dashboard"` in its answer.
- `merchant_type` KSA (Q4-SA-067) is cited from the same gateways answer.

### Not read

The reports journey steps, the export templates steps, the community `latest.json` answers, the demo stores' orders and wallet answers, the billing and ads translations, the Salla Point onboarding answers, and the storefront journey's other bank transfer steps (40 to 43, 69 to 71, 89 to 91).

### Problems

- The checker reads a JSON answer's HTML-bearing string with its tags in place in one of its forms, so a statement that ran from a key across the tags (`"answer": "<div >…`) was not found; Q4-SA-077 records the answer's text alone, with the question in its identifier.
