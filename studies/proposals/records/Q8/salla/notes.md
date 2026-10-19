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
