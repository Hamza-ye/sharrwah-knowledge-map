# Run 20261010T072550Z-sanaa-operators-search

The 99 pages found by the Arabic-first search for the businesses that payments in the Sana'a zone run through. The search's own list is `evidence/yemen/finding-aids/20261010-sanaa-operators-search.tsv`, rows B001–B099. Each item here cites its row.

The pages cover:

- **Wallets and banks:** their own pages, app-store listings and public Telegram channels.
- **Couriers.**
- **Sana'a sellers' payment-instruction pages.**

**Fetched from:** a Claude Code cloud container outside Yemen, on 10 October 2026 (UTC). The method was the same as the other runs: a raw fetch, then a Chromium render, then date hints.

## Results

| Result | Count |
| --- | --- |
| captured | 93 |
| blocked from here | 6: the Sana'a central bank site, SabaCash's services page, Floosak's own domain, Yemen Kuwait Bank's Floosak page, and two seller pages (1MDP and eMahallat) |

By date hint: 33 from 2025–2026, 5 from 2023–2024, 11 from before 2023 (historical), 44 undated live pages, and 6 undated because they were not captured.

## Notes

- **Telegram posts.** A Telegram post's normal page shows almost no text, so each post was also fetched through Telegram's public embed view. `embed.html` holds that page and `embed-text.txt` the post's text, channel and posting time. The posting time is the post's date in the manifest.
- **Seller pages show personal data.** Their captures can contain phone and wallet numbers. They stay in this private repository, and the search's list itself does not record them.
- **Two pages captured as served.** Jawali's merchant QR form answered with a script check, and Kuraimi's service-point finder is interactive. Both were captured as they first loaded. Nothing was submitted.
- **Archive copies were not fetched.** The search's list gives Wayback Machine addresses for 50 rows, including every blocked page. The Wayback Machine was refusing or resetting connections from here during this run, so no archive copy was taken.
