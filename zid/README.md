# Zid

What Zid (zid.sa) states and shows about itself, captured at the source, in English. The Arabic strings of the
merchant dashboard are held beside the English ones (`structures/dashboard-locales/`).

## The instrument

Zid's public demo, `https://dashboard.zid.sa/en-sa/demo`, signs any visitor in to the merchant dashboard as the owner
of one store: Zid Demo Store, store 127604, on the Professional plan (yearly, to 2026-11-05), with the storefront
`https://zid-demostore.com/`. Every visitor shares that store, so what it shows includes what earlier visitors changed,
and what a run changes is seen by later visitors. Its facts, each with the answer it comes from, are in
[index/instruments.json](index/instruments.json). The runs were made from Yemen (`run.json`: `network`).

## Where to start

| To find | Read |
| --- | --- |
| Every page of the dashboard, as Zid's code lists it | [structures/dashboard-route-manifest/](structures/dashboard-route-manifest/) (437 routes), and [structures/dashboard-page-index/](structures/dashboard-page-index/) (the dashboard's own index of 119 pages: key, path, English and Arabic title) |
| What a page shows, and in which run | [index/ledger/dashboard-routes.tsv](index/ledger/dashboard-routes.tsv): each manifest route, whether a run opened it, and the step files that hold it (`steps/NNN.text.txt`, `.aria.yaml`, `.html`, `.png`) |
| What the dashboard's API answered (the store, its settings, plan, permissions, markets) | each browser run's `answers.jsonl`, and the bodies under its `answers/hermod.zid.sa/` |
| The store's plan: every policy, whether it is enabled, its limits, and the plan it is available in | [structures/store-plan-policies/](structures/store-plan-policies/) |
| The permissions a team member can be given | [structures/store-permissions/](structures/store-permissions/) |
| The dashboard's own words, in English and Arabic | [structures/dashboard-locales/items.jsonl](structures/dashboard-locales/items.jsonl): one string per line, by `<namespace>:<key>`, the key the dashboard's code names |
| Every self-description seen, held or not | [structures/REGISTER.tsv](structures/REGISTER.tsv) |
| Every run, and what is unusual about one | [index/runs.tsv](index/runs.tsv), [index/run-notes.tsv](index/run-notes.tsv) |
| What is not held yet, and how it can be | [GAPS.md](GAPS.md) |
