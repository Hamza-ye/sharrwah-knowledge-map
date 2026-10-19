# Q8, Salla (checking run): notes

## What was read
- Copies: 27 concerns copied and 94 set aside (selection.tsv). `copied-view.tsv` was read once, right after the accounts, with each statement cut to about 260 characters.
- Accounts: studies/proposals/records/Q8/shopify/account.md and studies/proposals/records/Q8/woocommerce/account.md. The checker reported no issues for either. No ids were looked up in their folders.
- Help map (observed-sa@4ca2e896a729215f422a137a364e7e9488610ba3, structures/salla/help-articles/ar/texts.jsonl), read in Arabic: glmfvz0wf6rvd9wiczinecb1, rhzl2dh5f5f9uz0qo813nttb, fzignds97xnb8tl1hvhsryri, e0czi8aai1sl4xdgr29432t0, u0mdz18srmw1qi072mkrg77w, sjr0h3lugcfnbgho0oco9q4j, r1nn6vwueas23lw7ixvpwj9h. That is 7 pages.
- Corpus searches (the commands are in not-found.tsv; the services search is below). Opened: the capture of docs.salla.dev/app-functions/welcome.md; the fetch-archive record raw/runs/20261006T003648Z-docs-dataschema-html/fetch.warc.gz@14214290 (docs.salla.dev/webhook-events/orders); and structures/salla/com-policies/terms/text.txt, searched with grep and read around its plan, service and support passages.
- The services search, for [1] and [2]: `python3 -I method/corpus_search.py salla "الخدمات الإضافية" "additional service" "additional services" "خدمات سلة" "Salla services" --max 10`. Of what it listed, only com-policies/terms was opened.
- The list of account points and search terms is in the scratch directory, as unmatched-points.md.

## Live pages
- None read.

## Not read
- Help map: gbc2ct0nerndys7sk4l2rvc1 (managing the store plan: subscriptions, invoices and upgrades), the Special-plan articles, and the Salla Capital articles.
- salla.com/plans, held at raw/runs/20261006T030341Z-com-toplevel/fetch.warc.gz@10313615.
- The plan comparison table in glmfvz0wf6rvd9wiczinecb1 has more than 20 rows. Recorded are the rows for these features: all product types, e-payments, Salla Ads, Mahally, SEO, VAT, theme choice, CSS/JS theme code and customer groups. Left out are the rows for these features: unlimited products and orders, Salla shipping labels, bank transfer, Sarie, standard and economy shipping, own couriers, free shipping, theme customization, store performance summary, default and own domain, customer sorting and blocking, customer import, and adding customers.

## Copies
- I found no copy wrong. Q8-SA-015 says more than copy Q8-SA-K0050 (it gives the plans and the limit of twice a year).
- Several copied gaps (G0006, G0019, G0022, G0101, G0102, G0155, G0213–G0216) say salla.com/terms is held but not read. It is readable at structures/salla/com-policies/terms/text.txt. Those gaps were not checked against what they ask for, since they don't bear on a sentence of Q8 as read.

## Problems
- To see the not-found format, I opened the head of studies/proposals/records/Q8/shopify/not-found.tsv. That is another run's folder, beyond the accounts. It did not steer what I searched for or recorded.
- The first corpus search's terms شارة and badge matched other senses, such as "اشارة" and UI badge strings. That filled most of its list with documents that couldn't show the point.
- The run was interrupted by a usage limit after the copies were made. At that point no statements had been written, so nothing was redone.

## Re-check against the observed runs, 19 October 2026

