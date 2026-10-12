# Pass 1, part F: notes

Source commit in every `source`: 9d0de523f1852ebf7716f0da01b6b619edc5e8fc. The `evidence/` tree is unchanged between that commit and the working tree.

## What was read

### Community clients run, `runs/20261010T051708Z-community-clients/`

Run facts used in every citation of this run: `README.md` says it was fetched from "a Claude Code cloud container outside Yemen", so `fetched_from` is `outside Yemen`; `url` is the repository address in `clients.tsv`; `source_date` and `held_at` are the date of the commit copied (`commit_date` in `clients.tsv`), with basis `published`. The README says a client "is not the provider's own documentation"; each condition row's note says so.

- `README.md` and `clients.tsv`: read (13 repositories).
- **Alsharie/AlQutaibiBank-payment** (14 files, commit 2024-03-06): read `README.md`, `composer.json`, `config/AlQutaibiBank.php`, the 8 files in `src/`, `.gitignore`; viewed `img.webp` (the bank's logo, no text beyond its name). Not read: `composer.lock` (dependency lock file). Rows: YQ-F001 to YQ-F005; YE-F001 to YE-F007.
- **Alsharie/adenbank-payment** (15 files, commit 2024-03-23; no README): read `composer.json`, `config/adenBank.php`, the 11 files in `src/`, `.gitignore`. Not read: `composer.lock`. Rows: YQ-F006 to YQ-F012; YE-F008 to YE-F016.
- **Alsharie/cash-payment** (17 files, commit 2024-03-17): read `README.md`, `composer.json`, `config/cashPay.php`, the 11 files in `src/`, `.gitignore`; viewed `img.png` (the "كاش cash" logo). Not read: `composer.lock`. Rows: YQ-F013 to YQ-F020; YE-F017 to YE-F028. Citations of `CashPayErrorCode.php` give as `url` the cited address into that file listed in `clients.tsv`.
- **Alsharie/floosak-payment** (21 files, commit 2024-01-30): read `README.md`, `composer.json`, `config/floosak.php`, the 16 files in `src/`, `.gitignore`; viewed `img.png` (the "فلوسك Floosak" logo). Not read: `composer.lock`. Rows: YQ-F021 to YQ-F027; YE-F029 to YE-F037.