### What was read
- The guides of observed-sa at 4ca2e896a729215f422a137a364e7e9488610ba3: README.md and docs/READING.md, whole.
- Open items: the 13 rows of not-found.tsv. account.md cites no copied gap, and the starting message listed no phrases.
- Searches for the open items (each `python3 -I method/corpus_search.py salla … --max 10`): "طرق الدفع" "payment method(s)" "بوابات الدفع" gateway(s) (N01); "ما الجديد" "what's new" "release notes" "تحديثات سلة" "جديد سلة" changelog (N02); beta betas بيتا "تجريبي" "early access" "الوصول المبكر" "development store(s)" "متجر تجريبي" (N05, N06); "متاجر متعددة" multi-stores "إدارة المتاجر" "Manage stores" "multiple stores" (N10); "ذكاء اصطناعي" "AI agent(s)" agentic "وكيل" (N03); "إصدار" "API version(s)" deprecated deprecation sunset "إيقاف" min_version "minimum version" version (N07, N08, N12, N13); "قنوات البيع" "sales channel(s)" "قناة بيع" (N09); "شارة" badge(s) "موثوق" certified "مميز" "built for" (N11); "حزمة" package(s) micro-frontend importmap module(s) (N04).
- Searches for the question's sentences: [1] "باقات سلة" "الباقة" plans plan "المتجر وقنوات البيع" persona; [2] addons add-on(s) "الإضافات" "الخدمات الإضافية" feature(s); [3] isbeta isnewfeature "قريباً" "coming soon" "ترقية الباقة" upgrade available_countries. The REST endpoints index (index/rest-endpoints.tsv) was read for the onboarding endpoints the brief points to.
- Files opened, all under raw/runs/ at that commit:
  - 20261012T010906Z-sweep-real-merchant-full-en: responses/1488.json (gateways/payment, step 42), responses/12212.json (marketplace/addons, step 337), steps/337.text.txt (/settings/plan), responses/0185.json (nav, step 5), responses/5527.json (marketplace/themes/versions, step 149), run.json, responses.jsonl.
  - 20261008T133523Z-sweep-demo-store-en: responses/2518.json (gateways/payment, step 71); the same groups and slugs as 1488.json, not recorded again.
  - 20261012T061749Z-journey-changelog-signed-en: steps/001.text.txt, steps/002.text.txt, responses/0001.json, responses/0003.json, actions.jsonl, run.json.
  - 20261008T131847Z-sweep-merchant-routes-ar: steps/077.text.txt (/manage/stores), run.json.
  - 20261008T141131Z-sweep-merchant-en: steps/138.text.txt (/persona/plans), responses/9578.json (marketplace/themes), responses/9552.json (marketplace/themes/summary), run.json.
  - 20261008T125139Z-sweep-merchant-routes-ar: steps/023.text.txt (/persona/qna), responses/0535.json (onboarding/persona-country), responses/0576.json (onboarding/create-store, not recorded), responses/0709.json (store/info), run.json.

### Stores
- Run 20261008T125139Z-sweep-merchant-routes-ar names no store in run.json. Q8-SA-051's store is named as the same run's store/info answer (responses/0709.json) states it: "Store 1", plan "basic", kyc_country "SA", currency "SAR" (Q8-SA-C081 to C083).
- The real-merchant store's plan is cited from its /settings/plan page, "Current plan Pro" (Q8-SA-C044).

### Open items
- Closed: Q8-SA-N02, by Q8-SA-038, Q8-SA-039 and Q8-SA-040 (moved unchanged to not-found-closed.tsv).
- Narrowed: Q8-SA-N01, by Q8-SA-041 and Q8-SA-042 (one store's payments answer and its empty available_countries); Q8-SA-N10, by Q8-SA-050 (the store list and its per-store plan and role).
- Unchanged, with the re-check search and the documents opened added to `searched` and `read`: Q8-SA-N03 to N09, N11 to N13.

### Wording check
- Every row that stays was checked against what its `read` names and the folder's records. No row gives a name, label, path or phrase as the platform's that they don't show, so no detail was removed. The narrowed N01 names `available_countries`, which Q8-SA-042 holds.

### Lists
- The changelog's categories (Q8-SA-039) hold 22 items, recorded in full.
- The payments answer (Q8-SA-042) is recorded in full from `quick_methods` to the end of `other_payment_methods`; `bank_transfers`, which holds the store's own bank account, is left out as not bearing on the question.

### Not read
- The other run documents the searches listed, by title and snippet; derived/plan-gates.tsv and derived/journey-catalog.tsv, whose rows mix the capture's words with Salla's; the changelog's posts list (changelog/lists, 317,889 bytes) beyond what the page showed; the user/features answers, since copies already hold the store feature settings.

### Problems
- The search caps each corpus at 10, and the help articles fill the first part of every listing, so the run documents come after them. A summary script in the scratch directory pulled out the run hits.
- JSON answers that write Arabic as escapes are quoted in the checker's decoded form (`json.dumps` with `ensure_ascii=False`, which puts a space after each colon and comma); ASCII-only passages are quoted from the raw file.
- Long lists (Q8-SA-039, 042, 043, 049) are cited in consecutive quotes of up to 300 characters, cut at item boundaries where possible.
